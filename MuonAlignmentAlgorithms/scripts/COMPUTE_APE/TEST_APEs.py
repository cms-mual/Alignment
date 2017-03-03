import ROOT, array, os, sys, re, math, random, subprocess
from math import *
import numpy as np
from scipy import linalg
sys.path.append('./File_useful/')
print "Usage: python TEST_APEs_Data.py -b"
execfile("File_useful/geometryXMLparser.py")
execfile("File_useful/plotscripts.py")
execfile("File_useful/Util_CalculateCovMatrix.py")

#xmlfileAPE        = "Geom/APEs_COV_DT_Data_AllContributions_AllTypesOfApes_6DOF_MCfromHW_cov.xml"
#xmlfileAPE        = "Geom/APEs_COV_t2_DT_Data_AllContributions_AllTypesOfApes_6DOF_MCfromHW_cov.xml"
xmlfileAPE        = "Geom/APEs_COVfromH_DT_Data_AllContributions_AllTypesOfApes_6DOF_MCfromHW.xml"
#xmlfileAPE        = "Geom/MuonAPE_asympt_My_VariancesAndCovariances_DT_6DOF_Simranjit.xml"
xmlfileFinalGeom  = "Geom/mc_DT-1100-111111_CMSSW_8_0_24_GTasym_45M_8TeV_misall_03.xml"
xmlfileIdealGeom  = "Geom/muonGeometry_IDEAL_AllZeroes.Ape6x6.StdTags.746p3.DBv2.xml"
g_fin = MuonGeometry(xmlfileFinalGeom)
g_ide = MuonGeometry(xmlfileIdealGeom)
g_ape = MuonGeometry(xmlfileAPE)
debug=True

ROOT.gStyle.SetOptStat(111111)
c1 = ROOT.TCanvas(); c1.cd()
folderCreation  = subprocess.Popen(['mkdir -p Plots/'], stdout=subprocess.PIPE, shell=True); folderCreation.communicate()
folderCreation  = subprocess.Popen(['mkdir -p Plots/DrawingEllipses'], stdout=subprocess.PIPE, shell=True); folderCreation.communicate()
# Coverage Plots
range_h=20
h_Ellipse_tot          = ROOT.TH1F("Ellipse","",range_h,0,range_h); h_Ellipse_tot.GetXaxis().SetTitle("Confidence interval")
h_Ellipse_tot_w_s      = [[ROOT.TH1F() for i in range(4)] for j in range(5)] #4 stations, 5 wheels (-2,-1,0,1,2)
h_Ellipse_tot_w_s_symm = [[ROOT.TH1F() for i in range(4)] for j in range(3)] #4 stations, 3 wheels (0,+-1,+-2)
h_Ellipse_tot_w        = [ROOT.TH1F() for i in range(3)] #only 3 wheels (0,+-1,+-2)
h_Ellipse_tot_s        = [ROOT.TH1F() for i in range(4)] #only 4 stations
for wheel in -2, -1, 0, +1, +2:
  for station in 1, 2, 3, 4:
    name="_wheel"+str(wheel+2)+"+stat_"+str(station-1)
    h_Ellipse_tot_w_s[int(wheel+2)][int(station-1)] = ROOT.TH1F("Ellipse"+name,"",range_h,0,range_h); h_Ellipse_tot_w_s[int(wheel+2)][int(station-1)].GetXaxis().SetTitle("Confidence interval")
for wheel in 0, 1, 2:
  name="_wheel"+str(wheel)
  h_Ellipse_tot_w[int(wheel)] = ROOT.TH1F("Ellipse"+name,"",range_h,0,range_h); h_Ellipse_tot_w[int(wheel)].GetXaxis().SetTitle("Confidence interval")
for station in 1, 2, 3, 4:
  name="_+stat_"+str(station)
  h_Ellipse_tot_s[int(station-1)] = ROOT.TH1F("Ellipse"+name,"",range_h,0,range_h); h_Ellipse_tot_s[int(station-1)].GetXaxis().SetTitle("Confidence interval")
for wheel in 0, 1, 2:
  for station in 1, 2, 3, 4:
    name="sym__wheel"+str(wheel)+"+stat_"+str(station)
    h_Ellipse_tot_w_s_symm[int(wheel)][int(station-1)] = ROOT.TH1F("Ellipse"+name,"",range_h,0,range_h); h_Ellipse_tot_w_s_symm[int(wheel)][int(station-1)].GetXaxis().SetTitle("Confidence interval")
