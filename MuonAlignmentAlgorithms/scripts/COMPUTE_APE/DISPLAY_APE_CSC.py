import ROOT, array, os, sys, re, math, random, subprocess
from math import *
import numpy as np
from scipy import linalg
sys.path.append('./File_useful/')
print "Usage: python DISPLAY_APE.py -b"
execfile("File_useful/geometryXMLparser.py")
execfile("File_useful/plotscripts.py")
#xmlfileAPE2        = "Geom/APEs_COV_DT_Data_AllContributions_AllTypesOfApes_6DOF_MCfromHW_cov.xml"
#xmlfileAPE2        = "Geom/APEs_COV_t2_DT_Data_AllContributions_AllTypesOfApes_6DOF_MCfromHW_cov.xml"
xmlfileAPE1        = "Geom/APEs_COVfromH_CSC_3DOF_MCfromHW_for2017Data.xml"
xmlfileAPE2        = "Geom/APEs_COVfromH_CSC_3DOF_MCfromHW_for2017Data.xml"
g_ape1 = MuonGeometry(xmlfileAPE1)
g_ape2 = MuonGeometry(xmlfileAPE2)
g_apes = []; g_apes.append(g_ape1); g_apes.append(g_ape2)
#myText="Circle: My APE from Histos; Cross: Simranjit's APE"
#myText="Circle: My APE from Histos; Cross: My APE from MINUITx2"
myText="APE asymptotic"

# Divide Canvas in 4
ROOT.gStyle.SetOptStat(0)
c1 = ROOT.TCanvas("c1","multipads",900,700);
c1.SetBottomMargin(.25);
c1.SetTopMargin(.15);
c1.Divide(1,4,0,0)
folderCreation  = subprocess.Popen(['mkdir -p Display_CSC/'], stdout=subprocess.PIPE, shell=True); folderCreation.communicate()

