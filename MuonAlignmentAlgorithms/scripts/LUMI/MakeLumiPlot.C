//------ This macro make a plot: Resolution vs Muons/chamber
#include <TH1F.h>
#include <TFile.h>
#include <TMath.h>
#include <TCanvas.h>
#include <TH2F.h>
#include <TF1.h>
#include <TH1D.h>
#include <TRandom3.h>
#include <TFormula.h>
#include <TPad.h>
#include <TLegend.h>
#include <TStyle.h>
#include <TROOT.h>
#include <TMarker.h>
#include <TChain.h>
#include <memory>
#include <string>
#include <map>
#include <vector>
#include "TTree.h"
#include "TLatex.h"
#include "TMath.h"
#include "TBranch.h"
#include "TFile.h"
#include "TStyle.h"
#include "TString.h"
#include "TEventList.h"
#include "TArrow.h"
#include <iostream>
#include <sstream>
#include <fstream>
#define NWheel 5
#define NChamber 4
#define NSector 14
#define NWheel_CSC 8
#define NRing_CSC 4
#define NSector_CSC 36

enum Wheel{ Wm2=0, Wm1, W0, Wp1, Wp2 };
enum Chamber{ Cha1=0, Cha2, Cha3, Cha4 };
enum HistoAr{ DT_m2_1=0, DT_m2_2, DT_m2_3, DT_m2_4, DT_m1_1, DT_m1_2, DT_m1_3, DT_m1_4, DT_0_1, DT_0_2, DT_0_3, DT_0_4, DT_p1_1, DT_p1_2, DT_p1_3, DT_p1_4, DT_p2_1, DT_p2_2, DT_p2_3, DT_p2_4 };
enum Wheel_CSC{ CSC_Wp1=0, CSC_Wp2, CSC_Wp3, CSC_Wp4, CSC_Wm1, CSC_Wm2, CSC_Wm3, CSC_Wm4 };
enum Ring_CSC{ CSC_R1=0, CSC_R2, CSC_R3, CSC_R4 };
enum HistoAr_CSC{ CSC_m1_1=0, CSC_m1_2, CSC_m1_3, CSC_m1_4, CSC_m2_1, CSC_m2_2, CSC_m3_1, CSC_m3_2, CSC_m4_1, CSC_m4_2, CSC_p1_1, CSC_p1_2, CSC_p1_3, CSC_p1_4, CSC_p2_1, CSC_p2_2, CSC_p3_1, CSC_p3_2, CSC_p4_1, CSC_p4_2 };

float*** Extract_Nmuons( TString Report, bool isDT );
void printStat( float*** StatErr, TString nameTXT );
TH1F** Init_plots( bool isDT, float MaxX );
TF1** Init_Fit( bool isDT, float MaxX );