# Variable to plots in Histograms with ellipses
Var = []; Var.append("XY"); Var.append("XZ"); Var.append("XPhiX"); Var.append("XPhiY"); Var.append("XPhiZ"); Var.append("YZ"); Var.append("YPhiX"); Var.append("YPhiY"); Var.append("YPhiZ"); Var.append("ZPhiX"); Var.append("ZPhiY"); Var.append("ZPhiZ"); Var.append("PhiXPhiY"); Var.append("PhiXPhiZ"); Var.append("PhiYPhiZ");
All_lim = [];
for wheel in -2, -1, 0, +1, +2:
  All_lim.append([])
  for station in 1, 2, 3, 4:
    All_lim[wheel+2].append([])
    for variable in range(len(Var)):
      All_lim[wheel+2][station-1].append(None)
for wheel in -2, -1, 0, +1, +2:
  for station in 1, 2, 3, 4:
    Max_X_diff=-1000; Max_Y_diff=-1000; Max_Z_diff=-1000; Max_PhiX_diff=-1000; Max_PhiY_diff=-1000; Max_PhiZ_diff=-1000;
    Min_X_diff=1000; Min_Y_diff=1000; Min_Z_diff=1000; Min_PhiX_diff=1000; Min_PhiY_diff=1000; Min_PhiZ_diff=1000;
    sectors = 12
    if (station==4): sectors=14
    for sector in range(1,sectors+1):
      #Position of the chamber. Note: cm and rad
      X_diff    = (g_fin.dt[wheel, station, sector].x    - g_ide.dt[wheel, station, sector].x)*signConventions["DT", wheel, station, sector][0]
      if ( station != 4 ) : Y_diff = (g_fin.dt[wheel, station, sector].y - g_ide.dt[wheel, station, sector].y)*signConventions["DT", wheel, station, sector][1]
      else:                 Y_diff = 0.0
      Z_diff    = (g_fin.dt[wheel, station, sector].z    - g_ide.dt[wheel, station, sector].z)*signConventions["DT", wheel, station, sector][2]
      PhiX_diff = (g_fin.dt[wheel, station, sector].phix - g_ide.dt[wheel, station, sector].phix)
      PhiY_diff = (g_fin.dt[wheel, station, sector].phiy - g_ide.dt[wheel, station, sector].phiy)
      PhiZ_diff = (g_fin.dt[wheel, station, sector].phiz - g_ide.dt[wheel, station, sector].phiz)   
      if(X_diff>Max_X_diff): Max_X_diff = X_diff
      if(Y_diff>Max_Y_diff): Max_Y_diff = Y_diff
      if(Z_diff>Max_Z_diff): Max_Z_diff = Z_diff
      if(PhiX_diff>Max_PhiX_diff): Max_PhiX_diff = PhiX_diff
      if(PhiY_diff>Max_PhiY_diff): Max_PhiY_diff = PhiY_diff
      if(PhiZ_diff>Max_PhiZ_diff): Max_PhiZ_diff = PhiZ_diff
      if(X_diff<Min_X_diff): Min_X_diff = X_diff
      if(Y_diff<Min_Y_diff): Min_Y_diff = Y_diff
      if(Z_diff<Min_Z_diff): Min_Z_diff = Z_diff
      if(PhiX_diff<Min_PhiX_diff): Min_PhiX_diff = PhiX_diff
      if(PhiY_diff<Min_PhiY_diff): Min_PhiY_diff = PhiY_diff
      if(PhiZ_diff<Min_PhiZ_diff): Min_PhiZ_diff = PhiZ_diff
    All_lim[wheel+2][station-1][0]=[Min_X_diff,Max_X_diff,Min_Y_diff,Max_Y_diff]
    All_lim[wheel+2][station-1][1]=[Min_X_diff,Max_X_diff,Min_Z_diff,Max_Z_diff]
    All_lim[wheel+2][station-1][2]=[Min_X_diff,Max_X_diff,Min_PhiX_diff,Max_PhiX_diff]
    All_lim[wheel+2][station-1][3]=[Min_X_diff,Max_X_diff,Min_PhiY_diff,Max_PhiY_diff] 
    All_lim[wheel+2][station-1][4]=[Min_X_diff,Max_X_diff,Min_PhiZ_diff,Max_PhiZ_diff]
    All_lim[wheel+2][station-1][5]=[Min_Y_diff,Max_Y_diff,Min_Z_diff,Max_Z_diff]
    All_lim[wheel+2][station-1][6]=[Min_Y_diff,Max_Y_diff,Min_PhiX_diff,Max_PhiX_diff] 
    All_lim[wheel+2][station-1][7]=[Min_Y_diff,Max_Y_diff,Min_PhiY_diff,Max_PhiY_diff]
    All_lim[wheel+2][station-1][8]=[Min_Y_diff,Max_Y_diff,Min_PhiZ_diff,Max_PhiZ_diff] 
    All_lim[wheel+2][station-1][9]=[Min_Z_diff,Max_Z_diff,Min_PhiX_diff,Max_PhiX_diff] 
    All_lim[wheel+2][station-1][10]=[Min_Z_diff,Max_Z_diff,Min_PhiY_diff,Max_PhiY_diff] 
    All_lim[wheel+2][station-1][11]=[Min_Z_diff,Max_Z_diff,Min_PhiZ_diff,Max_PhiZ_diff] 
    All_lim[wheel+2][station-1][12]=[Min_PhiX_diff,Max_PhiX_diff,Min_PhiY_diff,Max_PhiY_diff] 
    All_lim[wheel+2][station-1][13]=[Min_PhiX_diff,Max_PhiX_diff,Min_PhiZ_diff,Max_PhiZ_diff] 
    All_lim[wheel+2][station-1][14]=[Min_PhiY_diff,Max_PhiY_diff,Min_PhiZ_diff,Max_PhiZ_diff] 