# Variables to plots
Var = [];
Var.append("XX"); Var.append("XY"); Var.append("XZ"); Var.append("XPhiX"); Var.append("XPhiY"); Var.append("XPhiZ"); Var.append("YY"); Var.append("YZ"); Var.append("YPhiX"); Var.append("YPhiY"); Var.append("YPhiZ"); Var.append("ZZ"); Var.append("ZPhiX"); Var.append("ZPhiY"); Var.append("ZPhiZ"); Var.append("PhiXPhiX"); Var.append("PhiXPhiY"); Var.append("PhiXPhiZ"); Var.append("PhiYPhiY"); Var.append("PhiYPhiZ"); Var.append("PhiZPhiZ");
Var.append("XY_corr"); Var.append("XZ_corr"); Var.append("XPhiX_corr"); Var.append("XPhiY_corr"); Var.append("XPhiZ_corr"); Var.append("YZ_corr"); Var.append("YPhiX_corr"); Var.append("YPhiY_corr"); Var.append("YPhiZ_corr"); Var.append("ZPhiX_corr"); Var.append("ZPhiY_corr"); Var.append("ZPhiZ_corr"); Var.append("PhiXPhiY_corr"); Var.append("PhiXPhiZ_corr"); Var.append("PhiYPhiZ_corr");
Names_histo = []
Names_histo.append("#sigma(x) [mm]");  Names_histo.append("#sigma(xy) [mm^2]"); Names_histo.append("#sigma(xz) [mm^2]"); Names_histo.append("#sigma(x#phi_{x}) [mm*mrad]"); Names_histo.append("#sigma(x#phi_{y}) [mm*mrad]"); Names_histo.append("#sigma(x#phi_{z}) [mm*mrad]"); Names_histo.append("#sigma(y) [mm]"); Names_histo.append("#sigma(yz) [mm^2]"); Names_histo.append("#sigma(y#phi_{x}) [mm*mrad]"); Names_histo.append("#sigma(y#phi_{y}) [mm*mrad]"); Names_histo.append("#sigma(y#phi_{z}) [mm*mrad]"); Names_histo.append("#sigma(z) [mm]"); Names_histo.append("#sigma(z#phi_{x}) [mm*mrad]"); Names_histo.append("#sigma(z#phi_{y}) [mm*mrad]"); Names_histo.append("#sigma(z#phi_{z}) [mm*mrad]"); Names_histo.append("#sigma(#phi_{x}) [mrad]"); Names_histo.append("#sigma(#phi_{x}#phi_{y}) [mrad*mrad]"); Names_histo.append("#sigma(#phi_{x}#phi_{z}) [mrad*mrad]"); Names_histo.append("#sigma(#phi_{y}) [mrad]"); Names_histo.append("#sigma(#phi_{y}#phi_{z}) [mrad*mrad]"); Names_histo.append("#sigma(#phi_{z}) [mrad]");
Names_histo.append("Corr(xy)"); Names_histo.append("Corr(xz)"); Names_histo.append("Corr(x#phi_{x})"); Names_histo.append("Corr(x#phi_{y})"); Names_histo.append("Corr(x#phi_{z})"); Names_histo.append("Corr(yz)"); Names_histo.append("Corr(y#phi_{x})"); Names_histo.append("Corr(y#phi_{y})"); Names_histo.append("Corr(y#phi_{z})"); Names_histo.append("Corr(z#phi_{x})"); Names_histo.append("Corr(z#phi_{y})"); Names_histo.append("Corr(z#phi_{z})"); Names_histo.append("Corr(#phi_{x}#phi_{y})"); Names_histo.append("Corr(#phi_{x}#phi_{z})"); Names_histo.append("Corr(#phi_{y}#phi_{z})");
# Find Histo Max and Min
Max_XX_ape=0; Max_XY_ape=0; Max_XZ_ape=0; Max_XPhiX_ape=0; Max_XPhiY_ape=0; Max_XPhiZ_ape=0; Max_YY_ape=0; Max_YZ_ape=0; Max_YPhiX_ape=0; Max_YPhiY_ape=0; Max_YPhiZ_ape=0; Max_ZZ_ape=0; Max_ZPhiX_ape=0; Max_ZPhiY_ape=0; Max_ZPhiZ_ape=0; Max_PhiXPhiX_ape=0; Max_PhiXPhiY_ape=0; Max_PhiXPhiZ_ape=0; Max_PhiYPhiY_ape=0; Max_PhiYPhiZ_ape=0; Max_PhiZPhiZ_ape=0;
Max_XY_ape_corr=0; Max_XZ_ape_corr=0; Max_XPhiX_ape_corr=0; Max_XPhiY_ape_corr=0; Max_XPhiZ_ape_corr=0; Max_YZ_ape_corr=0; Max_YPhiX_ape_corr=0; Max_YPhiY_ape_corr=0; Max_YPhiZ_ape_corr=0; Max_ZPhiX_ape_corr=0; Max_ZPhiY_ape_corr=0; Max_ZPhiZ_ape_corr=0; Max_PhiXPhiY_ape_corr=0; Max_PhiXPhiZ_ape_corr=0; Max_PhiYPhiZ_ape_corr=0;
Min_XX_ape=100; Min_XY_ape=100; Min_XZ_ape=100; Min_XPhiX_ape=100; Min_XPhiY_ape=100; Min_XPhiZ_ape=100; Min_YY_ape=100; Min_YZ_ape=100; Min_YPhiX_ape=100; Min_YPhiY_ape=100; Min_YPhiZ_ape=100; Min_ZZ_ape=100; Min_ZPhiX_ape=100; Min_ZPhiY_ape=100; Min_ZPhiZ_ape=100; Min_PhiXPhiX_ape=100; Min_PhiXPhiY_ape=100; Min_PhiXPhiZ_ape=100; Min_PhiYPhiY_ape=100; Min_PhiYPhiZ_ape=100; Min_PhiZPhiZ_ape=100;
Min_XY_ape_corr=100; Min_XZ_ape_corr=100; Min_XPhiX_ape_corr=100; Min_XPhiY_ape_corr=100; Min_XPhiZ_ape_corr=100; Min_YZ_ape_corr=100; Min_YPhiX_ape_corr=100; Min_YPhiY_ape_corr=100; Min_YPhiZ_ape_corr=100; Min_ZPhiX_ape_corr=100; Min_ZPhiY_ape_corr=100; Min_ZPhiZ_ape_corr=100; Min_PhiXPhiY_ape_corr=100; Min_PhiXPhiZ_ape_corr=100; Min_PhiYPhiZ_ape_corr=100;
for myAPE in g_apes:
    for endcap in (1, 2):
      for disk in (1, 2, 3, 4):
        if disk == 1: rings = (1,2,3,4) 
        else:         rings = (1,2)
        for ring in rings:
          #for sector in GetCSCSectors(disk,ring):
          sector = 2;
          XX_ape       = sqrt(myAPE.csc[endcap, disk, ring, sector].xx*10*10)
          XY_ape       = myAPE.csc[endcap, disk, ring, sector].xy*10*10
          XZ_ape       = myAPE.csc[endcap, disk, ring, sector].xz*10*10
          YY_ape       = sqrt(myAPE.csc[endcap, disk, ring, sector].yy*10*10)
          YZ_ape       = myAPE.csc[endcap, disk, ring, sector].yz*10*10
          ZZ_ape       = sqrt(myAPE.csc[endcap, disk, ring, sector].zz*10*10)
          XPhiX_ape    = myAPE.csc[endcap, disk, ring, sector].xa*10*1000 
          XPhiY_ape    = myAPE.csc[endcap, disk, ring, sector].xb*10*1000
          XPhiZ_ape    = myAPE.csc[endcap, disk, ring, sector].xc*10*1000
          YPhiX_ape    = myAPE.csc[endcap, disk, ring, sector].ya*10*1000
          YPhiY_ape    = myAPE.csc[endcap, disk, ring, sector].yb*10*1000
          YPhiZ_ape    = myAPE.csc[endcap, disk, ring, sector].yc*10*1000
          ZPhiX_ape    = myAPE.csc[endcap, disk, ring, sector].za*10*1000
          ZPhiY_ape    = myAPE.csc[endcap, disk, ring, sector].zb*10*1000
          ZPhiZ_ape    = myAPE.csc[endcap, disk, ring, sector].zc*10*1000
          PhiXPhiX_ape = sqrt(myAPE.csc[endcap, disk, ring, sector].aa*1000*1000)
          PhiXPhiY_ape = myAPE.csc[endcap, disk, ring, sector].ab*1000*1000
          PhiXPhiZ_ape = myAPE.csc[endcap, disk, ring, sector].ac*1000*1000
          PhiYPhiY_ape = sqrt(myAPE.csc[endcap, disk, ring, sector].bb*1000*1000)
          PhiYPhiZ_ape = myAPE.csc[endcap, disk, ring, sector].bc*1000*1000
          PhiZPhiZ_ape = sqrt(myAPE.csc[endcap, disk, ring, sector].cc*1000*1000)
          XY_ape_corr       = XY_ape/(XX_ape*YY_ape)
          XZ_ape_corr       = XZ_ape/(XX_ape*ZZ_ape) 
          YZ_ape_corr       = YZ_ape/(YY_ape*ZZ_ape)
          XPhiX_ape_corr    = XPhiX_ape/(XX_ape*PhiXPhiX_ape)
          XPhiY_ape_corr    = XPhiY_ape/(XX_ape*PhiYPhiY_ape)
          XPhiZ_ape_corr    = XPhiZ_ape/(XX_ape*PhiZPhiZ_ape)
          YPhiX_ape_corr    = YPhiX_ape/(YY_ape*PhiXPhiX_ape)
          YPhiY_ape_corr    = YPhiY_ape/(YY_ape*PhiYPhiY_ape)
          YPhiZ_ape_corr    = YPhiZ_ape/(YY_ape*PhiZPhiZ_ape)
          ZPhiX_ape_corr    = ZPhiX_ape/(ZZ_ape*PhiXPhiX_ape)
          ZPhiY_ape_corr    = ZPhiY_ape/(ZZ_ape*PhiYPhiY_ape)
          ZPhiZ_ape_corr    = ZPhiZ_ape/(ZZ_ape*PhiZPhiZ_ape)
          PhiXPhiY_ape_corr = PhiXPhiY_ape/(PhiXPhiX_ape*PhiYPhiY_ape)
          PhiXPhiZ_ape_corr = PhiXPhiZ_ape/(PhiXPhiX_ape*PhiZPhiZ_ape)
          PhiYPhiZ_ape_corr = PhiYPhiZ_ape/(PhiYPhiY_ape*PhiZPhiZ_ape)
          if(XX_ape>Max_XX_ape): Max_XX_ape = XX_ape
          if(XY_ape>Max_XY_ape): Max_XY_ape = XY_ape
          if(XZ_ape>Max_XZ_ape): Max_XZ_ape = XZ_ape
          if(YY_ape>Max_YY_ape): Max_YY_ape = YY_ape
          if(YZ_ape>Max_YZ_ape): Max_YZ_ape = YZ_ape
          if(ZZ_ape>Max_ZZ_ape): Max_ZZ_ape = ZZ_ape
          if(XPhiX_ape>Max_XPhiX_ape): Max_XPhiX_ape = XPhiX_ape
          if(XPhiY_ape>Max_XPhiY_ape): Max_XPhiY_ape = XPhiY_ape
          if(XPhiZ_ape>Max_XPhiZ_ape): Max_XPhiZ_ape = XPhiZ_ape
          if(YPhiX_ape>Max_YPhiX_ape): Max_YPhiX_ape = YPhiX_ape
          if(YPhiY_ape>Max_YPhiY_ape): Max_YPhiY_ape = YPhiY_ape
          if(YPhiZ_ape>Max_YPhiZ_ape): Max_YPhiZ_ape = YPhiZ_ape
          if(ZPhiX_ape>Max_ZPhiX_ape): Max_ZPhiX_ape = ZPhiX_ape
          if(ZPhiY_ape>Max_ZPhiY_ape): Max_ZPhiY_ape = ZPhiY_ape
          if(ZPhiZ_ape>Max_ZPhiZ_ape): Max_ZPhiZ_ape = ZPhiZ_ape
          if(PhiXPhiX_ape>Max_PhiXPhiX_ape): Max_PhiXPhiX_ape = PhiXPhiX_ape
          if(PhiXPhiY_ape>Max_PhiXPhiY_ape): Max_PhiXPhiY_ape = PhiXPhiY_ape
          if(PhiXPhiZ_ape>Max_PhiXPhiZ_ape): Max_PhiXPhiZ_ape = PhiXPhiZ_ape
          if(PhiYPhiY_ape>Max_PhiYPhiY_ape): Max_PhiYPhiY_ape = PhiYPhiY_ape
          if(PhiYPhiZ_ape>Max_PhiYPhiZ_ape): Max_PhiYPhiZ_ape = PhiYPhiZ_ape
          if(PhiZPhiZ_ape>Max_PhiZPhiZ_ape): Max_PhiZPhiZ_ape = PhiZPhiZ_ape
          if(XY_ape_corr>Max_XY_ape_corr):             Max_XY_ape_corr = XY_ape_corr
          if(XZ_ape_corr>Max_XZ_ape_corr):             Max_XZ_ape_corr = XZ_ape_corr
          if(XPhiX_ape_corr>Max_XPhiX_ape_corr):       Max_XPhiX_ape_corr = XPhiX_ape_corr
          if(XPhiY_ape_corr>Max_XPhiY_ape_corr):       Max_XPhiY_ape_corr = XPhiY_ape_corr
          if(XPhiZ_ape_corr>Max_XPhiZ_ape_corr):       Max_XPhiZ_ape_corr = XPhiZ_ape_corr
          if(YZ_ape_corr>Max_YZ_ape_corr):             Max_YZ_ape_corr = YZ_ape_corr
          if(YPhiX_ape_corr>Max_YPhiX_ape_corr):       Max_YPhiX_ape_corr = YPhiX_ape_corr
          if(YPhiY_ape_corr>Max_YPhiY_ape_corr):       Max_YPhiY_ape_corr = YPhiY_ape_corr
          if(YPhiZ_ape_corr>Max_YPhiZ_ape_corr):       Max_YPhiZ_ape_corr = YPhiZ_ape_corr
          if(ZPhiX_ape_corr>Max_ZPhiX_ape_corr):       Max_ZPhiX_ape_corr = ZPhiX_ape_corr
          if(ZPhiY_ape_corr>Max_ZPhiY_ape_corr):       Max_ZPhiY_ape_corr = ZPhiY_ape_corr
          if(ZPhiZ_ape_corr>Max_ZPhiZ_ape_corr):       Max_ZPhiZ_ape_corr = ZPhiZ_ape_corr
          if(PhiXPhiY_ape_corr>Max_PhiXPhiY_ape_corr): Max_PhiXPhiY_ape_corr = PhiXPhiY_ape_corr
          if(PhiXPhiZ_ape_corr>Max_PhiXPhiZ_ape_corr): Max_PhiXPhiZ_ape_corr = PhiXPhiZ_ape_corr
          if(PhiYPhiZ_ape_corr>Max_PhiYPhiZ_ape_corr): Max_PhiYPhiZ_ape_corr = PhiYPhiZ_ape_corr
          if(XX_ape<Min_XX_ape): Min_XX_ape = XX_ape
          if(XY_ape<Min_XY_ape): Min_XY_ape = XY_ape
          if(XZ_ape<Min_XZ_ape): Min_XZ_ape = XZ_ape
          if(YY_ape<Min_YY_ape): Min_YY_ape = YY_ape
          if(YZ_ape<Min_YZ_ape): Min_YZ_ape = YZ_ape
          if(ZZ_ape<Min_ZZ_ape): Min_ZZ_ape = ZZ_ape
          if(XPhiX_ape<Min_XPhiX_ape): Min_XPhiX_ape = XPhiX_ape
          if(XPhiY_ape<Min_XPhiY_ape): Min_XPhiY_ape = XPhiY_ape
          if(XPhiZ_ape<Min_XPhiZ_ape): Min_XPhiZ_ape = XPhiZ_ape
          if(YPhiX_ape<Min_YPhiX_ape): Min_YPhiX_ape = YPhiX_ape
          if(YPhiY_ape<Min_YPhiY_ape): Min_YPhiY_ape = YPhiY_ape
          if(YPhiZ_ape<Min_YPhiZ_ape): Min_YPhiZ_ape = YPhiZ_ape
          if(ZPhiX_ape<Min_ZPhiX_ape): Min_ZPhiX_ape = ZPhiX_ape
          if(ZPhiY_ape<Min_ZPhiY_ape): Min_ZPhiY_ape = ZPhiY_ape
          if(ZPhiZ_ape<Min_ZPhiZ_ape): Min_ZPhiZ_ape = ZPhiZ_ape
          if(PhiXPhiX_ape<Min_PhiXPhiX_ape): Min_PhiXPhiX_ape = PhiXPhiX_ape
          if(PhiXPhiY_ape<Min_PhiXPhiY_ape): Min_PhiXPhiY_ape = PhiXPhiY_ape
          if(PhiXPhiZ_ape<Min_PhiXPhiZ_ape): Min_PhiXPhiZ_ape = PhiXPhiZ_ape
          if(PhiYPhiY_ape<Min_PhiYPhiY_ape): Min_PhiYPhiY_ape = PhiYPhiY_ape
          if(PhiYPhiZ_ape<Min_PhiYPhiZ_ape): Min_PhiYPhiZ_ape = PhiYPhiZ_ape
          if(PhiZPhiZ_ape<Min_PhiZPhiZ_ape): Min_PhiZPhiZ_ape = PhiZPhiZ_ape
          if(XY_ape_corr<Min_XY_ape_corr):             Min_XY_ape_corr = XY_ape_corr
          if(XZ_ape_corr<Min_XZ_ape_corr):             Min_XZ_ape_corr = XZ_ape_corr
          if(XPhiX_ape_corr<Min_XPhiX_ape_corr):       Min_XPhiX_ape_corr = XPhiX_ape_corr
          if(XPhiY_ape_corr<Min_XPhiY_ape_corr):       Min_XPhiY_ape_corr = XPhiY_ape_corr
          if(XPhiZ_ape_corr<Min_XPhiZ_ape_corr):       Min_XPhiZ_ape_corr = XPhiZ_ape_corr
          if(YZ_ape_corr<Min_YZ_ape_corr):             Min_YZ_ape_corr = YZ_ape_corr
          if(YPhiX_ape_corr<Min_YPhiX_ape_corr):       Min_YPhiX_ape_corr = YPhiX_ape_corr
          if(YPhiY_ape_corr<Min_YPhiY_ape_corr):       Min_YPhiY_ape_corr = YPhiY_ape_corr
          if(YPhiZ_ape_corr<Min_YPhiZ_ape_corr):       Min_YPhiZ_ape_corr = YPhiZ_ape_corr
          if(ZPhiX_ape_corr<Min_ZPhiX_ape_corr):       Min_ZPhiX_ape_corr = ZPhiX_ape_corr
          if(ZPhiY_ape_corr<Min_ZPhiY_ape_corr):       Min_ZPhiY_ape_corr = ZPhiY_ape_corr
          if(ZPhiZ_ape_corr<Min_ZPhiZ_ape_corr):       Min_ZPhiZ_ape_corr = ZPhiZ_ape_corr
          if(PhiXPhiY_ape_corr<Min_PhiXPhiY_ape_corr): Min_PhiXPhiY_ape_corr = PhiXPhiY_ape_corr
          if(PhiXPhiZ_ape_corr<Min_PhiXPhiZ_ape_corr): Min_PhiXPhiZ_ape_corr = PhiXPhiZ_ape_corr
          if(PhiYPhiZ_ape_corr<Min_PhiYPhiZ_ape_corr): Min_PhiYPhiZ_ape_corr = PhiYPhiZ_ape_corr
