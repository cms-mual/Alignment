import ROOT as r
import struct, math, os, sys
from array import array
from functions_layers import *
from collections import defaultdict
import numpy as np

#Checka and Inizialization
nSigma=1.
if(len(sys.argv) < 2):
  print "USAGE: python DT_DEBUG_plots_pt2.py OutputFolder_MC Output.root -b"; sys.exit(0);
folder = sys.argv[1]
rootfile = sys.argv[2]
print ">>> Setting folder:", folder, rootfile
os.system("mkdir -p " + folder + "/Residual_bins")
suffix=".pdf"
#Input File and TTree
fh = r.TFile(folder+"/"+rootfile); fh.cd();
#Drawing
print "Start drawing histograms."
c1 = r.TCanvas("Canvas1", "Alignment Visualizations")
c1.SetGridx(); c1.SetGridy()
c1.SetCanvasSize(696,472)
r.gStyle.SetOptStat("rme")

#Loop on the files
dic_chamber = defaultdict(list);
dic_chamber_h = defaultdict(list)
dic_chamber_hsk = defaultdict(list)
dirList = r.gDirectory.GetListOfKeys()
for htemp in dirList:
  notDrawn=True
  hist = htemp.ReadObj()
  #Fit the histograms that contains the residualX in bins of X
  if( "ResidualX_Bin_" in hist.GetName()):
    r.gStyle.SetOptStat("rme")
    notDrawn=False
    fitparamsGauss = 0., 0., 0., 0., 0., 0.
    if(hist.GetEntries()>7000):
      fitgaus(hist, nSigma, "QE")
      fitparamsGauss = getFitParamsGauss(hist)
    hist.Draw("colz"); c1.SaveAs(folder + "/Residual_bins/" + hist.GetName() + suffix)
    start=hist.GetName().find('_ID_') + 4
    chamber_ID=hist.GetName()[start:]
    dic_chamber[chamber_ID].append(fitparamsGauss)
    #Save also the mean and the skewness from the histograms (if stat. is sufficient) and save them in a map you will use later
    if(hist.GetEntries()>7000):
      fitparamsGauss_h = float(hist.GetEntries()), float(math.sqrt(hist.GetEntries())/hist.GetEntries()), float(hist.GetMean()), float(hist.GetMeanError()), float(hist.GetRMS()), float(hist.GetRMSError())
      fitparamsGauss_hsk = float(hist.GetSkewness(1)), float (hist.GetSkewness(11))
    else:
      fitparamsGauss_h = 0., 0., 0., 0., 0., 0
      fitparamsGauss_hsk = 0., 0.
    dic_chamber_h[chamber_ID].append(fitparamsGauss_h)
    dic_chamber_hsk[chamber_ID].append(fitparamsGauss_hsk)
  #Now the other histograms
  if(htemp.GetClassName()=="TH1F" and notDrawn):
    hist.Draw(); c1.SaveAs(folder + "/" + hist.GetName() + suffix)
  #Now the TH2
  if(htemp.GetClassName()=="TH2F" and notDrawn):
    r.gStyle.SetOptStat(0)
    if("Occupancy_XYres" in hist.GetName() and not "entries" in hist.GetName() ):
      hist.GetZaxis().SetRangeUser(-2,2)
    hist.Draw("colz"); c1.SaveAs(folder + "/" + hist.GetName() + suffix)
    if("Occupancy_XYres" in hist.GetName() and not "entries" in hist.GetName() ):
      hist.GetZaxis().SetRangeUser(-1,1)
      hist.Draw("colz"); c1.SaveAs(folder + "/" + hist.GetName() + "_zoomed" + suffix)
