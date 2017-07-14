import subprocess, time, sys, os, ROOT
sys.path.insert(0, '../Alignment/MuonAlignmentAlgorithms/scripts')
from plotscripts import *

def get_Corr(tfiles_plotting,MEpm_l,MEpm_t,Station,Ring):
    correction = []
    tfilesN_plotting = []
    tfilesN_plotting.append(ROOT.TFile(str(tfiles_plotting)))
    label = "CSCvsphi_me%s%s%s" % (MEpm_l, Station, Ring)
    htitle = "%s%s/%s" % (MEpm_t, Station, Ring)
    Shift = mapplot_shiftValues(tfilesN_plotting, label, "x", window=15., title=htitle, fitsine=True,fitpeaks=True, peaksbins=2)
    correction.append(Shift[0])
    correction.append(Shift[1])
    return correction

def mapplot_shiftValues(tfiles, name, param, mode="from2d", window=10., abscissa=None, title="", 
            widebins=False, fitsine=False, fitline=False, reset_palette=False, fitsawteeth=False, fitpeaks=False, peaksbins=1, fixfitpars={}, **args):
    Shift = []
    ROOT.gROOT.SetBatch(ROOT.kTRUE)
    c1 = ROOT.TCanvas("c1","c1",800,600)
    tdrStyle.SetOptTitle(1)
    tdrStyle.SetTitleBorderSize(0)
    tdrStyle.SetOptStat(0)
    tdrStyle.SetOptFit(0)
    tdrStyle.SetTitleFontSize(0.05)
    tdrStyle.SetPadRightMargin(0.1) # to see the pallete labels on the left
    c1.Clear()
    c1.ResetAttPad()
    
    if reset_palette: set_palette("blues")
    global hist, hist2d, hist2dweight, tline1, tline2, tline3
    
    if fitsine or fitsawteeth:
        id = mapNameToId(name)
        if not id:
            print "bad id for ", name
            raise Exception
    
    hdir = "AlignmentMonitorMuonSystemMap1D/iter1/"
    hpref= "%s_%s" % (name, param)
    hhh  = hdir+hpref ### _2d ? if "h2d" in args:
    
    combine_all = False
    if "ALL" in name  and  ("CSCvsr" in name  or  "DTvsz" in name): combine_all = True
    
    add1d =  ("vsphi" in name) and (param == "x")

    if "h2d" in args:
      hist2d = args["h2d"].Clone(hpref+"_2d_")
      if "CSC" in name  and  add1d: hist1d = args["h1d"].Clone(hpref+"_1d_")

    elif combine_all:
      nch = 12
      if  "DT" in name  and  name[6:9]=='st4': nch = 14
      if  "CSC" in name: nch = 36
      chambers = ["%02d" % ch for ch in range (2,nch+1)]

      ch_hhh = hhh.replace('ALL','01')
      ch_hpref = hpref.replace('ALL','01')
      hist2d = tfiles[0].Get(ch_hhh+"_2d").Clone(ch_hpref+"_2d_")
      if "CSC" in name  and  add1d: hist1d = tfiles[0].Get(ch_hhh+"_1d").Clone(ch_hpref+"_1d_")
      
      for ch in chambers:
        ch_hhh = hhh.replace('ALL',ch)
        ch_hpref = hpref.replace('ALL',ch)
        hist2d.Add(tfiles[0].Get(ch_hhh+"_2d"))
        if "CSC" in name  and  add1d: hist1d.Add(tfiles[0].Get(ch_hhh+"_1d"))
        for tfile in tfiles[1:]:
          hist2d.Add(tfile.Get(ch_hhh+"_2d"))
          if "CSC" in name   and  add1d: hist1d.Add(tfile.Get(ch_hhh+"_1d"))
    
    else:
      hist2d = tfiles[0].Get(hhh+"_2d").Clone(hpref+"_2d_")
      if "CSC" in name  and  add1d: hist1d = tfiles[0].Get(hhh+"_1d").Clone(hpref+"_1d_")
      for tfile in tfiles[1:]:
        hist2d.Add(tfile.Get(hhh+"_2d"))
        if "CSC" in name   and  add1d: hist1d.Add(tfile.Get(hhh+"_1d"))

    
    if mode == "from2d":
        the2d = hist2d
        
        hist = the2d.ProjectionX()
        hist.Reset()
        
        skip = 1
        if widebins:
            hist.Rebin(10)
            skip = 10

        for i in xrange(0, int(the2d.GetNbinsX()), skip):
            tmp = the2d.ProjectionY("tmp", i+1, i + skip)
            if tmp.GetEntries() > 1:
                hist.SetBinContent(i/skip+1, tmp.GetMean())
                hist.SetBinError(i/skip+1, ROOT.TMath.StudentQuantile(0.841345,tmp.GetEntries()) * tmp.GetRMS() / sqrt(tmp.GetEntries()))
            else:
                hist.SetBinContent(i/skip+1, 0.)
                hist.SetBinError(i/skip+1, 0.)

        hpeaks = createPeaksProfile(the2d, peaksbins)

    else:
        raise Exception

    hist.SetAxisRange(-window, window, "Y")
    if abscissa is not None: hist.SetAxisRange(abscissa[0], abscissa[1], "X")
    hist.SetMarkerStyle(20)
    hist.SetMarkerSize(0.75)
    hist.GetXaxis().CenterTitle()
    hist.GetYaxis().CenterTitle()
    hist.GetYaxis().SetTitleOffset(0.75)
    hist.GetXaxis().SetTitleSize(0.05)
    hist.GetYaxis().SetTitleSize(0.05)
    hist.SetTitle(title)
    if "vsphi" in name: hist.SetXTitle("Global #phi position (rad)")
    elif "vsz" in name: hist.SetXTitle("Global z position (cm)")
    elif "vsr" in name: hist.SetXTitle("Global R position (cm)")
    if "DT" in name:
        if param == "x": hist.SetYTitle("x' residual (mm)")
        if param == "dxdz": hist.SetYTitle("dx'/dz residual (mrad)")
        if param == "y": hist.SetYTitle("y' residual (mm)")
        if param == "dydz": hist.SetYTitle("dy'/dz residual (mrad)")
    if "CSC" in name:
        if param == "x": hist.SetYTitle("r#phi residual (mm)")
        if param == "dxdz": hist.SetYTitle("d(r#phi)/dz residual (mrad)")
    hist.SetMarkerColor(ROOT.kBlack)
    hist.SetLineColor(ROOT.kBlack)
    hist.Draw()
    hist2d.Draw("colzsame")
    if widebins: hist.Draw("samee1")
    else: hist.Draw("same")

    hpeaks.SetMarkerStyle(20)
    hpeaks.SetMarkerSize(0.9)
    hpeaks.SetMarkerColor(ROOT.kRed)
    hpeaks.SetLineColor(ROOT.kRed)
    hpeaks.SetLineWidth(2)
    #if fitpeaks: hpeaks.Draw("same")
    hpeaks.Draw("same")

    if fitsine and "vsphi" in name:
        global fitsine_const, fitsine_sin, fitsine_cos, fitsine_chi2, fitsine_ndf
        if 'CSC' in name:
          f = ROOT.TF1("f", "[0] + [1]*sin(x) + [2]*cos(x)", -pi/180.*5., pi*(2.-5./180.))
        else:
          f = ROOT.TF1("f", "[0] + [1]*sin(x) + [2]*cos(x)", -pi, pi)
        f.SetLineColor(ROOT.kRed)
        f.SetLineWidth(2)
        if len(fixfitpars)>0:
          for fpar in fixfitpars.keys():
            f.FixParameter(fpar, fixfitpars[fpar])
        #hist.Fit(f,"N")
        if fitpeaks: hpeaks.Fit(f,"NQ")
        else: hist.Fit(f,"NEQ")
        if len(fixfitpars)>0:
          for fpar in fixfitpars.keys():
            f.ReleaseParameter(fpar)
        fitsine_const = f.GetParameter(0), f.GetParError(0)
        fitsine_sin = f.GetParameter(1), f.GetParError(1)
        fitsine_cos = f.GetParameter(2), f.GetParError(2)
        Shift.append( round(float(f.GetParameter(1)),4) )
        Shift.append( round(float(f.GetParameter(2)),4) )
        fitsine_chi2 = f.GetChisquare()
        fitsine_ndf = f.GetNDF()
        global MAP_RESULTS_FITSIN
        # 'phi' coefficienct will be updated further for CSC
        MAP_RESULTS_FITSIN[id] = {'a':fitsine_const, 'phi':fitsine_const, 'sin': fitsine_sin, 'cos': fitsine_cos, 'chi2': fitsine_chi2, 'ndf': fitsine_ndf}
        f.Draw("same")
        global fitsine_ttext, fitsine_etext
        text_xposition = -1.
        if 'CSC' in name: text_xposition = 2.
        fitsine_ttext = ROOT.TLatex(text_xposition, 0.8*window, 
                "%+.3f %+.3f sin#phi %+.3f cos#phi" % (fitsine_const[0], fitsine_sin[0], fitsine_cos[0]))
        fitsine_ttext.SetTextColor(ROOT.kRed)
        fitsine_ttext.SetTextSize(0.05)
        fitsine_ttext.Draw()
        fitsine_etext = ROOT.TLatex(text_xposition, 0.70*window, 
                " #pm%.3f    #pm%.3f            #pm%.3f" % (fitsine_const[1], fitsine_sin[1], fitsine_cos[1]))
        fitsine_etext.SetTextColor(ROOT.kRed)
        fitsine_etext.SetTextSize(0.045)
        fitsine_etext.Draw()

        # additional estimate of phiz ring rotation from 1d distribution
        if 'CSC' in name and add1d:
          # zero-order rough fit to obtain the fitting range:
          f0 = ROOT.TF1("f0", "gaus", hist1d.GetBinLowEdge(1), -hist1d.GetBinLowEdge(1))
          fit = hist1d.Fit(f0,"NRQ")
          rangea, rangeb = hist1d.GetMean() - hist1d.GetRMS(), hist1d.GetMean() + hist1d.GetRMS()
          if fit==0: rangea, rangeb = f0.GetParameter(1) - f0.GetParameter(2), f0.GetParameter(1) + f0.GetParameter(2)
          #print rangea, rangeb
          
          # second fit for finding the peak:
          f1 = ROOT.TF1("f1", "gaus", rangea, rangeb)
          fit = hist1d.Fit(f1,"NRQ")
          nn = hist1d.GetEntries()
          dphiz, ephiz = 0, 0
          if nn>0:  dphiz, ephiz = hist1d.GetMean(), ROOT.TMath.StudentQuantile(0.841345,nn) * hist1d.GetRMS() / sqrt(nn)
          if fit==0: dphiz, ephiz = f1.GetParameter(1), f1.GetParError(1)
          #print dphiz, ephiz
          MAP_RESULTS_FITSIN[id]['phi'] = (dphiz, ephiz)
          
          global ttex_sine_, ttex_sine, ttex_1d_, ttex_1d
          postal_address = idToPostalAddress(id+'/01')
          ttex_sine_ = ROOT.TLatex(0, 0.8*window,"#Delta#phi_{z}^{sine} (mrad):")
          ttex_sine_.SetTextColor(ROOT.kGreen+2); ttex_sine_.SetTextSize(0.04); ttex_sine_.Draw()
          ttex_sine = ROOT.TLatex(0, 0.7*window,"   %+.3f#pm%.3f" %
                                  (-100*fitsine_const[0]/signConventions[postal_address][3], 
                                   100*fitsine_const[1]/signConventions[postal_address][3]))
          ttex_sine.SetTextColor(ROOT.kGreen+2); ttex_sine.SetTextSize(0.04); ttex_sine.Draw()
          ttex_1d_ = ROOT.TLatex(0, 0.6*window,"#Delta#phi_{z}^{phi} (mrad):")
          ttex_1d_.SetTextColor(ROOT.kGreen+2); ttex_1d_.SetTextSize(0.04); ttex_1d_.Draw()
          ttex_1d = ROOT.TLatex(0, 0.5*window,"   %+.3f#pm%.3f" % (-dphiz, ephiz))
          ttex_1d.SetTextColor(ROOT.kGreen+2); ttex_1d.SetTextSize(0.04); ttex_1d.Draw()
          ROOT.gPad.Update()

    if fitline:
        f = ROOT.TF1("f", "[0] + [1]*x", -1000., 1000.)
        hist2d.Fit(f, "q")
        hist2d.GetFunction("f").SetLineColor(ROOT.kRed)
        global fitline_const, fitline_linear, fitline_chi2, fitline_ndf
        fitline_const = hist2d.GetFunction("f").GetParameter(0), hist2d.GetFunction("f").GetParError(0)
        fitline_linear = hist2d.GetFunction("f").GetParameter(1), hist2d.GetFunction("f").GetParError(1)
        fitline_chi2 = hist2d.GetFunction("f").GetChisquare()
        fitline_ndf = hist2d.GetFunction("f").GetNDF()
        hist2d.GetFunction("f").Draw("same")
        global fitline_ttext
        if "vsz" in name: which = "Z"
        elif "vsr" in name: which = "R"
        fitline_ttext = ROOT.TText(hist.GetBinCenter(hist.GetNbinsX()/4), 
                0.8*window, "%.3g %+.3g %s" % (fitline_const[0], fitline_linear[0], which))
        fitline_ttext.SetTextColor(ROOT.kRed)
        fitline_ttext.Draw()

    ROOT.gPad.RedrawAxis()

    if "vsphi" in name: 
        if not widebins: philines(name, window, abscissa)
        if abscissa is None:
          if 'CSC' in name:
            tline1 = ROOT.TLine(-pi/180.*5., 0, pi*(2.-5./180.), 0); tline1.Draw()
            tline2 = ROOT.TLine(-pi/180.*5., -window, pi*(2.-5./180.), -window); tline2.SetLineWidth(2); tline2.Draw()
            tline3 = ROOT.TLine(-pi/180.*5., window, pi*(2.-5./180.), window); tline3.Draw()
          else:
            tline1 = ROOT.TLine(-pi, 0, pi, 0); tline1.Draw()
            tline2 = ROOT.TLine(-pi, -window, pi, -window); tline2.SetLineWidth(2); tline2.Draw()
            tline3 = ROOT.TLine(-pi, window, pi, window); tline3.Draw()
        else:
            tline1 = ROOT.TLine(abscissa[0], 0, abscissa[1], 0); tline1.Draw()
            tline2 = ROOT.TLine(abscissa[0], -window, abscissa[1], -window); tline2.SetLineWidth(2); tline2.Draw()
            tline3 = ROOT.TLine(abscissa[0], window, abscissa[1], window); tline3.Draw()
    elif "vsz" in name:
        if not widebins: zlines(window, abscissa)
        if abscissa is None:
            tline1 = ROOT.TLine(-660, 0, 660, 0); tline1.Draw()
            tline2 = ROOT.TLine(-660, -window, 660, -window); tline2.SetLineWidth(2); tline2.Draw()
            tline3 = ROOT.TLine(-660, window, 660, window); tline3.Draw()
        else:
            tline1 = ROOT.TLine(abscissa[0], 0, abscissa[1], 0); tline1.Draw()
            tline2 = ROOT.TLine(abscissa[0], -window, abscissa[1], -window); tline2.SetLineWidth(2); tline2.Draw()
            tline3 = ROOT.TLine(abscissa[0], window, abscissa[1], window); tline3.Draw()
    elif "vsr" in name:
        if "mem1" in name or "mep1" in name and not widebins: rlines(1, window, abscissa)
        if "mem2" in name or "mep2" in name and not widebins: rlines(2, window, abscissa)
        if "mem3" in name or "mep3" in name and not widebins: rlines(3, window, abscissa)
        if "mem4" in name or "mep4" in name and not widebins: rlines(4, window, abscissa)
        if abscissa is None:
            tline1 = ROOT.TLine(100, 0, 700, 0); tline1.Draw()
            tline2 = ROOT.TLine(100, -window, 700, -window); tline2.SetLineWidth(2); tline2.Draw()
            tline3 = ROOT.TLine(100, window, 700, window); tline3.Draw()
        else:
            tline1 = ROOT.TLine(abscissa[0], 0, abscissa[1], 0); tline1.Draw()
            tline2 = ROOT.TLine(abscissa[0], -window, abscissa[1], -window); tline2.SetLineWidth(2); tline2.Draw()
            tline3 = ROOT.TLine(abscissa[0], window, abscissa[1], window); tline3.Draw()

    if "vsphi" in name and fitsawteeth:
        global CPP_LOADED
        if not CPP_LOADED:
            phiedges2c()
            ROOT.gROOT.ProcessLine(".L phiedges_fitfunctions.C++")
            CPP_LOADED = True
        fn={0: ROOT.fitf0,
            1: ROOT.fitf2,
            2: ROOT.fitf2,
            3: ROOT.fitf3,
            4: ROOT.fitf4,
            5: ROOT.fitf5,
            6: ROOT.fitf6,
            7: ROOT.fitf7,
            8: ROOT.fitf8,
            9: ROOT.fitf9,
            10: ROOT.fitf10,
            11: ROOT.fitf11,
            12: ROOT.fitf12,
            13: ROOT.fitf13
        } [stationIndex(name)]
        fn.SetNpx(5000)
        fn.SetLineColor(ROOT.kYellow)
        hist.Fit(fn,"N")
        fn.Draw("same")

        # get properly arranged phi edges
        edges = (phiedges[stationIndex(name)])[:]
        ed = sorted(edges)
        # add some padding to the end
        ed.append(pi+abs(ed[0]))

        global sawtooth_a, sawtooth_b
        sawtooth_a = []
        sawtooth_da = []
        sawtooth_b = []
        for pr in range(0,fn.GetNpar(),2):
            sawtooth_a.append( (fn.GetParameter(pr), fn.GetParError(pr)) )
            sawtooth_b.append( (fn.GetParameter(pr+1), fn.GetParError(pr+1)) )
            sawtooth_da.append( (fn.Eval(ed[pr/2]+0.01), fn.Eval(ed[pr/2+1]-0.01)) )
        global MAP_RESULTS_SAWTOOTH
        MAP_RESULTS_SAWTOOTH[id] = {'a': sawtooth_a, 'da': sawtooth_da, 'b': sawtooth_b, 'chi2': fn.GetChisquare(), 'ndf': fn.GetNDF()}

    # fill number of contributiong bins
    
    
    #ROOT.SetOwnership(hist,False)
    ROOT.SetOwnership(hist2d,False)
    ROOT.SetOwnership(hist,False)
    ROOT.SetOwnership(tline1,False)
    ROOT.SetOwnership(tline2,False)
    ROOT.SetOwnership(tline3,False)
    return Shift

