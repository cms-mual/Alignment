import ROOT as r
import struct, math, os, sys
from array import array
from functions_layers import *
from collections import defaultdict
import numpy as np
import shutil

#Checka and Inizialization
if(len(sys.argv) < 2):
  print "USAGE: python MakeOccupancyFlat_pt2.py Output_Occupancy Output.root -b"; sys.exit(0);
folder = sys.argv[1]
rootfile = sys.argv[2]
print ">>> Setting folder:", folder, rootfile
os.system("mkdir -p " + folder)
suffix=".pdf"
#Input and output File and TTree
fh = r.TFile(folder+"/"+rootfile);
fout = r.TFile(folder + "/Output_weights.root","recreate");
#Drawing
print "Start drawing histograms."
c1 = r.TCanvas("Canvas1", "Alignment Visualizations")
c1.SetGridx(); c1.SetGridy()
c1.SetCanvasSize(696,472)
r.gStyle.SetOptStat("rme")

#Loop on the files
fh.cd()
dirList = r.gDirectory.GetListOfKeys()
for htemp in dirList:
  hist = htemp.ReadObj()
  if(htemp.GetClassName()=="TH1F"):
    r.gStyle.SetOptStat(0)
    hist.Draw();  c1.SaveAs(folder + "/" + hist.GetName() + ".pdf")
  if(htemp.GetClassName()=="TH2F"):
    r.gStyle.SetOptStat(0)
    if("Occupancy_XY_ID_" in hist.GetName() and not"Occupancy_XYres" in hist.GetName()):
      #Get the name and draw the original histo
      start=hist.GetName().find('_ID_') + 4
      chamber_ID=hist.GetName()[start:]
      chamber_ID_separated = chamber_ID.split("_") #Wheel, Station, Sector
      hist.Draw("colz");  c1.SaveAs(folder + "/Occupancy_XY_" + chamber_ID + ".pdf")
      #Create TH2 with weights
      Occupancy_XYweight = r.TH2F("Occupancy_XYweight_"+chamber_ID,"",100, -210, 210, 100, -210, 210)
      Occupancy_XYtest = r.TH2F("Occupancy_XYtest_"+chamber_ID,"",100, -210, 210, 100, -210, 210)
      #Get the bin margins and the Max and Min
      boundaries=findBinBound(hist,"TH2F") #lowerX, upperX, lowerY, upperY
      MinMaxBin=findMinMaxBin(boundaries[0],boundaries[1],boundaries[2],boundaries[3],hist,"TH2F")
      #minValue=hist.GetBinContent(MinMaxBin[0]+1,MinMaxBin[1]+1)
      maxValue=hist.GetBinContent(MinMaxBin[2]+1,MinMaxBin[3]+1)
      for nBX in range(hist.GetNbinsX()):
        for nBY in range(hist.GetNbinsY()):
          Cont=hist.GetBinContent(nBX+1,nBY+1)
          prob = 1.
          if(Cont>maxValue*(20/100)): # Do not touch poorly populated bins
            prob = 100./Cont
          if(nBX<=boundaries[0] or nBX>=boundaries[1] or nBY<=boundaries[2] or nBY>=boundaries[3] ): # Set to zero events outside the borders
            prob = 0.
          Occupancy_XYweight.SetBinContent(nBX+1,nBY+1,prob)
          Occupancy_XYtest.SetBinContent(nBX+1,nBY+1,Cont*prob)
      Occupancy_XYweight.Draw("colz");  c1.SaveAs(folder + "/Occupancy_XY_" + chamber_ID + "_Weight.pdf")
      Occupancy_XYtest.Draw("colz");  c1.SaveAs(folder + "/Occupancy_XY_" + chamber_ID + "_Test.pdf")
      fout.cd()
      Occupancy_XYweight.Write();
      fh.cd()
fout.cd()
fout.Close()
