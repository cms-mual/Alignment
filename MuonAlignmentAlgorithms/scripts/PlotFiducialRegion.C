#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <map>
#include <sstream>
#include <set>
#include <cmath>
#include <cstdlib>
//Root Stuff
#include "TFile.h"
#include "TCanvas.h"
#include "TTree.h"
#include "TROOT.h"
#include "TH1F.h"
#include "TH2F.h"
#include "TH1.h"
#include "TF1.h"

using std::cout;
using std::endl;
using std::vector;
using std::string;
using std::map;
using std::pair;
using std::stringstream;

void PlotFiducialRegion( TString fileRoot = "mc_CSC-1100-101111_initial_MC_53_V14_v1_IdealGeomFidCutTest_01.root " ){
  
  //Open File and TTree
  TCanvas* myc1 = new TCanvas("myc1", "CMS", 600, 600);
  TFile *f = TFile::Open( fileRoot.Data() );
  if (f->IsZombie()) cout<<"Error opening file: "<<fileRoot.Data()<<endl;
  TTree *Tree = (TTree*) f->Get("mual_ttree");
  if (!Tree) cout<<"Error opening TTree!"<<endl;
  TString Comm = "mkdir -p FidCutsPlots";
  system( Comm.Data() );
  Comm = "rm -rf FidCutsPlots/*";
  system( Comm.Data() );

  //Loop
  for( int iStation=1; iStation<=4; iStation++ ){
    for( int iRing=1; iRing<=4; iRing++ ){
      int Station = iStation;
      int Ring = iRing;
      if( Station!=1 && Ring>2 ) continue;
      char Selection[50];
      sprintf( Selection, "station==%d && ring_wheel==%d", Station, Ring );
      Tree->Draw( "pos_y:pos_x", Selection, "colz" );
      stringstream ss_Station, ss_Ring;
      ss_Station << Station; ss_Ring << Ring;
      TString nameHisto = "FidCutsPlots/CSC_Station_" + ss_Station.str() + "_Ring_" + ss_Ring.str() + ".png";
      myc1->SaveAs( nameHisto.Data() );
    }
  }
//  //Variables to use
//  Bool_t is_dt, is_plus;
//  UChar_t station, sector;
//  Char_t ring_wheel;
//  Float_t pos_x, pos_y;
//  Tree->SetBranchAddress("is_dt",&is_dt);
//  Tree->SetBranchAddress("is_plus",&is_plus);
//  Tree->SetBranchAddress("station",&station);
//  Tree->SetBranchAddress("sector",&sector);
//  Tree->SetBranchAddress("ring_wheel",&ring_wheel);
//  Tree->SetBranchAddress("pos_x",&pos_x);
//  Tree->SetBranchAddress("pos_y",&pos_y);
//  //TH1F **h = new TH1F*[size];
//
//  //Loop
//  for( int entry=0; entry<Tree->GetEntries(); ++entry){
//    Tree->GetEntry(entry);
//    
//  }
}
