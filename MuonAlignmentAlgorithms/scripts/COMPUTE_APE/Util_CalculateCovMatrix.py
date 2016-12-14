def initCovMatrix( elements = 0 ):
  cov = [[]]
  cov = [[elements for i in xrange(6)] for i in xrange(6)]
  return cov

def calculateCovMatrix(M):
  mu = calculateMean(M)
  cov = initCovMatrix()
  #print "Initial covariance matrix:"
  #printCovMatrix(cov)
  index=0
  for i in range(6):
    for j in range(6):
      cov[i][j] = mu[index]
      index=index+1
  N = len(M)
  for i in xrange(6):
    for j in xrange(6):
      for n in range(N):
        if M[n] != None:
          cov[i][j] = cov[i][j] + ( M[n][i*6] - mu[i*6] ) * ( M[n][j*6] - mu[j*6] )
  for i in range(6):
    for j in range(6):
      cov[i][j] = cov[i][j]/(N-1)
  #print "Covariance matrix:"
  #printCovMatrix(cov)
  print "Sqrt from covariance matrix"
  printSqrtCovMatrix(cov)
  return cov

def calculateCovStatMatrix(M):
  mu = calculateMean(M)
  cov = initCovMatrix()
  #print "Initial stat covariance matrix:"
  #printCovMatrix(cov)
  index=0
  for i in range(6):
    for j in range(6):
      cov[i][j] = mu[index]
      index=index+1
  #print "Stat covariance matrix:"
  #printCovMatrix(cov)
  print "Sqrt from stat covariance matrix"
  printSqrtCovMatrix(cov)
  
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
  N = len(M)
  for n in range(N):
    for i in range(36):
      if M[n] != None : mu[i] = mu[i] + M[n][i]
  for i in range(36):
    mu[i] = mu[i]/N
  #print "Means:"
  #printMean(mu)
  return mu

def printMean(mu):
  for i in range(len(mu)):
    print ('% 1.10f' % mu[i] )

def sumMatrix(cov1, cov2):
  cov = initCovMatrix()
  for i in range(6):
    for j in range(6):
      cov[i][j] = cov1[i][j] + cov2[i][j]
  
  return cov

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