my_bins = 100
h_2Dellipse = [];
for wheel in -2, -1, 0, 1, 2:
  h_2Dellipse.append([])
  for station in 1, 2, 3, 4:
    h_2Dellipse[wheel+2].append([])
    for nEll in range(len(Var)):
      name = "h_2Dellipse_" + str(wheel) + "_" + str(station) + "_" + Var[nEll]
      minX = All_lim[wheel+2][station-1][nEll][0] * 2.
      maxX = All_lim[wheel+2][station-1][nEll][1] * 2.
      minY = All_lim[wheel+2][station-1][nEll][2] * 2.
      maxY = All_lim[wheel+2][station-1][nEll][3] * 2.
      if(fabs(minX)>fabs(maxX)): maxX = fabs(minX)
      if(fabs(minX)<fabs(maxX)): minX = -fabs(maxX)
      if(fabs(minY)>fabs(maxY)): maxY = fabs(minY)
      if(fabs(minY)<fabs(maxY)): minY = -fabs(maxY)
      h_2Dellipse[wheel+2][station-1].append( ROOT.TH2F(name, "", my_bins, minX, maxX, my_bins, minY, maxY) )
      XaxisN=Var[nEll][0];    YaxisN=Var[nEll][1];
      if(len(Var[nEll])==5):  XaxisN=Var[nEll][0];   YaxisN=Var[nEll][1:];
      elif(len(Var[nEll])>5): XaxisN=Var[nEll][0:4]; YaxisN=Var[nEll][4:];
      h_2Dellipse[wheel+2][station-1][nEll].GetXaxis().SetTitle(XaxisN)
      h_2Dellipse[wheel+2][station-1][nEll].GetYaxis().SetTitle(YaxisN)

