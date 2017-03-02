import ROOT, array, os, sys, re, math, random
import numpy
from math import *
sys.path.append('./File_useful/')
execfile("File_useful/geometryXMLparser.py")
execfile("File_useful/plotscripts.py")
execfile("File_useful/Util_CalculateCovMatrix.py")
# All units are in cm and cm^2 here
xmlfileORI        = "Geom/mc_DT-1100-111111_CMSSW_8_0_24_GTasym_45M_8TeV_misall_03.xml"
xmlfileCOMP       = "Geom/mc_DT-1100-111111_CMSSW_8_0_24_GTasym_45M_8TeV_misall_03.xml"
reportfile        = "Geom/mc_DT-1100-111111_CMSSW_8_0_24_GTasym_45M_8TeV_misall_03_report.py"
xmlfileIdealGeom  = "Geom/muonGeometry_IDEAL_AllZeroes.Ape6x6.StdTags.746p3.DBv2.xml"
outName = "_6DOF_MCfromHW"
is3DOF=False # This modify the extraction of the covariance elements, since covariance matrix will be different
execfile(reportfile)
report = reports
g1 = MuonGeometry(xmlfileORI)
g2 = MuonGeometry(xmlfileCOMP)
gI = MuonGeometry(xmlfileIdealGeom)
debug=False

# Covariance from Final-Ideal geoemtry
# init
cov_fromH = [];
position = []; rotation = []
cov_xx = []; cov_xy = []; cov_xz = []; cov_xphix = []; cov_xphiy = []; cov_xphiz = []; cov_yy = []; cov_yz = []; cov_yphix = []; cov_yphiy = []; cov_yphiz = []; cov_zz = []; cov_zphix = []; cov_zphiy = []; cov_zphiz = []; cov_phixphix = []; cov_phixphiy = []; cov_phixphiz = []; cov_phiyphiy = []; cov_phiyphiz = []; cov_phizphiz = [];
for wheel in -2, -1, 0, +1, +2:
  cov_fromH.append([]);
  position.append([]); rotation.append([]);
  cov_xx.append([]);  cov_xy.append([]); cov_xz.append([]); cov_xphix.append([]); cov_xphiy.append([]); cov_xphiz.append([]); cov_yy.append([]); cov_yz.append([]); cov_yphix.append([]); cov_yphiy.append([]); cov_yphiz.append([]); cov_zz.append([]); cov_zphix.append([]); cov_zphiy.append([]); cov_zphiz.append([]); cov_phixphix.append([]); cov_phixphiy.append([]); cov_phixphiz.append([]); cov_phiyphiy.append([]); cov_phiyphiz.append([]); cov_phizphiz.append([]);
  for station in 1, 2, 3, 4:
    cov_fromH[wheel+2].append(None);
    position[wheel+2].append(None); rotation[wheel+2].append(None);
    cov_xx[wheel+2].append(None);  cov_xy[wheel+2].append(None); cov_xz[wheel+2].append(None); cov_xphix[wheel+2].append(None); cov_xphiy[wheel+2].append(None); cov_xphiz[wheel+2].append(None); cov_yy[wheel+2].append(None); cov_yz[wheel+2].append(None); cov_yphix[wheel+2].append(None); cov_yphiy[wheel+2].append(None); cov_yphiz[wheel+2].append(None); cov_zz[wheel+2].append(None); cov_zphix[wheel+2].append(None); cov_zphiy[wheel+2].append(None); cov_zphiz[wheel+2].append(None); cov_phixphix[wheel+2].append(None); cov_phixphiy[wheel+2].append(None); cov_phixphiz[wheel+2].append(None); cov_phiyphiy[wheel+2].append(None); cov_phiyphiz[wheel+2].append(None); cov_phizphiz[wheel+2].append(None);
