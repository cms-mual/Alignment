from signConventions import *
import numpy as np
from math import sqrt

def initCovMatrix( elements = 0 ):
  cov = [[]]
  cov = [[elements for i in range(6)] for i in range(6)]
  return cov

#M is N vectoir of 36 size, where N is the number of the sectors, and where in each vecotor only diagonal copmponent are !=0
#mu is a vector of 36, with all 0 except the diagonal elements of the matrix (mean of te previous one)
def calculateSystMatrix(M):
  mu = calculateMean(M)
  sd = calculateSD(M,mu) #Given M and mu make the standard deviation for each diagonal component
  cov = initCovMatrix()
  index=0
  for i in range(6):
    for j in range(6):
      cov[i][j] = sd[index]*sd[index]
      index=index+1
  #Computing off-diagonal terms (Not used at the moment, we take them from the covariance matrix)
#  N = len(M)
#  for i in range(6):
#    for j in range(6):
#      for n in range(N):
#        if M[n] != None:
#          cov[i][j] = cov[i][j] + ( M[n][i*6] - mu[i*6] ) * ( M[n][j*6] - mu[j*6] )
#  for i in range(6):
#    for j in range(6):
#      cov[i][j] = cov[i][j]/(N-1)
  print( "Syst. Unc. matrix (squared, as the covariance):")
  printCovMatrix(cov)
  return cov

def calculateCovStatMatrix_noAverage(M): # M = M_FIT[wheel][station][sector]
  cov = initCovMatrix()
  index = 0
  for i in range(6):
    for j in range(6):
      cov[i][j] = M[index]
      index = index+1
  return cov

def calculateCovStatMatrix(M): # M = M_FIT[wheel][station]
  mu = calculateMean(M) #Average all sectros and make a single matrix
  cov = initCovMatrix() 
  index=0
  for i in range(6):
    for j in range(6):
      cov[i][j] = mu[index]
      index=index+1
  print( "Covariance matrix:")
  printCovMatrix(cov)
  return cov

def calculateCovStatMatrix_times2(M): # M = M_FIT[wheel][station]
  mu      = calculateMean(M) #Average all sectros and make a single matrix
  cov     = initCovMatrix()
  index=0
  for i in range(6):
    for j in range(6):
      # To increae the variance of a fator 2 we need to multiply APE by 4, sicne it conatins sigma^2. Multiplying the whole matrix is ok, sicne it preserve the correlations.
      cov[i][j] = mu[index]*4
      index=index+1
  return cov

def printM(M):              # M is a list of list: [Sector1_APE[xx,xy,xz...], Sector2_APE[xx,xy,xz...], Sector3_APE[xx,xy,xz...]... ].
  index=0
  for n in M:
    if M[index] != None :
      print( "Sec: ", index+1, " , len: ", len(n), ") ",end='')
      for i in range(len(n)):    # Covariance matrix has 36 elements[xx,xy,xz...], while difference between geoemtries only fiagonal ones (6)
        print ('% 1.10f' % M[index][i] , end='')
    else:
      print( n, ": Not valid")
    index=index+1
    print()

def printCovMatrix(cov):
  for i in range(6):
    for j in range(6):
      print ('% 1.10f' % cov[i][j], end='')
    print()

def printSqrtCovMatrix(cov):
  for i in range(6):
    for j in range(6):
      print ('% 1.10f' % sqrt( abs( cov[i][j] ) ), end='')
    print()

def calculateMean(M):
  mu = [0 for i in range(36)]
  N = len(M) #All sectors
  for n in range(N):
    for i in range(36):
      if M[n] != None : mu[i] = mu[i] + M[n][i]
  for i in range(36):
    mu[i] = mu[i]/N
  #print( "Means:")
  #printMean(mu)
  return mu

#sd=sqrt(SUM[(xi-mu)^2]/N)
def calculateSD(M,mu):
  sd = [0 for i in range(36)]
  N = len(M) # All sectors
  for n in range(N):
    for i in range(36):
      if M[n] != None : sd[i] = sd[i] + (M[n][i]-mu[i])*(M[n][i]-mu[i])
  for i in range(36):
    sd[i] = sqrt(sd[i]/N)
  return sd

def printMean(mu):
  for i in range(len(mu)):
    print ('% 1.10f' % mu[i] )

def sumMatrix(cov1, cov2):
  cov = initCovMatrix()
  for i in range(6):
    for j in range(6):
      cov[i][j] = cov1[i][j] + cov2[i][j]
  return cov

def sumCov_Syst_matrix(cov, syst):
  #Total unc. diagonal is summed in quadrature
  totUnc = []
  for i in range(6):
    totUnc.append(sqrt(cov[i][i] + syst[i][i])) #NOTE: they are already squared
  #Diagonal terms are totUnc[i]. Off-diagonal terms are rho_xy*sigma_x*sigma_y
  cov_tot = initCovMatrix()
  for i in range(6):
    for j in range(6):
      if(i==j):
        cov_tot[i][i]=totUnc[i]*totUnc[i]
      else:
        if(cov[i][i]!=0 and cov[j][j]!=0): #In station 4 thise are 0 andyou cannot make the division
          #Computing correlation from cov. matrix [rho = cov_xy/(var_x*var_y)]
          rho = cov[i][j]/(sqrt(cov[i][i])*sqrt(cov[j][j]))
          #Now build the covariance term using the same correlation but the complete uncertainty (no sqrt because totunc is not squared)
          cov_tot[i][j] = rho * ( totUnc[i]*totUnc[j] )
        else:
          cov_tot[i][j] = 0.
  return cov_tot

def testCorrelation(cov, totUnc):
  for i in range(6):
    for j in range(6):
      if(j>=i and cov[i][i]!=0 and cov[j][j]!=0 and totUnc[i][i]!=0 and totUnc[j][j]!=0):
        rho_cov    = cov[i][j]/(sqrt(cov[i][i])*sqrt(cov[j][j]))
        rho_totUnc = totUnc[i][j]/(sqrt(totUnc[i][i])*sqrt(totUnc[j][j]))
        if(rho_cov-rho_totUnc>0.00000000001): print( "WARNING: corrlation is different. ",i,j,") ",rho_cov,rho_totUnc)