//DT
//.x MakeLumiPlot.C+(true, "6","dx","cha_all","whe_all",0.8,210000.)
//.x MakeLumiPlot.C+(true, "6","dx","cha_1","whe_all",0.18,210000.)
//CSC
//.x MakeLumiPlot.C+(false, "6","dx","ring_1","whe_all",0.50,210000.)
void MakeLumiPlot( bool isDT=true, TString DOF="6", TString rms_type="dx", TString ShowChamber="cha_all", TString ShowWheel="whe_all", float MAX_Value=0.8, float MaxX=210000.){

  vector<TString> Report_files; Report_files.clear();
  vector<TString> Report_RMS; Report_RMS.clear();
  string Report_data;
  cout<<"--- START NOW ---"<<endl;
  if( isDT ){
    if( DOF=="6" ){
	Report_files.push_back("mc_DT-1100-111111_SingleMuon_MCRyan_8TeVspec_RECO_7_4_6_patch3_pt20_v1_FidBSpotFixMisal_OnethirdReal_03_report.py");
	Report_files.push_back("mc_DT-1100-111111_SingleMuon_MCRyan_8TeVspec_RECO_7_4_6_patch3_pt20_v1_FidBSpotFixMisal_Half_03_report.py");
	Report_files.push_back("mc_DT-1100-111111_SingleMuon_MCRyan_8TeVspec_RECO_7_4_6_patch3_pt20_v1_FidBSpotFixMisal_Onethird_03_report.py");
	Report_files.push_back("mc_DT-1100-111111_SingleMuon_MCRyan_8TeVspec_RECO_7_4_6_patch3_pt20_v1_FidBSpotFixMisal_03_report.py");
	Report_files.push_back("mc_DT-1100-111111_SingleMuon_MCRyan_8TeVspec_RECO_7_4_6_patch3_pt20_v1_FidBSpotFixMisal_1over8_03_report.py");
	Report_RMS.push_back("RMS_50M_6DOF_OnethirdReal.txt");
	Report_RMS.push_back("RMS_50M_6DOF_Half.txt");
	Report_RMS.push_back("RMS_50M_6DOF_Onethird.txt");
	Report_RMS.push_back("RMS_50M_6DOF.txt");
	Report_RMS.push_back("RMS_50M_6DOF_1over8.txt");
    }
    if( DOF=="3" ){
	Report_files.push_back("mc_DT-1100-110001_SingleMuon_MCRyan_8TeVspec_RECO_7_4_6_patch3_pt20_v1_FidBSpotFixMisal_03_report.py");
	Report_RMS.push_back("RMS_50M_3DOF.txt");
    }
    //Data
    Report_data="data_DT-1100-110001_SingleMuon_Run2015D-PromptReco-v3_RECO_CMSSW_7_4_12_patch4_pt20_pakhotin_v2_03_report.py";
  }//isCSC
  else{
    if( DOF=="6" ){
	Report_files.push_back("mc_CSC-1100-111111_SingleMuon_MCRyan_8TeVspec_RECO_7_4_6_patch3_pt20_v1_FID5DOF_ALL_01_report.py");
	Report_files.push_back("mc_CSC-1100-111111_SingleMuon_MCRyan_8TeVspec_RECO_7_4_6_patch3_pt20_v1_FID5DOF_01_report.py");
	Report_RMS.push_back("RMS_80M_111101_CSC.txt");
	Report_RMS.push_back("RMS_50M_111101_CSC.txt");
    }
    Report_data="data_CSC-1100-100001_SingleMuon_Run2015D-PromptReco-v3_RECO_CMSSW_7_4_12_patch4_pt20_pakhotin_v5_03_report.py";
  }
  //Histograms definition
  TCanvas* myc1 = new TCanvas("Lumi_vs_reso", "CMS", 600, 600);
  gStyle->SetOptStat(0);
  TH1F *Data = new TH1F("Data","",2000,0.,MaxX); Data->SetMarkerStyle(29); Data->SetMarkerSize(1.6); Data->SetMarkerColor(kBlack);
  TH1F *ResoPlots_dummy = new TH1F("ResoPlots_dummy","",1000,0.,MaxX); 
  cout<<"Let's initialize plots and functions!"<<endl;
  TH1F **ResoPlots = Init_plots( isDT, MaxX );
  TF1 **f = Init_Fit( isDT, MaxX );
  //First histo to be plotted
  ResoPlots_dummy->SetTitle("Lumi: 2.6 fb^{-1}");
  ResoPlots_dummy->GetYaxis()->SetTitleOffset(1.4);
  ResoPlots_dummy->GetXaxis()->SetTitle("Muons/Chamber");
  if(rms_type=="dx") ResoPlots_dummy->GetYaxis()->SetTitle("#Delta X RMS [mm]");
  if(rms_type=="dy") ResoPlots_dummy->GetYaxis()->SetTitle("#Delta Y RMS [mm]");
  if(rms_type=="dz") ResoPlots_dummy->GetYaxis()->SetTitle("#Delta Z RMS [mm]");
  if(rms_type=="dphiz") ResoPlots_dummy->GetYaxis()->SetTitle("#Delta #Phi X RMS [mrad]");
  //Extract muon/chamber for data
  cout<<"Opening DATA report file: "<<Report_data<<endl;
  float Chambers_data_w[NWheel][NChamber]={-1};
  float Chambers_data_w_csc[NWheel_CSC][NRing_CSC]={-1};
  float*** Chambers_data = Extract_Nmuons(Report_data, isDT);
  if(isDT){
    for(int jwheel=0; jwheel<NWheel; jwheel++){
	for(int kcham=0; kcham<NChamber; kcham++){
	  int maxSec = NSector;
	  if(kcham!=3) maxSec=12;
	  float Nmu(0.), totSec(0.);
	  for(int hsec=0; hsec<maxSec; hsec++){
	    Nmu += Chambers_data[jwheel][kcham][hsec];
	    totSec++;
	  }
	  Chambers_data_w[jwheel][kcham] = Nmu/totSec;
	}
    }
  }// and CSC
  else{
    for(int jwheel=0; jwheel<NWheel_CSC; jwheel++){
	int maxRing = NRing_CSC;
	if( jwheel!=CSC_Wp1 && jwheel!=CSC_Wm1 ) maxRing = 2;
	for(int kRing=0; kRing<maxRing; kRing++){
	  int maxSec = NSector_CSC;
	  if( jwheel!=CSC_Wp1 && jwheel!=CSC_Wm1 && kRing!=CSC_R2 ) maxSec = 18;
	  float Nmu(0.), totSec(0.);
	  for(int hsec=0; hsec<maxSec; hsec++){
	    Nmu += Chambers_data[jwheel][kRing][hsec];
	    totSec++;
	  }
	  Chambers_data_w_csc[jwheel][kRing] = Nmu/totSec;
	}
    }
  }
  //Now Extract muon/chamber for each file
  float Chambers_w[NWheel][NChamber]={-1};
  float Chambers_RMS[NWheel][NChamber]={-1};
  float Chambers_w_csc[NWheel_CSC][NRing_CSC]={-1};
  float Chambers_RMS_csc[NWheel_CSC][NRing_CSC]={-1};
  for(int i=0; i<int(Report_files.size()); i++){
    cout<<"Opening MC file: "<<Report_files[i]<<endl;
    cout<<"Opening MC RMS files: "<<Report_RMS[i]<<endl;
    if(isDT){
	float*** Chambers = Extract_Nmuons(Report_files[i].Data(), isDT);
	//Average Chamber number of muons
	for(int jwheel=0; jwheel<NWheel; jwheel++){
	  for(int kcham=0; kcham<NChamber; kcham++){
	    int maxSec = NSector;
	    if(kcham!=3) maxSec=12;
	    float Nmu(0.), totSec(0.);
	    for(int hsec=0; hsec<maxSec; hsec++){
		Nmu += Chambers[jwheel][kcham][hsec];
		totSec++;
	    }
	    Chambers_w[jwheel][kcham] = Nmu/totSec;
	  }
	}
    }
    else{
//	for(int i=0; i<int(Report_files.size()); i++){
	  float*** Chambers = Extract_Nmuons(Report_files[i].Data(), isDT);
	  //Average Chamber number of muons
	  for(int jwheel=0; jwheel<NWheel_CSC; jwheel++){
	    int maxRing = NRing_CSC;
	    if( jwheel!=CSC_Wp1 && jwheel!=CSC_Wm1 ) maxRing = 2;
	    for(int kRing=0; kRing<maxRing; kRing++){
		int maxSec = NSector_CSC;
		if( jwheel!=CSC_Wp1 && jwheel!=CSC_Wm1 && kRing!=CSC_R2 ) maxSec = 18;
		float Nmu(0.), totSec(0.);
		for(int hsec=0; hsec<maxSec; hsec++){
		  Nmu += Chambers[jwheel][kRing][hsec];
		  totSec++;
		}
		Chambers_w_csc[jwheel][kRing] = Nmu/totSec;
	    }
	  }
//	}
    }
    //Now Extract Sigma
    std::string Line;
    std::ifstream Myfile( Report_RMS[i].Data() );
    if( !Myfile ) std::cout<<"ERROR opening "<<Report_RMS[i].Data()<<std::endl;
    int cha(1);
    while (std::getline(Myfile, Line)){
	TString Line2(Line);
	std::istringstream buf(Line2.Data());
	std::istream_iterator<std::string> beg(buf), end;
	std::vector<std::string> tokens(beg, end);
	int index=-1;
	if(rms_type=="dx") index=1;
	if(rms_type=="dy") index=2;
	if(rms_type=="dz") index=3;
	if(rms_type=="dphix") index=4;
	if(rms_type=="dphiy") index=5;
	if(rms_type=="dphiz") index=6;
	if(isDT){
	  int wheels(-1), chamb(-1);
	  if(cha<5)       { wheels = Wp2; chamb = cha; }
	  else if(cha<9)  { wheels = Wp1; chamb = cha-4; }
	  else if(cha<13) { wheels = W0;  chamb = cha-8; }
	  else if(cha<17) { wheels = Wm1; chamb = cha-12; }
	  else            { wheels = Wm2; chamb = cha-16; }
	  Chambers_RMS[wheels][chamb-1] = std::atof(tokens[index].c_str());
	}
	else{
	  int wheels(-1), iRing(-1);
	  if(cha<4)       { wheels = CSC_Wp1; iRing = cha; }
	  else if(cha<6)  { wheels = CSC_Wp2; iRing = cha-3; }
	  else if(cha<8)  { wheels = CSC_Wp3; iRing = cha-5; }
	  else if(cha<10) { wheels = CSC_Wp4; iRing = cha-7; }
	  else if(cha<13) { wheels = CSC_Wm1; iRing = cha-9; }
	  else if(cha<15) { wheels = CSC_Wm2; iRing = cha-12; }
	  else if(cha<17) { wheels = CSC_Wm3; iRing = cha-14; }
	  else            { wheels = CSC_Wm4; iRing = cha-16; }
	  Chambers_RMS_csc[wheels][iRing-1] = std::atof(tokens[index].c_str());
	}
	cha++;
    }
    if( !isDT ) Chambers_RMS_csc[CSC_Wm1][4-1] = Chambers_RMS_csc[CSC_Wm1][1-1];
    if( !isDT ) Chambers_RMS_csc[CSC_Wp1][4-1] = Chambers_RMS_csc[CSC_Wp1][1-1];
    if( isDT ){
	for(int jwheel=0; jwheel<NWheel; jwheel++){
	  for(int kcham=0; kcham<NChamber; kcham++){
	    int thisbin = ResoPlots[DT_m2_1]->FindBin(Chambers_w[jwheel][kcham]);
	    if( Chambers_w[jwheel][kcham] > MaxX ) cout<<"WARNING: you need to increase the X axis limit! "<<Chambers_w[jwheel][kcham] <<" or "<<Chambers_data_w[jwheel][kcham]<<endl;
	    if(jwheel==Wm2 && kcham==Cha1) ResoPlots[DT_m2_1]->SetBinContent(thisbin,Chambers_RMS[jwheel][kcham]); 
	    if(jwheel==Wm2 && kcham==Cha2) ResoPlots[DT_m2_2]->SetBinContent(thisbin,Chambers_RMS[jwheel][kcham]); 
	    if(jwheel==Wm2 && kcham==Cha3) ResoPlots[DT_m2_3]->SetBinContent(thisbin,Chambers_RMS[jwheel][kcham]); 
	    if(jwheel==Wm2 && kcham==Cha4) ResoPlots[DT_m2_4]->SetBinContent(thisbin,Chambers_RMS[jwheel][kcham]); 
	    if(jwheel==Wm1 && kcham==Cha1) ResoPlots[DT_m1_1]->SetBinContent(thisbin,Chambers_RMS[jwheel][kcham]); 
	    if(jwheel==Wm1 && kcham==Cha2) ResoPlots[DT_m1_2]->SetBinContent(thisbin,Chambers_RMS[jwheel][kcham]); 
	    if(jwheel==Wm1 && kcham==Cha3) ResoPlots[DT_m1_3]->SetBinContent(thisbin,Chambers_RMS[jwheel][kcham]); 
	    if(jwheel==Wm1 && kcham==Cha4) ResoPlots[DT_m1_4]->SetBinContent(thisbin,Chambers_RMS[jwheel][kcham]); 
	    if(jwheel==W0 && kcham==Cha1)  ResoPlots[DT_0_1]->SetBinContent(thisbin,Chambers_RMS[jwheel][kcham]);  
	    if(jwheel==W0 && kcham==Cha2)  ResoPlots[DT_0_2]->SetBinContent(thisbin,Chambers_RMS[jwheel][kcham]);  
	    if(jwheel==W0 && kcham==Cha3)  ResoPlots[DT_0_3]->SetBinContent(thisbin,Chambers_RMS[jwheel][kcham]);  
	    if(jwheel==W0 && kcham==Cha4)  ResoPlots[DT_0_4]->SetBinContent(thisbin,Chambers_RMS[jwheel][kcham]);  
	    if(jwheel==Wp1 && kcham==Cha1) ResoPlots[DT_p1_1]->SetBinContent(thisbin,Chambers_RMS[jwheel][kcham]); 
	    if(jwheel==Wp1 && kcham==Cha2) ResoPlots[DT_p1_2]->SetBinContent(thisbin,Chambers_RMS[jwheel][kcham]); 
	    if(jwheel==Wp1 && kcham==Cha3) ResoPlots[DT_p1_3]->SetBinContent(thisbin,Chambers_RMS[jwheel][kcham]); 
	    if(jwheel==Wp1 && kcham==Cha4) ResoPlots[DT_p1_4]->SetBinContent(thisbin,Chambers_RMS[jwheel][kcham]); 
	    if(jwheel==Wp2 && kcham==Cha1) ResoPlots[DT_p2_1]->SetBinContent(thisbin,Chambers_RMS[jwheel][kcham]); 
	    if(jwheel==Wp2 && kcham==Cha2) ResoPlots[DT_p2_2]->SetBinContent(thisbin,Chambers_RMS[jwheel][kcham]); 
	    if(jwheel==Wp2 && kcham==Cha3) ResoPlots[DT_p2_3]->SetBinContent(thisbin,Chambers_RMS[jwheel][kcham]); 
	    if(jwheel==Wp2 && kcham==Cha4) ResoPlots[DT_p2_4]->SetBinContent(thisbin,Chambers_RMS[jwheel][kcham]); 
	  }
	}
    }
    else{
	for(int jwheel=0; jwheel<NWheel_CSC; jwheel++){
	  int maxRing = NRing_CSC;
	  if( jwheel!=CSC_Wp1 && jwheel!=CSC_Wm1 ) maxRing = 2;
	  for(int kcham=0; kcham<maxRing; kcham++){
	    int thisbin = ResoPlots[CSC_Wp1]->FindBin(Chambers_w_csc[jwheel][kcham]);
	    if( Chambers_w_csc[jwheel][kcham] > MaxX ) cout<<"WARNING: you need to increase the X axis limit! "<<Chambers_w_csc[jwheel][kcham] <<" or "<<Chambers_data_w_csc[jwheel][kcham]<<endl;
	    if(jwheel==CSC_Wp1 && kcham==CSC_R1) ResoPlots[CSC_p1_1]->SetBinContent(thisbin,Chambers_RMS_csc[jwheel][kcham]); 
	    if(jwheel==CSC_Wp1 && kcham==CSC_R2) ResoPlots[CSC_p1_2]->SetBinContent(thisbin,Chambers_RMS_csc[jwheel][kcham]); 
	    if(jwheel==CSC_Wp1 && kcham==CSC_R3) ResoPlots[CSC_p1_3]->SetBinContent(thisbin,Chambers_RMS_csc[jwheel][kcham]); 
	    if(jwheel==CSC_Wp1 && kcham==CSC_R4) ResoPlots[CSC_p1_4]->SetBinContent(thisbin,Chambers_RMS_csc[jwheel][kcham]); 
	    if(jwheel==CSC_Wp2 && kcham==CSC_R1) ResoPlots[CSC_p2_1]->SetBinContent(thisbin,Chambers_RMS_csc[jwheel][kcham]); 
	    if(jwheel==CSC_Wp2 && kcham==CSC_R2) ResoPlots[CSC_p2_2]->SetBinContent(thisbin,Chambers_RMS_csc[jwheel][kcham]); 
	    if(jwheel==CSC_Wp3 && kcham==CSC_R1) ResoPlots[CSC_p3_1]->SetBinContent(thisbin,Chambers_RMS_csc[jwheel][kcham]); 
	    if(jwheel==CSC_Wp3 && kcham==CSC_R2) ResoPlots[CSC_p3_2]->SetBinContent(thisbin,Chambers_RMS_csc[jwheel][kcham]); 
	    if(jwheel==CSC_Wp4 && kcham==CSC_R1) ResoPlots[CSC_p4_1]->SetBinContent(thisbin,Chambers_RMS_csc[jwheel][kcham]); 
	    if(jwheel==CSC_Wp4 && kcham==CSC_R2) ResoPlots[CSC_p4_2]->SetBinContent(thisbin,Chambers_RMS_csc[jwheel][kcham]); 
	    if(jwheel==CSC_Wm1 && kcham==CSC_R1) ResoPlots[CSC_m1_1]->SetBinContent(thisbin,Chambers_RMS_csc[jwheel][kcham]); 
	    if(jwheel==CSC_Wm1 && kcham==CSC_R2) ResoPlots[CSC_m1_2]->SetBinContent(thisbin,Chambers_RMS_csc[jwheel][kcham]); 
	    if(jwheel==CSC_Wm1 && kcham==CSC_R3) ResoPlots[CSC_m1_3]->SetBinContent(thisbin,Chambers_RMS_csc[jwheel][kcham]); 
	    if(jwheel==CSC_Wm1 && kcham==CSC_R4) ResoPlots[CSC_m1_4]->SetBinContent(thisbin,Chambers_RMS_csc[jwheel][kcham]); 
	    if(jwheel==CSC_Wm2 && kcham==CSC_R1) ResoPlots[CSC_m2_1]->SetBinContent(thisbin,Chambers_RMS_csc[jwheel][kcham]); 
	    if(jwheel==CSC_Wm2 && kcham==CSC_R2) ResoPlots[CSC_m2_2]->SetBinContent(thisbin,Chambers_RMS_csc[jwheel][kcham]); 
	    if(jwheel==CSC_Wm3 && kcham==CSC_R1) ResoPlots[CSC_m3_1]->SetBinContent(thisbin,Chambers_RMS_csc[jwheel][kcham]); 
	    if(jwheel==CSC_Wm3 && kcham==CSC_R2) ResoPlots[CSC_m3_2]->SetBinContent(thisbin,Chambers_RMS_csc[jwheel][kcham]); 
	    if(jwheel==CSC_Wm4 && kcham==CSC_R1) ResoPlots[CSC_m4_1]->SetBinContent(thisbin,Chambers_RMS_csc[jwheel][kcham]); 
	    if(jwheel==CSC_Wm4 && kcham==CSC_R2) ResoPlots[CSC_m4_2]->SetBinContent(thisbin,Chambers_RMS_csc[jwheel][kcham]); 
	  }
	}
    }
  }//for each sample
  //Now Draw the Histograms
  ResoPlots_dummy->SetMinimum(0.);
  ResoPlots_dummy->SetMaximum(MAX_Value);
  ResoPlots_dummy->Draw("");
  if( isDT && (ShowChamber=="cha_all" || ShowChamber.Contains("1")) && (ShowWheel.Contains("whe_all") || ShowWheel.Contains("m2")) )ResoPlots[DT_m2_1]->Draw("Psame");
  if( isDT && (ShowChamber=="cha_all" || ShowChamber.Contains("2")) && (ShowWheel.Contains("whe_all") || ShowWheel.Contains("m2")) )ResoPlots[DT_m2_2]->Draw("Psame");
  if( isDT && (ShowChamber=="cha_all" || ShowChamber.Contains("3")) && (ShowWheel.Contains("whe_all") || ShowWheel.Contains("m2")) )ResoPlots[DT_m2_3]->Draw("Psame");
  if( isDT && (ShowChamber=="cha_all" || ShowChamber.Contains("4")) && (ShowWheel.Contains("whe_all") || ShowWheel.Contains("m2")) )ResoPlots[DT_m2_4]->Draw("Psame");
  if( isDT && (ShowChamber=="cha_all" || ShowChamber.Contains("1")) && (ShowWheel.Contains("whe_all") || ShowWheel.Contains("m1")) )ResoPlots[DT_m1_1]->Draw("Psame");
  if( isDT && (ShowChamber=="cha_all" || ShowChamber.Contains("2")) && (ShowWheel.Contains("whe_all") || ShowWheel.Contains("m1")) )ResoPlots[DT_m1_2]->Draw("Psame");
  if( isDT && (ShowChamber=="cha_all" || ShowChamber.Contains("3")) && (ShowWheel.Contains("whe_all") || ShowWheel.Contains("m1")) )ResoPlots[DT_m1_3]->Draw("Psame");
  if( isDT && (ShowChamber=="cha_all" || ShowChamber.Contains("4")) && (ShowWheel.Contains("whe_all") || ShowWheel.Contains("m1")) )ResoPlots[DT_m1_4]->Draw("Psame");
  if( isDT && (ShowChamber=="cha_all" || ShowChamber.Contains("1")) && (ShowWheel.Contains("whe_all") || ShowWheel.Contains("0")) ) ResoPlots[DT_0_1]->Draw("Psame");
  if( isDT && (ShowChamber=="cha_all" || ShowChamber.Contains("2")) && (ShowWheel.Contains("whe_all") || ShowWheel.Contains("0")) ) ResoPlots[DT_0_2]->Draw("Psame");
  if( isDT && (ShowChamber=="cha_all" || ShowChamber.Contains("3")) && (ShowWheel.Contains("whe_all") || ShowWheel.Contains("0")) ) ResoPlots[DT_0_3]->Draw("Psame");
  if( isDT && (ShowChamber=="cha_all" || ShowChamber.Contains("4")) && (ShowWheel.Contains("whe_all") || ShowWheel.Contains("0")) ) ResoPlots[DT_0_4]->Draw("Psame");
  if( isDT && (ShowChamber=="cha_all" || ShowChamber.Contains("1")) && (ShowWheel.Contains("whe_all") || ShowWheel.Contains("p1")) )ResoPlots[DT_p1_1]->Draw("Psame");
  if( isDT && (ShowChamber=="cha_all" || ShowChamber.Contains("2")) && (ShowWheel.Contains("whe_all") || ShowWheel.Contains("p1")) )ResoPlots[DT_p1_2]->Draw("Psame");
  if( isDT && (ShowChamber=="cha_all" || ShowChamber.Contains("3")) && (ShowWheel.Contains("whe_all") || ShowWheel.Contains("p1")) )ResoPlots[DT_p1_3]->Draw("Psame");
  if( isDT && (ShowChamber=="cha_all" || ShowChamber.Contains("4")) && (ShowWheel.Contains("whe_all") || ShowWheel.Contains("p1")) )ResoPlots[DT_p1_4]->Draw("Psame");
  if( isDT && (ShowChamber=="cha_all" || ShowChamber.Contains("1")) && (ShowWheel.Contains("whe_all") || ShowWheel.Contains("p2")) )ResoPlots[DT_p2_1]->Draw("Psame");
  if( isDT && (ShowChamber=="cha_all" || ShowChamber.Contains("2")) && (ShowWheel.Contains("whe_all") || ShowWheel.Contains("p2")) )ResoPlots[DT_p2_2]->Draw("Psame");
  if( isDT && (ShowChamber=="cha_all" || ShowChamber.Contains("3")) && (ShowWheel.Contains("whe_all") || ShowWheel.Contains("p2")) )ResoPlots[DT_p2_3]->Draw("Psame");
  if( isDT && (ShowChamber=="cha_all" || ShowChamber.Contains("4")) && (ShowWheel.Contains("whe_all") || ShowWheel.Contains("p2")) )ResoPlots[DT_p2_4]->Draw("Psame");
  if( !isDT && (ShowChamber=="ring_all" || ShowChamber.Contains("1")) && (ShowWheel.Contains("whe_all") || ShowWheel.Contains("m1")) )ResoPlots[CSC_m1_1]->Draw("Psame");
  if( !isDT && (ShowChamber=="ring_all" || ShowChamber.Contains("2")) && (ShowWheel.Contains("whe_all") || ShowWheel.Contains("m1")) )ResoPlots[CSC_m1_2]->Draw("Psame");
  if( !isDT && (ShowChamber=="ring_all" || ShowChamber.Contains("3")) && (ShowWheel.Contains("whe_all") || ShowWheel.Contains("m1")) )ResoPlots[CSC_m1_3]->Draw("Psame");
  if( !isDT && (ShowChamber=="ring_all" || ShowChamber.Contains("4")) && (ShowWheel.Contains("whe_all") || ShowWheel.Contains("m1")) )ResoPlots[CSC_m1_4]->Draw("Psame");
  if( !isDT && (ShowChamber=="ring_all" || ShowChamber.Contains("1")) && (ShowWheel.Contains("whe_all") || ShowWheel.Contains("m2")) )ResoPlots[CSC_m2_1]->Draw("Psame");
  if( !isDT && (ShowChamber=="ring_all" || ShowChamber.Contains("2")) && (ShowWheel.Contains("whe_all") || ShowWheel.Contains("m2")) )ResoPlots[CSC_m2_2]->Draw("Psame");
  if( !isDT && (ShowChamber=="ring_all" || ShowChamber.Contains("1")) && (ShowWheel.Contains("whe_all") || ShowWheel.Contains("m3")) )ResoPlots[CSC_m3_1]->Draw("Psame");
  if( !isDT && (ShowChamber=="ring_all" || ShowChamber.Contains("2")) && (ShowWheel.Contains("whe_all") || ShowWheel.Contains("m3")) )ResoPlots[CSC_m3_2]->Draw("Psame");
  if( !isDT && (ShowChamber=="ring_all" || ShowChamber.Contains("1")) && (ShowWheel.Contains("whe_all") || ShowWheel.Contains("m4")) )ResoPlots[CSC_m4_1]->Draw("Psame");
  if( !isDT && (ShowChamber=="ring_all" || ShowChamber.Contains("2")) && (ShowWheel.Contains("whe_all") || ShowWheel.Contains("m4")) )ResoPlots[CSC_m4_2]->Draw("Psame");
  if( !isDT && (ShowChamber=="ring_all" || ShowChamber.Contains("1")) && (ShowWheel.Contains("whe_all") || ShowWheel.Contains("p1")) )ResoPlots[CSC_p1_1]->Draw("Psame");
  if( !isDT && (ShowChamber=="ring_all" || ShowChamber.Contains("2")) && (ShowWheel.Contains("whe_all") || ShowWheel.Contains("p1")) )ResoPlots[CSC_p1_2]->Draw("Psame");
  if( !isDT && (ShowChamber=="ring_all" || ShowChamber.Contains("3")) && (ShowWheel.Contains("whe_all") || ShowWheel.Contains("p1")) )ResoPlots[CSC_p1_3]->Draw("Psame");
  if( !isDT && (ShowChamber=="ring_all" || ShowChamber.Contains("4")) && (ShowWheel.Contains("whe_all") || ShowWheel.Contains("p1")) )ResoPlots[CSC_p1_4]->Draw("Psame");
  if( !isDT && (ShowChamber=="ring_all" || ShowChamber.Contains("1")) && (ShowWheel.Contains("whe_all") || ShowWheel.Contains("p2")) )ResoPlots[CSC_p2_1]->Draw("Psame");
  if( !isDT && (ShowChamber=="ring_all" || ShowChamber.Contains("2")) && (ShowWheel.Contains("whe_all") || ShowWheel.Contains("p2")) )ResoPlots[CSC_p2_2]->Draw("Psame");
  if( !isDT && (ShowChamber=="ring_all" || ShowChamber.Contains("1")) && (ShowWheel.Contains("whe_all") || ShowWheel.Contains("p3")) )ResoPlots[CSC_p3_1]->Draw("Psame");
  if( !isDT && (ShowChamber=="ring_all" || ShowChamber.Contains("2")) && (ShowWheel.Contains("whe_all") || ShowWheel.Contains("p3")) )ResoPlots[CSC_p3_2]->Draw("Psame");
  if( !isDT && (ShowChamber=="ring_all" || ShowChamber.Contains("1")) && (ShowWheel.Contains("whe_all") || ShowWheel.Contains("p4")) )ResoPlots[CSC_p4_1]->Draw("Psame");
  if( !isDT && (ShowChamber=="ring_all" || ShowChamber.Contains("2")) && (ShowWheel.Contains("whe_all") || ShowWheel.Contains("p4")) )ResoPlots[CSC_p4_2]->Draw("Psame");
  TLegend *leg = new TLegend(0.66,0.52,0.89,0.88);
  leg->SetHeader("Notation:");
  leg->SetBorderSize(0);
  leg->SetTextFont(132);
  leg->SetTextSize(0.02);
  if( isDT ){
  leg->AddEntry(ResoPlots[DT_0_1], "Black: wheel 0","lep");
  leg->AddEntry(ResoPlots[DT_m1_1],"Blue: wheel 1","lep");
  leg->AddEntry(ResoPlots[DT_m2_1],"Red: wheel 2","lep");
  leg->AddEntry(ResoPlots[DT_m2_1],"Chamber 1","lep");
  leg->AddEntry(ResoPlots[DT_m2_2],"Chamber 2","lep");
  leg->AddEntry(ResoPlots[DT_m2_3],"Chamber 3","lep");
  leg->AddEntry(ResoPlots[DT_m2_4],"Chamber 4","lep");
  leg->AddEntry(ResoPlots[DT_m2_4],"Lines: statistic in DATA","l");
  }
  else{
  leg->AddEntry(ResoPlots[CSC_m1_1],"Black: wheel 1","lep");
  leg->AddEntry(ResoPlots[CSC_m2_1],"Blue: wheel 2","lep");
  leg->AddEntry(ResoPlots[CSC_m3_1],"Green: wheel 3","lep");
  leg->AddEntry(ResoPlots[CSC_m4_1],"Red: wheel 4","lep");
  leg->AddEntry(ResoPlots[CSC_m1_1],"Ring 1","lep");
  leg->AddEntry(ResoPlots[CSC_m1_2],"Ring 2","lep");
  leg->AddEntry(ResoPlots[CSC_m1_3],"Ring 3","lep");
  leg->AddEntry(ResoPlots[CSC_m1_4],"Ring 4","lep");
  leg->AddEntry(ResoPlots[CSC_m1_4],"Lines: statistic in DATA","l");
  }
  leg->Draw("same");

  if( isDT ){
    f[DT_m2_1]->SetParameter(0,Chambers_RMS[Wm2][Cha1]); f[DT_m2_1]->SetParameter(1,Chambers_w[Wm2][Cha1]); 
    f[DT_m2_2]->SetParameter(0,Chambers_RMS[Wm2][Cha2]); f[DT_m2_2]->SetParameter(1,Chambers_w[Wm2][Cha2]); 
    f[DT_m2_3]->SetParameter(0,Chambers_RMS[Wm2][Cha3]); f[DT_m2_3]->SetParameter(1,Chambers_w[Wm2][Cha3]); 
    f[DT_m2_4]->SetParameter(0,Chambers_RMS[Wm2][Cha4]); f[DT_m2_4]->SetParameter(1,Chambers_w[Wm2][Cha4]); 
    f[DT_m1_1]->SetParameter(0,Chambers_RMS[Wm1][Cha1]); f[DT_m1_1]->SetParameter(1,Chambers_w[Wm1][Cha1]); 
    f[DT_m1_2]->SetParameter(0,Chambers_RMS[Wm1][Cha2]); f[DT_m1_2]->SetParameter(1,Chambers_w[Wm1][Cha2]); 
    f[DT_m1_3]->SetParameter(0,Chambers_RMS[Wm1][Cha3]); f[DT_m1_3]->SetParameter(1,Chambers_w[Wm1][Cha3]); 
    f[DT_m1_4]->SetParameter(0,Chambers_RMS[Wm1][Cha4]); f[DT_m1_4]->SetParameter(1,Chambers_w[Wm1][Cha4]); 
    f[DT_0_1]->SetParameter(0,Chambers_RMS[W0][Cha1]);   f[DT_0_1]->SetParameter(1,Chambers_w[W0][Cha1]);   
    f[DT_0_2]->SetParameter(0,Chambers_RMS[W0][Cha2]);   f[DT_0_2]->SetParameter(1,Chambers_w[W0][Cha2]);   
    f[DT_0_3]->SetParameter(0,Chambers_RMS[W0][Cha3]);   f[DT_0_3]->SetParameter(1,Chambers_w[W0][Cha3]);   
    f[DT_0_4]->SetParameter(0,Chambers_RMS[W0][Cha4]);   f[DT_0_4]->SetParameter(1,Chambers_w[W0][Cha4]);   
    f[DT_p1_1]->SetParameter(0,Chambers_RMS[Wp1][Cha1]); f[DT_p1_1]->SetParameter(1,Chambers_w[Wp1][Cha1]); 
    f[DT_p1_2]->SetParameter(0,Chambers_RMS[Wp1][Cha2]); f[DT_p1_2]->SetParameter(1,Chambers_w[Wp1][Cha2]); 
    f[DT_p1_3]->SetParameter(0,Chambers_RMS[Wp1][Cha3]); f[DT_p1_3]->SetParameter(1,Chambers_w[Wp1][Cha3]); 
    f[DT_p1_4]->SetParameter(0,Chambers_RMS[Wp1][Cha4]); f[DT_p1_4]->SetParameter(1,Chambers_w[Wp1][Cha4]);
    f[DT_p2_1]->SetParameter(0,Chambers_RMS[Wp2][Cha1]); f[DT_p2_1]->SetParameter(1,Chambers_w[Wp2][Cha1]); 
    f[DT_p2_2]->SetParameter(0,Chambers_RMS[Wp2][Cha2]); f[DT_p2_2]->SetParameter(1,Chambers_w[Wp2][Cha2]); 
    f[DT_p2_3]->SetParameter(0,Chambers_RMS[Wp2][Cha3]); f[DT_p2_3]->SetParameter(1,Chambers_w[Wp2][Cha3]); 
    f[DT_p2_4]->SetParameter(0,Chambers_RMS[Wp2][Cha4]); f[DT_p2_4]->SetParameter(1,Chambers_w[Wp2][Cha4]); 
  }
  else{
    f[CSC_m1_1]->SetParameter(0,Chambers_RMS_csc[CSC_Wm1][CSC_R1]); f[CSC_m1_1]->SetParameter(1,Chambers_w_csc[CSC_Wm1][CSC_R1]);
    f[CSC_m1_2]->SetParameter(0,Chambers_RMS_csc[CSC_Wm1][CSC_R2]); f[CSC_m1_2]->SetParameter(1,Chambers_w_csc[CSC_Wm1][CSC_R2]);
    f[CSC_m1_3]->SetParameter(0,Chambers_RMS_csc[CSC_Wm1][CSC_R3]); f[CSC_m1_3]->SetParameter(1,Chambers_w_csc[CSC_Wm1][CSC_R3]);
    f[CSC_m1_4]->SetParameter(0,Chambers_RMS_csc[CSC_Wm1][CSC_R4]); f[CSC_m1_4]->SetParameter(1,Chambers_w_csc[CSC_Wm1][CSC_R4]);
    f[CSC_m2_1]->SetParameter(0,Chambers_RMS_csc[CSC_Wm2][CSC_R1]); f[CSC_m2_1]->SetParameter(1,Chambers_w_csc[CSC_Wm2][CSC_R1]);
    f[CSC_m2_2]->SetParameter(0,Chambers_RMS_csc[CSC_Wm2][CSC_R2]); f[CSC_m2_2]->SetParameter(1,Chambers_w_csc[CSC_Wm2][CSC_R2]);
    f[CSC_m3_1]->SetParameter(0,Chambers_RMS_csc[CSC_Wm3][CSC_R1]); f[CSC_m3_1]->SetParameter(1,Chambers_w_csc[CSC_Wm3][CSC_R1]);
    f[CSC_m3_2]->SetParameter(0,Chambers_RMS_csc[CSC_Wm3][CSC_R2]); f[CSC_m3_2]->SetParameter(1,Chambers_w_csc[CSC_Wm3][CSC_R2]);
    f[CSC_m4_1]->SetParameter(0,Chambers_RMS_csc[CSC_Wm4][CSC_R1]); f[CSC_m4_1]->SetParameter(1,Chambers_w_csc[CSC_Wm4][CSC_R1]);
    f[CSC_m4_2]->SetParameter(0,Chambers_RMS_csc[CSC_Wm4][CSC_R2]); f[CSC_m4_2]->SetParameter(1,Chambers_w_csc[CSC_Wm4][CSC_R2]);
    f[CSC_p1_1]->SetParameter(0,Chambers_RMS_csc[CSC_Wp1][CSC_R1]); f[CSC_p1_1]->SetParameter(1,Chambers_w_csc[CSC_Wp1][CSC_R1]);
    f[CSC_p1_2]->SetParameter(0,Chambers_RMS_csc[CSC_Wp1][CSC_R2]); f[CSC_p1_2]->SetParameter(1,Chambers_w_csc[CSC_Wp1][CSC_R2]);
    f[CSC_p1_3]->SetParameter(0,Chambers_RMS_csc[CSC_Wp1][CSC_R3]); f[CSC_p1_3]->SetParameter(1,Chambers_w_csc[CSC_Wp1][CSC_R3]);
    f[CSC_p1_4]->SetParameter(0,Chambers_RMS_csc[CSC_Wp1][CSC_R4]); f[CSC_p1_4]->SetParameter(1,Chambers_w_csc[CSC_Wp1][CSC_R4]);
    f[CSC_p2_1]->SetParameter(0,Chambers_RMS_csc[CSC_Wp2][CSC_R1]); f[CSC_p2_1]->SetParameter(1,Chambers_w_csc[CSC_Wp2][CSC_R1]);
    f[CSC_p2_2]->SetParameter(0,Chambers_RMS_csc[CSC_Wp2][CSC_R2]); f[CSC_p2_2]->SetParameter(1,Chambers_w_csc[CSC_Wp2][CSC_R2]);
    f[CSC_p3_1]->SetParameter(0,Chambers_RMS_csc[CSC_Wp3][CSC_R1]); f[CSC_p3_1]->SetParameter(1,Chambers_w_csc[CSC_Wp3][CSC_R1]);
    f[CSC_p3_2]->SetParameter(0,Chambers_RMS_csc[CSC_Wp3][CSC_R2]); f[CSC_p3_2]->SetParameter(1,Chambers_w_csc[CSC_Wp3][CSC_R2]);
    f[CSC_p4_1]->SetParameter(0,Chambers_RMS_csc[CSC_Wp4][CSC_R1]); f[CSC_p4_1]->SetParameter(1,Chambers_w_csc[CSC_Wp4][CSC_R1]);
    f[CSC_p4_2]->SetParameter(0,Chambers_RMS_csc[CSC_Wp4][CSC_R2]); f[CSC_p4_2]->SetParameter(1,Chambers_w_csc[CSC_Wp4][CSC_R2]);
  }
  if( isDT ){
     if( (ShowChamber=="cha_all" || ShowChamber.Contains("1")) && (ShowWheel.Contains("whe_all") || ShowWheel.Contains("m2"))) f[DT_m2_1]->Draw("same"); 
     if( (ShowChamber=="cha_all" || ShowChamber.Contains("2")) && (ShowWheel.Contains("whe_all") || ShowWheel.Contains("m2"))) f[DT_m2_2]->Draw("same");
     if( (ShowChamber=="cha_all" || ShowChamber.Contains("3")) && (ShowWheel.Contains("whe_all") || ShowWheel.Contains("m2"))) f[DT_m2_3]->Draw("same");
     if( (ShowChamber=="cha_all" || ShowChamber.Contains("4")) && (ShowWheel.Contains("whe_all") || ShowWheel.Contains("m2"))) f[DT_m2_4]->Draw("same");
     if( (ShowChamber=="cha_all" || ShowChamber.Contains("1")) && (ShowWheel.Contains("whe_all") || ShowWheel.Contains("m1"))) f[DT_m1_1]->Draw("same");
     if( (ShowChamber=="cha_all" || ShowChamber.Contains("2")) && (ShowWheel.Contains("whe_all") || ShowWheel.Contains("m1"))) f[DT_m1_2]->Draw("same");
     if( (ShowChamber=="cha_all" || ShowChamber.Contains("3")) && (ShowWheel.Contains("whe_all") || ShowWheel.Contains("m1"))) f[DT_m1_3]->Draw("same");
     if( (ShowChamber=="cha_all" || ShowChamber.Contains("4")) && (ShowWheel.Contains("whe_all") || ShowWheel.Contains("m1"))) f[DT_m1_4]->Draw("same");
     if( (ShowChamber=="cha_all" || ShowChamber.Contains("1")) && (ShowWheel.Contains("whe_all") || ShowWheel.Contains("0")))  f[DT_0_1]->Draw("same");
     if( (ShowChamber=="cha_all" || ShowChamber.Contains("2")) && (ShowWheel.Contains("whe_all") || ShowWheel.Contains("0")))  f[DT_0_2]->Draw("same");
     if( (ShowChamber=="cha_all" || ShowChamber.Contains("3")) && (ShowWheel.Contains("whe_all") || ShowWheel.Contains("0")))  f[DT_0_3]->Draw("same");
     if( (ShowChamber=="cha_all" || ShowChamber.Contains("4")) && (ShowWheel.Contains("whe_all") || ShowWheel.Contains("0")))  f[DT_0_4]->Draw("same");
     if( (ShowChamber=="cha_all" || ShowChamber.Contains("1")) && (ShowWheel.Contains("whe_all") || ShowWheel.Contains("p1"))) f[DT_p1_1]->Draw("same");
     if( (ShowChamber=="cha_all" || ShowChamber.Contains("2")) && (ShowWheel.Contains("whe_all") || ShowWheel.Contains("p1"))) f[DT_p1_2]->Draw("same");
     if( (ShowChamber=="cha_all" || ShowChamber.Contains("3")) && (ShowWheel.Contains("whe_all") || ShowWheel.Contains("p1"))) f[DT_p1_3]->Draw("same");
     if( (ShowChamber=="cha_all" || ShowChamber.Contains("4")) && (ShowWheel.Contains("whe_all") || ShowWheel.Contains("p1"))) f[DT_p1_4]->Draw("same");
     if( (ShowChamber=="cha_all" || ShowChamber.Contains("1")) && (ShowWheel.Contains("whe_all") || ShowWheel.Contains("p2"))) f[DT_p2_1]->Draw("same");
     if( (ShowChamber=="cha_all" || ShowChamber.Contains("2")) && (ShowWheel.Contains("whe_all") || ShowWheel.Contains("p2"))) f[DT_p2_2]->Draw("same");
     if( (ShowChamber=="cha_all" || ShowChamber.Contains("3")) && (ShowWheel.Contains("whe_all") || ShowWheel.Contains("p2"))) f[DT_p2_3]->Draw("same");
     if( (ShowChamber=="cha_all" || ShowChamber.Contains("4")) && (ShowWheel.Contains("whe_all") || ShowWheel.Contains("p2"))) f[DT_p2_4]->Draw("same");
  }
  else{
     if( (ShowChamber=="ring_all" || ShowChamber.Contains("1")) && (ShowWheel.Contains("whe_all") || ShowWheel.Contains("m1"))) f[CSC_m1_1]->Draw("same"); 
     if( (ShowChamber=="ring_all" || ShowChamber.Contains("2")) && (ShowWheel.Contains("whe_all") || ShowWheel.Contains("m1"))) f[CSC_m1_2]->Draw("same");
     if( (ShowChamber=="ring_all" || ShowChamber.Contains("3")) && (ShowWheel.Contains("whe_all") || ShowWheel.Contains("m1"))) f[CSC_m1_3]->Draw("same");
     if( (ShowChamber=="ring_all" || ShowChamber.Contains("4")) && (ShowWheel.Contains("whe_all") || ShowWheel.Contains("m1"))) f[CSC_m1_4]->Draw("same");
     if( (ShowChamber=="ring_all" || ShowChamber.Contains("1")) && (ShowWheel.Contains("whe_all") || ShowWheel.Contains("m2"))) f[CSC_m2_1]->Draw("same");
     if( (ShowChamber=="ring_all" || ShowChamber.Contains("2")) && (ShowWheel.Contains("whe_all") || ShowWheel.Contains("m2"))) f[CSC_m2_2]->Draw("same");
     if( (ShowChamber=="ring_all" || ShowChamber.Contains("1")) && (ShowWheel.Contains("whe_all") || ShowWheel.Contains("m3"))) f[CSC_m3_1]->Draw("same");
     if( (ShowChamber=="ring_all" || ShowChamber.Contains("2")) && (ShowWheel.Contains("whe_all") || ShowWheel.Contains("m3"))) f[CSC_m3_2]->Draw("same");
     if( (ShowChamber=="ring_all" || ShowChamber.Contains("1")) && (ShowWheel.Contains("whe_all") || ShowWheel.Contains("m4"))) f[CSC_m4_1]->Draw("same");
     if( (ShowChamber=="ring_all" || ShowChamber.Contains("2")) && (ShowWheel.Contains("whe_all") || ShowWheel.Contains("m4"))) f[CSC_m4_2]->Draw("same");
     if( (ShowChamber=="ring_all" || ShowChamber.Contains("1")) && (ShowWheel.Contains("whe_all") || ShowWheel.Contains("p1"))) f[CSC_p1_1]->Draw("same");
     if( (ShowChamber=="ring_all" || ShowChamber.Contains("2")) && (ShowWheel.Contains("whe_all") || ShowWheel.Contains("p1"))) f[CSC_p1_2]->Draw("same");
     if( (ShowChamber=="ring_all" || ShowChamber.Contains("3")) && (ShowWheel.Contains("whe_all") || ShowWheel.Contains("p1"))) f[CSC_p1_3]->Draw("same");
     if( (ShowChamber=="ring_all" || ShowChamber.Contains("4")) && (ShowWheel.Contains("whe_all") || ShowWheel.Contains("p1"))) f[CSC_p1_4]->Draw("same");
     if( (ShowChamber=="ring_all" || ShowChamber.Contains("1")) && (ShowWheel.Contains("whe_all") || ShowWheel.Contains("p2"))) f[CSC_p2_1]->Draw("same");
     if( (ShowChamber=="ring_all" || ShowChamber.Contains("2")) && (ShowWheel.Contains("whe_all") || ShowWheel.Contains("p2"))) f[CSC_p2_2]->Draw("same");
     if( (ShowChamber=="ring_all" || ShowChamber.Contains("1")) && (ShowWheel.Contains("whe_all") || ShowWheel.Contains("p3"))) f[CSC_p3_1]->Draw("same");
     if( (ShowChamber=="ring_all" || ShowChamber.Contains("2")) && (ShowWheel.Contains("whe_all") || ShowWheel.Contains("p3"))) f[CSC_p3_2]->Draw("same");
     if( (ShowChamber=="ring_all" || ShowChamber.Contains("1")) && (ShowWheel.Contains("whe_all") || ShowWheel.Contains("p4"))) f[CSC_p4_1]->Draw("same");
     if( (ShowChamber=="ring_all" || ShowChamber.Contains("2")) && (ShowWheel.Contains("whe_all") || ShowWheel.Contains("p4"))) f[CSC_p4_2]->Draw("same");
  }
  //Intersection
  if( isDT ){
    if( (ShowChamber=="cha_all" || ShowChamber.Contains("1")) && (ShowWheel.Contains("whe_all") || ShowWheel.Contains("m2"))) Data->SetBinContent(Data->FindBin(Chambers_data_w[Wm2][Cha1]),f[DT_m2_1]->Eval(Chambers_data_w[Wm2][Cha1]));
    if( (ShowChamber=="cha_all" || ShowChamber.Contains("2")) && (ShowWheel.Contains("whe_all") || ShowWheel.Contains("m2"))) Data->SetBinContent(Data->FindBin(Chambers_data_w[Wm2][Cha2]),f[DT_m2_2]->Eval(Chambers_data_w[Wm2][Cha2]));
    if( (ShowChamber=="cha_all" || ShowChamber.Contains("3")) && (ShowWheel.Contains("whe_all") || ShowWheel.Contains("m2"))) Data->SetBinContent(Data->FindBin(Chambers_data_w[Wm2][Cha3]),f[DT_m2_3]->Eval(Chambers_data_w[Wm2][Cha3]));
    if( (ShowChamber=="cha_all" || ShowChamber.Contains("4")) && (ShowWheel.Contains("whe_all") || ShowWheel.Contains("m2"))) Data->SetBinContent(Data->FindBin(Chambers_data_w[Wm2][Cha4]),f[DT_m2_4]->Eval(Chambers_data_w[Wm2][Cha4]));
    if( (ShowChamber=="cha_all" || ShowChamber.Contains("1")) && (ShowWheel.Contains("whe_all") || ShowWheel.Contains("m1"))) Data->SetBinContent(Data->FindBin(Chambers_data_w[Wm1][Cha1]),f[DT_m1_1]->Eval(Chambers_data_w[Wm1][Cha1]));
    if( (ShowChamber=="cha_all" || ShowChamber.Contains("2")) && (ShowWheel.Contains("whe_all") || ShowWheel.Contains("m1"))) Data->SetBinContent(Data->FindBin(Chambers_data_w[Wm1][Cha2]),f[DT_m1_2]->Eval(Chambers_data_w[Wm1][Cha2]));
    if( (ShowChamber=="cha_all" || ShowChamber.Contains("3")) && (ShowWheel.Contains("whe_all") || ShowWheel.Contains("m1"))) Data->SetBinContent(Data->FindBin(Chambers_data_w[Wm1][Cha3]),f[DT_m1_3]->Eval(Chambers_data_w[Wm1][Cha3]));
    if( (ShowChamber=="cha_all" || ShowChamber.Contains("4")) && (ShowWheel.Contains("whe_all") || ShowWheel.Contains("m1"))) Data->SetBinContent(Data->FindBin(Chambers_data_w[Wm1][Cha4]),f[DT_m1_4]->Eval(Chambers_data_w[Wm1][Cha4]));
    if( (ShowChamber=="cha_all" || ShowChamber.Contains("1")) && (ShowWheel.Contains("whe_all") || ShowWheel.Contains("0")))  Data->SetBinContent(Data->FindBin(Chambers_data_w[W0][Cha1]), f[DT_0_1]->Eval(Chambers_data_w[W0][Cha1]));
    if( (ShowChamber=="cha_all" || ShowChamber.Contains("2")) && (ShowWheel.Contains("whe_all") || ShowWheel.Contains("0")))  Data->SetBinContent(Data->FindBin(Chambers_data_w[W0][Cha2]), f[DT_0_2]->Eval(Chambers_data_w[W0][Cha2]));
    if( (ShowChamber=="cha_all" || ShowChamber.Contains("3")) && (ShowWheel.Contains("whe_all") || ShowWheel.Contains("0")))  Data->SetBinContent(Data->FindBin(Chambers_data_w[W0][Cha3]), f[DT_0_3]->Eval(Chambers_data_w[W0][Cha3]));
    if( (ShowChamber=="cha_all" || ShowChamber.Contains("4")) && (ShowWheel.Contains("whe_all") || ShowWheel.Contains("0")))  Data->SetBinContent(Data->FindBin(Chambers_data_w[W0][Cha4]), f[DT_0_4]->Eval(Chambers_data_w[W0][Cha4]));
    if( (ShowChamber=="cha_all" || ShowChamber.Contains("1")) && (ShowWheel.Contains("whe_all") || ShowWheel.Contains("p1"))) Data->SetBinContent(Data->FindBin(Chambers_data_w[Wp1][Cha1]),f[DT_p1_1]->Eval(Chambers_data_w[Wp1][Cha1]));
    if( (ShowChamber=="cha_all" || ShowChamber.Contains("2")) && (ShowWheel.Contains("whe_all") || ShowWheel.Contains("p1"))) Data->SetBinContent(Data->FindBin(Chambers_data_w[Wp1][Cha2]),f[DT_p1_2]->Eval(Chambers_data_w[Wp1][Cha2]));
    if( (ShowChamber=="cha_all" || ShowChamber.Contains("3")) && (ShowWheel.Contains("whe_all") || ShowWheel.Contains("p1"))) Data->SetBinContent(Data->FindBin(Chambers_data_w[Wp1][Cha3]),f[DT_p1_3]->Eval(Chambers_data_w[Wp1][Cha3]));
    if( (ShowChamber=="cha_all" || ShowChamber.Contains("4")) && (ShowWheel.Contains("whe_all") || ShowWheel.Contains("p1"))) Data->SetBinContent(Data->FindBin(Chambers_data_w[Wp1][Cha4]),f[DT_p1_4]->Eval(Chambers_data_w[Wp1][Cha4]));
    if( (ShowChamber=="cha_all" || ShowChamber.Contains("1")) && (ShowWheel.Contains("whe_all") || ShowWheel.Contains("p2"))) Data->SetBinContent(Data->FindBin(Chambers_data_w[Wp2][Cha1]),f[DT_p2_1]->Eval(Chambers_data_w[Wp2][Cha1]));
    if( (ShowChamber=="cha_all" || ShowChamber.Contains("2")) && (ShowWheel.Contains("whe_all") || ShowWheel.Contains("p2"))) Data->SetBinContent(Data->FindBin(Chambers_data_w[Wp2][Cha2]),f[DT_p2_2]->Eval(Chambers_data_w[Wp2][Cha2]));
    if( (ShowChamber=="cha_all" || ShowChamber.Contains("3")) && (ShowWheel.Contains("whe_all") || ShowWheel.Contains("p2"))) Data->SetBinContent(Data->FindBin(Chambers_data_w[Wp2][Cha3]),f[DT_p2_3]->Eval(Chambers_data_w[Wp2][Cha3]));
    if( (ShowChamber=="cha_all" || ShowChamber.Contains("4")) && (ShowWheel.Contains("whe_all") || ShowWheel.Contains("p2"))) Data->SetBinContent(Data->FindBin(Chambers_data_w[Wp2][Cha4]),f[DT_p2_4]->Eval(Chambers_data_w[Wp2][Cha4]));
  }
  else{
    if( (ShowChamber=="ring_all" || ShowChamber.Contains("1")) && (ShowWheel.Contains("whe_all") || ShowWheel.Contains("m1"))) Data->SetBinContent(Data->FindBin(Chambers_data_w_csc[CSC_Wm1][CSC_R1]),f[CSC_m1_1]->Eval(Chambers_data_w_csc[CSC_Wm1][CSC_R1]));
    if( (ShowChamber=="ring_all" || ShowChamber.Contains("2")) && (ShowWheel.Contains("whe_all") || ShowWheel.Contains("m1"))) Data->SetBinContent(Data->FindBin(Chambers_data_w_csc[CSC_Wm1][CSC_R2]),f[CSC_m1_2]->Eval(Chambers_data_w_csc[CSC_Wm1][CSC_R2]));
    if( (ShowChamber=="ring_all" || ShowChamber.Contains("3")) && (ShowWheel.Contains("whe_all") || ShowWheel.Contains("m1"))) Data->SetBinContent(Data->FindBin(Chambers_data_w_csc[CSC_Wm1][CSC_R3]),f[CSC_m1_3]->Eval(Chambers_data_w_csc[CSC_Wm1][CSC_R3]));
    if( (ShowChamber=="ring_all" || ShowChamber.Contains("4")) && (ShowWheel.Contains("whe_all") || ShowWheel.Contains("m1"))) Data->SetBinContent(Data->FindBin(Chambers_data_w_csc[CSC_Wm1][CSC_R4]),f[CSC_m1_4]->Eval(Chambers_data_w_csc[CSC_Wm1][CSC_R4]));
    if( (ShowChamber=="ring_all" || ShowChamber.Contains("1")) && (ShowWheel.Contains("whe_all") || ShowWheel.Contains("m2"))) Data->SetBinContent(Data->FindBin(Chambers_data_w_csc[CSC_Wm2][CSC_R1]),f[CSC_m2_1]->Eval(Chambers_data_w_csc[CSC_Wm2][CSC_R1]));
    if( (ShowChamber=="ring_all" || ShowChamber.Contains("2")) && (ShowWheel.Contains("whe_all") || ShowWheel.Contains("m2"))) Data->SetBinContent(Data->FindBin(Chambers_data_w_csc[CSC_Wm2][CSC_R2]),f[CSC_m2_2]->Eval(Chambers_data_w_csc[CSC_Wm2][CSC_R2]));
    if( (ShowChamber=="ring_all" || ShowChamber.Contains("1")) && (ShowWheel.Contains("whe_all") || ShowWheel.Contains("m3"))) Data->SetBinContent(Data->FindBin(Chambers_data_w_csc[CSC_Wm3][CSC_R1]),f[CSC_m3_1]->Eval(Chambers_data_w_csc[CSC_Wm3][CSC_R1]));
    if( (ShowChamber=="ring_all" || ShowChamber.Contains("2")) && (ShowWheel.Contains("whe_all") || ShowWheel.Contains("m3"))) Data->SetBinContent(Data->FindBin(Chambers_data_w_csc[CSC_Wm3][CSC_R2]),f[CSC_m3_2]->Eval(Chambers_data_w_csc[CSC_Wm3][CSC_R2]));
    if( (ShowChamber=="ring_all" || ShowChamber.Contains("1")) && (ShowWheel.Contains("whe_all") || ShowWheel.Contains("m4"))) Data->SetBinContent(Data->FindBin(Chambers_data_w_csc[CSC_Wm4][CSC_R1]),f[CSC_m4_1]->Eval(Chambers_data_w_csc[CSC_Wm4][CSC_R1]));
    if( (ShowChamber=="ring_all" || ShowChamber.Contains("2")) && (ShowWheel.Contains("whe_all") || ShowWheel.Contains("m4"))) Data->SetBinContent(Data->FindBin(Chambers_data_w_csc[CSC_Wm4][CSC_R2]),f[CSC_m4_2]->Eval(Chambers_data_w_csc[CSC_Wm4][CSC_R2]));
    if( (ShowChamber=="ring_all" || ShowChamber.Contains("1")) && (ShowWheel.Contains("whe_all") || ShowWheel.Contains("p1"))) Data->SetBinContent(Data->FindBin(Chambers_data_w_csc[CSC_Wp1][CSC_R1]),f[CSC_p1_1]->Eval(Chambers_data_w_csc[CSC_Wp1][CSC_R1]));
    if( (ShowChamber=="ring_all" || ShowChamber.Contains("2")) && (ShowWheel.Contains("whe_all") || ShowWheel.Contains("p1"))) Data->SetBinContent(Data->FindBin(Chambers_data_w_csc[CSC_Wp1][CSC_R2]),f[CSC_p1_2]->Eval(Chambers_data_w_csc[CSC_Wp1][CSC_R2]));
    if( (ShowChamber=="ring_all" || ShowChamber.Contains("3")) && (ShowWheel.Contains("whe_all") || ShowWheel.Contains("p1"))) Data->SetBinContent(Data->FindBin(Chambers_data_w_csc[CSC_Wp1][CSC_R3]),f[CSC_p1_3]->Eval(Chambers_data_w_csc[CSC_Wp1][CSC_R3]));
    if( (ShowChamber=="ring_all" || ShowChamber.Contains("4")) && (ShowWheel.Contains("whe_all") || ShowWheel.Contains("p1"))) Data->SetBinContent(Data->FindBin(Chambers_data_w_csc[CSC_Wp1][CSC_R4]),f[CSC_p1_4]->Eval(Chambers_data_w_csc[CSC_Wp1][CSC_R4]));
    if( (ShowChamber=="ring_all" || ShowChamber.Contains("1")) && (ShowWheel.Contains("whe_all") || ShowWheel.Contains("p2"))) Data->SetBinContent(Data->FindBin(Chambers_data_w_csc[CSC_Wp2][CSC_R1]),f[CSC_p2_1]->Eval(Chambers_data_w_csc[CSC_Wp2][CSC_R1]));
    if( (ShowChamber=="ring_all" || ShowChamber.Contains("2")) && (ShowWheel.Contains("whe_all") || ShowWheel.Contains("p2"))) Data->SetBinContent(Data->FindBin(Chambers_data_w_csc[CSC_Wp2][CSC_R2]),f[CSC_p2_2]->Eval(Chambers_data_w_csc[CSC_Wp2][CSC_R2]));
    if( (ShowChamber=="ring_all" || ShowChamber.Contains("1")) && (ShowWheel.Contains("whe_all") || ShowWheel.Contains("p3"))) Data->SetBinContent(Data->FindBin(Chambers_data_w_csc[CSC_Wp3][CSC_R1]),f[CSC_p3_1]->Eval(Chambers_data_w_csc[CSC_Wp3][CSC_R1]));
    if( (ShowChamber=="ring_all" || ShowChamber.Contains("2")) && (ShowWheel.Contains("whe_all") || ShowWheel.Contains("p3"))) Data->SetBinContent(Data->FindBin(Chambers_data_w_csc[CSC_Wp3][CSC_R2]),f[CSC_p3_2]->Eval(Chambers_data_w_csc[CSC_Wp3][CSC_R2]));
    if( (ShowChamber=="ring_all" || ShowChamber.Contains("1")) && (ShowWheel.Contains("whe_all") || ShowWheel.Contains("p4"))) Data->SetBinContent(Data->FindBin(Chambers_data_w_csc[CSC_Wp4][CSC_R1]),f[CSC_p4_1]->Eval(Chambers_data_w_csc[CSC_Wp4][CSC_R1]));
    if( (ShowChamber=="ring_all" || ShowChamber.Contains("2")) && (ShowWheel.Contains("whe_all") || ShowWheel.Contains("p4"))) Data->SetBinContent(Data->FindBin(Chambers_data_w_csc[CSC_Wp4][CSC_R2]),f[CSC_p4_2]->Eval(Chambers_data_w_csc[CSC_Wp4][CSC_R2]));
  }
  Data->Draw("Psame");
  TString isDTorCSC = isDT ? "DT_" : "CSC_";
  TString NameH = isDTorCSC + "Lumi_vs_reso_" + DOF + "DOF_" + rms_type + "_" + ShowChamber + "_" + ShowWheel;
  myc1->SaveAs( TString(NameH + ".pdf").Data() );
  myc1->SaveAs( TString(NameH + ".root").Data() );
  delete myc1;
}