# Computation
for wheel in (-2, -1, 0, 1, 2):
  for station in (1, 2, 3, 4):
    varx = []; vary = []; varz = []; varphix = []; varphiy = []; varphiz = [];
    null = 0
    cov_f = [[]]; cov_f = [[null for i in xrange(6)] for i in xrange(6)]
    cov_sim = [[]]; cov_sim = [[null for i in xrange(6)] for i in xrange(6)]
    if station != 4: sectors = (1,2,3,4,5,6,7,8,9,10,11,12)
    else: sectors = (1,2,3,4,5,6,7,8,9,10,11,12,13,14)
    for sector in sectors:
      dx_cm = (g1.dt[wheel, station, sector].x - gI.dt[wheel, station, sector].x)*signConventions["DT", wheel, station, sector][0]
      dy_cm = (g1.dt[wheel, station, sector].y - gI.dt[wheel, station, sector].y)*signConventions["DT", wheel, station, sector][1]
      dz_cm = (g1.dt[wheel, station, sector].z - gI.dt[wheel, station, sector].z)*signConventions["DT", wheel, station, sector][2]
      dphix_rad = (g1.dt[wheel, station, sector].phix - gI.dt[wheel, station, sector].phix)
      dphiy_rad = (g1.dt[wheel, station, sector].phiy - gI.dt[wheel, station, sector].phiy)
      dphiz_rad = (g1.dt[wheel, station, sector].phiz - gI.dt[wheel, station, sector].phiz)
      varx.append(dx_cm); vary.append(dy_cm); varz.append(dz_cm); varphix.append(dphix_rad); varphiy.append(dphiy_rad); varphiz.append(dphiz_rad);
    #Compute convariance
    print "Chamber:", wheel, station
    All_vectors = numpy.vstack( (varx,vary,varz,varphix,varphiy,varphiz) )
    cov_f = numpy.cov(All_vectors)
    print cov_f
    cov_fromH[wheel+2][station-1] = cov_f
#Initialize
M_FIT = []
M_DIF = []
for wheel in -2, -1, 0, +1, +2:
  M_FIT.append([])
  M_DIF.append([])
  for station in 1, 2, 3, 4:
    M_FIT[wheel+2].append([])
    M_DIF[wheel+2].append([])
    if station != 4:
      for sector in 1,2,3,4,5,6,7,8,9,10,11,12:
        M_FIT[wheel+2][station-1].append(None)
        M_DIF[wheel+2][station-1].append(None)
    else:
      for sector in 1,2,3,4,5,6,7,8,9,10,11,12,13,14:
        M_FIT[wheel+2][station-1].append(None)
        M_DIF[wheel+2][station-1].append(None)