def calculateCrosCovMatrix(M1, M2):
  
  N1 = len(M1)
  N2 = len(M2)
  if N1 != N2 :
    print( "calculateCrosCovMatrix: Error! Matrixes with different dimensions")
    return
  
  mu1 = calculateMean(M1)
  mu2 = calculateMean(M2)
  
  cov12 = initCovMatrix()
  
  for i in range(6):
    for j in range(6):
      for n in range(N1):
        if M1[n] != None and M2[n] != None : cov12[i][j] = cov12[i][j] + ( M1[n][i] - mu1[i] ) * ( M2[n][j] - mu2[j] )
  
  cov21 = initCovMatrix()
  
  for i in range(6):
    for j in range(6):
      for n in range(N1):
        if M1[n] != None and M2[n] != None : cov21[i][j] = cov21[i][j] + ( M1[n][j] - mu1[j] ) * ( M2[n][i] - mu2[i] )
  
  for i in range(6):
    for j in range(6):
      cov12[i][j] = cov12[i][j]/(N1-1)
      cov21[i][j] = cov21[i][j]/(N1-1)
  
  print( "Covariance matrix cov12:")
  printCovMatrix(cov12)
  print( "Covariance matrix cov21:")
  printCovMatrix(cov21)
  
  crossCov = sumMatrix( cov12, cov21 )
  print( "Cross-covariance matrix cov12+cov21:")
  printCovMatrix(crossCov)
  
  return crossCov

#Function to check if the covariance matrix is invertible (i.e. not singular)
def is_invertible(a):
  return a.shape[0] == a.shape[1] and np.linalg.matrix_rank(a) == a.shape[0]

#Apply sign covention to M_Fit so that later you can make an average
def signConvention(M_fit):
  newM_fit = []
  for wheel in -2, -1, 0, +1, +2:
    newM_fit.append([])
    for station in 1, 2, 3, 4:
      newM_fit[wheel+2].append([])
      if station != 4:
        for sector in 1,2,3,4,5,6,7,8,9,10,11,12:
          newM_fit[wheel+2][station-1].append(None)
      else:
        for sector in 1,2,3,4,5,6,7,8,9,10,11,12,13,14:
          newM_fit[wheel+2][station-1].append(None)
  for wheel in -2,-1,0,1,2:
    for station in 1,2,3,4:
      sectors = (1,2,3,4,5,6,7,8,9,10,11,12)
      if(station==4): sectors = (1,2,3,4,5,6,7,8,9,10,11,12,13,14)
      for sector in sectors:
        cov = M_fit[wheel+2][station-1][sector-1]
        if (cov is None):
          newM_fit[wheel+2][station-1][sector-1] = None;
          continue;
        else:
          if(len(cov)==36):
            cov_signConv = signConvention_cov(cov,wheel,station,sector)
          else:
            cov_signConv = signConvention_cov_2D(cov,wheel,station,sector)
          newM_fit[wheel+2][station-1][sector-1] = cov_signConv
  return newM_fit

def signConvention_cov(cov,wheel,station,sector):
  xx=0; xy=1; xz=2; xphix=3; xphiy=4; xphiz=5; yx=6; yy=7; yz=8; yphix=9; yphiy=10; yphiz=11; zx=12; zy=13; zz=14; zphix=15; zphiy=16; zphiz=17;
  phixx=18; phixy=19; phixz=20; phixphix=21; phixphiy=22; phixphiz=23; phiyx=24; phiyy=25; phiyz=26; phiyphix=27; phiyphiy=28; phiyphiz=29; phizx=30; phizy=31; phizz=32; phizphix=33; phizphiy=34; phizphiz=35;
  cov_signConv = []
  for index in range(36):
      sign = 1;
      if(index==xx):       sign = signConventions["DT", wheel, station, sector][0]*signConventions["DT", wheel, station, sector][0]
      if(index==xy):       sign = signConventions["DT", wheel, station, sector][0]*signConventions["DT", wheel, station, sector][1]
      if(index==xz):       sign = signConventions["DT", wheel, station, sector][0]*signConventions["DT", wheel, station, sector][2]
      if(index==xphix):    sign = signConventions["DT", wheel, station, sector][0]*signConventions["DT", wheel, station, sector][0]
      if(index==xphiy):    sign = signConventions["DT", wheel, station, sector][0]*signConventions["DT", wheel, station, sector][1]
      if(index==xphiz):    sign = signConventions["DT", wheel, station, sector][0]*signConventions["DT", wheel, station, sector][2]
      if(index==yx):       sign = signConventions["DT", wheel, station, sector][1]*signConventions["DT", wheel, station, sector][0]
      if(index==yy):       sign = signConventions["DT", wheel, station, sector][1]*signConventions["DT", wheel, station, sector][1]
      if(index==yz):       sign = signConventions["DT", wheel, station, sector][1]*signConventions["DT", wheel, station, sector][2]
      if(index==yphix):    sign = signConventions["DT", wheel, station, sector][1]*signConventions["DT", wheel, station, sector][0]
      if(index==yphiy):    sign = signConventions["DT", wheel, station, sector][1]*signConventions["DT", wheel, station, sector][1]
      if(index==yphiz):    sign = signConventions["DT", wheel, station, sector][1]*signConventions["DT", wheel, station, sector][2]
      if(index==zx):       sign = signConventions["DT", wheel, station, sector][2]*signConventions["DT", wheel, station, sector][0]
      if(index==zy):       sign = signConventions["DT", wheel, station, sector][2]*signConventions["DT", wheel, station, sector][1]
      if(index==zz):       sign = signConventions["DT", wheel, station, sector][2]*signConventions["DT", wheel, station, sector][2]
      if(index==zphix):    sign = signConventions["DT", wheel, station, sector][2]*signConventions["DT", wheel, station, sector][0]
      if(index==zphiy):    sign = signConventions["DT", wheel, station, sector][2]*signConventions["DT", wheel, station, sector][1]
      if(index==zphiz):    sign = signConventions["DT", wheel, station, sector][2]*signConventions["DT", wheel, station, sector][2]
      if(index==phixx):    sign = signConventions["DT", wheel, station, sector][0]*signConventions["DT", wheel, station, sector][0]
      if(index==phixy):    sign = signConventions["DT", wheel, station, sector][0]*signConventions["DT", wheel, station, sector][1]
      if(index==phixz):    sign = signConventions["DT", wheel, station, sector][0]*signConventions["DT", wheel, station, sector][2]
      if(index==phixphix): sign = signConventions["DT", wheel, station, sector][0]*signConventions["DT", wheel, station, sector][0]
      if(index==phixphiy): sign = signConventions["DT", wheel, station, sector][0]*signConventions["DT", wheel, station, sector][1]
      if(index==phixphiz): sign = signConventions["DT", wheel, station, sector][0]*signConventions["DT", wheel, station, sector][2]
      if(index==phiyx):    sign = signConventions["DT", wheel, station, sector][1]*signConventions["DT", wheel, station, sector][0]
      if(index==phiyy):    sign = signConventions["DT", wheel, station, sector][1]*signConventions["DT", wheel, station, sector][1]
      if(index==phiyz):    sign = signConventions["DT", wheel, station, sector][1]*signConventions["DT", wheel, station, sector][2]
      if(index==phiyphix): sign = signConventions["DT", wheel, station, sector][1]*signConventions["DT", wheel, station, sector][0]
      if(index==phiyphiy): sign = signConventions["DT", wheel, station, sector][1]*signConventions["DT", wheel, station, sector][1]
      if(index==phiyphiz): sign = signConventions["DT", wheel, station, sector][1]*signConventions["DT", wheel, station, sector][2]
      if(index==phizx):    sign = signConventions["DT", wheel, station, sector][2]*signConventions["DT", wheel, station, sector][0]
      if(index==phizy):    sign = signConventions["DT", wheel, station, sector][2]*signConventions["DT", wheel, station, sector][1]
      if(index==phizz):    sign = signConventions["DT", wheel, station, sector][2]*signConventions["DT", wheel, station, sector][2]
      if(index==phizphix): sign = signConventions["DT", wheel, station, sector][2]*signConventions["DT", wheel, station, sector][0]
      if(index==phizphiy): sign = signConventions["DT", wheel, station, sector][2]*signConventions["DT", wheel, station, sector][1]
      if(index==phizphiz): sign = signConventions["DT", wheel, station, sector][2]*signConventions["DT", wheel, station, sector][2]
      cov_signConv.append( cov[index]*sign )
  return cov_signConv