float*** Extract_Nmuons( TString Report, bool isDT ){

  if( isDT && Report.Contains("_CSC") ) return NULL;
  if( !isDT && Report.Contains("_DT") ) return NULL;
  std::ifstream myfile( Report );
  if(!myfile) std::cout<<"ERROR opening "<<Report<<std::endl;
  if( isDT ){
    int Nline=1;
    int wheel_data(-10), chamb_data(-10), sector_data(-10), Value_data(-10);
    float*** Chambers = 0; Chambers = new float**[NWheel];
    for(int i=0; i<NWheel; i++) Chambers[i] = new float*[NChamber];
    for(int i=0; i<NWheel; i++){ for(int j=0; j<NChamber; j++){ Chambers[i][j] = new float[NSector]; }}
    for(int i=0; i<NWheel; i++){ for(int j=0; j<NChamber; j++){ for(int k=0; k<NSector; k++){ Chambers[i][j][k]=-1.;}}}

    std::string line;
    while (std::getline(myfile, line)){
	TString line2(line);
	Nline++;
	if( line2.Contains("reports.append") && line2.Contains("DT") ){
	  std::istringstream buf(line2.Data());
	  std::istream_iterator<std::string> beg(buf), end;
	  std::vector<std::string> tokens(beg, end);
	  wheel_data = std::atoi(tokens[2].c_str());
	  chamb_data = std::atoi(tokens[3].c_str());
	  sector_data = std::atoi(tokens[4].substr(0,2).c_str());
	  Nline=-1;
	}
	if( line2.Contains("reports") && line2.Contains("posNum") && Nline==0 ){
	  std::istringstream buf(line2.Data());
	  std::istream_iterator<std::string> beg(buf), end;
	  std::vector<std::string> tokens(beg, end);
	  Value_data = std::atoi(tokens[2].c_str());
	}
	if(Nline==0){
	  int mywheel=-1;
	  if( wheel_data==-2 ) mywheel=Wm2;
	  if( wheel_data==-1 ) mywheel=Wm1;
	  if( wheel_data==0 )  mywheel=W0;
	  if( wheel_data==1 )  mywheel=Wp1;
	  if( wheel_data==2 )  mywheel=Wp2;
	  Chambers[mywheel][chamb_data-1][sector_data-1]=Value_data;
	}
    }
    return Chambers;
  }// Now CSC
  else{
    int Nline=1;
    int ME(-10), wheel_data(-10), chamb_data(-10), sector_data(-10), Value_data(-10);
    float*** Chambers = 0; Chambers = new float**[NWheel_CSC];
    for(int i=0; i<NWheel_CSC; i++) Chambers[i] = new float*[NRing_CSC];
    for(int i=0; i<NWheel_CSC; i++){ for(int j=0; j<NRing_CSC; j++){ Chambers[i][j] = new float[NSector_CSC]; }}
    for(int i=0; i<NWheel_CSC; i++){ for(int j=0; j<NRing_CSC; j++){ for(int k=0; k<NSector_CSC; k++){ Chambers[i][j][k]=-1.;}}}
    std::string line;
    while (std::getline(myfile, line)){
	TString line2(line);
	Nline++;
	if( line2.Contains("reports.append") && line2.Contains("CSC") ){
	  std::istringstream buf(line2.Data());
	  std::istream_iterator<std::string> beg(buf), end;
	  std::vector<std::string> tokens(beg, end);
	  ME = std::atoi(tokens[2].c_str());
	  wheel_data = std::atoi(tokens[3].c_str());
	  chamb_data = std::atoi(tokens[4].c_str());
	  sector_data = std::atoi(tokens[5].substr(0,2).c_str());
	  Nline=-1;
	}
	if( line2.Contains("reports") && line2.Contains("posNum") && Nline==0 ){
	  std::istringstream buf(line2.Data());
	  std::istream_iterator<std::string> beg(buf), end;
	  std::vector<std::string> tokens(beg, end);
	  Value_data = std::atoi(tokens[2].c_str());
	}
	if(Nline==0){
	  int mywheel=-1;
	  if( ME==1 && wheel_data==1 ) mywheel=CSC_Wp1;
	  if( ME==1 && wheel_data==2 ) mywheel=CSC_Wp2;
	  if( ME==1 && wheel_data==3 ) mywheel=CSC_Wp3;
	  if( ME==1 && wheel_data==4 ) mywheel=CSC_Wp4;
	  if( ME==2 && wheel_data==1 ) mywheel=CSC_Wm1;
	  if( ME==2 && wheel_data==2 ) mywheel=CSC_Wm2;
	  if( ME==2 && wheel_data==3 ) mywheel=CSC_Wm3;
	  if( ME==2 && wheel_data==4 ) mywheel=CSC_Wm4;
	  Chambers[mywheel][chamb_data-1][sector_data-1]=Value_data;
	}
    }
    return Chambers;
  }
}