#loop over chambers
for wheel in -2, -1, 0, +1, +2:
  for station in 1, 2, 3, 4:
    sectors = 12
    if (station==4): sectors=14
    for sector in range(1,sectors+1):
      print "\n********************************************************************"
      print "Chamber: wheel = %s, station = %s, sector = %s" % (wheel, station, sector)
      print "********************************************************************"
      #Position of the chamber. Note: cm and rad
      X_diff    = (g_fin.dt[wheel, station, sector].x    - g_ide.dt[wheel, station, sector].x)*signConventions["DT", wheel, station, sector][0]
      if ( station != 4 ) : Y_diff = (g_fin.dt[wheel, station, sector].y - g_ide.dt[wheel, station, sector].y)*signConventions["DT", wheel, station, sector][1]
      else:                 Y_diff = 0.0
      Z_diff    = (g_fin.dt[wheel, station, sector].z    - g_ide.dt[wheel, station, sector].z)*signConventions["DT", wheel, station, sector][2]
      PhiX_diff = (g_fin.dt[wheel, station, sector].phix - g_ide.dt[wheel, station, sector].phix)
      PhiY_diff = (g_fin.dt[wheel, station, sector].phiy - g_ide.dt[wheel, station, sector].phiy)
      PhiZ_diff = (g_fin.dt[wheel, station, sector].phiz - g_ide.dt[wheel, station, sector].phiz)
      #APE value
      XX_ape       = g_ape.dt[wheel, station, sector].xx
      XY_ape       = g_ape.dt[wheel, station, sector].xy
      XZ_ape       = g_ape.dt[wheel, station, sector].xz
      YY_ape       = g_ape.dt[wheel, station, sector].yy
      YZ_ape       = g_ape.dt[wheel, station, sector].yz
      ZZ_ape       = g_ape.dt[wheel, station, sector].zz
      XPhiX_ape    = g_ape.dt[wheel, station, sector].xa
      XPhiY_ape    = g_ape.dt[wheel, station, sector].xb
      XPhiZ_ape    = g_ape.dt[wheel, station, sector].xc
      YPhiX_ape    = g_ape.dt[wheel, station, sector].ya
      YPhiY_ape    = g_ape.dt[wheel, station, sector].yb
      YPhiZ_ape    = g_ape.dt[wheel, station, sector].yc
      ZPhiX_ape    = g_ape.dt[wheel, station, sector].za
      ZPhiY_ape    = g_ape.dt[wheel, station, sector].zb
      ZPhiZ_ape    = g_ape.dt[wheel, station, sector].zc
      PhiXPhiX_ape = g_ape.dt[wheel, station, sector].aa
      PhiXPhiY_ape = g_ape.dt[wheel, station, sector].ab
      PhiXPhiZ_ape = g_ape.dt[wheel, station, sector].ac
      PhiYPhiY_ape = g_ape.dt[wheel, station, sector].bb
      PhiYPhiZ_ape = g_ape.dt[wheel, station, sector].bc
      PhiZPhiZ_ape = g_ape.dt[wheel, station, sector].cc
      #Write the components
      vec_diff = np.array([[X_diff],[Y_diff],[Z_diff],[PhiX_diff],[PhiY_diff],[PhiZ_diff]])
      cov_matrix = np.array([ [XX_ape,XY_ape,XZ_ape,XPhiX_ape,XPhiY_ape,XPhiZ_ape], [XY_ape,YY_ape,YZ_ape,YPhiX_ape,YPhiY_ape,YPhiZ_ape], [XZ_ape,YZ_ape,ZZ_ape,ZPhiX_ape,ZPhiY_ape,ZPhiZ_ape], [XPhiX_ape,YPhiX_ape,ZPhiX_ape,PhiXPhiX_ape,PhiXPhiY_ape,PhiXPhiZ_ape], [XPhiY_ape,YPhiY_ape,ZPhiY_ape,PhiXPhiY_ape,PhiYPhiY_ape,PhiYPhiZ_ape], [XPhiZ_ape,YPhiZ_ape,ZPhiZ_ape,PhiXPhiZ_ape,PhiYPhiZ_ape,PhiZPhiZ_ape,] ])
      if(debug):
        print "Pos:",vec_diff.T
        print "APE:",cov_matrix
      #Make the maths: (r-r0)COV-1(r-r0)<confid_level -> vec_diff * cov_matrix-1 * vec_diff < 1
      if(is_invertible(cov_matrix)):
        first_prod = linalg.inv(cov_matrix).dot(vec_diff)
        if debug : print "Cov_matr-1 * vec_diff = ",first_prod.T
        final_num = np.dot(first_prod.T,vec_diff)
        if debug : print "Final: ",final_num
        h_Ellipse_tot.Fill(float(final_num))
        h_Ellipse_tot_w_s[wheel+2][station-1].Fill(float(final_num))
        h_Ellipse_tot_w_s_symm[abs(int(wheel))][station-1].Fill(float(final_num))
        h_Ellipse_tot_w[abs(int(wheel))].Fill(float(final_num))
        h_Ellipse_tot_s[station-1].Fill(float(final_num))
      else:
        print "SINGULAR MATRIX"
        h_Ellipse_tot.Fill(-1.)
      #Fill the Histograms
      h_2Dellipse[wheel+2][station-1][0].Fill(X_diff, Y_diff)
      h_2Dellipse[wheel+2][station-1][1].Fill(X_diff, Z_diff)
      h_2Dellipse[wheel+2][station-1][2].Fill(X_diff, PhiX_diff)
      h_2Dellipse[wheel+2][station-1][3].Fill(X_diff, PhiY_diff)
      h_2Dellipse[wheel+2][station-1][4].Fill(X_diff, PhiZ_diff)
      h_2Dellipse[wheel+2][station-1][5].Fill(Y_diff, Z_diff)
      h_2Dellipse[wheel+2][station-1][6].Fill(Y_diff, PhiX_diff)
      h_2Dellipse[wheel+2][station-1][7].Fill(Y_diff, PhiY_diff)
      h_2Dellipse[wheel+2][station-1][8].Fill(Y_diff, PhiZ_diff)
      h_2Dellipse[wheel+2][station-1][9].Fill(Z_diff, PhiX_diff)
      h_2Dellipse[wheel+2][station-1][10].Fill(Z_diff, PhiY_diff)
      h_2Dellipse[wheel+2][station-1][11].Fill(Z_diff, PhiZ_diff)
      h_2Dellipse[wheel+2][station-1][12].Fill(PhiX_diff, PhiY_diff)
      h_2Dellipse[wheel+2][station-1][13].Fill(PhiX_diff, PhiZ_diff)
      h_2Dellipse[wheel+2][station-1][14].Fill(PhiY_diff, PhiZ_diff)
    for Variable in range(len(Var)):
      # Overimposing COV matrix
      if(Variable==0): cov1 = np.array([ [XX_ape,XY_ape], [XY_ape,YY_ape] ])
      if(Variable==1): cov1 = np.array([ [XX_ape,XZ_ape], [XZ_ape,ZZ_ape] ])
      if(Variable==2): cov1 = np.array([ [XX_ape,XPhiX_ape], [XPhiX_ape,PhiXPhiX_ape] ])
      if(Variable==3): cov1 = np.array([ [XX_ape,XPhiY_ape], [XPhiY_ape,PhiYPhiY_ape] ])
      if(Variable==4): cov1 = np.array([ [XX_ape,XPhiZ_ape], [XPhiZ_ape,PhiZPhiZ_ape] ])
      if(Variable==5): cov1 = np.array([ [YY_ape,YZ_ape], [YZ_ape,ZZ_ape] ])
      if(Variable==6): cov1 = np.array([ [YY_ape,YPhiX_ape], [YPhiX_ape,PhiXPhiX_ape] ])
      if(Variable==7): cov1 = np.array([ [YY_ape,YPhiY_ape], [YPhiY_ape,PhiYPhiY_ape] ])
      if(Variable==8): cov1 = np.array([ [YY_ape,YPhiZ_ape], [YPhiZ_ape,PhiZPhiZ_ape] ])
      if(Variable==9): cov1 = np.array([ [ZZ_ape,ZPhiX_ape], [ZPhiX_ape,PhiXPhiX_ape] ])
      if(Variable==10): cov1 = np.array([ [ZZ_ape,ZPhiY_ape], [ZPhiY_ape,PhiYPhiY_ape] ])
      if(Variable==11): cov1 = np.array([ [ZZ_ape,ZPhiZ_ape], [ZPhiZ_ape,PhiZPhiZ_ape] ])
      if(Variable==12): cov1 = np.array([ [PhiXPhiX_ape,PhiXPhiY_ape], [PhiXPhiY_ape,PhiYPhiY_ape] ])
      if(Variable==13): cov1 = np.array([ [PhiXPhiX_ape,PhiXPhiZ_ape], [PhiXPhiZ_ape,PhiZPhiZ_ape] ])
      if(Variable==14): cov1 = np.array([ [PhiYPhiY_ape,PhiYPhiZ_ape], [PhiYPhiZ_ape,PhiZPhiZ_ape] ])
      #cov1_x, cov1_y = np.random.multivariate_normal([0, 0], cov1, 9000).T
      minX = h_2Dellipse[wheel+2][station-1][Variable].GetXaxis().GetBinCenter(1) - h_2Dellipse[wheel+2][station-1][Variable].GetXaxis().GetBinWidth(1)
      maxX = h_2Dellipse[wheel+2][station-1][Variable].GetXaxis().GetBinCenter(h_2Dellipse[wheel+2][station-1][Variable].GetNbinsX()) + h_2Dellipse[wheel+2][station-1][Variable].GetXaxis().GetBinWidth(1)
      minY = h_2Dellipse[wheel+2][station-1][Variable].GetYaxis().GetBinCenter(1) - h_2Dellipse[wheel+2][station-1][Variable].GetYaxis().GetBinWidth(1)
      maxY = h_2Dellipse[wheel+2][station-1][Variable].GetXaxis().GetBinCenter(h_2Dellipse[wheel+2][station-1][Variable].GetNbinsX()) + h_2Dellipse[wheel+2][station-1][Variable].GetXaxis().GetBinWidth(1)
      #h_cov1 = ROOT.TH2F(h_2Dellipse[wheel+2][station-1][Variable].GetName()+"_cov1","",my_bins, minX, maxX, my_bins, minY, maxY)
      #h_cov1.SetLineColor(2); h_cov1.SetFillColor(2); h_cov1.SetMarkerColor(2); h_cov1.SetLineColorAlpha(2, .3); h_cov1.SetFillColorAlpha(2, .3); h_cov1.SetMarkerColorAlpha(2, .3);
      #for myCov in range(len(cov1_x)): h_cov1.Fill( cov1_x[myCov], cov1_y[myCov] )
      c1.cd()
      h_2Dellipse[wheel+2][station-1][Variable].Draw()