def writeXML_DB_Converter(outputfile, InputXML, outPutDB,  GlobPos, TagGP, Run):
    outputfile.write("import FWCore.ParameterSet.Config as cms\n")
    outputfile.write("import sys\n")
    outputfile.write("\n")
    outputfile.write("process = cms.Process('CONVERT')\n")
    outputfile.write("process.source = cms.Source('EmptySource',firstRun = cms.untracked.uint32(" + Run + "))\n")
    outputfile.write("process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(1))\n")
    outputfile.write("\n")
    outputfile.write("process.load('Configuration.Geometry.GeometryIdeal_cff')\n")
    outputfile.write("process.load('Geometry.MuonNumbering.muonNumberingInitialization_cfi')\n")
    outputfile.write("\n")
    outputfile.write("process.MuonGeometryDBConverter = cms.EDAnalyzer('MuonGeometryDBConverter',\n")
    outputfile.write("    input = cms.string('xml'),\n")
    outputfile.write("    fileName = cms.string('" + InputXML + "'),\n")
    outputfile.write("    shiftErr = cms.double(1000.),\n")
    outputfile.write("    angleErr = cms.double(6.28),\n")
    outputfile.write("    output = cms.string('db'))\n")
    outputfile.write("\n")
    outputfile.write("from CondCore.CondDB.CondDB_cfi import *\n")
    outputfile.write("CondDBSetup = CondDB.clone()\n")
    outputfile.write("CondDBSetup.__delattr__('connect')\n")
    outputfile.write("process.PoolDBOutputService = cms.Service('PoolDBOutputService',\n")
    outputfile.write("    CondDBSetup,\n")
    outputfile.write("    connect = cms.string('sqlite_file:" + outPutDB + "'),\n")
    outputfile.write("    toPut = cms.VPSet(\n")
    outputfile.write("        cms.PSet(record = cms.string('DTAlignmentRcd'), tag = cms.string('DTAlignmentRcd')),\n")
    outputfile.write("        cms.PSet(record = cms.string('DTAlignmentErrorExtendedRcd'), tag = cms.string('DTAlignmentErrorExtendedRcd')),\n")
    outputfile.write("        cms.PSet(record = cms.string('CSCAlignmentRcd'), tag = cms.string('CSCAlignmentRcd')),\n")
    outputfile.write("        cms.PSet(record = cms.string('CSCAlignmentErrorExtendedRcd'), tag = cms.string('CSCAlignmentErrorExtendedRcd'))))\n")
    outputfile.write("\n")
    outputfile.write("process.inertGlobalPositionRcd = cms.ESSource('PoolDBESSource',\n")
    outputfile.write("    CondDBSetup,\n")
    outputfile.write("    connect = cms.string('sqlite_file:" + GlobPos + "'),\n")
    outputfile.write("    toGet = cms.VPSet(cms.PSet(record = cms.string('GlobalPositionRcd'), tag = cms.string('" + TagGP + "'))))\n")
    outputfile.write("\n")
    outputfile.write("process.Path = cms.Path(process.MuonGeometryDBConverter)\n")