FinalMax = []
FinalMax.append(Max_XX_ape); FinalMax.append(Max_XY_ape); FinalMax.append(Max_XZ_ape); FinalMax.append(Max_XPhiX_ape); FinalMax.append(Max_XPhiY_ape); FinalMax.append(Max_XPhiZ_ape); FinalMax.append(Max_YY_ape); FinalMax.append(Max_YZ_ape); FinalMax.append(Max_YPhiX_ape); FinalMax.append(Max_YPhiY_ape); FinalMax.append(Max_YPhiZ_ape); FinalMax.append(Max_ZZ_ape); FinalMax.append(Max_ZPhiX_ape); FinalMax.append(Max_ZPhiY_ape); FinalMax.append(Max_ZPhiZ_ape); FinalMax.append(Max_PhiXPhiX_ape); FinalMax.append(Max_PhiXPhiY_ape); FinalMax.append(Max_PhiXPhiZ_ape); FinalMax.append(Max_PhiYPhiY_ape); FinalMax.append(Max_PhiYPhiZ_ape); FinalMax.append(Max_PhiZPhiZ_ape);
FinalMax.append(Max_XY_ape_corr); FinalMax.append(Max_XZ_ape_corr); FinalMax.append(Max_XPhiX_ape_corr); FinalMax.append(Max_XPhiY_ape_corr); FinalMax.append(Max_XPhiZ_ape_corr); FinalMax.append(Max_YZ_ape_corr); FinalMax.append(Max_YPhiX_ape_corr); FinalMax.append(Max_YPhiY_ape_corr); FinalMax.append(Max_YPhiZ_ape_corr); FinalMax.append(Max_ZPhiX_ape_corr); FinalMax.append(Max_ZPhiY_ape_corr); FinalMax.append(Max_ZPhiZ_ape_corr); FinalMax.append(Max_PhiXPhiY_ape_corr); FinalMax.append(Max_PhiXPhiZ_ape_corr); FinalMax.append(Max_PhiYPhiZ_ape_corr); 
FinalMin = []
FinalMin.append(Min_XX_ape); FinalMin.append(Min_XY_ape); FinalMin.append(Min_XZ_ape); FinalMin.append(Min_XPhiX_ape); FinalMin.append(Min_XPhiY_ape); FinalMin.append(Min_XPhiZ_ape); FinalMin.append(Min_YY_ape); FinalMin.append(Min_YZ_ape); FinalMin.append(Min_YPhiX_ape); FinalMin.append(Min_YPhiY_ape); FinalMin.append(Min_YPhiZ_ape); FinalMin.append(Min_ZZ_ape); FinalMin.append(Min_ZPhiX_ape); FinalMin.append(Min_ZPhiY_ape); FinalMin.append(Min_ZPhiZ_ape); FinalMin.append(Min_PhiXPhiX_ape); FinalMin.append(Min_PhiXPhiY_ape); FinalMin.append(Min_PhiXPhiZ_ape); FinalMin.append(Min_PhiYPhiY_ape); FinalMin.append(Min_PhiYPhiZ_ape); FinalMin.append(Min_PhiZPhiZ_ape);
FinalMin.append(Min_XY_ape_corr); FinalMin.append(Min_XZ_ape_corr); FinalMin.append(Min_XPhiX_ape_corr); FinalMin.append(Min_XPhiY_ape_corr); FinalMin.append(Min_XPhiZ_ape_corr); FinalMin.append(Min_YZ_ape_corr); FinalMin.append(Min_YPhiX_ape_corr); FinalMin.append(Min_YPhiY_ape_corr); FinalMin.append(Min_YPhiZ_ape_corr); FinalMin.append(Min_ZPhiX_ape_corr); FinalMin.append(Min_ZPhiY_ape_corr); FinalMin.append(Min_ZPhiZ_ape_corr); FinalMin.append(Min_PhiXPhiY_ape_corr); FinalMin.append(Min_PhiXPhiZ_ape_corr); FinalMin.append(Min_PhiYPhiZ_ape_corr); 

