import ROOT as r
import struct, math, os, sys
from array import array
from functions_layers import *

#Parameters you may want to change
selectedDT = [(0,4,10),(0,4,14),(0,4,11),(0,4,12),(0,4,1),(0,3,10),(0,4,2),(1,4,2)] # The chamber you want to study (wheel, station, chamber)
isMC = True
prefix="OutputFolder"
#Parameters to do not be changed
r.TH1.SetDefaultSumw2(True)
r.gErrorIgnoreLevel = r.kWarning # Suppress "Info in..." messages
#Check and inizialization
if(len(sys.argv) < 1):
  print "USAGE python DT_DEBUG_plots_pt1.py ../mc_DT-1100-111111_CMSSW_8_0_17_ideal_45M_8TeV_Layer_v2_03/mc_DT-1100-111111_CMSSW_8_0_17_ideal_45M_8TeV_Layer_v2_03.root -b"; sys.exit(0);
filename = sys.argv[1]
print ">>> Setting filename:", filename
print ">>> Setting selectedDT:", selectedDT
if(isMC):
  prefix += "_MC"
prefix += "/"
print ">>> Output into folder:",prefix
os.system("mkdir -p " + prefix + "/Residual_bins")
c1 = r.TCanvas("Canvas1", "Alignment Visualizations")

#Input Fle and TTree
fh = r.TFile(filename)
tt = r.gDirectory.Get("mual_ttree")
#Histos
m_h_Residual_X={}; m_h_Residual_Y={}; m_h_Occupancy_X={}; m_h_Occupancy_reb_X={}; m_h_Occupancy_Y={};
m_h_Occupancy_XY={}; m_h_Occupancy_XY_weighted={}; m_h_Occupancy_XYresX={}; m_h_Occupancy_XYresX_entries={}; m_h_Occupancy_XYresY={}; m_h_X_ResX={};
ResXBin=18; ResXBinRange=360;
l_h_ResX_AllBin = [dict() for x in range(ResXBin)]

for thisChamber in selectedDT:
  index_chamber = convertChamberToIndex(thisChamber)
  IDName="_ID_" + str(thisChamber[0]) + "_" + str(thisChamber[1]) + "_" + str(thisChamber[2])
  m_h_Residual_X[index_chamber] = r.TH1F("Residual_X"+IDName, ";Residual X [cm]; Entries", 100, -5, 5)
  m_h_Residual_Y[index_chamber] = r.TH1F("Residual_Y"+IDName, ";Residual Y [cm]; Entries", 100, -5, 5)
  m_h_Occupancy_X[index_chamber] = r.TH1F("Occupancy_X"+IDName, ";Position X [cm]; Entries", 100, -210, 210)
  m_h_Occupancy_reb_X[index_chamber] = r.TH1F("Occupancy_reb_X"+IDName, ";Position X [cm]; Entries", 18, -180, 180)
  m_h_Occupancy_Y[index_chamber] = r.TH1F("Occupancy_Y"+IDName, ";Position Y [cm]; Entries", 100, -100, 100)
  m_h_Occupancy_XY[index_chamber] = r.TH2F("Occupancy_XY"+IDName, ";Position X [cm]; Position Y [cm]", 100, -210, 210, 100, -100, 100)
  m_h_Occupancy_XY_weighted[index_chamber] = r.TH2F("Occupancy_XY_weighted"+IDName, ";Position X [cm]; Position Y [cm]", 100, -210, 210, 100, -100, 100)
  m_h_Occupancy_XYresX[index_chamber] = r.TH2F("Occupancy_XYresX"+IDName, ";Position X [cm]; Position Y [cm]", 840, -210, 210, 400, -100, 100)
  m_h_Occupancy_XYresY[index_chamber] = r.TH2F("Occupancy_XYresY"+IDName, ";Position X [cm]; Position Y [cm]", 840, -210, 210, 400, -100, 100)
  m_h_Occupancy_XYresX_entries[index_chamber] = r.TH2F("Occupancy_XYresX_entries"+IDName, ";Position X [cm]; Position Y [cm]", 840, -210, 210, 400, -100, 100)
  m_h_X_ResX[index_chamber] = r.TH2F("m_h_X_ResX"+IDName, ";Position X [cm]; Residual X [cm]", 100, -210, 210, 100, -2, 2)
  for nBin in range(ResXBin):
    l_h_ResX_AllBin[nBin][index_chamber] = r.TH1F("ResidualX_Bin_"+str(nBin)+IDName, ";Residual X [cm]; Entries", 100, -5, 5)
  for i in range(m_h_Occupancy_XYresX[index_chamber].GetNbinsX()):
    for j in range(m_h_Occupancy_XYresX[index_chamber].GetNbinsY()):
      m_h_Occupancy_XYresX[index_chamber].SetBinContent(i,j,-999)
      m_h_Occupancy_XYresY[index_chamber].SetBinContent(i,j,-999)
      m_h_Occupancy_XYresX_entries[index_chamber].SetBinContent(i,j,0)
  for i in range(m_h_X_ResX[index_chamber].GetNbinsX()):
    for j in range(m_h_X_ResX[index_chamber].GetNbinsY()):
      m_h_X_ResX[index_chamber].SetBinContent(i,j,0)
