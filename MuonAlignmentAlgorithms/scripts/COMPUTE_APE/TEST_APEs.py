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
c1 = ROOT.TCanvas()
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
    limits = []
    limits.append(Min_X_diff); limits.append(Max_X_diff); limits.append(Min_Y_diff); limits.append(Max_Y_diff);
    All_lim[wheel+2][station-1][0]=limits; 
    limits[0]=Min_X_diff; limits[1]=Max_X_diff; limits[2]=Min_Z_diff; limits[3]=Max_Z_diff;
    All_lim[wheel+2][station-1][1]=limits;
    limits[0]=Min_X_diff; limits[1]=Max_X_diff; limits[2]=Min_PhiX_diff; limits[3]=Max_PhiX_diff;
    All_lim[wheel+2][station-1][2]=limits;
    limits[0]=Min_X_diff; limits[1]=Max_X_diff; limits[2]=Min_PhiY_diff; limits[3]=Max_PhiY_diff;
    All_lim[wheel+2][station-1][3]=limits; 
    limits[0]=Min_X_diff; limits[1]=Max_X_diff; limits[2]=Min_PhiZ_diff; limits[3]=Max_PhiZ_diff;
    All_lim[wheel+2][station-1][4]=limits;
    limits[0]=Min_Y_diff; limits[1]=Max_Y_diff; limits[2]=Min_Z_diff; limits[3]=Max_Z_diff;
    All_lim[wheel+2][station-1][5]=limits; 
    limits[0]=Min_Y_diff; limits[1]=Max_Y_diff; limits[2]=Min_PhiX_diff; limits[3]=Max_PhiX_diff;
    All_lim[wheel+2][station-1][6]=limits; 
    limits[0]=Min_Y_diff; limits[1]=Max_Y_diff; limits[2]=Min_PhiY_diff; limits[3]=Max_PhiY_diff;
    All_lim[wheel+2][station-1][7]=limits;
    limits[0]=Min_Y_diff; limits[1]=Max_Y_diff; limits[2]=Min_PhiZ_diff; limits[3]=Max_PhiZ_diff;
    All_lim[wheel+2][station-1][8]=limits; 
    limits[0]=Min_Z_diff; limits[1]=Max_Z_diff; limits[2]=Min_PhiX_diff; limits[3]=Max_PhiX_diff;
    All_lim[wheel+2][station-1][9]=limits; 
    limits[0]=Min_Z_diff; limits[1]=Max_Z_diff; limits[2]=Min_PhiY_diff; limits[3]=Max_PhiY_diff;
    All_lim[wheel+2][station-1][10]=limits; 
    limits[0]=Min_Z_diff; limits[1]=Max_Z_diff; limits[2]=Min_PhiZ_diff; limits[3]=Max_PhiZ_diff;
    All_lim[wheel+2][station-1][11]=limits; 
    limits[0]=Min_PhiX_diff; limits[1]=Max_PhiX_diff; limits[2]=Min_PhiY_diff; limits[3]=Max_PhiY_diff;
    All_lim[wheel+2][station-1][12]=limits; 
    limits[0]=Min_PhiX_diff; limits[1]=Max_PhiX_diff; limits[2]=Min_PhiZ_diff; limits[3]=Max_PhiZ_diff;
    All_lim[wheel+2][station-1][13]=limits; 
    limits[0]=Min_PhiY_diff; limits[1]=Max_PhiY_diff; limits[2]=Min_PhiZ_diff; limits[3]=Max_PhiZ_diff;
    All_lim[wheel+2][station-1][14]=limits; 
my_bins = 100
h_2Dellipse = [];
for wheel in -2, -1, 0, 1, 2:
  h_2Dellipse.append([])
  for station in 1, 2, 3, 4:
    h_2Dellipse[wheel+2].append([])
    for nEll in range(len(Var)):
      name = "h_2Dellipse_" + str(wheel) + "_" + str(station) + "_" + Var[nEll]
      min1 = All_lim[wheel+2][station-1][nEll][0] * 2. 
      max1 = All_lim[wheel+2][station-1][nEll][1] * 2.
      min2 = All_lim[wheel+2][station-1][nEll][2] * 2.
      max2 = All_lim[wheel+2][station-1][nEll][3] * 2.
      h_2Dellipse[wheel+2][station-1].append( ROOT.TH2F(name, "", my_bins, min1, max1, my_bins, min2, max2) )
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
      h_2Dellipse[wheel+2][station-1][Variable].Draw()
      name = "Wheel_" + str(wheel) + "Station_" + str(station) + "Var_" + Var[Variable]
      c1.SaveAs("Plots/DrawingEllipses/"+name+".png")

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