def signConvention_cov_2D(cov,wheel,station,sector):
  xx=0; xy=1; xz=2; xphix=3; xphiy=4; xphiz=5; yx=6; yy=7; yz=8; yphix=9; yphiy=10; yphiz=11; zx=12; zy=13; zz=14; zphix=15; zphiy=16; zphiz=17;
  phixx=18; phixy=19; phixz=20; phixphix=21; phixphiy=22; phixphiz=23; phiyx=24; phiyy=25; phiyz=26; phiyphix=27; phiyphiy=28; phiyphiz=29; phizx=30; phizy=31; phizz=32; phizphix=33; phizphiy=34; phizphiz=35;
  cov_signConv = initCovMatrix()

  index = 0
  for indeX in range(6):
      for indeY in range(6):
          sign = 1;
          if(index==xx):       sign = signConventions["DT", wheel, station, sector][0]*signConventions["DT", wheel, station, sector][0]
          if(index==xy):       sign = signConventions["DT", wheel, station, sector][0]*signConventions["DT", wheel, station, sector][1]
          if(index==xz):       sign = signConventions["DT", wheel, station, sector][0]*signConventions["DT", wheel, station, sector][2]
          if(index==xphix):    sign = signConventions["DT", wheel, station, sector][0]*signConventions["DT", wheel, station, sector][0]
          if(index==xphiy):    sign = signConventions["DT", wheel, station, sector][0]*signConventions["DT", wheel, station, sector][1]
          if(index==xphiz):    sign = signConventions["DT", wheel, station, sector][0]*signConventions["DT", wheel, station, sector][2]
          if(index==yx):       sign = signConventions["DT", wheel, station, sector][1]*signConventions["DT", wheel, station, sector][0]
          if(index==yy):       sign = signConventions["DT", wheel, station, sector][1]*signConventions["DT", wheel, station, sector][1]
          if(index==yz):       sign = signConventions["DT", wheel, station, sector][1]*signConventions["DT", wheel, station, sector][2]
          if(index==yphix):    sign = signConventions["DT", wheel, station, sector][1]*signConventions["DT", wheel, station, sector][0]
          if(index==yphiy):    sign = signConventions["DT", wheel, station, sector][1]*signConventions["DT", wheel, station, sector][1]
          if(index==yphiz):    sign = signConventions["DT", wheel, station, sector][1]*signConventions["DT", wheel, station, sector][2]
          if(index==zx):       sign = signConventions["DT", wheel, station, sector][2]*signConventions["DT", wheel, station, sector][0]
          if(index==zy):       sign = signConventions["DT", wheel, station, sector][2]*signConventions["DT", wheel, station, sector][1]
          if(index==zz):       sign = signConventions["DT", wheel, station, sector][2]*signConventions["DT", wheel, station, sector][2]
          if(index==zphix):    sign = signConventions["DT", wheel, station, sector][2]*signConventions["DT", wheel, station, sector][0]
          if(index==zphiy):    sign = signConventions["DT", wheel, station, sector][2]*signConventions["DT", wheel, station, sector][1]
          if(index==zphiz):    sign = signConventions["DT", wheel, station, sector][2]*signConventions["DT", wheel, station, sector][2]
          if(index==phixx):    sign = signConventions["DT", wheel, station, sector][0]*signConventions["DT", wheel, station, sector][0]
          if(index==phixy):    sign = signConventions["DT", wheel, station, sector][0]*signConventions["DT", wheel, station, sector][1]
          if(index==phixz):    sign = signConventions["DT", wheel, station, sector][0]*signConventions["DT", wheel, station, sector][2]
          if(index==phixphix): sign = signConventions["DT", wheel, station, sector][0]*signConventions["DT", wheel, station, sector][0]
          if(index==phixphiy): sign = signConventions["DT", wheel, station, sector][0]*signConventions["DT", wheel, station, sector][1]
          if(index==phixphiz): sign = signConventions["DT", wheel, station, sector][0]*signConventions["DT", wheel, station, sector][2]
          if(index==phiyx):    sign = signConventions["DT", wheel, station, sector][1]*signConventions["DT", wheel, station, sector][0]
          if(index==phiyy):    sign = signConventions["DT", wheel, station, sector][1]*signConventions["DT", wheel, station, sector][1]
          if(index==phiyz):    sign = signConventions["DT", wheel, station, sector][1]*signConventions["DT", wheel, station, sector][2]
          if(index==phiyphix): sign = signConventions["DT", wheel, station, sector][1]*signConventions["DT", wheel, station, sector][0]
          if(index==phiyphiy): sign = signConventions["DT", wheel, station, sector][1]*signConventions["DT", wheel, station, sector][1]
          if(index==phiyphiz): sign = signConventions["DT", wheel, station, sector][1]*signConventions["DT", wheel, station, sector][2]
          if(index==phizx):    sign = signConventions["DT", wheel, station, sector][2]*signConventions["DT", wheel, station, sector][0]
          if(index==phizy):    sign = signConventions["DT", wheel, station, sector][2]*signConventions["DT", wheel, station, sector][1]
          if(index==phizz):    sign = signConventions["DT", wheel, station, sector][2]*signConventions["DT", wheel, station, sector][2]
          if(index==phizphix): sign = signConventions["DT", wheel, station, sector][2]*signConventions["DT", wheel, station, sector][0]
          if(index==phizphiy): sign = signConventions["DT", wheel, station, sector][2]*signConventions["DT", wheel, station, sector][1]
          if(index==phizphiz): sign = signConventions["DT", wheel, station, sector][2]*signConventions["DT", wheel, station, sector][2]
          cov_signConv[indeX][indeY] = cov[indeX][indeY]*sign
          index = index+1
  return np.ndarray(shape=(6,6), dtype=float, buffer=np.array(cov_signConv))

