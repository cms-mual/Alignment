import ROOT, array, os, sys, re, math, random
from math import *
import numpy as np
from scipy import linalg
sys.path.append('./File_useful/')
print "Usage: python TEST_APEs_Data.py -b"
execfile("geometryXMLparser.py")
execfile("plotscripts.py")
execfile("Util_CalculateCovMatrix.py")

xmlfileAPE        = "Geom/APEs_COV_DT_Data_AllContributions_AllTypesOfApes_6DOF_MCfromHW_cov.xml"
#xmlfileAPE        = "Geom/APEs_COV_t2_DT_Data_AllContributions_AllTypesOfApes_6DOF_MCfromHW_cov.xml"
#xmlfileAPE        = "Geom/APEs_COVfromH_DT_Data_AllContributions_AllTypesOfApes_6DOF_MCfromHW.xml"
#xmlfileAPE        = "Geom/APEs_COVfromH_DT_Data_AllContributions_AllTypesOfApes_6DOF_MCfromHW_covFixsig.xml"

xmlfileFinalGeom  = "Geom/mc_DT-1100-111111_CMSSW_8_0_24_GTasym_45M_8TeV_misall_03.xml"
#xmlfileFinalGeom  = "Geom/mc_DT-1100-111111_CMSSW_8_0_24_GTasym_45M_8TeV_misallFixsigma_03.xml"

xmlfileIdealGeom  = "Geom/muonGeometry_IDEAL_AllZeroes.Ape6x6.StdTags.746p3.DBv2.xml"
g_fin = MuonGeometry(xmlfileFinalGeom)
g_ide = MuonGeometry(xmlfileIdealGeom)
g_ape = MuonGeometry(xmlfileAPE)
debug=True