#For chamber that is an object described in the report file
NfitFailed=0
for r in report:
  index=1
  if ( r.postal_address[0] == "DT" and r.status == "PASS") :
      wheel   = r.postal_address[1]
      station = r.postal_address[2]
      sector  = r.postal_address[3]
      if(station==4 and (sector==10 or sector==14 or sector==4 or sector==13)):
        print "SKIPPING BAD SECTORS"
        continue
      if(debug): print "0)", wheel, station, sector
      # Extract the covariance matrix and place it in the list E_stat
      E_stat=[]
      Cov_M = r.CovMatrix
      for covItem in Cov_M:
        #STATION 1 2 3
        if ( station != 4 ): #In station 1,2,3 are 144 numbers, because there are 12 params, but we want the fisr six (three): xx, xy, xz, xphix, xphiy, xphiz, A, B, 0, 0, 0, 0; yx, yy, yz... (xx, xy, xphiz, xA, xB, 0, 0, 0, 0, 0, 0, 0, yx, yy...)
          #3DOF
          if(is3DOF):
            if( index==25 ):
              E_stat.append(float(0)); E_stat.append(float(0)); E_stat.append(float(0)); E_stat.append(float(0)); E_stat.append(float(0)); E_stat.append(float(0)); #add a raw of 0
              E_stat.append(float(0)); E_stat.append(float(0)); E_stat.append(float(0)); E_stat.append(float(0)); E_stat.append(float(0)); E_stat.append(float(0));
              E_stat.append(float(0)); E_stat.append(float(0)); E_stat.append(float(0)); E_stat.append(float(0)); E_stat.append(float(0)); E_stat.append(float(0));
            if( index==1 or index==2 or index==13 or index==14 or index==25 or index==26 ):
              E_stat.append(float(covItem))
            if( index==3 or index==15 or index==27 ):
              E_stat.append(float(0)); E_stat.append(float(0)); E_stat.append(float(0)); E_stat.append(float(covItem));  # add 0 to Y component that is not there
          #6DOF
          else:
            if( (index>0 and index<7) or (index>12 and index<19) or (index>24 and index<31) or (index>36 and index<43) or (index>48 and index<(6*9+1)) or (index>60 and index<(6*11+1)) ):
              E_stat.append(float(covItem)) 
        #STATION 4
        else:                 #In station 4 there are 64 numbers, because there are 8 params, but we want the first five (two): xx, xz, xphix, xphiy, xphiz, A, 0, 0; zx, zz, zphix... (xx, xphiz, xA, 0, 0, 0, 0, 0, phizx, phizphiz...)
          #3DOF
          if(is3DOF):
            if( index==1 or index==9 ):
              E_stat.append(float(covItem))
            if( index==2 or index==10 ): 
              E_stat.append(float(0)); E_stat.append(float(0)); E_stat.append(float(0)); E_stat.append(float(0)); E_stat.append(float(covItem));  # add 0 to Y component that is not there
            if( index==3 ):
              E_stat.append(float(0)); E_stat.append(float(0)); E_stat.append(float(0)); E_stat.append(float(0)); E_stat.append(float(0)); E_stat.append(float(0)); #add a raw of 0
              E_stat.append(float(0)); E_stat.append(float(0)); E_stat.append(float(0)); E_stat.append(float(0)); E_stat.append(float(0)); E_stat.append(float(0));
              E_stat.append(float(0)); E_stat.append(float(0)); E_stat.append(float(0)); E_stat.append(float(0)); E_stat.append(float(0)); E_stat.append(float(0));
              E_stat.append(float(0)); E_stat.append(float(0)); E_stat.append(float(0)); E_stat.append(float(0)); E_stat.append(float(0)); E_stat.append(float(0));          
          #6DOF
          else:
            if( index==2 or index==10 or index==18 or index==26 or index==34 ):
              E_stat.append(float(0)) # add 0 to Y component that is not there
            if( index==8 ):
              E_stat.append(float(0)); E_stat.append(float(0)); E_stat.append(float(0)); E_stat.append(float(0)); E_stat.append(float(0)); E_stat.append(float(0)); #add a raw of 0
            if( (index>0 and index<6) or (index>8 and index<14) or (index>16 and index<22) or (index>24 and index<30) or (index>32 and index<38) ):#or (index>40 and index<46) or (index>48 and index<54) or (index>56 and index<62) or (index>64 and index<70) ) :
              E_stat.append(float(covItem)) # vector with 25 elements
        index=index+1
      if(debug): print "1)", len(E_stat), " -> ", E_stat
      # Differece with another geometry (representing diagonal syst. error only if integrated luminosity is high)
      # You now are making a diagonal 6x6 matrix
      D_SL = []
      d12x_cm = (g1.dt[wheel, station, sector].x - g2.dt[wheel, station, sector].x)*signConventions["DT", wheel, station, sector][0]
      D_SL.append(d12x_cm); D_SL.append(0); D_SL.append(0); D_SL.append(0); D_SL.append(0); D_SL.append(0); 
      if ( station != 4 ) : d12y_cm = (g1.dt[wheel, station, sector].y - g2.dt[wheel, station, sector].y)*signConventions["DT", wheel, station, sector][1]
      else :                d12y_cm = 0.0
      D_SL.append(0); D_SL.append(d12y_cm); D_SL.append(0); D_SL.append(0); D_SL.append(0); D_SL.append(0); 
      d12z_cm = (g1.dt[wheel, station, sector].z - g2.dt[wheel, station, sector].z)*signConventions["DT", wheel, station, sector][2]
      D_SL.append(0); D_SL.append(0); D_SL.append(d12z_cm); D_SL.append(0); D_SL.append(0); D_SL.append(0); 
      d12phix_rad = (g1.dt[wheel, station, sector].phix - g2.dt[wheel, station, sector].phix)
      D_SL.append(0); D_SL.append(0); D_SL.append(0); D_SL.append(d12phix_rad); D_SL.append(0); D_SL.append(0); 
      d12phiy_rad = (g1.dt[wheel, station, sector].phiy - g2.dt[wheel, station, sector].phiy)
      D_SL.append(0); D_SL.append(0); D_SL.append(0); D_SL.append(0); D_SL.append(d12phiy_rad); D_SL.append(0); 
      d12phiz_rad = (g1.dt[wheel, station, sector].phiz - g2.dt[wheel, station, sector].phiz)
      D_SL.append(0); D_SL.append(0); D_SL.append(0); D_SL.append(0); D_SL.append(0); D_SL.append(d12phiz_rad)
      if(debug): print "2)", len(D_SL), " -> ", D_SL
      # Save final quantities in a map that for each chamber has a 6x6 matrix
      M_FIT[wheel+2][station-1][sector-1] = E_stat
      M_DIF[wheel+2][station-1][sector-1] = D_SL
  if ( r.postal_address[0] == "DT" and r.status != "PASS") :
    wheel   = r.postal_address[1]
    station = r.postal_address[2]
    sector  = r.postal_address[3]
    NfitFailed=NfitFailed+1
    m_null = []
    for iN in range(36): m_null.append(0)
    M_FIT[wheel+2][station-1][sector-1] = m_null
    M_DIF[wheel+2][station-1][sector-1] = m_null