def resizeAPEs(cov,cov_fromH):
  new_cov = []
  for wheel in -2, -1, 0, +1, +2:
    new_cov.append([]);
    for station in 1, 2, 3, 4:
      new_cov[wheel+2].append([]);
      if station != 4:
        for sector in 1,2,3,4,5,6,7,8,9,10,11,12:
          new_cov[wheel+2][station-1].append(None)
      else:
        for sector in 1,2,3,4,5,6,7,8,9,10,11,12,13,14:
          new_cov[wheel+2][station-1].append(None)
  for wheel in -2, -1, 0, +1, +2:
    for station in 1, 2, 3, 4:
      sectors = 1,2,3,4,5,6,7,8,9,10,11,12
      if station == 4: sectors = 1,2,3,4,5,6,7,8,9,10,11,12,13,14
      for sector in sectors:
        thecov = cov[wheel+2][station-1][sector-1]
        thecov_fromH = cov_fromH[wheel+2][station-1][sector-1]
        thenewcov = initCovMatrix()
        for iX in range(6):
          for iY in range(6):
            if iX==iY : thenewcov[iX][iY] = thecov_fromH[iX][iY]
        for iX in range(6):
          for iY in range(6):
            if iX!=iY :
              if sqrt(thecov[iX][iX]*thecov[iY][iY])>0 :
                rho = thecov[iX][iY]/(sqrt(thecov[iX][iX]*thecov[iY][iY]))
                thenewcov[iX][iY] = rho * (sqrt(thenewcov[iX][iX]*thenewcov[iY][iY]))
              else:
                thenewcov[iX][iY] = thecov[iX][iY]
        new_cov[wheel+2][station-1][sector-1] = thenewcov
  return new_cov

def resizeAPEs_CSC(cov,cov_fromH):
  new_cov = []
  for endcap in (1, 2):
    new_cov.append([])
    for disk in (1, 2, 3, 4):
      new_cov[endcap-1].append([])
      if disk == 1: rings = (1,2,3,4)
      else:         rings = (1,2)
      for ring in rings:
        new_cov[endcap-1][disk-1].append([])
        for sector in GetCSCSectors(disk,ring):
          new_cov[endcap-1][disk-1][ring-1].append(None)
  for endcap in (1, 2):
    for disk in (1, 2, 3, 4):
      if disk == 1: rings = (1,2,3,4)
      else:         rings = (1,2)
      for ring in rings:
        for sector in GetCSCSectors(disk,ring):
          thecov = cov[endcap-1][disk-1][ring-1][sector-1]
          thecov_fromH = cov_fromH[endcap-1][disk-1][ring-1][sector-1]
          thenewcov = initCovMatrix()
          for iX in range(6):
            for iY in range(6):
              if iX==iY : thenewcov[iX][iY] = thecov_fromH[iX][iY]
          for iX in range(6):
            for iY in range(6):
              if iX!=iY :
                if sqrt(thecov[iX][iX]*thecov[iY][iY])>0 :
                  rho = thecov[iX][iY]/(sqrt(thecov[iX][iX]*thecov[iY][iY]))
                  thenewcov[iX][iY] = rho * (sqrt(thenewcov[iX][iX]*thenewcov[iY][iY]))
                else:
                  thenewcov[iX][iY] = thecov[iX][iY]
          new_cov[endcap-1][disk-1][ring-1][sector-1] = thenewcov
  return new_cov