#Plots
ROOT.gStyle.SetOptStat(111111)
c1 = ROOT.TCanvas()
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
#loop over chambers
Below_95=0; Below_99=0
w0_Below_95=0; w1_Below_95=0; w2_Below_95=0; w0_Below_99=0; w1_Below_99=0; w2_Below_99=0;
s1_Below_95=0; s2_Below_95=0; s3_Below_95=0; s4_Below_95=0; s1_Below_99=0; s2_Below_99=0; s3_Below_99=0; s4_Below_99=0;
for wheel in -2, -1, 0, +1, +2:
  for station in 1, 2, 3, 4:
    sectors = 12
    if (station==4): sectors=14
    for sector in range(1,sectors+1):
      print "\n********************************************************************"
      print "Chamber: wheel = %s, station = %s, sector = %s" % (wheel, station, sector)
      print "********************************************************************"
      #Position of the chmamber. Note: X_fin is cm
      X_fin = g_fin.dt[wheel, station, sector].x#*signConventions["DT", wheel, station, sector][0]
      if ( station != 4 ) : Y_fin = g_fin.dt[wheel, station, sector].y#*signConventions["DT", wheel, station, sector][1]
      else:                 Y_fin = 0.0
      Z_fin = g_fin.dt[wheel, station, sector].z#*signConventions["DT", wheel, station, sector][2]
      PhiX_fin = g_fin.dt[wheel, station, sector].phix
      PhiY_fin = g_fin.dt[wheel, station, sector].phiy
      PhiZ_fin = g_fin.dt[wheel, station, sector].phiz
      #Position Ideal
      X_ide = g_ide.dt[wheel, station, sector].x
      if ( station != 4 ) : Y_ide = g_ide.dt[wheel, station, sector].y
      else:                 Y_ide = 0.0
      Z_ide = g_ide.dt[wheel, station, sector].z
      PhiX_ide = g_ide.dt[wheel, station, sector].phix
      PhiY_ide = g_ide.dt[wheel, station, sector].phiy
      PhiZ_ide = g_ide.dt[wheel, station, sector].phiz     
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
      vec_pos = np.array([[X_fin],[Y_fin],[Z_fin],[PhiX_fin],[PhiY_fin],[PhiZ_fin]])
      vec_ide = np.array([[X_ide],[Y_ide],[Z_ide],[PhiX_ide],[PhiY_ide],[PhiZ_ide]])
      vec_diff = vec_pos - vec_ide
      cov_matrix = np.array([ [XX_ape,XY_ape,XZ_ape,XPhiX_ape,XPhiY_ape,XPhiZ_ape], [XY_ape,YY_ape,YZ_ape,YPhiX_ape,YPhiY_ape,YPhiZ_ape], [XZ_ape,YZ_ape,ZZ_ape,ZPhiX_ape,ZPhiY_ape,ZPhiZ_ape], [XPhiX_ape,YPhiX_ape,ZPhiX_ape,PhiXPhiX_ape,PhiXPhiY_ape,PhiXPhiZ_ape], [XPhiY_ape,YPhiY_ape,ZPhiY_ape,PhiXPhiY_ape,PhiYPhiY_ape,PhiYPhiZ_ape], [XPhiZ_ape,YPhiZ_ape,ZPhiZ_ape,PhiXPhiZ_ape,PhiYPhiZ_ape,PhiZPhiZ_ape,] ])
      if(debug):
        print "Pos:",vec_pos.T
        print "Ide:",vec_ide.T
        print "APE:",cov_matrix
      #Make the maths: (r-r0)COV-1(r-r0)<confid_level -> vec_diff * cov_matrix-1 * vec_diff < 1
      if(is_invertible(cov_matrix)):
        first_prod = linalg.inv(cov_matrix).dot(vec_diff)
        print "Cov_matr-1 * vec_diff = ",first_prod.T
        final_num = np.dot(first_prod.T,vec_diff)
        print "Final: ",final_num
        h_Ellipse_tot.Fill(float(final_num))
        h_Ellipse_tot_w_s[wheel+2][station-1].Fill(float(final_num))
        h_Ellipse_tot_w_s_symm[abs(int(wheel))][station-1].Fill(float(final_num))
        h_Ellipse_tot_w[abs(int(wheel))].Fill(float(final_num))
        h_Ellipse_tot_s[station-1].Fill(float(final_num))
        if(final_num<3.85): Below_95=Below_95+1
        if(final_num<6.65): Below_99=Below_99+1
        if(final_num<3.85 and abs(int(wheel))==0): w0_Below_95=w0_Below_95+1
        if(final_num<3.85 and abs(int(wheel))==1): w1_Below_95=w1_Below_95+1
        if(final_num<3.85 and abs(int(wheel))==2): w2_Below_95=w2_Below_95+1
        if(final_num<6.65 and abs(int(wheel))==0): w0_Below_99=w0_Below_99+1
        if(final_num<6.65 and abs(int(wheel))==1): w1_Below_99=w1_Below_99+1
        if(final_num<6.65 and abs(int(wheel))==2): w2_Below_99=w2_Below_99+1
        if(final_num<3.85 and station==1): s1_Below_95=s1_Below_95+1
        if(final_num<3.85 and station==2): s2_Below_95=s2_Below_95+1
        if(final_num<3.85 and station==3): s3_Below_95=s3_Below_95+1
        if(final_num<3.85 and station==4): s4_Below_95=s4_Below_95+1
        if(final_num<6.65 and station==1): s1_Below_99=s1_Below_99+1
        if(final_num<6.65 and station==2): s2_Below_99=s2_Below_99+1
        if(final_num<6.65 and station==3): s3_Below_99=s3_Below_99+1
        if(final_num<6.65 and station==4): s4_Below_99=s4_Below_99+1
      else:
        print "SINGULAR MATRIX"
        h_Ellipse_tot.Fill(-1.)
print "0.95% is actually: ",float(Below_95)/250.
print "0.99% is actually: ",float(Below_99)/250.
print "Wheel 0: 0.95% is actually: ",float(w0_Below_95)/50.
print "Wheel 1: 0.95% is actually: ",float(w1_Below_95)/100.
print "Wheel 2: 0.95% is actually: ",float(w2_Below_95)/100.
print "Wheel 0: 0.99% is actually: ",float(w0_Below_99)/50.
print "Wheel 1: 0.99% is actually: ",float(w1_Below_99)/100.
print "Wheel 2: 0.99% is actually: ",float(w2_Below_99)/100.
print "Station 1: 0.95% is actually: ",float(s1_Below_95)/60.
print "Station 2: 0.95% is actually: ",float(s2_Below_95)/60.
print "Station 3: 0.95% is actually: ",float(s3_Below_95)/60.
print "Station 4: 0.95% is actually: ",float(s4_Below_95)/70.
print "Station 1: 0.99% is actually: ",float(s1_Below_99)/60.
print "Station 2: 0.99% is actually: ",float(s2_Below_99)/60.
print "Station 3: 0.99% is actually: ",float(s3_Below_99)/60.
print "Station 4: 0.99% is actually: ",float(s4_Below_99)/70.

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
