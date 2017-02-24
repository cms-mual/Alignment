#include "TFile.h"
#include "TStopwatch.h"
#include "TCanvas.h"
#include "TTree.h"
#include "TF1.h"
#include "TH1.h"
#include "TH2.h"
#include "TChain.h"
#include "TRandom3.h"
#include "TStyle.h"
#include "TPaveText.h"
#include "TLatex.h"
#include "TLegend.h"
#include "TROOT.h"
#include "TMatrixDSym.h"
#include "TMath.h"
#include "TF2.h"
#include "TGraph.h"
#include <fstream>
#include <vector>
#include <sstream>
#include <iostream>
#include <string> 
#include "TMinuit.h"
#include "TFitResultPtr.h"
#include "TFitResult.h"
#include "TMatrixDSym.h"
#include "TVirtualFitter.h"
#include "Math/MinimizerOptions.h"

//Simple TOY model to test the coverage given by the Covariance matrix
void TestCovMatr_Simple() {

  TCanvas *c1 = new TCanvas("c1"); c1->cd();
  TString folder="Plots_L_10k/";
  //Number of fits to be performed
  const int Ntry_tot=4000;
  //For coverage studies
  float is_inside1_c=0, is_inside2_c=0;
  //Plots
  TH1F *h_x_err   = new TH1F("h_x_err","",5000,0.001,0.1); h_x_err->GetXaxis()->SetTitle("X Error");
  TH1F *h_y_err   = new TH1F("h_y_err","",5000,0.001,0.1); h_y_err->GetXaxis()->SetTitle("Y Error");
  TH1F *h_x_errD  = new TH1F("h_x_errD","",5000,0.001,0.1); h_x_errD->GetXaxis()->SetTitle("X Error");
  TH1F *h_y_errD  = new TH1F("h_y_errD","",5000,0.001,0.1); h_y_errD->GetXaxis()->SetTitle("Y Error");
  TH1F *h_pull_x  = new TH1F("h_pull_x","",100,-2., 2); h_pull_x->GetXaxis()->SetTitle("X Pull");
  TH1F *h_pull_y  = new TH1F("h_pull_y","",100,-2., 2); h_pull_y->GetXaxis()->SetTitle("Y Pull");
  //Loop over Ntry_tot. Eech loop is a fit.
  for(int Ntry=0; Ntry<Ntry_tot; Ntry++){
    std::string s_Ntry = std::to_string(Ntry);
    const int nGen=10000;
    //Histosgrams for monitoring what is going on
    TString namex="h_x_"+s_Ntry, namey="h_y_"+s_Ntry, namexy="h_xy_"+s_Ntry; 
    TH1F *h_x   = new TH1F(namex.Data(),"",100,-10,10); h_x->GetXaxis()->SetTitle("X");
    TH1F *h_y   = new TH1F(namey.Data(),"",100,-10,10); h_y->GetXaxis()->SetTitle("Y");
    TH2F *h_xy  = new TH2F(namexy.Data(),"",100,-5,5,100,-5,5); h_xy->GetXaxis()->SetTitle("X"); h_xy->GetYaxis()->SetTitle("Y");
    //TOY distribution to be fitted
    TString s_sigma_x = "1.5", s_sigma_y = "1.5"; std::string::size_type str;
    float sigma_x = std::stof(s_sigma_x.Data(),&str); float sigma_y = std::stof(s_sigma_y.Data(),&str);
    TF2 *Gauss2D     = new TF2("Gauss2D",        "exp( -( (pow(x-0,2))/(2*pow("+s_sigma_x+",2)) + (pow(y-0,2))/(2*pow("+s_sigma_y+",2)) ) )",-10,10,-10,10);
    //Fundamental, you want TF2 to represent a function with 100 points and not the defailt 30. Otherwise the fit is biased.
    Gauss2D->SetNpx(100); Gauss2D->SetNpy(100);
    //Function used to fit
    TF2 *Gauss2D_fit = new TF2("Gauss2D_fit","[0]*exp( -( (pow(x-0,2))/(2*pow([1],2)) + (pow(y-0,2))/(2*pow([2],2)) ) )",-4,4,-4,4);
    Gauss2D_fit->SetParName(0, "Norm");
    Gauss2D_fit->SetParName(1, "sigmaX");
    Gauss2D_fit->SetParName(2, "sigmaY");
    Gauss2D_fit->SetParameter(0, 100.); Gauss2D_fit->SetParLimits(0, 0., nGen);
    Gauss2D_fit->SetParameter(1, sigma_x); Gauss2D_fit->SetParLimits(1, 0., 2*sigma_x);
    Gauss2D_fit->SetParameter(2, sigma_y); Gauss2D_fit->SetParLimits(2, 0., 2*sigma_y);
    //Filling contol histograms
    float a_x[nGen]={0.};
    float a_y[nGen]={0.};
    for(int i=0; i<nGen; i++ ){
	double x_gen, y_gen;
	Gauss2D->GetRandom2(x_gen,y_gen);
	h_x->Fill(x_gen);
	h_y->Fill(y_gen);
	a_x[i]=x_gen; a_y[i]=y_gen;
	h_xy->Fill(x_gen,y_gen);
    }
    //Make the fit
    TVirtualFitter::SetDefaultFitter("Minuit");
//    ROOT::Math::MinimizerOptions::SetDefaultErrorDef(1.+1.E-15); //Set that you are using a log likelihood, and the error should be 0.5 and not 1.+1.E-15 that is default for likelihood (better than using SET ERR because you set it before the fit)
    TFitResultPtr fit_res = h_xy->Fit("Gauss2D_fit","LS");
//    Int_t ierflg = 0;
//    Double_t arglist[1]={0.5}; 
//    gMinuit->mnexcm("SET ERR",arglist,1,ierflg); //redundant since you already have "ROOT::Math::MinimizerOptions::SetDefaultErrorDef(0.5);"
    //Set Strategy. Default is 1. 0 means quick, 2 means more accurate.
//    arglist[0]=2;
//    ierflg = 0;
//    gMinuit->mnexcm("SET STR", arglist, 1, ierflg);
    //Set Error Computation. HESSE is ok for parabolid likelihood, MINOS is better for non paraboloid.
//    arglist[0]=0;
//    gMinuit->mnexcm("MINOS", arglist, 0, ierflg);
    //Extract params
    float post_Norm   = fit_res->Parameter(0);
    float post_sigmax = fit_res->Parameter(1);
    float post_sigmay = fit_res->Parameter(2);
    //Covariance matrix
    TMatrixDSym mat(3); 
    gMinuit->mnemat( mat.GetMatrixArray(), 3);
    //Alternative covariance matrix and test of they are the same
    if(false){
	TMatrixDSym mat2 = fit_res->GetCovarianceMatrix();
	cout<<"Covariance matrix1a: "<<mat[0][0]<<" "<<mat[0][1]<<" "<<mat[0][2]<<endl;
	cout<<"Covariance matrix1b: "<<mat[1][0]<<" "<<mat[1][1]<<" "<<mat[1][2]<<endl;
	cout<<"Covariance matrix1c: "<<mat[2][0]<<" "<<mat[2][1]<<" "<<mat[2][2]<<endl;
	cout<<"Should be equal to:"<<endl;
	cout<<"Covariance matrix2a: "<<mat2[0][0]<<" "<<mat2[0][1]<<" "<<mat2[0][2]<<endl;
	cout<<"Covariance matrix2b: "<<mat2[1][0]<<" "<<mat2[1][1]<<" "<<mat2[1][2]<<endl;
	cout<<"Covariance matrix2c: "<<mat2[2][0]<<" "<<mat2[2][1]<<" "<<mat2[2][2]<<endl;
    }
    //Fill Plots
    h_x_err->Fill(sqrt(mat[1][1])/sigma_x); //Relative error
    h_y_err->Fill(sqrt(mat[2][2])/sigma_y);
    h_x_errD->Fill( fabs(fabs(post_sigmax-sigma_x)-sqrt(mat[1][1]))); //RealError - Error from Cov. Matix
    h_y_errD->Fill( fabs(fabs(post_sigmay-sigma_y)-sqrt(mat[2][2])));
    h_pull_x->Fill( (post_sigmax-sigma_x)/sqrt(mat[1][1]) );
    h_pull_y->Fill( (post_sigmay-sigma_y)/sqrt(mat[2][2]) );
    //Check if real value is inside the error (assuming uncorrlation)
    if( fabs(post_sigmax-sigma_x)<sqrt( mat[1][1]) ) is_inside1_c++;
    if( fabs(post_sigmay-sigma_y)<sqrt( mat[2][2]) ) is_inside2_c++;
    //Draw histos only for 2 fits (otherwise too histograms)
    gStyle->SetOptStat(111111);
    if(Ntry<5){
	//Draw likelihood. Paramteres start from 1!
	gMinuit->Command("SCAn 1 50 3 10");
	TString name_gr=folder+"/Like_Norm_"+s_Ntry+".pdf";
	TGraph *gro = (TGraph*)gMinuit->GetPlot(); gro->SetMarkerStyle(29); gro->SetMarkerSize(0.9); gro->Draw("APL"); c1->SaveAs(name_gr.Data());
	gMinuit->Command("SCAn 2 50 1 2");
	name_gr=folder+"/Like_SigmaX_"+s_Ntry+".pdf";
	TGraph *gr1 = (TGraph*)gMinuit->GetPlot(); gr1->SetMarkerStyle(29); gr1->SetMarkerSize(0.9); gr1->Draw("APL"); c1->SaveAs(name_gr.Data());
	gMinuit->Command("SCAn 3 50 1 2");
	name_gr=folder+"/Like_SigmaY_"+s_Ntry+".pdf";
	TGraph *gr2 = (TGraph*)gMinuit->GetPlot(); gr2->SetMarkerStyle(29); gr2->SetMarkerSize(0.9); gr2->Draw("APL"); c1->SaveAs(name_gr.Data());
	cout<<"Results: "<<post_Norm<<" "<<post_sigmax<<" "<<post_sigmay<<endl;
	cout<<"Covariance matrix: "<<mat[1][1]<<" "<<mat[1][2]<<endl;
	cout<<"Covariance matrix: "<<mat[2][1]<<" "<<mat[2][2]<<endl;
	cout<<"Sqrt(N)/N: "<<sqrt(nGen)/nGen<<endl;
	cout<<"Error 1 is: "<<sqrt(mat[1][1])/sigma_x<<endl;
	cout<<"Error 2 is: "<<sqrt(mat[2][2])/sigma_y<<endl;
	TGraph* gr = new TGraph(nGen,a_x,a_y);
	gr->Draw("Ap");
	TString name=folder+"/G_xy_"+s_Ntry+".pdf";
	c1->SaveAs(name.Data());
	h_x->Draw();
	name=folder+"/h_x_"+s_Ntry+".pdf";
	c1->SaveAs(name.Data());
	h_y->Draw();
	name=folder+"/h_y_"+s_Ntry+".pdf";
	c1->SaveAs(name.Data());
	h_xy->Draw("colz");
	name=folder+"/h_xy_"+s_Ntry+".pdf";
	c1->SaveAs(name.Data());
	//Countour sigmax vs sigmay. Contour(Int_t npoints = 10, Int_t pa1=0, Int_t pa2=1). params start from 0!
	//To get the n-sigma contour the ERRDEF parameter in Minuit has to set to n^2. The fcn function has to be set before the routine is called.
	name_gr=folder+"/Like_Contour_"+s_Ntry+".pdf";
	TGraph *grc = (TGraph*)gMinuit->Contour(80, 1, 2); grc->SetMarkerStyle(29); grc->SetMarkerSize(0.9); grc->Draw("APL"); c1->SaveAs(name_gr.Data());
	delete gr;
    }
    delete h_x;
    delete h_y;
    delete h_xy;
    delete Gauss2D;
    delete Gauss2D_fit;
  }
  h_x_err->Draw();
  c1->SaveAs(folder+"/h_error_X.pdf");
  h_y_err->Draw();
  c1->SaveAs(folder+"/h_error_Y.pdf");
  h_x_errD->Draw();
  c1->SaveAs(folder+"/h_errorD_X.pdf");
  h_y_errD->Draw();
  c1->SaveAs(folder+"/h_errorD_Y.pdf");
  h_pull_x->Draw();
  c1->SaveAs(folder+"/h_pull_X.pdf");
  h_pull_y->Draw();
  c1->SaveAs(folder+"/h_pull_Y.pdf");
  
  delete h_x_err;
  delete h_y_err;
  delete h_x_errD;
  delete h_y_errD;
  delete h_pull_x;
  delete h_pull_y;
  delete c1;
  cout<<"Coverage for the first parameter: "<<is_inside1_c/Ntry_tot<<endl;
  cout<<"Coverage for the second parameter: "<<is_inside2_c/Ntry_tot<<endl;
}