def GetCSCSectors(disk,ring):
  if disk == 1:
    sectors = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36)
  else:
    if ring == 1: sectors = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18)
    else:         sectors = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36)
  return sectors

#Apply sign covention to M_Fit so that later you can make an average
def signConvention_CSC(M_fit):
  newM_fit = []
  for endcap in (1, 2):
    newM_fit.append([])
    for disk in (1, 2, 3, 4):
      newM_fit[endcap-1].append([])
      if disk == 1: rings = (1,2,3,4)
      else:         rings = (1,2)
      for ring in rings:
        newM_fit[endcap-1][disk-1].append([])
        for sector in GetCSCSectors(disk,ring):
          newM_fit[endcap-1][disk-1][ring-1].append(None)
  for endcap in (1, 2):
    for disk in (1, 2, 3, 4):
      if disk == 1: rings = (1,2,3,4)
      else:         rings = (1,2)
      for ring in rings:
        for sector in GetCSCSectors(disk,ring):
          cov = M_fit[endcap-1][disk-1][ring-1][sector-1]
          if (cov is None):
            newM_fit[endcap-1][disk-1][ring-1][sector-1] = None;
            continue;
          else:
            if(len(cov)==36):
              cov_signConv = signConvention_cov_CSC(cov, endcap, disk, ring, sector)
            else:
              cov_signConv = signConvention_cov_2D_CSC(cov, endcap, disk, ring, sector)
            newM_fit[endcap-1][disk-1][ring-1][sector-1] = cov_signConv
  return newM_fit

def signConvention_cov_CSC(cov,endcap,disk,ring,sector):
  xx=0; xy=1; xz=2; xphix=3; xphiy=4; xphiz=5; yx=6; yy=7; yz=8; yphix=9; yphiy=10; yphiz=11; zx=12; zy=13; zz=14; zphix=15; zphiy=16; zphiz=17;
  phixx=18; phixy=19; phixz=20; phixphix=21; phixphiy=22; phixphiz=23; phiyx=24; phiyy=25; phiyz=26; phiyphix=27; phiyphiy=28; phiyphiz=29; phizx=30; phizy=31; phizz=32; phizphix=33; phizphiy=34; phizphiz=35;
  cov_signConv = []
  for index in range(36):
      sign = 1;
      if(index==xx):       sign = signConventions["CSC", endcap,disk,ring,sector][0]*signConventions["CSC", endcap,disk,ring,sector][0]
      if(index==xy):       sign = signConventions["CSC", endcap,disk,ring,sector][0]*signConventions["CSC", endcap,disk,ring,sector][1]
      if(index==xz):       sign = signConventions["CSC", endcap,disk,ring,sector][0]*signConventions["CSC", endcap,disk,ring,sector][2]
      if(index==xphix):    sign = signConventions["CSC", endcap,disk,ring,sector][0]*signConventions["CSC", endcap,disk,ring,sector][0]
      if(index==xphiy):    sign = signConventions["CSC", endcap,disk,ring,sector][0]*signConventions["CSC", endcap,disk,ring,sector][1]
      if(index==xphiz):    sign = signConventions["CSC", endcap,disk,ring,sector][0]*signConventions["CSC", endcap,disk,ring,sector][2]
      if(index==yx):       sign = signConventions["CSC", endcap,disk,ring,sector][1]*signConventions["CSC", endcap,disk,ring,sector][0]
      if(index==yy):       sign = signConventions["CSC", endcap,disk,ring,sector][1]*signConventions["CSC", endcap,disk,ring,sector][1]
      if(index==yz):       sign = signConventions["CSC", endcap,disk,ring,sector][1]*signConventions["CSC", endcap,disk,ring,sector][2]
      if(index==yphix):    sign = signConventions["CSC", endcap,disk,ring,sector][1]*signConventions["CSC", endcap,disk,ring,sector][0]
      if(index==yphiy):    sign = signConventions["CSC", endcap,disk,ring,sector][1]*signConventions["CSC", endcap,disk,ring,sector][1]
      if(index==yphiz):    sign = signConventions["CSC", endcap,disk,ring,sector][1]*signConventions["CSC", endcap,disk,ring,sector][2]
      if(index==zx):       sign = signConventions["CSC", endcap,disk,ring,sector][2]*signConventions["CSC", endcap,disk,ring,sector][0]
      if(index==zy):       sign = signConventions["CSC", endcap,disk,ring,sector][2]*signConventions["CSC", endcap,disk,ring,sector][1]
      if(index==zz):       sign = signConventions["CSC", endcap,disk,ring,sector][2]*signConventions["CSC", endcap,disk,ring,sector][2]
      if(index==zphix):    sign = signConventions["CSC", endcap,disk,ring,sector][2]*signConventions["CSC", endcap,disk,ring,sector][0]
      if(index==zphiy):    sign = signConventions["CSC", endcap,disk,ring,sector][2]*signConventions["CSC", endcap,disk,ring,sector][1]
      if(index==zphiz):    sign = signConventions["CSC", endcap,disk,ring,sector][2]*signConventions["CSC", endcap,disk,ring,sector][2]
      if(index==phixx):    sign = signConventions["CSC", endcap,disk,ring,sector][0]*signConventions["CSC", endcap,disk,ring,sector][0]
      if(index==phixy):    sign = signConventions["CSC", endcap,disk,ring,sector][0]*signConventions["CSC", endcap,disk,ring,sector][1]
      if(index==phixz):    sign = signConventions["CSC", endcap,disk,ring,sector][0]*signConventions["CSC", endcap,disk,ring,sector][2]
      if(index==phixphix): sign = signConventions["CSC", endcap,disk,ring,sector][0]*signConventions["CSC", endcap,disk,ring,sector][0]
      if(index==phixphiy): sign = signConventions["CSC", endcap,disk,ring,sector][0]*signConventions["CSC", endcap,disk,ring,sector][1]
      if(index==phixphiz): sign = signConventions["CSC", endcap,disk,ring,sector][0]*signConventions["CSC", endcap,disk,ring,sector][2]
      if(index==phiyx):    sign = signConventions["CSC", endcap,disk,ring,sector][1]*signConventions["CSC", endcap,disk,ring,sector][0]
      if(index==phiyy):    sign = signConventions["CSC", endcap,disk,ring,sector][1]*signConventions["CSC", endcap,disk,ring,sector][1]
      if(index==phiyz):    sign = signConventions["CSC", endcap,disk,ring,sector][1]*signConventions["CSC", endcap,disk,ring,sector][2]
      if(index==phiyphix): sign = signConventions["CSC", endcap,disk,ring,sector][1]*signConventions["CSC", endcap,disk,ring,sector][0]
      if(index==phiyphiy): sign = signConventions["CSC", endcap,disk,ring,sector][1]*signConventions["CSC", endcap,disk,ring,sector][1]
      if(index==phiyphiz): sign = signConventions["CSC", endcap,disk,ring,sector][1]*signConventions["CSC", endcap,disk,ring,sector][2]
      if(index==phizx):    sign = signConventions["CSC", endcap,disk,ring,sector][2]*signConventions["CSC", endcap,disk,ring,sector][0]
      if(index==phizy):    sign = signConventions["CSC", endcap,disk,ring,sector][2]*signConventions["CSC", endcap,disk,ring,sector][1]
      if(index==phizz):    sign = signConventions["CSC", endcap,disk,ring,sector][2]*signConventions["CSC", endcap,disk,ring,sector][2]
      if(index==phizphix): sign = signConventions["CSC", endcap,disk,ring,sector][2]*signConventions["CSC", endcap,disk,ring,sector][0]
      if(index==phizphiy): sign = signConventions["CSC", endcap,disk,ring,sector][2]*signConventions["CSC", endcap,disk,ring,sector][1]
      if(index==phizphiz): sign = signConventions["CSC", endcap,disk,ring,sector][2]*signConventions["CSC", endcap,disk,ring,sector][2]
      cov_signConv.append( cov[index]*sign )
  return cov_signConv