#Now we have the Covariance matrix (stat. only) and the diff. between 2 geometries (syst only is there is high integrated luminosity)
#Covariance matrix give us: sigma_x(stat), sigma_y(stat)... and off-diagonal terms sigma_xy(stat), sigma_xz(stat)...
#Off-diagonal terms can be written in term of correlation: rho_xy, rho_xz... where rho_xy=sigma_xy(stat)/(sigma_x(stat)*sigma_y(stat))
#Since total error will be sigma_x = sqrt(sigma_x(stat)^2+sigma_x(syst)^2)
#We can write the final matrix fro APE as: sigma_x, sigma_y... and the off-diagonal terms as rho_xy*sigma_x*sigma_y... (where rho is taken from cov. matrix)
covTot = []
cov_only = []
cov_only_times2 = []
cov_only_all = []
for wheel in -2, -1, 0, +1, +2:
  covTot.append([])
  cov_only.append([])
  cov_only_times2.append([])
  cov_only_all.append([])
  for station in 1, 2, 3, 4:
    covTot[wheel+2].append(None)
    cov_only[wheel+2].append(None)
    cov_only_times2[wheel+2].append(None)
    cov_only_all[wheel+2].append([])
    sectors=12
    if(station==4): sectors=14
    for sector in range(sectors):
      cov_only_all[wheel+2][station-1].append(None)

for wheel in -2, -1, 0, +1, +2:
  for station in 1, 2, 3, 4:
    print "\n********************************************************************"
    print "Group of chambers: wheel = %s, station = %s" % (wheel, station)
    print "********************************************************************"
    #Covariance averaging same wheel/station
    print "Covariance matrix Matrix for wheel = %s, station = %s" % (wheel, station)
    cov_FIT = calculateCovStatMatrix( M_FIT[wheel+2][station-1] )
    cov_only[wheel+2][station-1] = cov_FIT #In case you want to use only the cov. matrix
    #Covariance in case you want a different APE per chamber
    sectors=12
    if(station==4): sectors=14
    for sector in range(sectors):
      matrix = None
      if(station==4 and (sector+1==4 or sector+1==10 or sector+1==13 or sector+1==14)): matrix = cov_FIT
      else: matrix = calculateCovStatMatrix_noAverage(M_FIT[wheel+2][station-1][sector])
      cov_only_all[wheel+2][station-1][sector] = matrix
    #Covariance times 2
    cov_only_times2[wheel+2][station-1] = calculateCovStatMatrix_times2( M_FIT[wheel+2][station-1] )
    #Difference among geometries
    cov_DIF = calculateSystMatrix( M_DIF[wheel+2][station-1] )
    #Now Sum Them:
    covTot[wheel+2][station-1] = sumCov_Syst_matrix(cov_FIT, cov_DIF) 
    print "Total covariance matrix for wheel = %s, station = %s" % (wheel, station)
    printCovMatrix( covTot[wheel+2][station-1] )        
    #Test that correlation is the same in covariance matrix and in covTot
    testCorrelation(cov_FIT, covTot[wheel+2][station-1])

#Print APE with only Covariance matrix
f_cov_APEsXml = open('APEs_COV_DT_Data_AllContributions_AllTypesOfApes' + outName + '.xml','w')
#Print APE with only Covariance matrix times 2
f_cov_APEs_t2Xml = open('APEs_COV_t2_DT_Data_AllContributions_AllTypesOfApes' + outName + '.xml','w')
#Print APE with only Covariance matrix not averaging per sector
f_cov_APEs_allXml = open('APEs_COVall_DT_Data_AllContributions_AllTypesOfApes' + outName + '.xml','w')
#Print APE total
f_AllAPEsXml = open('APEs_DT_Data_AllContributions_AllTypesOfApes' + outName + '.xml','w')
#Print APE total, but only "diagonal elements"
f_DE_AllAPEsXml = open('APEs_DE_DT_Data_AllContributions_AllTypesOfApes' + outName + '.xml','w')
#print APE from Covariance matrix from histograms
f_cov_fromHistXml = open('APEs_COVfromH_DT_Data_AllContributions_AllTypesOfApes' + outName + '.xml','w')