# Histograms initialization
#h_wheel0 = []; h_wheel1 = []; h_wheel2 = [];
h_disk1 = []; h_disk2 = []; h_disk3 = []; h_disk4 = []; 
for ring in 1, 2, 3, 4:
  if ring == 1 or ring ==2 :  h_disk1.append([]);  h_disk2.append([]); h_disk3.append([]); h_disk4.append([]);
  if ring == 3 or ring ==4 :  h_disk1.append([]);
  nAPE=0
  for  myAPE in g_apes:
    if ring == 1 or ring ==2 :  h_disk1[ring-1].append([]); h_disk2[ring-1].append([]); h_disk3[ring-1].append([]); h_disk4[ring-1].append([]);
    if ring == 3 or ring ==4 :  h_disk1[ring-1].append([]);
    for Variable in range(len(Var)):
      if ring == 1 or ring ==2 :  h_disk1[ring-1][nAPE].append(ROOT.TH1F); h_disk2[ring-1][nAPE].append(ROOT.TH1F); h_disk3[ring-1][nAPE].append(ROOT.TH1F);  h_disk4[ring-1][nAPE].append(ROOT.TH1F);
      if ring == 3 or ring ==4 :  h_disk1[ring-1][nAPE].append(ROOT.TH1F);
    nAPE=nAPE+1
