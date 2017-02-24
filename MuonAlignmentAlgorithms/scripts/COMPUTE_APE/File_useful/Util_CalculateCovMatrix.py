def initCovMatrix( elements = 0 ):
  cov = [[]]
  cov = [[elements for i in xrange(6)] for i in xrange(6)]
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
#  for i in xrange(6):
#    for j in xrange(6):
#      for n in range(N):
#        if M[n] != None:
#          cov[i][j] = cov[i][j] + ( M[n][i*6] - mu[i*6] ) * ( M[n][j*6] - mu[j*6] )
#  for i in range(6):
#    for j in range(6):
#      cov[i][j] = cov[i][j]/(N-1)
  print "Syst. Unc. matrix (squared, as the covariance):"
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
  print "Covariance matrix:"
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
      print "Sec: ", index+1, " , len: ", len(n), ") ",
      for i in range(len(n)):    # Covariance matrix has 36 elements[xx,xy,xz...], while difference between geoemtries only fiagonal ones (6)
        print ('% 1.10f' % M[index][i] ),
    else:
      print n, ": Not valid"
    index=index+1
    print

def printCovMatrix(cov):
  for i in range(6):
    for j in range(6):
      print ('% 1.10f' % cov[i][j]),
    print

def printSqrtCovMatrix(cov):
  for i in range(6):
    for j in range(6):
      print ('% 1.10f' % sqrt( abs( cov[i][j] ) ) ),
    print

def calculateMean(M):
  mu = [0 for i in xrange(36)]
  N = len(M) #All sectors
  for n in range(N):
    for i in range(36):
      if M[n] != None : mu[i] = mu[i] + M[n][i]
  for i in range(36):
    mu[i] = mu[i]/N
  #print "Means:"
  #printMean(mu)
  return mu

#sd=sqrt(SUM[(xi-mu)^2]/N)
def calculateSD(M,mu):
  sd = [0 for i in xrange(36)]
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
        if(rho_cov-rho_totUnc>0.00000000001): print "WARNING: corrlation is different. ",i,j,") ",rho_cov,rho_totUnc

def calculateCrosCovMatrix(M1, M2):
  
  N1 = len(M1)
  N2 = len(M2)
  if N1 != N2 :
    print "calculateCrosCovMatrix: Error! Matrixes with different dimensions"
    return
  
  mu1 = calculateMean(M1)
  mu2 = calculateMean(M2)
  
  cov12 = initCovMatrix()
  
  for i in xrange(6):
    for j in xrange(6):
      for n in range(N1):
        if M1[n] != None and M2[n] != None : cov12[i][j] = cov12[i][j] + ( M1[n][i] - mu1[i] ) * ( M2[n][j] - mu2[j] )
  
  cov21 = initCovMatrix()
  
  for i in xrange(6):
    for j in xrange(6):
      for n in range(N1):
        if M1[n] != None and M2[n] != None : cov21[i][j] = cov21[i][j] + ( M1[n][j] - mu1[j] ) * ( M2[n][i] - mu2[i] )
  
  for i in range(6):
    for j in range(6):
      cov12[i][j] = cov12[i][j]/(N1-1)
      cov21[i][j] = cov21[i][j]/(N1-1)
  
  print "Covariance matrix cov12:"
  printCovMatrix(cov12)
  print "Covariance matrix cov21:"
  printCovMatrix(cov21)
  
  crossCov = sumMatrix( cov12, cov21 )
  print "Cross-covariance matrix cov12+cov21:"
  printCovMatrix(crossCov)
  
  return crossCov

#Function to check if the covariance matrix is invertible (i.e. not singular)
def is_invertible(a):
  return a.shape[0] == a.shape[1] and np.linalg.matrix_rank(a) == a.shape[0]
