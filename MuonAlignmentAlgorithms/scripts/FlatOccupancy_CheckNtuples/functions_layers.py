import ROOT as r
import struct, math, os, sys
from array import array

#This function just return a unique number for each chamber, so that I can create a map to this key.
def convertChamberToIndex(Tuple):
  if(len(Tuple)<2):
    print "WARNING: Chmabers have 3 numbers"; sys.exit(0);
  if( Tuple[0]==0 ):
    Wheel=7
  if( Tuple[0]<0 ):
    Wheel=-Tuple[0]+3
  return str(Wheel*1000 + Tuple[1]*100 + Tuple[2])

def findBin(pos_x,ResXBin,BinWidth):
  MyBin=-999
  if(pos_x<-180):
    return MyBin
  if(pos_x>180):
    return MyBin
  for i in range(ResXBin):
    if(pos_x<-160+i*BinWidth):
      MyBin=i; break
  return int(MyBin)

def fitgaus(hist, sigmas, opts):
    lower, upper = hist.GetMean()-sigmas*hist.GetRMS(), hist.GetMean()+sigmas*hist.GetRMS()
    hist.Fit("gaus",opts, "", lower, upper)

def getFitParamsGauss(hist):
    fit = hist.GetFunction("gaus")
    p0 = fit.GetParameter(0) 
    p0e = fit.GetParError(0)
    p1 = fit.GetParameter(1)
    p1e = fit.GetParError(1)
    p2 = fit.GetParameter(2)
    p2e = fit.GetParError(2)
    return p0, p0e, p1, p1e, p2, p2e

def fitLineStraight(hist, opts):
    nimBin=10
    lower=-1
    upper=-1
    for nB in range(hist.GetN()):
      if(hist.GetY()[nB]!=0 and hist.GetErrorY(nB)!=0):
        lower=hist.GetX()[nB]; nimBin=nB; break;
    for nB in range(hist.GetN()):
      if(nB>nimBin+1 and nB>0 and hist.GetY()[nB]==0 and hist.GetErrorY(nB)==0):
        upper=hist.GetX()[nB-1]; break;
    if(upper==-1):
      upper=hist.GetX()[hist.GetN()-1];
    if(lower!=-1 and upper!=-1):
      StraightLine = r.TF1("StraightLine","[0]", lower, upper);
      hist.Fit("StraightLine",opts)
      fit = hist.GetFunction("StraightLine")
      return fit.GetParameter(0), fit.GetParError(0)

def fitLine(hist, opts):
    nimBin=10
    lower=-1
    upper=-1
    for nB in range(hist.GetN()):
      if(hist.GetY()[nB]!=0 and hist.GetErrorY(nB)!=0):
        lower=hist.GetX()[nB]; nimBin=nB; break;
    for nB in range(hist.GetN()):
      if(nB>nimBin+1 and nB>0 and hist.GetY()[nB]==0 and hist.GetErrorY(nB)==0):
        upper=hist.GetX()[nB-1]; break;
    if(upper==-1):
      upper=hist.GetX()[hist.GetN()-1];
    if(lower!=-1 and upper!=-1):
      StraightLine = r.TF1("StraightLine","[0]+[1]*x", lower, upper);
      hist.Fit("StraightLine",opts)
      fit = hist.GetFunction("StraightLine")
      return fit.GetParameter(0), fit.GetParError(0), fit.GetParameter(1), fit.GetParError(1)

#Retrieve the first and last bin populated in a TH2 or TH1 (you will have to add "+1" to the bin number as always)
def findBinBound(hist, h_type):
  if(h_type!="TH1F" and h_type!="TH2F"):
    print "WARNING: ", h_type, "not recognized"
  lowerX=-1; lowerY=-1;
  upperX=-1; upperY=-1;
  if(h_type=="TH2F"):
    nBinX=hist.GetNbinsX(); nBinY=hist.GetNbinsY()
    #Find maximum, so that the range is in bins with at least 

    for nB in range(nBinX):
      if(hist.GetBinContent(nB+1,int(nBinY/2))>0):
        lowerX=nB; break;
    for nB in range(nBinX):
      if(nB>lowerX and hist.GetBinContent(nB+1,int(nBinY/2))==0 and hist.GetBinContent(nB+2,int(nBinY/2))==0):
        upperX=nB-1; break;
    for nB in range(nBinY):
      if(hist.GetBinContent(int(nBinX/2),nB)>0):
        lowerY=nB; break;
    for nB in range(nBinY):
      if(nB>lowerY and hist.GetBinContent(int(nBinX/2),nB+1)==0 and hist.GetBinContent(int(nBinX/2),nB+2)==0):
        upperY=nB-1; break;
  if(h_type=="TH1F"):
    nBinX=hist.GetNbinsX()
    for nB in range(nBinX):
      if(hist.GetBinContent(nB+1)>0):
        lowerX=nB; break;
    for nB in range(nBinX):
      if(nB>lowerX and hist.GetBinContent(nB+1)==0 and hist.GetBinContent(nB+2)==0):
        upperX=nB-1; break;
  if(h_type=="TH1F" and (lowerX==-1 or upperX==-1)):
    print "WARNING: 1D external bins not found!"
  if(h_type=="TH2F" and (lowerX==-1 or lowerY==-1 or upperX==-1 or upperY==-1)):
    print "WARNING: 2D external bins not found!"
  return lowerX, upperX, lowerY, upperY

#Retrieves the bins corresponding to the minimum a TH1F/TH2F inside a bin range (you will have to add "+1" to the bin number as always)
def findMinMaxBin(lowerX, upperX, lowerY, upperY, hist, h_type):
  if(h_type!="TH1F" and h_type!="TH2F"):
    print "WARNING: ", h_type, "not recognized"
  minX=-1; minY=-1
  maxX=-1; maxY=-1
  minBin=9999999.
  if(h_type=="TH2F"):
    nBinX=hist.GetNbinsX(); nBinY=hist.GetNbinsY()
    #Find Maximum, because you will choose the minimum at least 20% of the maximum
    maxBin=0
    for nBX in range(nBinX):
      for nBY in range(nBinY):
        if(nBX>lowerX-1 and nBX<upperX and nBY>lowerY and nBY<upperY):
          thisBin=hist.GetBinContent(nBX+1,nBY+1)
          if(thisBin>maxBin):
            maxBin=thisBin
            maxX=nBX; maxY=nBY
    for nBX in range(nBinX):
      for nBY in range(nBinY):
        if(nBX>lowerX-1 and nBX<upperX and nBY>lowerY and nBY<upperY):
          thisBin=hist.GetBinContent(nBX+1,nBY+1)
          if(thisBin<minBin and thisBin>maxBin*(20/100)):
            minBin=thisBin
            minX=nBX; minY=nBY
  if(h_type=="TH1F"):
    nBinX=hist.GetNbinsX()
    maxBin=0
    for nBX in range(nBinX):
        if(nBX>lowerX and nBX<upperX):
          thisBin=hist.GetBinContent(nBX+1)
          if(thisBin>maxBin):
            maxBin=thisBin
            maxX=nBX
    for nBX in range(nBinX):
        if(nBX>lowerX and nBX<upperX):
          thisBin=hist.GetBinContent(nBX+1)
          if(thisBin<minBin and thisBin>maxBin):
            minBin=thisBin
            minX=nBX
  if(h_type=="TH2F" and (minX==-1 or minY==-1)):
    print "WARNING: 2D min bin not found!"
  if(h_type=="TH1F" and minX==-1):
    print "WARNING: 1D min bin not found!"
  return minX, minY, maxX, maxY