def signConvention_cov_2D_CSC(cov, endcap, disk, ring, sector):
  xx=0; xy=1; xz=2; xphix=3; xphiy=4; xphiz=5; yx=6; yy=7; yz=8; yphix=9; yphiy=10; yphiz=11; zx=12; zy=13; zz=14; zphix=15; zphiy=16; zphiz=17;
  phixx=18; phixy=19; phixz=20; phixphix=21; phixphiy=22; phixphiz=23; phiyx=24; phiyy=25; phiyz=26; phiyphix=27; phiyphiy=28; phiyphiz=29; phizx=30; phizy=31; phizz=32; phizphix=33; phizphiy=34; phizphiz=35;
  cov_signConv = initCovMatrix()
  index = 0
  for indeX in range(6):
      for indeY in range(6):
          sign = 1;
          if(index==xx):       sign = signConventions["CSC",endcap, disk, ring, sector][0]*signConventions["CSC",endcap, disk, ring, sector][0]
          if(index==xy):       sign = signConventions["CSC",endcap, disk, ring, sector][0]*signConventions["CSC",endcap, disk, ring, sector][1]
          if(index==xz):       sign = signConventions["CSC",endcap, disk, ring, sector][0]*signConventions["CSC",endcap, disk, ring, sector][2]
          if(index==xphix):    sign = signConventions["CSC",endcap, disk, ring, sector][0]*signConventions["CSC",endcap, disk, ring, sector][0]
          if(index==xphiy):    sign = signConventions["CSC",endcap, disk, ring, sector][0]*signConventions["CSC",endcap, disk, ring, sector][1]
          if(index==xphiz):    sign = signConventions["CSC",endcap, disk, ring, sector][0]*signConventions["CSC",endcap, disk, ring, sector][2]
          if(index==yx):       sign = signConventions["CSC",endcap, disk, ring, sector][1]*signConventions["CSC",endcap, disk, ring, sector][0]
          if(index==yy):       sign = signConventions["CSC",endcap, disk, ring, sector][1]*signConventions["CSC",endcap, disk, ring, sector][1]
          if(index==yz):       sign = signConventions["CSC",endcap, disk, ring, sector][1]*signConventions["CSC",endcap, disk, ring, sector][2]
          if(index==yphix):    sign = signConventions["CSC",endcap, disk, ring, sector][1]*signConventions["CSC",endcap, disk, ring, sector][0]
          if(index==yphiy):    sign = signConventions["CSC",endcap, disk, ring, sector][1]*signConventions["CSC",endcap, disk, ring, sector][1]
          if(index==yphiz):    sign = signConventions["CSC",endcap, disk, ring, sector][1]*signConventions["CSC",endcap, disk, ring, sector][2]
          if(index==zx):       sign = signConventions["CSC",endcap, disk, ring, sector][2]*signConventions["CSC",endcap, disk, ring, sector][0]
          if(index==zy):       sign = signConventions["CSC",endcap, disk, ring, sector][2]*signConventions["CSC",endcap, disk, ring, sector][1]
          if(index==zz):       sign = signConventions["CSC",endcap, disk, ring, sector][2]*signConventions["CSC",endcap, disk, ring, sector][2]
          if(index==zphix):    sign = signConventions["CSC",endcap, disk, ring, sector][2]*signConventions["CSC",endcap, disk, ring, sector][0]
          if(index==zphiy):    sign = signConventions["CSC",endcap, disk, ring, sector][2]*signConventions["CSC",endcap, disk, ring, sector][1]
          if(index==zphiz):    sign = signConventions["CSC",endcap, disk, ring, sector][2]*signConventions["CSC",endcap, disk, ring, sector][2]
          if(index==phixx):    sign = signConventions["CSC",endcap, disk, ring, sector][0]*signConventions["CSC",endcap, disk, ring, sector][0]
          if(index==phixy):    sign = signConventions["CSC",endcap, disk, ring, sector][0]*signConventions["CSC",endcap, disk, ring, sector][1]
          if(index==phixz):    sign = signConventions["CSC",endcap, disk, ring, sector][0]*signConventions["CSC",endcap, disk, ring, sector][2]
          if(index==phixphix): sign = signConventions["CSC",endcap, disk, ring, sector][0]*signConventions["CSC",endcap, disk, ring, sector][0]
          if(index==phixphiy): sign = signConventions["CSC",endcap, disk, ring, sector][0]*signConventions["CSC",endcap, disk, ring, sector][1]
          if(index==phixphiz): sign = signConventions["CSC",endcap, disk, ring, sector][0]*signConventions["CSC",endcap, disk, ring, sector][2]
          if(index==phiyx):    sign = signConventions["CSC",endcap, disk, ring, sector][1]*signConventions["CSC",endcap, disk, ring, sector][0]
          if(index==phiyy):    sign = signConventions["CSC",endcap, disk, ring, sector][1]*signConventions["CSC",endcap, disk, ring, sector][1]
          if(index==phiyz):    sign = signConventions["CSC",endcap, disk, ring, sector][1]*signConventions["CSC",endcap, disk, ring, sector][2]
          if(index==phiyphix): sign = signConventions["CSC",endcap, disk, ring, sector][1]*signConventions["CSC",endcap, disk, ring, sector][0]
          if(index==phiyphiy): sign = signConventions["CSC",endcap, disk, ring, sector][1]*signConventions["CSC",endcap, disk, ring, sector][1]
          if(index==phiyphiz): sign = signConventions["CSC",endcap, disk, ring, sector][1]*signConventions["CSC",endcap, disk, ring, sector][2]
          if(index==phizx):    sign = signConventions["CSC",endcap, disk, ring, sector][2]*signConventions["CSC",endcap, disk, ring, sector][0]
          if(index==phizy):    sign = signConventions["CSC",endcap, disk, ring, sector][2]*signConventions["CSC",endcap, disk, ring, sector][1]
          if(index==phizz):    sign = signConventions["CSC",endcap, disk, ring, sector][2]*signConventions["CSC",endcap, disk, ring, sector][2]
          if(index==phizphix): sign = signConventions["CSC",endcap, disk, ring, sector][2]*signConventions["CSC",endcap, disk, ring, sector][0]
          if(index==phizphiy): sign = signConventions["CSC",endcap, disk, ring, sector][2]*signConventions["CSC",endcap, disk, ring, sector][1]
          if(index==phizphiz): sign = signConventions["CSC",endcap, disk, ring, sector][2]*signConventions["CSC",endcap, disk, ring, sector][2]
          cov_signConv[indeX][indeY] = cov[indeX][indeY]*sign
          index = index+1
  return np.ndarray(shape=(6,6), dtype=float, buffer=np.array(cov_signConv))

