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
#include "TString.h"
#include "TStyle.h"
#include "TEventList.h"
#include "TArrow.h"
#include <iostream>
#include <sstream>
#include <fstream>
#include <utility>
enum Wheel{ WHEEL=0, STATION, SECTOR, CHI2 };

//.x -b -q HackXML.C+
void HackXML(){
 
  cout<<"Opening file."<<endl;
  std::ifstream infile( "MuonGeometry_MC_Run2Startup_June2015_Csc2mm1mrad_DtHWUnct_v1.StdTags.746p3.DBv2_FIXED.xml" );
  TString Line1 = "CSCLayer endcap=\"2\" station=\"4\" ring=\"2\"";
  TString Line2 = "CSCChamber endcap=\"2\" station=\"4\" ring=\"2\"";
  TString Line3 = "CSCLayer endcap=\"1\" station=\"4\" ring=\"2\"";
  TString Line4 = "CSCChamber endcap=\"1\" station=\"4\" ring=\"2\"";
  TString LineS = "  <setposition relativeto=\"ideal\" x=\"0.0000000000\" y=\"0.0000000000\" z=\"0.0000000000\" phix=\"-0.0000000000\" phiy=\"-0.0000000000\" phiz=\"0.0000000000\" />";
  ofstream outputFile( "idealMuonGeometry_DESRUN2_74_V4.APEsExtd.StdTags.746p3.DBv2_FIX2.xml" );
  int Nline = 0, LineToBeChanged = -1;
  for( string line; getline( infile, line ); ){
    Nline++;
    TString MyLine = line;
    cout<<"L "<<MyLine<<endl;
    if( MyLine.Contains(Line1) || MyLine.Contains(Line2) || MyLine.Contains(Line3) || MyLine.Contains(Line4) ){
	LineToBeChanged = Nline+1;
    }
    if( Nline == LineToBeChanged ) outputFile << LineS.Data() << endl;
    else outputFile << line << endl;
  }
  cout<<"End of the script."<<endl;
}
