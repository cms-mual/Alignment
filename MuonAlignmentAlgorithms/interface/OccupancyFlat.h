#include <TFile.h>
#include <TMath.h>
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
#include "TMath.h"
#include "TBranch.h"
#include "TString.h"
#include "TEventList.h"
#include "TArrow.h"
#include <iostream>
#include <sstream>
#include <fstream>

float FindWeightFlatOccupancy( int n_wheel, int n_station, int n_sector, float positionX, float positionY){
  float weight = 1.;
  //From Here copy the weights
  if(n_wheel==-2){
    if(n_station==1){
	if(n_sector==1){
	  if(positionX<999. && positionY<999.) weight = 1;
	  else if(positionX<999. && positionY<999.) weight = 1;
	  else weight = 1;
	}
    }
  }
  if(n_wheel==-1){
  }
  //Stop copy here
  return weight;
}