f_cov_APEsXml.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n")
f_cov_APEsXml.write("<?xml-stylesheet type=\"text/xml\" href=\"MuonAlignment.xsl\"?>\n")
f_cov_APEsXml.write("<MuonAlignment>\n\n")

f_cov_APEs_t2Xml.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n")
f_cov_APEs_t2Xml.write("<?xml-stylesheet type=\"text/xml\" href=\"MuonAlignment.xsl\"?>\n")
f_cov_APEs_t2Xml.write("<MuonAlignment>\n\n")

f_cov_APEs_allXml.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n")
f_cov_APEs_allXml.write("<?xml-stylesheet type=\"text/xml\" href=\"MuonAlignment.xsl\"?>\n")
f_cov_APEs_allXml.write("<MuonAlignment>\n\n")

f_AllAPEsXml.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n")
f_AllAPEsXml.write("<?xml-stylesheet type=\"text/xml\" href=\"MuonAlignment.xsl\"?>\n")
f_AllAPEsXml.write("<MuonAlignment>\n\n")

f_DE_AllAPEsXml.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n")
f_DE_AllAPEsXml.write("<?xml-stylesheet type=\"text/xml\" href=\"MuonAlignment.xsl\"?>\n")
f_DE_AllAPEsXml.write("<MuonAlignment>\n\n")

f_cov_fromHistXml.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n")
f_cov_fromHistXml.write("<?xml-stylesheet type=\"text/xml\" href=\"MuonAlignment.xsl\"?>\n")
f_cov_fromHistXml.write("<MuonAlignment>\n\n")