# Histograms definition
nAPE=0
Color = [];
for myAPE in g_apes:
  # Histograms
  weight=0.8;
  Style = 3001
  Color.append(1); Color.append(2); Color.append(4); Color.append(3); Color.append(5);
  if nAPE==1:
    Style = 3009
    Color[0]=12; Color[1]=46; Color[2]=9; Color[3]=8; Color[4]=32;
    weight=0.5
  for ring in 1, 2, 3, 4:
    for Variable in range(len(Var)):
      name1 = str("Disk1_Ring"+str(ring)+"_Var"+Var[Variable])+"_"+str(nAPE)
      if ring == 1 or ring ==2 : 
        name2 = str("Disk2_Ring"+str(ring)+"_Var"+Var[Variable])+"_"+str(nAPE)
        name3 = str("Disk3_Ring"+str(ring)+"_Var"+Var[Variable])+"_"+str(nAPE)
        name4 = str("Disk4_Ring"+str(ring)+"_Var"+Var[Variable])+"_"+str(nAPE)
      maxRange = FinalMax[int(Variable)] * 1.1
      minRange = FinalMin[int(Variable)] * 1.1
      if(Var[Variable]=="XX" or Var[Variable]=="YY" or Var[Variable]=="ZZ" or Var[Variable]=="PhiXPhiX" or Var[Variable]=="PhiYPhiY" or Var[Variable]=="PhiZPhiZ"): minRange=0
      if( "corr" in Var[Variable] ): minRange=-1; maxRange=1;
      h_disk1[ring-1][nAPE][Variable] = ROOT.TH1F(name1, "", 300, minRange, maxRange); h_disk1[ring-1][nAPE][Variable].GetXaxis().SetTitle(Names_histo[Variable]); h_disk1[ring-1][nAPE][Variable].GetYaxis().SetTitle("Disk 1"); h_disk1[ring-1][nAPE][Variable].GetXaxis().SetTitleSize(.1); h_disk1[ring-1][nAPE][Variable].GetYaxis().SetTitleSize(0.15); h_disk1[ring-1][nAPE][Variable].GetYaxis().SetTitleOffset(0.2); h_disk1[ring-1][nAPE][Variable].SetFillColor(Color[ring-1]); h_disk1[ring-1][nAPE][Variable].SetLineColor(Color[ring-1]); h_disk1[ring-1][nAPE][Variable].SetFillStyle(Style); h_disk1[ring-1][nAPE][Variable].SetMaximum(1.3); h_disk1[ring-1][nAPE][Variable].SetMarkerStyle(20); h_disk1[ring-1][nAPE][Variable].SetMarkerColor(Color[ring-1]);
      if nAPE==1:
          h_disk1[ring-1][nAPE][Variable].SetMarkerStyle(34);          
      if( ring==1 or ring==2 ):
        h_disk2[ring-1][nAPE][Variable] = ROOT.TH1F(name2, "", 300, minRange, maxRange); h_disk2[ring-1][nAPE][Variable].GetXaxis().SetTitle(Names_histo[Variable]); h_disk2[ring-1][nAPE][Variable].GetYaxis().SetTitle("Disk 2"); h_disk2[ring-1][nAPE][Variable].GetXaxis().SetTitleSize(.1); h_disk2[ring-1][nAPE][Variable].GetYaxis().SetTitleSize(0.15); h_disk2[ring-1][nAPE][Variable].GetYaxis().SetTitleOffset(0.2); h_disk2[ring-1][nAPE][Variable].SetFillColor(Color[ring-1]); h_disk2[ring-1][nAPE][Variable].SetLineColor(Color[ring-1]); h_disk2[ring-1][nAPE][Variable].SetFillStyle(Style); h_disk2[ring-1][nAPE][Variable].SetMaximum(1.3); h_disk2[ring-1][nAPE][Variable].SetMarkerStyle(20); h_disk2[ring-1][nAPE][Variable].SetMarkerColor(Color[ring-1]);
        if nAPE==1:
          h_disk2[ring-1][nAPE][Variable].SetMarkerStyle(34);
        h_disk3[ring-1][nAPE][Variable] = ROOT.TH1F(name3, "", 300, minRange, maxRange); h_disk3[ring-1][nAPE][Variable].GetXaxis().SetTitle(Names_histo[Variable]); h_disk3[ring-1][nAPE][Variable].GetYaxis().SetTitle("Disk 3"); h_disk3[ring-1][nAPE][Variable].GetXaxis().SetTitleSize(.1); h_disk3[ring-1][nAPE][Variable].GetYaxis().SetTitleSize(0.15); h_disk3[ring-1][nAPE][Variable].GetYaxis().SetTitleOffset(0.2); h_disk3[ring-1][nAPE][Variable].SetFillColor(Color[ring-1]); h_disk3[ring-1][nAPE][Variable].SetLineColor(Color[ring-1]); h_disk3[ring-1][nAPE][Variable].SetFillStyle(Style); h_disk3[ring-1][nAPE][Variable].SetMaximum(1.3); h_disk3[ring-1][nAPE][Variable].SetMarkerStyle(20); h_disk3[ring-1][nAPE][Variable].SetMarkerColor(Color[ring-1]);
        if nAPE==1:
          h_disk3[ring-1][nAPE][Variable].SetMarkerStyle(34);
        h_disk4[ring-1][nAPE][Variable] = ROOT.TH1F(name4, "", 300, minRange, maxRange); h_disk4[ring-1][nAPE][Variable].GetXaxis().SetTitle(Names_histo[Variable]); h_disk4[ring-1][nAPE][Variable].GetYaxis().SetTitle("Disk 4"); h_disk4[ring-1][nAPE][Variable].GetXaxis().SetTitleSize(.1); h_disk4[ring-1][nAPE][Variable].GetYaxis().SetTitleSize(0.15);  h_disk4[ring-1][nAPE][Variable].GetYaxis().SetTitleOffset(0.2); h_disk4[ring-1][nAPE][Variable].SetFillColor(Color[ring-1]); h_disk4[ring-1][nAPE][Variable].SetLineColor(Color[ring-1]); h_disk4[ring-1][nAPE][Variable].SetFillStyle(Style); h_disk4[ring-1][nAPE][Variable].SetMaximum(1.3); h_disk4[ring-1][nAPE][Variable].SetMarkerStyle(20); h_disk4[ring-1][nAPE][Variable].SetMarkerColor(Color[ring-1]);
        if nAPE==1:
          h_disk4[ring-1][nAPE][Variable].SetMarkerStyle(34);
  #Loop over the Chambers
  for endcap in (1, 2):
    for disk in (1, 2, 3, 4):
      if disk == 1: rings = (1,2,3,4) 
      else:         rings = (1,2)
      for ring in rings:
        #for sector in GetCSCSectors(disk,ring):
        sector = 2;
        #APE value in mm and mrad
        XX_ape       = sqrt(myAPE.csc[endcap, disk, ring, sector].xx*10*10)
        XY_ape       = myAPE.csc[endcap, disk, ring, sector].xy*10*10
        XZ_ape       = myAPE.csc[endcap, disk, ring, sector].xz*10*10
        YY_ape       = sqrt(myAPE.csc[endcap, disk, ring, sector].yy*10*10)
        YZ_ape       = myAPE.csc[endcap, disk, ring, sector].yz*10*10
        ZZ_ape       = sqrt(myAPE.csc[endcap, disk, ring, sector].zz*10*10)
        XPhiX_ape    = myAPE.csc[endcap, disk, ring, sector].xa*10*1000
        XPhiY_ape    = myAPE.csc[endcap, disk, ring, sector].xb*10*1000
        XPhiZ_ape    = myAPE.csc[endcap, disk, ring, sector].xc*10*1000
        YPhiX_ape    = myAPE.csc[endcap, disk, ring, sector].ya*10*1000
        YPhiY_ape    = myAPE.csc[endcap, disk, ring, sector].yb*10*1000
        YPhiZ_ape    = myAPE.csc[endcap, disk, ring, sector].yc*10*1000
        ZPhiX_ape    = myAPE.csc[endcap, disk, ring, sector].za*10*1000
        ZPhiY_ape    = myAPE.csc[endcap, disk, ring, sector].zb*10*1000
        ZPhiZ_ape    = myAPE.csc[endcap, disk, ring, sector].zc*10*1000
        PhiXPhiX_ape = sqrt(myAPE.csc[endcap, disk, ring, sector].aa*1000*1000)
        PhiXPhiY_ape = myAPE.csc[endcap, disk, ring, sector].ab*1000*1000
        PhiXPhiZ_ape = myAPE.csc[endcap, disk, ring, sector].ac*1000*1000
        PhiYPhiY_ape = sqrt(myAPE.csc[endcap, disk, ring, sector].bb*1000*1000)
        PhiYPhiZ_ape = myAPE.csc[endcap, disk, ring, sector].bc*1000*1000
        PhiZPhiZ_ape = sqrt(myAPE.csc[endcap, disk, ring, sector].cc*1000*1000)
        XY_ape_corr       = XY_ape/(XX_ape*YY_ape)
        XZ_ape_corr       = XZ_ape/(XX_ape*ZZ_ape) 
        YZ_ape_corr       = YZ_ape/(YY_ape*ZZ_ape)
        XPhiX_ape_corr    = XPhiX_ape/(XX_ape*PhiXPhiX_ape)
        XPhiY_ape_corr    = XPhiY_ape/(XX_ape*PhiYPhiY_ape)
        XPhiZ_ape_corr    = XPhiZ_ape/(XX_ape*PhiZPhiZ_ape)
        YPhiX_ape_corr    = YPhiX_ape/(YY_ape*PhiXPhiX_ape)
        YPhiY_ape_corr    = YPhiY_ape/(YY_ape*PhiYPhiY_ape)
        YPhiZ_ape_corr    = YPhiZ_ape/(YY_ape*PhiZPhiZ_ape)
        ZPhiX_ape_corr    = ZPhiX_ape/(ZZ_ape*PhiXPhiX_ape)
        ZPhiY_ape_corr    = ZPhiY_ape/(ZZ_ape*PhiYPhiY_ape)
        ZPhiZ_ape_corr    = ZPhiZ_ape/(ZZ_ape*PhiZPhiZ_ape)
        PhiXPhiY_ape_corr = PhiXPhiY_ape/(PhiXPhiX_ape*PhiYPhiY_ape)
        PhiXPhiZ_ape_corr = PhiXPhiZ_ape/(PhiXPhiX_ape*PhiZPhiZ_ape)
        PhiYPhiZ_ape_corr = PhiYPhiZ_ape/(PhiYPhiY_ape*PhiZPhiZ_ape)
        myValue = []
        myValue.append(XX_ape); myValue.append(XY_ape); myValue.append(XZ_ape); myValue.append(XPhiX_ape); myValue.append(XPhiY_ape); myValue.append(XPhiZ_ape); myValue.append(YY_ape); myValue.append(YZ_ape); myValue.append(YPhiX_ape); myValue.append(YPhiY_ape); myValue.append(YPhiZ_ape); myValue.append(ZZ_ape); myValue.append(ZPhiX_ape); myValue.append(ZPhiY_ape); myValue.append(ZPhiZ_ape); myValue.append(PhiXPhiX_ape); myValue.append(PhiXPhiY_ape); myValue.append(PhiXPhiZ_ape); myValue.append(PhiYPhiY_ape); myValue.append(PhiYPhiZ_ape); myValue.append(PhiZPhiZ_ape);
        myValue.append(XY_ape_corr); myValue.append(XZ_ape_corr); myValue.append(YZ_ape_corr); myValue.append(XPhiX_ape_corr); myValue.append(XPhiY_ape_corr); myValue.append(XPhiZ_ape_corr); myValue.append(YPhiX_ape_corr); myValue.append(YPhiY_ape_corr); myValue.append(YPhiZ_ape_corr); myValue.append(ZPhiX_ape_corr); myValue.append(ZPhiY_ape_corr); myValue.append(ZPhiZ_ape_corr); myValue.append(PhiXPhiY_ape_corr); myValue.append(PhiXPhiZ_ape_corr); myValue.append(PhiYPhiZ_ape_corr);
        for Variable in range(len(Var)):
          if(disk==1):        h_disk1[ring-1][nAPE][Variable].Fill( myValue[Variable], weight  )
          if(disk==2):        h_disk2[ring-1][nAPE][Variable].Fill( myValue[Variable], weight  )
          if(disk==3):        h_disk3[ring-1][nAPE][Variable].Fill( myValue[Variable], weight  )
          if(disk==4):        h_disk4[ring-1][nAPE][Variable].Fill( myValue[Variable], weight  )
  nAPE=nAPE+1
