import ROOT as r
import struct, math, os, sys
from array import array
from functions_layers import *

#Parameters you may want to change
prefix="Output_Occupancy"
#Parameters to do not be changed
r.TH1.SetDefaultSumw2(True)
r.gErrorIgnoreLevel = r.kWarning # Suppress "Info in..." messages
#Check and inizialization
if(len(sys.argv) < 1):
  print "USAGE python MakeOccupancyFlat_pt1.py ../mc_DT-1100-111111_CMSSW_8_0_17_ideal_45M_8TeV_PhiYsign_v3_01/mc_DT-1100-111111_CMSSW_8_0_17_ideal_45M_8TeV_PhiYsign_v3_01.root -b"; sys.exit(0);
filename = sys.argv[1]
print ">>> Setting filename:", filename

print ">>> Output into folder:",prefix
os.system("mkdir -p " + prefix )
c1 = r.TCanvas("Canvas1", "Alignment Visualizations")
#Input Fle and TTree
fh = r.TFile(filename)
tt = r.gDirectory.Get("mual_ttree")
#Histos
m_h_Occupancy_X={};
m_h_Occupancy_XY={};
h_angley_254= r.TH1F("m_h_angley_254", "254 conv. to wheel -2", 100, -1.5, 0.2)
h_angley_255= r.TH1F("m_h_angley_255", "255 conv. to wheel -1", 100, -1.5, 0.2)

#Loop on the TTree
selectedDT=[]
print "Starting the Loop."
TotalEvent=tt.GetEntries()
count=0
for idx, muon in enumerate(tt):
  if(count % 500000 == 0): print ">>> Event:", count, " / ", TotalEvent
  count += 1
  #Selection
  if not( muon.is_dt ): continue;
  if not( muon.pt>10 ): continue;
  #Chamber
  wheel, station, sector = ord(muon.ring_wheel), ord(muon.station), ord(muon.sector)
  if(wheel==254):
    wheel=-2 #unicode wrongly convert -2 to 254
    h_angley_254.Fill(muon.angle_y)
  if(wheel==255):
    wheel=-1 #unicode wrongly convert -1 to 255
    h_angley_255.Fill(muon.angle_y)
  thisChamber = (wheel,station,sector)
  index_chamber = convertChamberToIndex(thisChamber)
  if not(thisChamber in selectedDT):
    selectedDT.append(thisChamber)
    IDName="_ID_" + str(thisChamber[0]) + "_" + str(thisChamber[1]) + "_" + str(thisChamber[2])
    m_h_Occupancy_XY[index_chamber] = r.TH2F("Occupancy_XY"+IDName, ";Position X [cm]; Position Y [cm]", 100, -210, 210, 100, -210, 210)
    m_h_Occupancy_X[index_chamber] = r.TH1F("Occupancy_X"+IDName, ";Position X [cm];Entries", 100, -210, 210)
  #Plots
  m_h_Occupancy_XY[index_chamber].Fill(muon.pos_x,muon.pos_y)
  m_h_Occupancy_X[index_chamber].Fill(muon.pos_x)
print "Loop ended."
print "Start drawing histograms."
c1.SetGridx(); c1.SetGridy()
c1.SetCanvasSize(696,472)
r.gStyle.SetOptStat("rme")
fout = r.TFile(prefix + "/Output.root","recreate"); fout.cd();
h_angley_254.Write()
h_angley_255.Write()
for thisChamber in selectedDT:
  print "Saving histos for chmaber:", thisChamber 
  #suffix=".pdf"
  IDName="_ID_" + str(thisChamber[0]) + "_" + str(thisChamber[1]) + "_" + str(thisChamber[2])
  index_chamber = convertChamberToIndex(thisChamber)
  r.gStyle.SetOptStat(0)
  m_h_Occupancy_XY[index_chamber].Write()
  m_h_Occupancy_X[index_chamber].Write()