#! NOW IT WORKS.
#! THE ONLY 3 VALUES YOU HAVE TO FIND AND CHANGE ARE: R1, R2 and Theta. I did it quickly, maybe you can check if it is fine or not
#! cov1 is the covariance matrix, so you have to take this infor from there.
      eigh_value1 = np.linalg.eigvals(cov1)[0]
      eigh_value2 = np.linalg.eigvals(cov1)[1]
      #eigh_vec1 = np.linalg.eigvals(cov1)
      #eigh_vec2 = np.linalg.eigvals(cov1)
      R1_95 = sqrt(5.991*eigh_value1)
      R2_95 = sqrt(5.991*eigh_value2)
      R1_90 = sqrt(4.605*eigh_value1)
      R2_90 = sqrt(4.605*eigh_value2)
      theta = np.arctan(eigh_value1/eigh_value2)
      ellipse_95 = ROOT.TEllipse(0., 0., R1_95, R2_95, 0, 360, theta); ellipse_95.SetLineColor(2); ellipse_95.SetFillColor(0); ellipse_95.SetFillColorAlpha(2,0.);
      ellipse_95.Draw("same")
      ellipse_90 = ROOT.TEllipse(0., 0., R1_90, R2_90, 0, 360, theta); ellipse_90.SetLineColor(2); ellipse_90.SetFillColor(0); ellipse_90.SetFillColorAlpha(2,0.);
      ellipse_90.Draw("same")
      name = "Wheel_" + str(wheel) + "Station_" + str(station) + "Var_" + Var[Variable]
      c1.SaveAs("Plots/DrawingEllipses/"+name+".pdf")