def signConvention_cov_2D_CSC_DIM3(cov, endcap, disk, ring, sector, isAligned):
  if(isAligned!="Aligned" and isAligned!="NotAligned"): 
    print( "WARNING: signConvention_cov_2D_CSC_DIM3 has a wrong isAligned argument")
    sys.exit()
  xx=0; xy=1; xphiz=2; yx=3; yy=4; yphiz=5; phizx=6; phizy=7; phizphiz=8;
  if(isAligned=="NotAligned"):
    zz=0; zphix=1; zphiy=2; phixz=3; phixphix=4; phixphiy=5; phiyz=6; phiyphix=7; phiyphiy=8;
  cov_signConv = [[]]; cov_signConv = [[0 for i in range(3)] for i in range(3)]
  index = 0
  for indeX in range(3):
      for indeY in range(3):
          sign = 1;
          if(isAligned=="Aligned"):
            if(index==xx):       sign = signConventions["CSC",endcap, disk, ring, sector][0]*signConventions["CSC",endcap, disk, ring, sector][0]
            if(index==xy):       sign = signConventions["CSC",endcap, disk, ring, sector][0]*signConventions["CSC",endcap, disk, ring, sector][1]
            if(index==xphiz):    sign = signConventions["CSC",endcap, disk, ring, sector][0]*signConventions["CSC",endcap, disk, ring, sector][2]
            if(index==yx):       sign = signConventions["CSC",endcap, disk, ring, sector][1]*signConventions["CSC",endcap, disk, ring, sector][0]
            if(index==yy):       sign = signConventions["CSC",endcap, disk, ring, sector][1]*signConventions["CSC",endcap, disk, ring, sector][1]
            if(index==yphiz):    sign = signConventions["CSC",endcap, disk, ring, sector][1]*signConventions["CSC",endcap, disk, ring, sector][2]
            if(index==phizx):    sign = signConventions["CSC",endcap, disk, ring, sector][2]*signConventions["CSC",endcap, disk, ring, sector][0]
            if(index==phizy):    sign = signConventions["CSC",endcap, disk, ring, sector][2]*signConventions["CSC",endcap, disk, ring, sector][1]
            if(index==phizphiz): sign = signConventions["CSC",endcap, disk, ring, sector][2]*signConventions["CSC",endcap, disk, ring, sector][2]
          if(isAligned=="NotAligned"):
            if(index==zz):       sign = signConventions["CSC",endcap, disk, ring, sector][2]*signConventions["CSC",endcap, disk, ring, sector][2]
            if(index==zphix):    sign = signConventions["CSC",endcap, disk, ring, sector][2]*signConventions["CSC",endcap, disk, ring, sector][0]
            if(index==zphiy):    sign = signConventions["CSC",endcap, disk, ring, sector][2]*signConventions["CSC",endcap, disk, ring, sector][1]
            if(index==phixz):    sign = signConventions["CSC",endcap, disk, ring, sector][0]*signConventions["CSC",endcap, disk, ring, sector][2]
            if(index==phixphix): sign = signConventions["CSC",endcap, disk, ring, sector][0]*signConventions["CSC",endcap, disk, ring, sector][0]
            if(index==phixphiy): sign = signConventions["CSC",endcap, disk, ring, sector][0]*signConventions["CSC",endcap, disk, ring, sector][1]
            if(index==phiyz):    sign = signConventions["CSC",endcap, disk, ring, sector][1]*signConventions["CSC",endcap, disk, ring, sector][2]
            if(index==phiyphix): sign = signConventions["CSC",endcap, disk, ring, sector][1]*signConventions["CSC",endcap, disk, ring, sector][0]
            if(index==phiyphiy): sign = signConventions["CSC",endcap, disk, ring, sector][1]*signConventions["CSC",endcap, disk, ring, sector][1]
          cov_signConv[indeX][indeY] = cov[indeX][indeY]*sign
          index = index+1
  return np.ndarray(shape=(3,3), dtype=float, buffer=np.array(cov_signConv))