TH1F** Init_plots( bool isDT, float MaxX ){
  int size = isDT ? 20 : 20;
  TH1F **h = new TH1F*[ size ];
  for(int jR=0; jR<size; jR++){
    TString NameH = "Name_" + std::to_string(jR);
    h[jR] = new TH1F( NameH.Data(), "", 1000, 0., MaxX );
    //DT
    if(jR==0 && isDT)  {h[DT_m2_1]->SetMarkerColor(kRed); h[DT_m2_1]->SetMarkerStyle(20);}   
    if(jR==1 && isDT)  {h[DT_m2_2]->SetMarkerColor(kRed); h[DT_m2_2]->SetMarkerStyle(21);} 
    if(jR==2 && isDT)  {h[DT_m2_3]->SetMarkerColor(kRed); h[DT_m2_3]->SetMarkerStyle(22);}
    if(jR==3 && isDT)  {h[DT_m2_4]->SetMarkerColor(kRed); h[DT_m2_4]->SetMarkerStyle(34);}
    if(jR==4 && isDT)  {h[DT_m1_1]->SetMarkerColor(kBlue); h[DT_m1_1]->SetMarkerStyle(20);}
    if(jR==5 && isDT)  {h[DT_m1_2]->SetMarkerColor(kBlue); h[DT_m1_2]->SetMarkerStyle(21);}
    if(jR==6 && isDT)  {h[DT_m1_3]->SetMarkerColor(kBlue); h[DT_m1_3]->SetMarkerStyle(22);}
    if(jR==7 && isDT)  {h[DT_m1_4]->SetMarkerColor(kBlue); h[DT_m1_4]->SetMarkerStyle(34);}
    if(jR==8 && isDT)  {h[DT_0_1]->SetMarkerColor(kBlack);  h[DT_0_1]->SetMarkerStyle(20);}
    if(jR==9 && isDT)  {h[DT_0_2]->SetMarkerColor(kBlack);  h[DT_0_2]->SetMarkerStyle(21);}
    if(jR==10 && isDT) {h[DT_0_3]->SetMarkerColor(kBlack);  h[DT_0_3]->SetMarkerStyle(22);}
    if(jR==11 && isDT) {h[DT_0_4]->SetMarkerColor(kBlack);  h[DT_0_4]->SetMarkerStyle(34);}
    if(jR==12 && isDT) {h[DT_p1_1]->SetMarkerColor(kBlue-3); h[DT_p1_1]->SetMarkerStyle(20);}
    if(jR==13 && isDT) {h[DT_p1_2]->SetMarkerColor(kBlue-3); h[DT_p1_2]->SetMarkerStyle(21);}
    if(jR==14 && isDT) {h[DT_p1_3]->SetMarkerColor(kBlue-3); h[DT_p1_3]->SetMarkerStyle(22);}
    if(jR==15 && isDT) {h[DT_p1_4]->SetMarkerColor(kBlue-3); h[DT_p1_4]->SetMarkerStyle(34);}
    if(jR==16 && isDT) {h[DT_p2_1]->SetMarkerColor(kRed-3); h[DT_p2_1]->SetMarkerStyle(20);}
    if(jR==17 && isDT) {h[DT_p2_2]->SetMarkerColor(kRed-3); h[DT_p2_2]->SetMarkerStyle(21);}
    if(jR==18 && isDT) {h[DT_p2_3]->SetMarkerColor(kRed-3); h[DT_p2_3]->SetMarkerStyle(22);}
    if(jR==19 && isDT) {h[DT_p2_4]->SetMarkerColor(kRed-3); h[DT_p2_4]->SetMarkerStyle(34);}
    //CSC
    if(jR==0 && !isDT)  {h[CSC_m1_1]->SetMarkerColor(kBlack);   h[CSC_m1_1]->SetMarkerStyle(20);}   
    if(jR==1 && !isDT)  {h[CSC_m1_2]->SetMarkerColor(kBlack);   h[CSC_m1_2]->SetMarkerStyle(21);} 
    if(jR==2 && !isDT)  {h[CSC_m1_3]->SetMarkerColor(kBlack);   h[CSC_m1_3]->SetMarkerStyle(22);}
    if(jR==3 && !isDT)  {h[CSC_m1_4]->SetMarkerColor(kBlack);   h[CSC_m1_4]->SetMarkerStyle(34);}
    if(jR==4 && !isDT)  {h[CSC_m2_1]->SetMarkerColor(kBlue);    h[CSC_m2_1]->SetMarkerStyle(20);}
    if(jR==5 && !isDT)  {h[CSC_m2_2]->SetMarkerColor(kBlue);    h[CSC_m2_2]->SetMarkerStyle(21);}
    if(jR==6 && !isDT)  {h[CSC_m3_1]->SetMarkerColor(kGreen);   h[CSC_m3_1]->SetMarkerStyle(20);}
    if(jR==7 && !isDT)  {h[CSC_m3_2]->SetMarkerColor(kGreen);   h[CSC_m3_2]->SetMarkerStyle(21);}
    if(jR==8 && !isDT)  {h[CSC_m4_1]->SetMarkerColor(kRed);     h[CSC_m4_1]->SetMarkerStyle(20);}
    if(jR==9 && !isDT)  {h[CSC_m4_2]->SetMarkerColor(kRed);     h[CSC_m4_2]->SetMarkerStyle(21);}
    if(jR==10 && !isDT) {h[CSC_p1_1]->SetMarkerColor(14);       h[CSC_p1_1]->SetMarkerStyle(20);}
    if(jR==11 && !isDT) {h[CSC_p1_2]->SetMarkerColor(14);       h[CSC_p1_2]->SetMarkerStyle(21);}
    if(jR==12 && !isDT) {h[CSC_p1_3]->SetMarkerColor(14);       h[CSC_p1_3]->SetMarkerStyle(22);}
    if(jR==13 && !isDT) {h[CSC_p1_4]->SetMarkerColor(14);       h[CSC_p1_4]->SetMarkerStyle(34);}
    if(jR==14 && !isDT) {h[CSC_p2_1]->SetMarkerColor(kBlue-3);  h[CSC_p2_1]->SetMarkerStyle(20);}
    if(jR==15 && !isDT) {h[CSC_p2_2]->SetMarkerColor(kBlue-3);  h[CSC_p2_2]->SetMarkerStyle(21);}
    if(jR==16 && !isDT) {h[CSC_p3_1]->SetMarkerColor(kGreen-3); h[CSC_p3_1]->SetMarkerStyle(20);}
    if(jR==17 && !isDT) {h[CSC_p3_2]->SetMarkerColor(kGreen-3); h[CSC_p3_2]->SetMarkerStyle(21);}
    if(jR==18 && !isDT) {h[CSC_p4_1]->SetMarkerColor(kRed-3);   h[CSC_p4_1]->SetMarkerStyle(20);}
    if(jR==19 && !isDT) {h[CSC_p4_2]->SetMarkerColor(kRed-3);   h[CSC_p4_2]->SetMarkerStyle(21);}
  }
  return h;
}