#Loop on the TTree
print "Starting the Loop"
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
  thisChamber = (wheel,station,sector)
  if(thisChamber in selectedDT):
    index_chamber = convertChamberToIndex(thisChamber)
    m_h_Residual_X[index_chamber].Fill(muon.res_x)
    m_h_Residual_Y[index_chamber].Fill(muon.res_y)
    m_h_Occupancy_X[index_chamber].Fill(muon.pos_x); m_h_Occupancy_reb_X[index_chamber].Fill(muon.pos_x);
    m_h_Occupancy_Y[index_chamber].Fill(muon.pos_y)
    m_h_Occupancy_XY[index_chamber].Fill(muon.pos_x,muon.pos_y)
    m_h_Occupancy_XY_weighted[index_chamber].Fill(muon.pos_x,muon.pos_y,muon.OccuWeight)
    binx = m_h_Occupancy_XYresX[index_chamber].GetXaxis().FindBin(muon.pos_x)
    biny = m_h_Occupancy_XYresX[index_chamber].GetYaxis().FindBin(muon.pos_y)
    if(muon.res_x!=0):
      if(m_h_Occupancy_XYresX[index_chamber].GetBinContent(binx,biny)==-999):
        m_h_Occupancy_XYresX[index_chamber].SetBinContent(binx,biny,muon.res_x)
      else:
        m_h_Occupancy_XYresX[index_chamber].SetBinContent(binx,biny,muon.res_x+m_h_Occupancy_XYresX[index_chamber].GetBinContent(binx,biny))
    if(muon.res_y!=0):
      if(m_h_Occupancy_XYresY[index_chamber].GetBinContent(binx,biny)==-999):
        m_h_Occupancy_XYresY[index_chamber].SetBinContent(binx,biny,muon.res_y)
      else:
        m_h_Occupancy_XYresY[index_chamber].SetBinContent(binx,biny,muon.res_x+m_h_Occupancy_XYresY[index_chamber].GetBinContent(binx,biny))
    m_h_Occupancy_XYresX_entries[index_chamber].SetBinContent(binx,biny,m_h_Occupancy_XYresX_entries[index_chamber].GetBinContent(binx,biny)+1)
    m_h_X_ResX[index_chamber].Fill(muon.pos_x,muon.res_x)
    MyBin = findBin(muon.pos_x,int(ResXBin),ResXBinRange/ResXBin) #You want 18 bins of 20 cm from -180 to 180. resXBin is 18, the other is the width, 360/18=120.
    if(MyBin==-999):
      print "WARNING, MyBin is -999 (muon.pos_x is too high or low)"
    l_h_ResX_AllBin[MyBin][index_chamber].Fill(muon.res_x)
print "Loop ended. Normalizing Histograms."
for thisChamber in selectedDT:
  index_chamber = convertChamberToIndex(thisChamber)
  for i in range(m_h_Occupancy_XYresX[index_chamber].GetNbinsX()):
    for j in range(m_h_Occupancy_XYresX[index_chamber].GetNbinsY()):
      if(m_h_Occupancy_XYresX[index_chamber].GetBinContent(i,j)!=-999):
        m_h_Occupancy_XYresX[index_chamber].SetBinContent(i,j,m_h_Occupancy_XYresX[index_chamber].GetBinContent(i,j)/m_h_Occupancy_XYresX_entries[index_chamber].GetBinContent(i,j))
      if(m_h_Occupancy_XYresY[index_chamber].GetBinContent(i,j)!=-999):
        m_h_Occupancy_XYresY[index_chamber].SetBinContent(i,j,m_h_Occupancy_XYresY[index_chamber].GetBinContent(i,j)/m_h_Occupancy_XYresX_entries[index_chamber].GetBinContent(i,j))

print "Start drawing histograms."
c1.SetGridx(); c1.SetGridy()
c1.SetCanvasSize(696,472)
r.gStyle.SetOptStat("rme")
fout = r.TFile(prefix + "Output.root","recreate"); fout.cd();
for thisChamber in selectedDT:
  print "Saving histos for chmaber:", thisChamber 
  #suffix=".pdf"
  IDName="_ID_" + str(thisChamber[0]) + "_" + str(thisChamber[1]) + "_" + str(thisChamber[2])
  index_chamber = convertChamberToIndex(thisChamber)
  m_h_Residual_X[index_chamber].Write()
  m_h_Residual_Y[index_chamber].Write()
  m_h_Occupancy_X[index_chamber].Write(); m_h_Occupancy_reb_X[index_chamber].Write();
  m_h_Occupancy_Y[index_chamber].Write()
  r.gStyle.SetOptStat(0)
  m_h_Occupancy_XY[index_chamber].Write()
  m_h_Occupancy_XY_weighted[index_chamber].Write()
  m_h_Occupancy_XYresX[index_chamber].Write()
  m_h_Occupancy_XYresX[index_chamber].Write()
  m_h_Occupancy_XYresY[index_chamber].Write()
  m_h_Occupancy_XYresY[index_chamber].Write()
  m_h_Occupancy_XYresX_entries[index_chamber].Write()
  m_h_X_ResX[index_chamber].Write()
  for nBin in range(ResXBin):
    l_h_ResX_AllBin[nBin][index_chamber].SetTitle("X Range: " + str(-ResXBinRange/2+nBin*(ResXBinRange)/ResXBin) + " , " + str(-ResXBinRange/2+(nBin+1)*(ResXBinRange)/ResXBin))
    l_h_ResX_AllBin[nBin][index_chamber].Write();