for wheel in -2, -1, 0, +1, +2:
  for station in 1, 2, 3, 4:
    if station != 4: sectors = (1,2,3,4,5,6,7,8,9,10,11,12)
    else:            sectors = (1,2,3,4,5,6,7,8,9,10,11,12,13,14)
    for sector in sectors:
      #Covariance APE
      xx       = cov_only[wheel+2][station-1][0][0]
      xy       = cov_only[wheel+2][station-1][0][1]
      xz       = cov_only[wheel+2][station-1][0][2]
      yy       = cov_only[wheel+2][station-1][1][1]
      if(station==4): yy = 0.01
      yz       = cov_only[wheel+2][station-1][1][2]
      zz       = cov_only[wheel+2][station-1][2][2]
      xphix    = cov_only[wheel+2][station-1][0][3]
      xphiy    = cov_only[wheel+2][station-1][0][4]
      xphiz    = cov_only[wheel+2][station-1][0][5]
      yphix    = cov_only[wheel+2][station-1][1][3]
      yphiy    = cov_only[wheel+2][station-1][1][4]
      yphiz    = cov_only[wheel+2][station-1][1][5]
      zphix    = cov_only[wheel+2][station-1][2][3]
      zphiy    = cov_only[wheel+2][station-1][2][4]
      zphiz    = cov_only[wheel+2][station-1][2][5]
      phixphix = cov_only[wheel+2][station-1][3][3]
      phixphiy = cov_only[wheel+2][station-1][3][4]
      phixphiz = cov_only[wheel+2][station-1][3][5]
      phiyphiy = cov_only[wheel+2][station-1][4][4]
      phiyphiz = cov_only[wheel+2][station-1][4][5]
      phizphiz = cov_only[wheel+2][station-1][5][5]
      f_cov_APEsXml.write("<operation>\n")
      f_cov_APEsXml.write( "  <DTChamber wheel=\"%s\" station=\"%s\" sector=\"%s\" />\n" % (wheel, station, sector) )
      f_cov_APEsXml.write( "  <setape xx=\"%s\" xy=\"%s\" xz=\"%s\" yy=\"%s\" yz=\"%s\" zz=\"%s\" xa=\"%s\" xb=\"%s\" xc=\"%s\" ya=\"%s\" yb=\"%s\" yc=\"%s\" za=\"%s\" zb=\"%s\" zc=\"%s\" aa=\"%s\" ab=\"%s\" ac=\"%s\" bb=\"%s\" bc=\"%s\" cc=\"%s\" />\n" % (xx, xy, xz, yy, yz, zz, xphix, xphiy, xphiz, yphix, yphiy, yphiz, zphix, zphiy, zphiz, phixphix, phixphiy, phixphiz, phiyphiy, phiyphiz, phizphiz) )
      f_cov_APEsXml.write("</operation>\n\n")
      #Covariance APE times 2
      xx       = cov_only_times2[wheel+2][station-1][0][0]
      xy       = cov_only_times2[wheel+2][station-1][0][1]
      xz       = cov_only_times2[wheel+2][station-1][0][2]
      yy       = cov_only_times2[wheel+2][station-1][1][1]
      if(station==4): yy = 0.01
      yz       = cov_only_times2[wheel+2][station-1][1][2]
      zz       = cov_only_times2[wheel+2][station-1][2][2]
      xphix    = cov_only_times2[wheel+2][station-1][0][3]
      xphiy    = cov_only_times2[wheel+2][station-1][0][4]
      xphiz    = cov_only_times2[wheel+2][station-1][0][5]
      yphix    = cov_only_times2[wheel+2][station-1][1][3]
      yphiy    = cov_only_times2[wheel+2][station-1][1][4]
      yphiz    = cov_only_times2[wheel+2][station-1][1][5]
      zphix    = cov_only_times2[wheel+2][station-1][2][3]
      zphiy    = cov_only_times2[wheel+2][station-1][2][4]
      zphiz    = cov_only_times2[wheel+2][station-1][2][5]
      phixphix = cov_only_times2[wheel+2][station-1][3][3]
      phixphiy = cov_only_times2[wheel+2][station-1][3][4]
      phixphiz = cov_only_times2[wheel+2][station-1][3][5]
      phiyphiy = cov_only_times2[wheel+2][station-1][4][4]
      phiyphiz = cov_only_times2[wheel+2][station-1][4][5]
      phizphiz = cov_only_times2[wheel+2][station-1][5][5]
      f_cov_APEs_t2Xml.write("<operation>\n")
      f_cov_APEs_t2Xml.write( "  <DTChamber wheel=\"%s\" station=\"%s\" sector=\"%s\" />\n" % (wheel, station, sector) )
      f_cov_APEs_t2Xml.write( "  <setape xx=\"%s\" xy=\"%s\" xz=\"%s\" yy=\"%s\" yz=\"%s\" zz=\"%s\" xa=\"%s\" xb=\"%s\" xc=\"%s\" ya=\"%s\" yb=\"%s\" yc=\"%s\" za=\"%s\" zb=\"%s\" zc=\"%s\" aa=\"%s\" ab=\"%s\" ac=\"%s\" bb=\"%s\" bc=\"%s\" cc=\"%s\" />\n" % (xx, xy, xz, yy, yz, zz, xphix, xphiy, xphiz, yphix, yphiy, yphiz, zphix, zphiy, zphiz, phixphix, phixphiy, phixphiz, phiyphiy, phiyphiz, phizphiz) )
      f_cov_APEs_t2Xml.write("</operation>\n\n")
      #Covariance APE all different
      xx = cov_only_all[wheel+2][station-1][sector-1][0][0]
      xy = cov_only_all[wheel+2][station-1][sector-1][0][1]
      xz = cov_only_all[wheel+2][station-1][sector-1][0][2]
      yy = cov_only_all[wheel+2][station-1][sector-1][1][1]
      if(station==4): yy = 0.01
      yz = cov_only_all[wheel+2][station-1][sector-1][1][2]
      zz = cov_only_all[wheel+2][station-1][sector-1][2][2]
      xphix    = cov_only_all[wheel+2][station-1][sector-1][0][3]
      xphiy    = cov_only_all[wheel+2][station-1][sector-1][0][4]
      xphiz    = cov_only_all[wheel+2][station-1][sector-1][0][5]
      yphix    = cov_only_all[wheel+2][station-1][sector-1][1][3]
      yphiy    = cov_only_all[wheel+2][station-1][sector-1][1][4]
      yphiz    = cov_only_all[wheel+2][station-1][sector-1][1][5]
      zphix    = cov_only_all[wheel+2][station-1][sector-1][2][3]
      zphiy    = cov_only_all[wheel+2][station-1][sector-1][2][4]
      zphiz    = cov_only_all[wheel+2][station-1][sector-1][2][5]
      phixphix = cov_only_all[wheel+2][station-1][sector-1][3][3]
      phixphiy = cov_only_all[wheel+2][station-1][sector-1][3][4]
      phixphiz = cov_only_all[wheel+2][station-1][sector-1][3][5]
      phiyphiy = cov_only_all[wheel+2][station-1][sector-1][4][4]
      phiyphiz = cov_only_all[wheel+2][station-1][sector-1][4][5]
      phizphiz = cov_only_all[wheel+2][station-1][sector-1][5][5]
      f_cov_APEs_allXml.write("<operation>\n")
      f_cov_APEs_allXml.write( "  <DTChamber wheel=\"%s\" station=\"%s\" sector=\"%s\" />\n" % (wheel, station, sector) )
      f_cov_APEs_allXml.write( "  <setape xx=\"%s\" xy=\"%s\" xz=\"%s\" yy=\"%s\" yz=\"%s\" zz=\"%s\" xa=\"%s\" xb=\"%s\" xc=\"%s\" ya=\"%s\" yb=\"%s\" yc=\"%s\" za=\"%s\" zb=\"%s\" zc=\"%s\" aa=\"%s\" ab=\"%s\" ac=\"%s\" bb=\"%s\" bc=\"%s\" cc=\"%s\" />\n" % (xx, xy, xz, yy, yz, zz, xphix, xphiy, xphiz, yphix, yphiy, yphiz, zphix, zphiy, zphiz, phixphix, phixphiy, phixphiz, phiyphiy, phiyphiz, phizphiz) )
      f_cov_APEs_allXml.write("</operation>\n\n")
      #Total APE     
      xx       = covTot[wheel+2][station-1][0][0]
      xy       = covTot[wheel+2][station-1][0][1]
      xz       = covTot[wheel+2][station-1][0][2]
      yy       = covTot[wheel+2][station-1][1][1]
      yz       = covTot[wheel+2][station-1][1][2]
      zz       = covTot[wheel+2][station-1][2][2]
      xphix    = covTot[wheel+2][station-1][0][3]
      xphiy    = covTot[wheel+2][station-1][0][4]
      xphiz    = covTot[wheel+2][station-1][0][5]
      yphix    = covTot[wheel+2][station-1][1][3]
      yphiy    = covTot[wheel+2][station-1][1][4]
      yphiz    = covTot[wheel+2][station-1][1][5]
      zphix    = covTot[wheel+2][station-1][2][3]
      zphiy    = covTot[wheel+2][station-1][2][4]
      zphiz    = covTot[wheel+2][station-1][2][5]
      phixphix = covTot[wheel+2][station-1][3][3]
      phixphiy = covTot[wheel+2][station-1][3][4]
      phixphiz = covTot[wheel+2][station-1][3][5]
      phiyphiy = covTot[wheel+2][station-1][4][4]
      phiyphiz = covTot[wheel+2][station-1][4][5]
      phizphiz = covTot[wheel+2][station-1][5][5]
      f_AllAPEsXml.write("<operation>\n")
      f_AllAPEsXml.write( "  <DTChamber wheel=\"%s\" station=\"%s\" sector=\"%s\" />\n" % (wheel, station, sector) )
      f_AllAPEsXml.write( "  <setape xx=\"%s\" xy=\"%s\" xz=\"%s\" yy=\"%s\" yz=\"%s\" zz=\"%s\" xa=\"%s\" xb=\"%s\" xc=\"%s\" ya=\"%s\" yb=\"%s\" yc=\"%s\" za=\"%s\" zb=\"%s\" zc=\"%s\" aa=\"%s\" ab=\"%s\" ac=\"%s\" bb=\"%s\" bc=\"%s\" cc=\"%s\" />\n" % (xx, xy, xz, yy, yz, zz, xphix, xphiy, xphiz, yphix, yphiy, yphiz, zphix, zphiy, zphiz, phixphix, phixphiy, phixphiz, phiyphiy, phiyphiz, phizphiz) )
      f_AllAPEsXml.write("</operation>\n\n")
      #Total Diagonal APE
      xx = covTot[wheel+2][station-1][0][0]
      xy = 0.0
      xz = 0.0
      yy = covTot[wheel+2][station-1][1][1]
      yz = 0.0
      zz = covTot[wheel+2][station-1][2][2]
      xphix    = 0.0
      xphiy    = 0.0
      xphiz    = 0.0
      yphix    = 0.0
      yphiy    = 0.0
      yphiz    = 0.0
      zphix    = 0.0
      zphiy    = 0.0
      zphiz    = 0.0
      phixphix = covTot[wheel+2][station-1][3][3]
      phixphiy = 0.0
      phixphiz = 0.0
      phiyphiy = covTot[wheel+2][station-1][4][4]
      phiyphiz = 0.0
      phizphiz = covTot[wheel+2][station-1][5][5]    
      f_DE_AllAPEsXml.write("<operation>\n")
      f_DE_AllAPEsXml.write( "  <DTChamber wheel=\"%s\" station=\"%s\" sector=\"%s\" />\n" % (wheel, station, sector) )
      f_DE_AllAPEsXml.write( "  <setape xx=\"%s\" xy=\"%s\" xz=\"%s\" yy=\"%s\" yz=\"%s\" zz=\"%s\" xa=\"%s\" xb=\"%s\" xc=\"%s\" ya=\"%s\" yb=\"%s\" yc=\"%s\" za=\"%s\" zb=\"%s\" zc=\"%s\" aa=\"%s\" ab=\"%s\" ac=\"%s\" bb=\"%s\" bc=\"%s\" cc=\"%s\" />\n" % (xx, xy, xz, yy, yz, zz, xphix, xphiy, xphiz, yphix, yphiy, yphiz, zphix, zphiy, zphiz, phixphix, phixphiy, phixphiz, phiyphiy, phiyphiz, phizphiz) )
      f_DE_AllAPEsXml.write("</operation>\n\n")
      #From Histograms  
      xx       = cov_fromH[wheel+2][station-1][0][0]
      xy       = cov_fromH[wheel+2][station-1][0][1]
      xz       = cov_fromH[wheel+2][station-1][0][2]
      yy       = cov_fromH[wheel+2][station-1][1][1]
      yz       = cov_fromH[wheel+2][station-1][1][2]
      zz       = cov_fromH[wheel+2][station-1][2][2]
      xphix    = cov_fromH[wheel+2][station-1][0][3]
      xphiy    = cov_fromH[wheel+2][station-1][0][4]
      xphiz    = cov_fromH[wheel+2][station-1][0][5]
      yphix    = cov_fromH[wheel+2][station-1][1][3]
      yphiy    = cov_fromH[wheel+2][station-1][1][4]
      yphiz    = cov_fromH[wheel+2][station-1][1][5]
      zphix    = cov_fromH[wheel+2][station-1][2][3]
      zphiy    = cov_fromH[wheel+2][station-1][2][4]
      zphiz    = cov_fromH[wheel+2][station-1][2][5]
      phixphix = cov_fromH[wheel+2][station-1][3][3]
      phixphiy = cov_fromH[wheel+2][station-1][3][4]
      phixphiz = cov_fromH[wheel+2][station-1][3][5]
      phiyphiy = cov_fromH[wheel+2][station-1][4][4]
      phiyphiz = cov_fromH[wheel+2][station-1][4][5]
      phizphiz = cov_fromH[wheel+2][station-1][5][5]
      f_cov_fromHistXml.write("<operation>\n")
      f_cov_fromHistXml.write( "  <DTChamber wheel=\"%s\" station=\"%s\" sector=\"%s\" />\n" % (wheel, station, sector) )
      f_cov_fromHistXml.write( "  <setape xx=\"%s\" xy=\"%s\" xz=\"%s\" yy=\"%s\" yz=\"%s\" zz=\"%s\" xa=\"%s\" xb=\"%s\" xc=\"%s\" ya=\"%s\" yb=\"%s\" yc=\"%s\" za=\"%s\" zb=\"%s\" zc=\"%s\" aa=\"%s\" ab=\"%s\" ac=\"%s\" bb=\"%s\" bc=\"%s\" cc=\"%s\" />\n" % (xx, xy, xz, yy, yz, zz, xphix, xphiy, xphiz, yphix, yphiy, yphiz, zphix, zphiy, zphiz, phixphix, phixphiy, phixphiz, phiyphiy, phiyphiz, phizphiz) )
      f_cov_fromHistXml.write("</operation>\n\n")
#Closing files
f_cov_APEsXml.write("</MuonAlignment>")
f_cov_APEsXml.close()
f_cov_APEs_t2Xml.write("</MuonAlignment>")
f_cov_APEs_t2Xml.close()
f_cov_APEs_allXml.write("</MuonAlignment>")
f_cov_APEs_allXml.close()
f_AllAPEsXml.write("</MuonAlignment>")
f_AllAPEsXml.close()
f_DE_AllAPEsXml.write("</MuonAlignment>")
f_DE_AllAPEsXml.close()
f_cov_fromHistXml.write("</MuonAlignment>")
f_cov_fromHistXml.close()

print "You have",NfitFailed,"fits that have FAILED (if more than 0 be carefull because APE will be 0 for those)!"