#Not take the fit mean, histo mean, etc. and fill a plot that show the trend vs X
x=[-170,-150,-130,-110,-90,-70,-50,-30,-10,10,30,50,70,90,110,130,150,170]
x_err=[10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
for key in dic_chamber:
  r.gStyle.SetOptStat(0)
  ThisBin=0
  g_X_ResXmean = r.TGraphErrors(len(x)); g_X_ResXmean.SetName("X_ResXmean_" + key);  g_X_ResXmean.SetTitle("");
  g_X_ResXsigma = r.TGraphErrors(len(x)); g_X_ResXsigma.SetName("X_ResXsigma_" + key); g_X_ResXsigma.SetTitle("");
  g_X_ResXmean_h = r.TGraphErrors(len(x)); g_X_ResXmean_h.SetName("X_ResXmean_h_" + key); g_X_ResXmean_h.SetTitle("");
  g_X_ResXsigma_h = r.TGraphErrors(len(x)); g_X_ResXsigma_h.SetName("X_ResXsigma_h_" + key); g_X_ResXsigma_h.SetTitle("");
  g_X_ResXmean_hsk = r.TGraphErrors(len(x)); g_X_ResXmean_hsk.SetName("X_ResXskew_" + key); g_X_ResXmean_hsk.SetTitle("");
  #Mean and Sigma from FIT vs X
  for parmams in dic_chamber[key]:
    if(parmams[2]!=0):
      g_X_ResXmean.SetPoint(ThisBin, x[ThisBin], parmams[2])
      g_X_ResXmean.SetPointError(ThisBin, x_err[ThisBin], parmams[3])
    if(parmams[3]!=0):
      g_X_ResXsigma.SetPoint(ThisBin, x[ThisBin], parmams[4])
      g_X_ResXsigma.SetPointError(ThisBin, x_err[ThisBin], parmams[5])
    ThisBin=ThisBin+1
  g_X_ResXmean.SetMinimum(-0.1); g_X_ResXmean.SetMaximum(0.1);
  g_X_ResXmean.Draw("APE"); g_X_ResXmean.GetXaxis().SetTitle("X [cm]"); g_X_ResXmean.GetYaxis().SetTitle("Res X #mu [cm]");
  param = fitLine(g_X_ResXmean,"QE")
  lat=r.TLatex(); lat.SetNDC(); lat.SetTextSize(0.025); lat.SetTextAlign(13); lat.SetTextColor(2);
  lat.DrawLatex(.5,.8,"y0: "+str(round(param[0],3))+" #pm "+str(round(param[1],3))+" a: "+str(round(param[2],5))+" #pm "+str(round(param[3],5)));
  c1.Update(); c1.SaveAs(folder + "/X_ResXmean_" + key + suffix)
  g_X_ResXmean.Draw("APE"); 
  param = fitLineStraight(g_X_ResXmean,"QE")
  lat2=r.TLatex(); lat2.SetNDC(); lat2.SetTextSize(0.025); lat2.SetTextAlign(13); lat2.SetTextColor(2);
  lat2.DrawLatex(.5,.8,"y0: "+str(round(param[0],3))+" #pm "+str(round(param[1],3)));  lat2.SetTextSize(0.025);
  c1.Update(); c1.SaveAs(folder + "/X_ResXmeanStr_" + key + suffix)
  g_X_ResXsigma.SetMinimum(1.5); g_X_ResXsigma.SetMaximum(2.2);
  g_X_ResXsigma.Draw("APE"); g_X_ResXsigma.GetXaxis().SetTitle("X [cm]"); g_X_ResXsigma.GetYaxis().SetTitle("Res X #sigma [cm]");
  c1.Update(); c1.SaveAs(folder + "/X_ResXsigma_" + key + suffix)
  #Mean and Sigma from HISTO vs X
  ThisBin=0
  for parmams in dic_chamber_h[key]:
    if(parmams[2]!=0):
      g_X_ResXmean_h.SetPoint(ThisBin, x[ThisBin], parmams[2])
      g_X_ResXmean_h.SetPointError(ThisBin, x_err[ThisBin], parmams[3])
    if(parmams[3]!=0):
      g_X_ResXsigma_h.SetPoint(ThisBin, x[ThisBin], parmams[4])
      g_X_ResXsigma_h.SetPointError(ThisBin, x_err[ThisBin], parmams[5])
    ThisBin=ThisBin+1
#  g_X_ResXmean_h.SetMinimum(-0.1); g_X_ResXmean_h.SetMaximum(0.1);
  g_X_ResXmean_h.Draw("APE"); g_X_ResXmean_h.GetXaxis().SetTitle("X [cm]"); g_X_ResXmean_h.GetYaxis().SetTitle("Res X mean [cm]");
  c1.Update(); c1.SaveAs(folder + "/X_ResXmean_h_" + key + suffix)
  g_X_ResXsigma_h.SetMinimum(1.5); g_X_ResXsigma_h.SetMaximum(2.2);
  g_X_ResXsigma_h.Draw("APE"); g_X_ResXsigma_h.GetXaxis().SetTitle("X [cm]"); g_X_ResXsigma_h.GetYaxis().SetTitle("Res X sigma [cm]");
  c1.Update(); c1.SaveAs(folder + "/X_ResXsigma_h_" + key + suffix)
  # Skewness vs X
  ThisBin=0
  for parmams in dic_chamber_hsk[key]:
    if(parmams[0]!=0):
      g_X_ResXmean_hsk.SetPoint(ThisBin, x[ThisBin], parmams[0])
      g_X_ResXmean_hsk.SetPointError(ThisBin, x_err[ThisBin], parmams[1])
    ThisBin=ThisBin+1
  g_X_ResXmean_hsk.SetMinimum(-0.05); g_X_ResXmean_hsk.SetMaximum(0.05);
  g_X_ResXmean_hsk.Draw("APE"); g_X_ResXmean_hsk.GetXaxis().SetTitle("X [cm]"); g_X_ResXmean_hsk.GetYaxis().SetTitle("Res X skewness [cm]");
  c1.Update(); c1.SaveAs(folder + "/X_ResXmean_hsk_" + key + suffix)