pdf = ROOT.TF1("pdf","ROOT::Math::chisquared_pdf(x, 6, 0)*250",0,range_h);
pdf.SetLineColor(2);
pdf2 = ROOT.TF1("pdf","ROOT::Math::chisquared_pdf(x, 8, 0)*250",0,range_h);
pdf2.SetLineColor(4);
pdf3 = ROOT.TF1("pdf","ROOT::Math::chisquared_pdf(x, 14, 0)*250",0,range_h);
pdf3.SetLineColor(3);
h_Ellipse_tot.Draw()
pdf.Draw("same"); pdf2.Draw("same"); pdf3.Draw("same");
c1.SaveAs("Plots/A_EllipseValue.png")
for wheel in -2, -1, 0, +1, +2:
  for station in 1, 2, 3, 4:
    h_Ellipse_tot_w_s[wheel+2][station-1].Draw()
    name="_wheel"+str(wheel)+"_station_"+str(station)
    c1.SaveAs("Plots/B_EllipseValue"+name+".png")
for wheel in 0, 1, 2:
  h_Ellipse_tot_w[wheel].Draw()
  name="_wheel"+str(wheel)
  c1.SaveAs("Plots/E_EllipseValue"+name+".png")
for station in 1, 2, 3, 4:
  h_Ellipse_tot_s[station-1].Draw()
  name="_station_"+str(station)
  c1.SaveAs("Plots/D_EllipseValue"+name+".png")
for wheel in 0, 1, 2:
  for station in 1, 2, 3, 4:
    h_Ellipse_tot_w_s_symm[wheel][station-1].Draw()
    name="Sym_wheel"+str(wheel)+"_station_"+str(station)
    c1.SaveAs("Plots/C_EllipseValue"+name+".png")