# Draw all the histos
legend=ROOT.TLegend(0.75,0.7,0.9,0.97)
legend.SetFillStyle(0)
legend.SetBorderSize(0)
legend.AddEntry(h_disk1[0][0][0], "Ring 1", "lep")
legend.AddEntry(h_disk1[1][0][0], "Ring 2", "lep")
legend.AddEntry(h_disk1[2][0][0], "Ring 3", "lep")
for Variable in range(len(Var)):
  firstDraw=True
  nAPE=0
  for myAPE in g_apes:
    c1.cd(1); ROOT.gPad.SetTickx(2); ROOT.gPad.SetTicky(2); ROOT.gPad.SetGrid(1,1);
    if firstDraw: h_disk1[0][nAPE][Variable].Draw();
    else: h_disk1[0][nAPE][Variable].Draw("same");
    h_disk1[1][nAPE][Variable].Draw("same"); h_disk1[2][nAPE][Variable].Draw("same"); 
    
    c1.cd(2); ROOT.gPad.SetTickx(2); ROOT.gPad.SetTicky(2); ROOT.gPad.SetGrid(1,1);
    h_disk2[ring-1][nAPE][Variable].GetXaxis().SetLabelOffset(999);
    if firstDraw: h_disk2[0][nAPE][Variable].Draw();
    else: h_disk2[0][nAPE][Variable].Draw("same");
    h_disk2[1][nAPE][Variable].Draw("same"); 

    c1.cd(3); ROOT.gPad.SetTickx(2); ROOT.gPad.SetTicky(2); ROOT.gPad.SetGrid(1,1);
    if firstDraw: h_disk3[0][nAPE][Variable].Draw();
    else: h_disk3[0][nAPE][Variable].Draw("same");
    h_disk3[1][nAPE][Variable].Draw("same");    
    
    c1.cd(4); ROOT.gPad.SetTicky(2); ROOT.gPad.SetGrid(1,1);
    if firstDraw: h_disk4[0][nAPE][Variable].Draw();
    else: h_disk4[0][nAPE][Variable].Draw("same");
    h_disk4[1][nAPE][Variable].Draw("same");   
    firstDraw=False

    

    nAPE=nAPE+1
    
  c1.cd(1);
  legend.Draw("same")
  minX = h_disk1[0][0][Variable].GetBinCenter(10)
  mytex = ROOT.TLatex(minX,1.2,myText);
  mytex.SetTextSize(0.07);
  mytex.Draw()
  name="Display_CSC/h_" + Var[Variable] + ".png"
  c1.SaveAs(name)