# From https://cms-mual.web.cern.ch/cms-mual/tmp/mc_CSC-1100-110001_CMSSW_8_0_24_GTasym_45M_8TeV_misall_03/
def GetZ_CSC(endcap,disk,ring):
  if(endcap==1):
    if( disk==1 and (ring==1 or ring==4)): sigma = 2./10
    elif( disk==1 and ring==2):            sigma = 2./10
    elif( disk==1 and ring==3):            sigma = 2.1/10
    elif( disk==2 and ring==1):            sigma = 1./10
    elif( disk==2 and ring==2):            sigma = 1.9/10
    elif( disk==3 and ring==1):            sigma = 1.6/10
    elif( disk==3 and ring==2):            sigma = 1.5/10
    elif( disk==4 and ring==1):            sigma = 1.1/10
    elif( disk==4 and ring==2):            sigma = 2./10
    else: print( "WARNING!!!!! No chamber found in GetZ_CSC."); return -1.
    return sigma/2.
  elif(endcap==2):
    if( disk==1 and (ring==1 or ring==4)): sigma = 1.4/10
    elif( disk==1 and ring==2):            sigma = 1.9/10
    elif( disk==1 and ring==3):            sigma = 1.8/10
    elif( disk==2 and ring==1):            sigma = 1.7/10
    elif( disk==2 and ring==2):            sigma = 2.1/10
    elif( disk==3 and ring==1):            sigma = 1.8/10
    elif( disk==3 and ring==2):            sigma = 1.5/10
    elif( disk==4 and ring==1):            sigma = 1.9/10
    elif( disk==4 and ring==2):            sigma = 2.1/10
    else: print( "WARNING!!!!! No chamber found in GetZ_CSC."); return -1.
    return sigma/2.
  else: print( "WARNING!!!!! No chamber found in GetZ_CSC."); return -1.


def GetPhiX_CSC(endcap,disk,ring):
  if(endcap==1):
    if( disk==1 and (ring==1 or ring==4)): sigma = 0.96/1000
    elif( disk==1 and ring==2):            sigma = 1.1/1000
    elif( disk==1 and ring==3):            sigma = 1.4/1000
    elif( disk==2 and ring==1):            sigma = 0.57/1000
    elif( disk==2 and ring==2):            sigma = 0.78/1000
    elif( disk==3 and ring==1):            sigma = 0.36/1000
    elif( disk==3 and ring==2):            sigma = 0.81/1000
    elif( disk==4 and ring==1):            sigma = 1.1/1000
    elif( disk==4 and ring==2):            sigma = 1.2/1000
    else: print( "WARNING!!!!! No chamber found in GetPhiX_CSC."); return -1.
    return sigma/2.
  elif(endcap==2):
    if( disk==1 and (ring==1 or ring==4)): sigma = 0.66/1000
    elif( disk==1 and ring==2):            sigma = 1.2/1000
    elif( disk==1 and ring==3):            sigma = 0.87/1000
    elif( disk==2 and ring==1):            sigma = 0.58/1000
    elif( disk==2 and ring==2):            sigma = 0.92/1000
    elif( disk==3 and ring==1):            sigma = 0.63/1000
    elif( disk==3 and ring==2):            sigma = 1.2/1000
    elif( disk==4 and ring==1):            sigma = 0.86/1000
    elif( disk==4 and ring==2):            sigma = 1.1/1000
    else: print( "WARNING!!!!! No chamber found in GetPhiX_CSC."); return -1.
    return sigma/2.
  else: print( "WARNING!!!!! No chamber found in GetZ_CSC."); return -1.

def GetPhiY_CSC(endcap,disk,ring):
  if(endcap==1):
    if( disk==1 and (ring==1 or ring==4)): sigma = 0.85/1000
    elif( disk==1 and ring==2):            sigma = 0.80/1000
    elif( disk==1 and ring==3):            sigma = 1.1/1000
    elif( disk==2 and ring==1):            sigma = 0.78/1000
    elif( disk==2 and ring==2):            sigma = 0.95/1000
    elif( disk==3 and ring==1):            sigma = 0.96/1000
    elif( disk==3 and ring==2):            sigma = 1.24/1000
    elif( disk==4 and ring==1):            sigma = 1.1/1000
    elif( disk==4 and ring==2):            sigma = 0.97/1000
    else: print( "WARNING!!!!! No chamber found in GetPhiY_CSC."); return -1.
    return sigma/2.
  elif(endcap==2):
    if( disk==1 and (ring==1 or ring==4)): sigma = 0.59/1000
    elif( disk==1 and ring==2):            sigma = 1.2/1000
    elif( disk==1 and ring==3):            sigma = 0.87/1000
    elif( disk==2 and ring==1):            sigma = 1.49/1000
    elif( disk==2 and ring==2):            sigma = 0.88/1000
    elif( disk==3 and ring==1):            sigma = 0.7/1000
    elif( disk==3 and ring==2):            sigma = 1.196/1000
    elif( disk==4 and ring==1):            sigma = 0.956/1000
    elif( disk==4 and ring==2):            sigma = 0.864/1000
    else: print( "WARNING!!!!! No chamber found in GetPhiY_CSC."); return -1.
    return sigma/2.
  else: print( "WARNING!!!!! No chamber found in GetZ_CSC."); return -1.