TF1** Init_Fit( bool isDT, float MaxX ){
  int size = isDT ? 20 : 20;
  TF1 **h = new TF1*[ size ];
  for(int jR=0; jR<size; jR++){
    TString NameH = "Name_" + std::to_string(jR);
    h[jR] = new TF1( NameH.Data(),"[0]*sqrt([1]/x)",0.,MaxX);
    //DT
    if(jR==0 && isDT)   h[DT_m2_1]->SetLineColor(kRed);
    if(jR==1 && isDT)   h[DT_m2_2]->SetLineColor(kRed);  
    if(jR==2 && isDT)   h[DT_m2_3]->SetLineColor(kRed); 
    if(jR==3 && isDT)   h[DT_m2_4]->SetLineColor(kRed); 
    if(jR==4 && isDT)   h[DT_m1_1]->SetLineColor(kBlue); 
    if(jR==5 && isDT)   h[DT_m1_2]->SetLineColor(kBlue); 
    if(jR==6 && isDT)   h[DT_m1_3]->SetLineColor(kBlue); 
    if(jR==7 && isDT)   h[DT_m1_4]->SetLineColor(kBlue); 
    if(jR==8 && isDT)   h[DT_0_1]->SetLineColor(kBlack);
    if(jR==9 && isDT)   h[DT_0_2]->SetLineColor(kBlack);
    if(jR==10 && isDT)  h[DT_0_3]->SetLineColor(kBlack);
    if(jR==11 && isDT)  h[DT_0_4]->SetLineColor(kBlack);
    if(jR==12 && isDT)  h[DT_p1_1]->SetLineColor(kBlue-3); 
    if(jR==13 && isDT)  h[DT_p1_2]->SetLineColor(kBlue-3); 
    if(jR==14 && isDT)  h[DT_p1_3]->SetLineColor(kBlue-3); 
    if(jR==15 && isDT)  h[DT_p1_4]->SetLineColor(kBlue-3); 
    if(jR==16 && isDT)  h[DT_p2_1]->SetLineColor(kRed-3); 
    if(jR==17 && isDT)  h[DT_p2_2]->SetLineColor(kRed-3); 
    if(jR==18 && isDT)  h[DT_p2_3]->SetLineColor(kRed-3); 
    if(jR==19 && isDT)  h[DT_p2_4]->SetLineColor(kRed-3); 
    //CSC
    if(jR==0 && !isDT)  h[CSC_m1_1]->SetLineColor(kBlack);    
    if(jR==1 && !isDT)  h[CSC_m1_2]->SetLineColor(kBlack);  
    if(jR==2 && !isDT)  h[CSC_m1_3]->SetLineColor(kBlack);  
    if(jR==3 && !isDT)  h[CSC_m1_4]->SetLineColor(kBlack);  
    if(jR==4 && !isDT)  h[CSC_m2_1]->SetLineColor(kBlue);   
    if(jR==5 && !isDT)  h[CSC_m2_2]->SetLineColor(kBlue);   
    if(jR==6 && !isDT)  h[CSC_m3_1]->SetLineColor(kGreen);  
    if(jR==7 && !isDT)  h[CSC_m3_2]->SetLineColor(kGreen);  
    if(jR==8 && !isDT)  h[CSC_m4_1]->SetLineColor(kRed);    
    if(jR==9 && !isDT)  h[CSC_m4_2]->SetLineColor(kRed);    
    if(jR==10 && !isDT) h[CSC_p1_1]->SetLineColor(14);
    if(jR==11 && !isDT) h[CSC_p1_2]->SetLineColor(14);
    if(jR==12 && !isDT) h[CSC_p1_3]->SetLineColor(14);
    if(jR==13 && !isDT) h[CSC_p1_4]->SetLineColor(14);
    if(jR==14 && !isDT) h[CSC_p2_1]->SetLineColor(kBlue-3); 
    if(jR==15 && !isDT) h[CSC_p2_2]->SetLineColor(kBlue-3); 
    if(jR==16 && !isDT) h[CSC_p3_1]->SetLineColor(kGreen-3);
    if(jR==17 && !isDT) h[CSC_p3_2]->SetLineColor(kGreen-3);
    if(jR==18 && !isDT) h[CSC_p4_1]->SetLineColor(kRed-3);  
    if(jR==19 && !isDT) h[CSC_p4_2]->SetLineColor(kRed-3);  
  }
  return h;
}
