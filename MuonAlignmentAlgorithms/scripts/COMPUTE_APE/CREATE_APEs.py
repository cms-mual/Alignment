import ROOT, array, os, sys, re, math, random
import numpy as np
from math import *
sys.path.append('./File_useful/')
execfile("File_useful/geometryXMLparser.py")
execfile("File_useful/plotscripts.py")
execfile("File_useful/Util_CalculateCovMatrix.py")
# DT or CSC ?
isDT   = False
isData = False
# All units are in cm and rad here
xmlfileORI        = "Geom/data_DT-1100-111111_2017B_CMSSW925p2_SingMu_MuAlCalIsoMuv1_92XdataRun2Promptv5_1refit_01.xml"
reportfile        = "Geom/data_DT-1100-111111_2017B_CMSSW925p2_SingMu_MuAlCalIsoMuv1_92XdataRun2Promptv5_1refit_01_report.py"
outName           = "_6DOF_2017Data"
is3DOF            = False #This modify the extraction of the covariance elements, since covariance matrix will be different
if not isDT:
  xmlfileORI      = "Geom/mc_CSC-1100-110001_CMSSW_9_0_1_GTasym_39M_13TeV_FixYME13_03.xml"
  reportfile      = "Geom/mc_CSC-1100-110001_CMSSW_9_0_1_GTasym_39M_13TeV_FixYME13_03_report.py"
  outName         = "_3DOF_MCfromHW_for2017Data"
  is3DOF          = True
xmlfileIdealGeom  = "Geom/muonGeometry_IDEAL_AllZeroes.Ape6x6.DBv2.xml"

execfile(reportfile)
report = reports
g1 = MuonGeometry(xmlfileORI)
if not isData:
  gI = MuonGeometry(xmlfileIdealGeom)
debug=False

if isDT:
  # Covariance from Final-Ideal geoemtry
  cov_fromH = []
  for wheel in -2, -1, 0, +1, +2:
    cov_fromH.append([]);
    for station in 1, 2, 3, 4:
      cov_fromH[wheel+2].append([])
      if station != 4:
        for sector in 1,2,3,4,5,6,7,8,9,10,11,12:
          cov_fromH[wheel+2][station-1].append(None)
      else:
        for sector in 1,2,3,4,5,6,7,8,9,10,11,12,13,14:
          cov_fromH[wheel+2][station-1].append(None)
  
  if not isData:
    for wheel in (-2, -1, 0, 1, 2):
      for station in (1, 2, 3, 4):
        varx = []; vary = []; varz = []; varphix = []; varphiy = []; varphiz = [];
        null = 0
        cov_f = [[]]; cov_f = [[null for i in xrange(6)] for i in xrange(6)]
        if station != 4: sectors = (1,2,3,4,5,6,7,8,9,10,11,12)
        else:            sectors = (1,2,3,4,5,6,7,8,9,10,11,12,13,14)
        for sector in sectors:
          dx_cm = (g1.dt[wheel, station, sector].x - gI.dt[wheel, station, sector].x)*signConventions["DT", wheel, station, sector][0]
          dy_cm = (g1.dt[wheel, station, sector].y - gI.dt[wheel, station, sector].y)*signConventions["DT", wheel, station, sector][1]
          dz_cm = (g1.dt[wheel, station, sector].z - gI.dt[wheel, station, sector].z)*signConventions["DT", wheel, station, sector][2]
          dphix_rad = (g1.dt[wheel, station, sector].phix - gI.dt[wheel, station, sector].phix)*signConventions["DT", wheel, station,sector][0] 
          dphiy_rad = (g1.dt[wheel, station, sector].phiy - gI.dt[wheel, station, sector].phiy)*signConventions["DT", wheel, station, sector][1]
          dphiz_rad = (g1.dt[wheel, station, sector].phiz - gI.dt[wheel, station, sector].phiz)*signConventions["DT", wheel, station, sector][2]
          varx.append(dx_cm); vary.append(dy_cm); varz.append(dz_cm); varphix.append(dphix_rad); varphiy.append(dphiy_rad); varphiz.append(dphiz_rad);
        #Compute convariance
        All_vectors = np.vstack( (varx,vary,varz,varphix,varphiy,varphiz) )
        cov_f = np.cov(All_vectors)
        if station != 4: sectors = (1,2,3,4,5,6,7,8,9,10,11,12)
        else:            sectors = (1,2,3,4,5,6,7,8,9,10,11,12,13,14)
        for sector in sectors:
          cov_fromH[wheel+2][station-1][sector-1] = signConvention_cov_2D(cov_f,wheel,station,sector)
  
  # APE from MINUIT and from comparing 2 geometries
  M_FIT = []
  for wheel in -2, -1, 0, +1, +2:
    M_FIT.append([])
    for station in 1, 2, 3, 4:
      M_FIT[wheel+2].append([])
      if station != 4:
        for sector in 1,2,3,4,5,6,7,8,9,10,11,12:
          M_FIT[wheel+2][station-1].append(None)
      else:
        for sector in 1,2,3,4,5,6,7,8,9,10,11,12,13,14:
          M_FIT[wheel+2][station-1].append(None)
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
          if ( station != 4 ): #In station 1,2,3 are 144 numbers, because there are 12 params, but we want the first six (three): xx, xy, xz, xphix, xphiy, xphiz, A, B, 0, 0, 0, 0; yx, yy, yz... (xx, xy, xphiz, xA, xB, 0, 0, 0, 0, 0, 0, 0, yx, yy...)
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
        # Save final quantities in a map that for each chamber has a 6x6 matrix
        M_FIT[wheel+2][station-1][sector-1] = E_stat
    if ( r.postal_address[0] == "DT" and r.status != "PASS") :
      wheel   = r.postal_address[1]
      station = r.postal_address[2]
      sector  = r.postal_address[3]
      NfitFailed=NfitFailed+1
      m_null = []
      for iN in range(36): m_null.append(0)
      M_FIT[wheel+2][station-1][sector-1] = m_null
  #Apply Sign Convention to M_FIT (so that you can average different sectors correctly)
  M_FIT = signConvention(M_FIT)
  
  #Now we have the Covariance matrix that give us: sigma_x(stat), sigma_y(stat)... and off-diagonal terms sigma_xy(stat), sigma_xz(stat)...
  #Off-diagonal terms can be written in term of correlation: rho_xy, rho_xz... where rho_xy=sigma_xy(stat)/(sigma_x(stat)*sigma_y(stat))
  cov_only = []
  cov_only_times2 = []
  cov_only_all = []
  for wheel in -2, -1, 0, +1, +2:
    cov_only.append([])
    cov_only_times2.append([])
    cov_only_all.append([])
    for station in 1, 2, 3, 4:
      cov_only[wheel+2].append([])
      cov_only_times2[wheel+2].append([])
      cov_only_all[wheel+2].append([])
      sectors = (1,2,3,4,5,6,7,8,9,10,11,12)
      if(station==4): sectors = (1,2,3,4,5,6,7,8,9,10,11,12,13,14)
      for sector in sectors:
        cov_only[wheel+2][station-1].append(None)
        cov_only_times2[wheel+2][station-1].append(None)
        cov_only_all[wheel+2][station-1].append(None)
  
  for wheel in -2, -1, 0, +1, +2:
    for station in 1, 2, 3, 4:
      sectors = (1,2,3,4,5,6,7,8,9,10,11,12)
      if(station==4): sectors = (1,2,3,4,5,6,7,8,9,10,11,12,13,14)
      print "\n********************************************************************"
      print "Group of chambers: wheel = %s, station = %s" % (wheel, station)
      print "********************************************************************"
  
      #Covariance averaging same wheel/station
      print "Covariance matrix Matrix for wheel = %s, station = %s" % (wheel, station)
      cov_FIT    = calculateCovStatMatrix( M_FIT[wheel+2][station-1] ) 
      cov_FIT_t2 = calculateCovStatMatrix_times2( M_FIT[wheel+2][station-1] )
      for sector in sectors:
        cov_only[wheel+2][station-1][sector-1]        = cov_FIT 
        cov_only_times2[wheel+2][station-1][sector-1] = cov_FIT_t2
  
      #Covariance not averaging same wheel/station
      for sector in sectors:
        matrix = None
        if(station==4 and (sector==4 or sector==10 or sector==13 or sector==14)): matrix = cov_FIT
        else: matrix = calculateCovStatMatrix_noAverage(M_FIT[wheel+2][station-1][sector-1])
        cov_only_all[wheel+2][station-1][sector-1] = matrix
  
  #Apply Sign Conventionagain, because this is what CMS is expecting
  cov_only = signConvention(cov_only)
  cov_only_times2 = signConvention(cov_only_times2)
  cov_only_all = signConvention(cov_only_all) 
  # Take the size from the APEs from teh histogram and give it to one from MINUIT
  if not isData:
    cov_only_resizedFromH = resizeAPEs(cov_only,cov_fromH)
  
  #Print APE with only Covariance matrix
  f_cov_APEsXml = open('APEs_COV_DT' + outName + '.xml','w')
  #Print APE with only Covariance matrix times 2
  f_cov_APEs_t2Xml = open('APEs_COV_t2_DT' + outName + '.xml','w')
  #Print APE with only Covariance matrix not averaging sectors
  f_cov_APEs_allXml = open('APEs_COVall_DT' + outName + '.xml','w')
  #print APE from Covariance matrix from histograms
  if not isData:
    f_cov_fromHistXml = open('APEs_COVfromH_DT' + outName + '.xml','w')
  #Print APE with only Covariance matrix but resized to Covariance matrix from histograms
  f_cov_APEs_resizedXml = open('APEs_COV_resized_DT' + outName + '.xml','w')
  
  f_cov_APEsXml.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n")
  f_cov_APEsXml.write("<?xml-stylesheet type=\"text/xml\" href=\"MuonAlignment.xsl\"?>\n")
  f_cov_APEsXml.write("<MuonAlignment>\n\n")
  
  f_cov_APEs_t2Xml.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n")
  f_cov_APEs_t2Xml.write("<?xml-stylesheet type=\"text/xml\" href=\"MuonAlignment.xsl\"?>\n")
  f_cov_APEs_t2Xml.write("<MuonAlignment>\n\n")
  
  f_cov_APEs_allXml.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n")
  f_cov_APEs_allXml.write("<?xml-stylesheet type=\"text/xml\" href=\"MuonAlignment.xsl\"?>\n")
  f_cov_APEs_allXml.write("<MuonAlignment>\n\n")
  if not isData: 
    f_cov_fromHistXml.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n")
    f_cov_fromHistXml.write("<?xml-stylesheet type=\"text/xml\" href=\"MuonAlignment.xsl\"?>\n")
    f_cov_fromHistXml.write("<MuonAlignment>\n\n")
  
  f_cov_APEs_resizedXml.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n")
  f_cov_APEs_resizedXml.write("<?xml-stylesheet type=\"text/xml\" href=\"MuonAlignment.xsl\"?>\n")
  f_cov_APEs_resizedXml.write("<MuonAlignment>\n\n")
  
  for wheel in -2, -1, 0, +1, +2:
    for station in 1, 2, 3, 4:
      if station != 4: sectors = (1,2,3,4,5,6,7,8,9,10,11,12)
      else:            sectors = (1,2,3,4,5,6,7,8,9,10,11,12,13,14)
      for sector in sectors:
        #Covariance APE
        xx       = cov_only[wheel+2][station-1][sector-1][0][0]
        xy       = cov_only[wheel+2][station-1][sector-1][0][1]
        xz       = cov_only[wheel+2][station-1][sector-1][0][2]
        yy       = cov_only[wheel+2][station-1][sector-1][1][1]
        yz       = cov_only[wheel+2][station-1][sector-1][1][2]
        zz       = cov_only[wheel+2][station-1][sector-1][2][2]
        xphix    = cov_only[wheel+2][station-1][sector-1][0][3]
        xphiy    = cov_only[wheel+2][station-1][sector-1][0][4]
        xphiz    = cov_only[wheel+2][station-1][sector-1][0][5]
        yphix    = cov_only[wheel+2][station-1][sector-1][1][3]
        yphiy    = cov_only[wheel+2][station-1][sector-1][1][4]
        yphiz    = cov_only[wheel+2][station-1][sector-1][1][5]
        zphix    = cov_only[wheel+2][station-1][sector-1][2][3]
        zphiy    = cov_only[wheel+2][station-1][sector-1][2][4]
        zphiz    = cov_only[wheel+2][station-1][sector-1][2][5]
        phixphix = cov_only[wheel+2][station-1][sector-1][3][3]
        phixphiy = cov_only[wheel+2][station-1][sector-1][3][4]
        phixphiz = cov_only[wheel+2][station-1][sector-1][3][5]
        phiyphiy = cov_only[wheel+2][station-1][sector-1][4][4]
        phiyphiz = cov_only[wheel+2][station-1][sector-1][4][5]
        phizphiz = cov_only[wheel+2][station-1][sector-1][5][5]
        if(station==4): xy=0; yy = 0.01; yz=0; yphix=0; yphiy=0; yphiz=0;
        f_cov_APEsXml.write("<operation>\n")
        f_cov_APEsXml.write( "  <DTChamber wheel=\"%s\" station=\"%s\" sector=\"%s\" />\n" % (wheel, station, sector) )
        f_cov_APEsXml.write( "  <setape xx=\"%s\" xy=\"%s\" xz=\"%s\" yy=\"%s\" yz=\"%s\" zz=\"%s\" xa=\"%s\" xb=\"%s\" xc=\"%s\" ya=\"%s\" yb=\"%s\" yc=\"%s\" za=\"%s\" zb=\"%s\" zc=\"%s\" aa=\"%s\" ab=\"%s\" ac=\"%s\" bb=\"%s\" bc=\"%s\" cc=\"%s\" />\n" % (xx, xy, xz, yy, yz, zz, xphix, xphiy, xphiz, yphix, yphiy, yphiz, zphix, zphiy, zphiz, phixphix, phixphiy, phixphiz, phiyphiy, phiyphiz, phizphiz) )
        f_cov_APEsXml.write("</operation>\n\n")
        #Covariance APE times 2
        xx       = cov_only_times2[wheel+2][station-1][sector-1][0][0]
        xy       = cov_only_times2[wheel+2][station-1][sector-1][0][1]
        xz       = cov_only_times2[wheel+2][station-1][sector-1][0][2]
        yy       = cov_only_times2[wheel+2][station-1][sector-1][1][1]
        yz       = cov_only_times2[wheel+2][station-1][sector-1][1][2]
        zz       = cov_only_times2[wheel+2][station-1][sector-1][2][2]
        xphix    = cov_only_times2[wheel+2][station-1][sector-1][0][3]
        xphiy    = cov_only_times2[wheel+2][station-1][sector-1][0][4]
        xphiz    = cov_only_times2[wheel+2][station-1][sector-1][0][5]
        yphix    = cov_only_times2[wheel+2][station-1][sector-1][1][3]
        yphiy    = cov_only_times2[wheel+2][station-1][sector-1][1][4]
        yphiz    = cov_only_times2[wheel+2][station-1][sector-1][1][5]
        zphix    = cov_only_times2[wheel+2][station-1][sector-1][2][3]
        zphiy    = cov_only_times2[wheel+2][station-1][sector-1][2][4]
        zphiz    = cov_only_times2[wheel+2][station-1][sector-1][2][5]
        phixphix = cov_only_times2[wheel+2][station-1][sector-1][3][3]
        phixphiy = cov_only_times2[wheel+2][station-1][sector-1][3][4]
        phixphiz = cov_only_times2[wheel+2][station-1][sector-1][3][5]
        phiyphiy = cov_only_times2[wheel+2][station-1][sector-1][4][4]
        phiyphiz = cov_only_times2[wheel+2][station-1][sector-1][4][5]
        phizphiz = cov_only_times2[wheel+2][station-1][sector-1][5][5]
        if(station==4): xy=0; yy = 0.01; yz=0; yphix=0; yphiy=0; yphiz=0;
        f_cov_APEs_t2Xml.write("<operation>\n")
        f_cov_APEs_t2Xml.write( "  <DTChamber wheel=\"%s\" station=\"%s\" sector=\"%s\" />\n" % (wheel, station, sector) )
        f_cov_APEs_t2Xml.write( "  <setape xx=\"%s\" xy=\"%s\" xz=\"%s\" yy=\"%s\" yz=\"%s\" zz=\"%s\" xa=\"%s\" xb=\"%s\" xc=\"%s\" ya=\"%s\" yb=\"%s\" yc=\"%s\" za=\"%s\" zb=\"%s\" zc=\"%s\" aa=\"%s\" ab=\"%s\" ac=\"%s\" bb=\"%s\" bc=\"%s\" cc=\"%s\" />\n" % (xx, xy, xz, yy, yz, zz, xphix, xphiy, xphiz, yphix, yphiy, yphiz, zphix, zphiy, zphiz, phixphix, phixphiy, phixphiz, phiyphiy, phiyphiz, phizphiz) )
        f_cov_APEs_t2Xml.write("</operation>\n\n")
        #Covariance APE all different
        xx = cov_only_all[wheel+2][station-1][sector-1][0][0]
        xy = cov_only_all[wheel+2][station-1][sector-1][0][1]
        xz = cov_only_all[wheel+2][station-1][sector-1][0][2]
        yy = cov_only_all[wheel+2][station-1][sector-1][1][1]
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
        if(station==4): xy=0; yy = 0.01; yz=0; yphix=0; yphiy=0; yphiz=0;
        f_cov_APEs_allXml.write("<operation>\n")
        f_cov_APEs_allXml.write( "  <DTChamber wheel=\"%s\" station=\"%s\" sector=\"%s\" />\n" % (wheel, station, sector) )
        f_cov_APEs_allXml.write( "  <setape xx=\"%s\" xy=\"%s\" xz=\"%s\" yy=\"%s\" yz=\"%s\" zz=\"%s\" xa=\"%s\" xb=\"%s\" xc=\"%s\" ya=\"%s\" yb=\"%s\" yc=\"%s\" za=\"%s\" zb=\"%s\" zc=\"%s\" aa=\"%s\" ab=\"%s\" ac=\"%s\" bb=\"%s\" bc=\"%s\" cc=\"%s\" />\n" % (xx, xy, xz, yy, yz, zz, xphix, xphiy, xphiz, yphix, yphiy, yphiz, zphix, zphiy, zphiz, phixphix, phixphiy, phixphiz, phiyphiy, phiyphiz, phizphiz) )
        f_cov_APEs_allXml.write("</operation>\n\n")
        #From Histograms  
        if not isData:
          xx       = cov_fromH[wheel+2][station-1][sector-1][0][0]
          xy       = cov_fromH[wheel+2][station-1][sector-1][0][1]
          xz       = cov_fromH[wheel+2][station-1][sector-1][0][2]
          yy       = cov_fromH[wheel+2][station-1][sector-1][1][1]
          yz       = cov_fromH[wheel+2][station-1][sector-1][1][2]
          zz       = cov_fromH[wheel+2][station-1][sector-1][2][2]
          xphix    = cov_fromH[wheel+2][station-1][sector-1][0][3]
          xphiy    = cov_fromH[wheel+2][station-1][sector-1][0][4]
          xphiz    = cov_fromH[wheel+2][station-1][sector-1][0][5]
          yphix    = cov_fromH[wheel+2][station-1][sector-1][1][3]
          yphiy    = cov_fromH[wheel+2][station-1][sector-1][1][4]
          yphiz    = cov_fromH[wheel+2][station-1][sector-1][1][5]
          zphix    = cov_fromH[wheel+2][station-1][sector-1][2][3]
          zphiy    = cov_fromH[wheel+2][station-1][sector-1][2][4]
          zphiz    = cov_fromH[wheel+2][station-1][sector-1][2][5]
          phixphix = cov_fromH[wheel+2][station-1][sector-1][3][3]
          phixphiy = cov_fromH[wheel+2][station-1][sector-1][3][4]
          phixphiz = cov_fromH[wheel+2][station-1][sector-1][3][5]
          phiyphiy = cov_fromH[wheel+2][station-1][sector-1][4][4]
          phiyphiz = cov_fromH[wheel+2][station-1][sector-1][4][5]
          phizphiz = cov_fromH[wheel+2][station-1][sector-1][5][5]
          if(station==4): xy=0; yy = 0.01; yz=0; yphix=0; yphiy=0; yphiz=0;
          f_cov_fromHistXml.write("<operation>\n")
          f_cov_fromHistXml.write( "  <DTChamber wheel=\"%s\" station=\"%s\" sector=\"%s\" />\n" % (wheel, station, sector) )
          f_cov_fromHistXml.write( "  <setape xx=\"%s\" xy=\"%s\" xz=\"%s\" yy=\"%s\" yz=\"%s\" zz=\"%s\" xa=\"%s\" xb=\"%s\" xc=\"%s\" ya=\"%s\" yb=\"%s\" yc=\"%s\" za=\"%s\" zb=\"%s\" zc=\"%s\" aa=\"%s\" ab=\"%s\" ac=\"%s\" bb=\"%s\" bc=\"%s\" cc=\"%s\" />\n" % (xx, xy, xz, yy, yz, zz, xphix, xphiy, xphiz, yphix, yphiy, yphiz, zphix, zphiy, zphiz, phixphix, phixphiy, phixphiz, phiyphiy, phiyphiz, phizphiz) )
          f_cov_fromHistXml.write("</operation>\n\n")
          #From COV matrix but resized to Histograms  
          xx       = cov_only_resizedFromH[wheel+2][station-1][sector-1][0][0]
          xy       = cov_only_resizedFromH[wheel+2][station-1][sector-1][0][1]
          xz       = cov_only_resizedFromH[wheel+2][station-1][sector-1][0][2]
          yy       = cov_only_resizedFromH[wheel+2][station-1][sector-1][1][1]
          yz       = cov_only_resizedFromH[wheel+2][station-1][sector-1][1][2]
          zz       = cov_only_resizedFromH[wheel+2][station-1][sector-1][2][2]
          xphix    = cov_only_resizedFromH[wheel+2][station-1][sector-1][0][3]
          xphiy    = cov_only_resizedFromH[wheel+2][station-1][sector-1][0][4]
          xphiz    = cov_only_resizedFromH[wheel+2][station-1][sector-1][0][5]
          yphix    = cov_only_resizedFromH[wheel+2][station-1][sector-1][1][3]
          yphiy    = cov_only_resizedFromH[wheel+2][station-1][sector-1][1][4]
          yphiz    = cov_only_resizedFromH[wheel+2][station-1][sector-1][1][5]
          zphix    = cov_only_resizedFromH[wheel+2][station-1][sector-1][2][3]
          zphiy    = cov_only_resizedFromH[wheel+2][station-1][sector-1][2][4]
          zphiz    = cov_only_resizedFromH[wheel+2][station-1][sector-1][2][5]
          phixphix = cov_only_resizedFromH[wheel+2][station-1][sector-1][3][3]
          phixphiy = cov_only_resizedFromH[wheel+2][station-1][sector-1][3][4]
          phixphiz = cov_only_resizedFromH[wheel+2][station-1][sector-1][3][5]
          phiyphiy = cov_only_resizedFromH[wheel+2][station-1][sector-1][4][4]
          phiyphiz = cov_only_resizedFromH[wheel+2][station-1][sector-1][4][5]
          phizphiz = cov_only_resizedFromH[wheel+2][station-1][sector-1][5][5]
          if(station==4): xy=0; yy = 0.01; yz=0; yphix=0; yphiy=0; yphiz=0;
          f_cov_APEs_resizedXml.write("<operation>\n")
          f_cov_APEs_resizedXml.write( "  <DTChamber wheel=\"%s\" station=\"%s\" sector=\"%s\" />\n" % (wheel, station, sector) )
          f_cov_APEs_resizedXml.write( "  <setape xx=\"%s\" xy=\"%s\" xz=\"%s\" yy=\"%s\" yz=\"%s\" zz=\"%s\" xa=\"%s\" xb=\"%s\" xc=\"%s\" ya=\"%s\" yb=\"%s\" yc=\"%s\" za=\"%s\" zb=\"%s\" zc=\"%s\" aa=\"%s\" ab=\"%s\" ac=\"%s\" bb=\"%s\" bc=\"%s\" cc=\"%s\" />\n" % (xx, xy, xz, yy, yz, zz, xphix, xphiy, xphiz, yphix, yphiy, yphiz, zphix, zphiy, zphiz, phixphix, phixphiy, phixphiz, phiyphiy, phiyphiz, phizphiz) )
          f_cov_APEs_resizedXml.write("</operation>\n\n")
  #Closing files
  f_cov_APEsXml.write("</MuonAlignment>")
  f_cov_APEsXml.close()
  f_cov_APEs_t2Xml.write("</MuonAlignment>")
  f_cov_APEs_t2Xml.close()
  f_cov_APEs_allXml.write("</MuonAlignment>")
  f_cov_APEs_allXml.close()
  if not isData:
    f_cov_fromHistXml.write("</MuonAlignment>")
    f_cov_fromHistXml.close()
    f_cov_APEs_resizedXml.write("</MuonAlignment>")
    f_cov_APEs_resizedXml.close()
  print "You have",NfitFailed,"fits that have FAILED (if more than 0 be carefull because APE will be 0 for those)!"
# Now let's do the CSC case
else:
  # Covariance from Final-Ideal geoemtry
  cov_fromH = [];
  for endcap in (1, 2):
    cov_fromH.append([])
    for disk in (1, 2, 3, 4):
      cov_fromH[endcap-1].append([])
      if disk == 1: rings = (1,2,3,4)
      else:         rings = (1,2)
      for ring in rings:
        cov_fromH[endcap-1][disk-1].append([])
        for sector in GetCSCSectors(disk,ring):
          cov_fromH[endcap-1][disk-1][ring-1].append(None)
  if not isData:
    for endcap in (1, 2):
      for disk in (1, 2, 3, 4):
        if disk == 1: rings = (1,2,3,4)
        else:         rings = (1,2)
        for ring in rings:
          varx = []; vary = []; varz = []; varphix = []; varphiy = []; varphiz = [];
          null = 0
          cov_f = [[]]; cov_f = [[null for i in xrange(6)] for i in xrange(6)]
          for sector in GetCSCSectors(disk,ring):
            dx_cm = (g1.csc[endcap, disk, ring, sector].x - gI.csc[endcap, disk, ring, sector].x)*signConventions["CSC", endcap, disk, ring, sector][0]
            dy_cm = (g1.csc[endcap, disk, ring, sector].y - gI.csc[endcap, disk, ring, sector].y)*signConventions["CSC", endcap, disk, ring, sector][1]
            dz_cm = (g1.csc[endcap, disk, ring, sector].z - gI.csc[endcap, disk, ring, sector].z)*signConventions["CSC", endcap, disk, ring, sector][2]
            dphix_rad = (g1.csc[endcap, disk, ring, sector].phix - gI.csc[endcap, disk, ring, sector].phix)*signConventions["CSC", endcap, disk, ring, sector][0] 
            dphiy_rad = (g1.csc[endcap, disk, ring, sector].phiy - gI.csc[endcap, disk, ring, sector].phiy)*signConventions["CSC", endcap, disk, ring, sector][1]
            dphiz_rad = (g1.csc[endcap, disk, ring, sector].phiz - gI.csc[endcap, disk, ring, sector].phiz)*signConventions["CSC", endcap, disk, ring, sector][2]
            varx.append(dx_cm); vary.append(dy_cm); varz.append(dz_cm); varphix.append(dphix_rad); varphiy.append(dphiy_rad); varphiz.append(dphiz_rad);
          #Compute convariance
          All_vectors = np.vstack( (varx,vary,varz,varphix,varphiy,varphiz) )
          cov_f = np.cov(All_vectors)
          for sector in GetCSCSectors(disk,ring):
            cov_fromH[endcap-1][disk-1][ring-1][sector-1] = signConvention_cov_2D_CSC(cov_f, endcap, disk, ring, sector)

  # APE from MINUIT and from comparing 2 geometries
  M_FIT = []
  for endcap in (1, 2):
    M_FIT.append([])
    for disk in (1, 2, 3, 4):
      M_FIT[endcap-1].append([])
      if disk == 1: rings = (1,2,3,4)
      else:         rings = (1,2)
      for ring in rings:
        M_FIT[endcap-1][disk-1].append([])
        for sector in GetCSCSectors(disk,ring):
          M_FIT[endcap-1][disk-1][ring-1].append(None)
  #For chamber that is an object described in the report file
  NfitFailed=0
  for r in report:
    index=1
    if ( r.postal_address[0] == "CSC" and r.status == "PASS") :
      endcap  = r.postal_address[1]
      disk    = r.postal_address[2]
      ring    = r.postal_address[3]
      sector  = r.postal_address[4]
      #if(debug): 
      print "0)", endcap, disk, ring, sector
      # Extract the covariance matrix and place it in the list E_stat
      E_stat=[]
      Cov_M = r.CovMatrix
      for covItem in Cov_M:
        if(index>63): continue #You have a 9x9 matrix. You need the first 6 raw, but the forth line is signa_x_residual and you have to skip it, i.e. after the 9x(6+1)=63 elements you are not interested
        if(True):#is3DOF):
          if((index==1 or index==2 or index==3) or (index==10 or index==11 or index==12) or (index==19 or index==20 or index==21)): #Lines with X, Y and PhiZ
            E_stat.append(float(covItem))
          if(index==2 or index==11 or index==20):
            E_stat.append(0.); E_stat.append(0.); E_stat.append(0.)
          if(index==13): # sigmaZ, sigmaPhiX, sigmaPhiY
            myError = GetZ_CSC(endcap,disk,ring)
            E_stat.append(0.); E_stat.append(0.); E_stat.append(myError*myError); E_stat.append(0.); E_stat.append(0.); E_stat.append(0.);
            myError = GetPhiX_CSC(endcap,disk,ring)
            E_stat.append(0.); E_stat.append(0.); E_stat.append(0.); E_stat.append(myError*myError); E_stat.append(0.); E_stat.append(0.);
            myError = GetPhiY_CSC(endcap,disk,ring)
            E_stat.append(0.); E_stat.append(0.); E_stat.append(0.); E_stat.append(0.); E_stat.append(myError*myError); E_stat.append(0.);
        index=index+1
      #if(debug):
      print "1)", len(E_stat), " -> ", E_stat
      # Save final quantities in a map that for each chamber has a 6x6 matrix
      M_FIT[endcap-1][disk-1][ring-1][sector-1] = E_stat
    if ( r.postal_address[0] == "CSC" and r.status != "PASS") :
      endcap  = r.postal_address[1]
      disk    = r.postal_address[2]
      ring    = r.postal_address[3]
      sector  = r.postal_address[4]
      NfitFailed=NfitFailed+1
      m_null = []
      for iN in range(36): m_null.append(0)
      M_FIT[endcap-1][disk-1][ring-1][sector-1] = m_null
  #Apply Sign Convention to M_FIT (so that you can average different sectors correctly)
  M_FIT = signConvention_CSC(M_FIT)

  #Now we have the Covariance matrix that give us: sigma_x(stat), sigma_y(stat)... and off-diagonal terms sigma_xy(stat), sigma_xz(stat)...
  #Off-diagonal terms can be written in term of correlation: rho_xy, rho_xz... where rho_xy=sigma_xy(stat)/(sigma_x(stat)*sigma_y(stat))
  cov_only = []
  cov_only_times2 = []
  cov_only_all = []
  for endcap in (1, 2):
    cov_only.append([])
    cov_only_times2.append([])
    cov_only_all.append([])
    for disk in (1, 2, 3, 4):
      cov_only[endcap-1].append([])
      cov_only_times2[endcap-1].append([])
      cov_only_all[endcap-1].append([])
      if disk == 1: rings = (1,2,3,4)
      else:         rings = (1,2)
      for ring in rings:
        cov_only[endcap-1][disk-1].append([])
        cov_only_times2[endcap-1][disk-1].append([])
        cov_only_all[endcap-1][disk-1].append([])
        for sector in GetCSCSectors(disk,ring):
          cov_only[endcap-1][disk-1][ring-1].append(None)
          cov_only_times2[endcap-1][disk-1][ring-1].append((None))
          cov_only_all[endcap-1][disk-1][ring-1].append((None))
  
  for endcap in (1, 2):
    for disk in (1, 2, 3, 4):
      if disk == 1: rings = (1,2,3,4)
      else:         rings = (1,2)
      for ring in rings:
        sectors = GetCSCSectors(disk,ring)
        print "\n********************************************************************"
        print "Group of chambers: endcap = %s, disk = %s, ring = %s" % (endcap, disk, ring)
        print "********************************************************************"
    
        #Covariance averaging same wheel/station
        print "Covariance matrix Matrix for endcap = %s, disk = %s, ring = %s" % (endcap, disk, ring)
        cov_FIT    = calculateCovStatMatrix( M_FIT[endcap-1][disk-1][ring-1] ) 
        cov_FIT_t2 = calculateCovStatMatrix_times2( M_FIT[endcap-1][disk-1][ring-1] )
        for sector in sectors:
          cov_only[endcap-1][disk-1][ring-1][sector-1]        = cov_FIT 
          cov_only_times2[endcap-1][disk-1][ring-1][sector-1] = cov_FIT_t2
    
        #Covariance not averaging same wheel/station
        for sector in sectors:
          matrix = calculateCovStatMatrix_noAverage(M_FIT[endcap-1][disk-1][ring-1][sector-1])
          cov_only_all[endcap-1][disk-1][ring-1][sector-1] = matrix
  
  #Apply Sign Conventionagain, because this is what CMS is expecting
  cov_only = signConvention_CSC(cov_only)
  cov_only_times2 = signConvention_CSC(cov_only_times2)
  cov_only_all = signConvention_CSC(cov_only_all)

  #Print APE with only Covariance matrix
  f_cov_APEsXml = open('APEs_COV_CSC' + outName + '.xml','w')
  #Print APE with only Covariance matrix times 2
  f_cov_APEs_t2Xml = open('APEs_COV_t2_CSC' + outName + '.xml','w')
  #Print APE with only Covariance matrix not averaging sectors
  f_cov_APEs_allXml = open('APEs_COVall_CSC' + outName + '.xml','w')
  #print APE from Covariance matrix from histograms
  if not isData:
    f_cov_fromHistXml = open('APEs_COVfromH_CSC' + outName + '.xml','w')
  #Print APE with only Covariance matrix but resized to Covariance matrix from histograms
  f_cov_APEs_resizedXml = open('APEs_COV_resized_CSC' + outName + '.xml','w')

  f_cov_APEsXml.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n")
  f_cov_APEsXml.write("<?xml-stylesheet type=\"text/xml\" href=\"MuonAlignment.xsl\"?>\n")
  f_cov_APEsXml.write("<MuonAlignment>\n\n")
  
  f_cov_APEs_t2Xml.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n")
  f_cov_APEs_t2Xml.write("<?xml-stylesheet type=\"text/xml\" href=\"MuonAlignment.xsl\"?>\n")
  f_cov_APEs_t2Xml.write("<MuonAlignment>\n\n")
  
  f_cov_APEs_allXml.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n")
  f_cov_APEs_allXml.write("<?xml-stylesheet type=\"text/xml\" href=\"MuonAlignment.xsl\"?>\n")
  f_cov_APEs_allXml.write("<MuonAlignment>\n\n")
  
  if not isData:
    f_cov_fromHistXml.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n")
    f_cov_fromHistXml.write("<?xml-stylesheet type=\"text/xml\" href=\"MuonAlignment.xsl\"?>\n")
    f_cov_fromHistXml.write("<MuonAlignment>\n\n")
  
  f_cov_APEs_resizedXml.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n")
  f_cov_APEs_resizedXml.write("<?xml-stylesheet type=\"text/xml\" href=\"MuonAlignment.xsl\"?>\n")
  f_cov_APEs_resizedXml.write("<MuonAlignment>\n\n")
 
  # APEs from histograms
  for endcap in (1, 2):
    for disk in (1, 2, 3, 4):
      if disk == 1: rings = (1,2,3,4) 
      else:         rings = (1,2)
      for ring in rings:
        for sector in GetCSCSectors(disk,ring):
          #Covariance APE
          xx       = cov_only[endcap-1][disk-1][ring-1][sector-1][0][0]
          xy       = cov_only[endcap-1][disk-1][ring-1][sector-1][0][1]
          xz       = cov_only[endcap-1][disk-1][ring-1][sector-1][0][2]
          yy       = cov_only[endcap-1][disk-1][ring-1][sector-1][1][1]
          yz       = cov_only[endcap-1][disk-1][ring-1][sector-1][1][2]
          zz       = cov_only[endcap-1][disk-1][ring-1][sector-1][2][2]
          xphix    = cov_only[endcap-1][disk-1][ring-1][sector-1][0][3]
          xphiy    = cov_only[endcap-1][disk-1][ring-1][sector-1][0][4]
          xphiz    = cov_only[endcap-1][disk-1][ring-1][sector-1][0][5]
          yphix    = cov_only[endcap-1][disk-1][ring-1][sector-1][1][3]
          yphiy    = cov_only[endcap-1][disk-1][ring-1][sector-1][1][4]
          yphiz    = cov_only[endcap-1][disk-1][ring-1][sector-1][1][5]
          zphix    = cov_only[endcap-1][disk-1][ring-1][sector-1][2][3]
          zphiy    = cov_only[endcap-1][disk-1][ring-1][sector-1][2][4]
          zphiz    = cov_only[endcap-1][disk-1][ring-1][sector-1][2][5]
          phixphix = cov_only[endcap-1][disk-1][ring-1][sector-1][3][3]
          phixphiy = cov_only[endcap-1][disk-1][ring-1][sector-1][3][4]
          phixphiz = cov_only[endcap-1][disk-1][ring-1][sector-1][3][5]
          phiyphiy = cov_only[endcap-1][disk-1][ring-1][sector-1][4][4]
          phiyphiz = cov_only[endcap-1][disk-1][ring-1][sector-1][4][5]
          phizphiz = cov_only[endcap-1][disk-1][ring-1][sector-1][5][5]
          f_cov_APEsXml.write("<operation>\n")
          f_cov_APEsXml.write( "  <CSCChamber endcap=\"%s\" station=\"%s\" ring=\"%s\" chamber=\"%s\" />\n" % (endcap,disk,ring,sector) )
          f_cov_APEsXml.write( "  <setape xx=\"%s\" xy=\"%s\" xz=\"%s\" yy=\"%s\" yz=\"%s\" zz=\"%s\" xa=\"%s\" xb=\"%s\" xc=\"%s\" ya=\"%s\" yb=\"%s\" yc=\"%s\" za=\"%s\" zb=\"%s\" zc=\"%s\" aa=\"%s\" ab=\"%s\" ac=\"%s\" bb=\"%s\" bc=\"%s\" cc=\"%s\" />\n" % (xx, xy, xz, yy, yz, zz, xphix, xphiy, xphiz, yphix, yphiy, yphiz, zphix, zphiy, zphiz, phixphix, phixphiy, phixphiz, phiyphiy, phiyphiz, phizphiz) )
          f_cov_APEsXml.write("</operation>\n\n")
          #Covariance APE times 2
          xx       = cov_only_times2[endcap-1][disk-1][ring-1][sector-1][0][0]
          xy       = cov_only_times2[endcap-1][disk-1][ring-1][sector-1][0][1]
          xz       = cov_only_times2[endcap-1][disk-1][ring-1][sector-1][0][2]
          yy       = cov_only_times2[endcap-1][disk-1][ring-1][sector-1][1][1]
          yz       = cov_only_times2[endcap-1][disk-1][ring-1][sector-1][1][2]
          zz       = cov_only_times2[endcap-1][disk-1][ring-1][sector-1][2][2]
          xphix    = cov_only_times2[endcap-1][disk-1][ring-1][sector-1][0][3]
          xphiy    = cov_only_times2[endcap-1][disk-1][ring-1][sector-1][0][4]
          xphiz    = cov_only_times2[endcap-1][disk-1][ring-1][sector-1][0][5]
          yphix    = cov_only_times2[endcap-1][disk-1][ring-1][sector-1][1][3]
          yphiy    = cov_only_times2[endcap-1][disk-1][ring-1][sector-1][1][4]
          yphiz    = cov_only_times2[endcap-1][disk-1][ring-1][sector-1][1][5]
          zphix    = cov_only_times2[endcap-1][disk-1][ring-1][sector-1][2][3]
          zphiy    = cov_only_times2[endcap-1][disk-1][ring-1][sector-1][2][4]
          zphiz    = cov_only_times2[endcap-1][disk-1][ring-1][sector-1][2][5]
          phixphix = cov_only_times2[endcap-1][disk-1][ring-1][sector-1][3][3]
          phixphiy = cov_only_times2[endcap-1][disk-1][ring-1][sector-1][3][4]
          phixphiz = cov_only_times2[endcap-1][disk-1][ring-1][sector-1][3][5]
          phiyphiy = cov_only_times2[endcap-1][disk-1][ring-1][sector-1][4][4]
          phiyphiz = cov_only_times2[endcap-1][disk-1][ring-1][sector-1][4][5]
          phizphiz = cov_only_times2[endcap-1][disk-1][ring-1][sector-1][5][5]
          f_cov_APEs_t2Xml.write("<operation>\n")
          f_cov_APEs_t2Xml.write( "  <CSCChamber endcap=\"%s\" station=\"%s\" ring=\"%s\" chamber=\"%s\" />\n" % (endcap,disk,ring,sector) )
          f_cov_APEs_t2Xml.write( "  <setape xx=\"%s\" xy=\"%s\" xz=\"%s\" yy=\"%s\" yz=\"%s\" zz=\"%s\" xa=\"%s\" xb=\"%s\" xc=\"%s\" ya=\"%s\" yb=\"%s\" yc=\"%s\" za=\"%s\" zb=\"%s\" zc=\"%s\" aa=\"%s\" ab=\"%s\" ac=\"%s\" bb=\"%s\" bc=\"%s\" cc=\"%s\" />\n" % (xx, xy, xz, yy, yz, zz, xphix, xphiy, xphiz, yphix, yphiy, yphiz, zphix, zphiy, zphiz, phixphix, phixphiy, phixphiz, phiyphiy, phiyphiz, phizphiz) )
          f_cov_APEs_t2Xml.write("</operation>\n\n")
          #Covariance APE all different
          xx = cov_only_all[endcap-1][disk-1][ring-1][sector-1][0][0]
          xy = cov_only_all[endcap-1][disk-1][ring-1][sector-1][0][1]
          xz = cov_only_all[endcap-1][disk-1][ring-1][sector-1][0][2]
          yy = cov_only_all[endcap-1][disk-1][ring-1][sector-1][1][1]
          yz = cov_only_all[endcap-1][disk-1][ring-1][sector-1][1][2]
          zz = cov_only_all[endcap-1][disk-1][ring-1][sector-1][2][2]
          xphix    = cov_only_all[endcap-1][disk-1][ring-1][sector-1][0][3]
          xphiy    = cov_only_all[endcap-1][disk-1][ring-1][sector-1][0][4]
          xphiz    = cov_only_all[endcap-1][disk-1][ring-1][sector-1][0][5]
          yphix    = cov_only_all[endcap-1][disk-1][ring-1][sector-1][1][3]
          yphiy    = cov_only_all[endcap-1][disk-1][ring-1][sector-1][1][4]
          yphiz    = cov_only_all[endcap-1][disk-1][ring-1][sector-1][1][5]
          zphix    = cov_only_all[endcap-1][disk-1][ring-1][sector-1][2][3]
          zphiy    = cov_only_all[endcap-1][disk-1][ring-1][sector-1][2][4]
          zphiz    = cov_only_all[endcap-1][disk-1][ring-1][sector-1][2][5]
          phixphix = cov_only_all[endcap-1][disk-1][ring-1][sector-1][3][3]
          phixphiy = cov_only_all[endcap-1][disk-1][ring-1][sector-1][3][4]
          phixphiz = cov_only_all[endcap-1][disk-1][ring-1][sector-1][3][5]
          phiyphiy = cov_only_all[endcap-1][disk-1][ring-1][sector-1][4][4]
          phiyphiz = cov_only_all[endcap-1][disk-1][ring-1][sector-1][4][5]
          phizphiz = cov_only_all[endcap-1][disk-1][ring-1][sector-1][5][5]
          f_cov_APEs_allXml.write("<operation>\n")
          f_cov_APEs_allXml.write( "  <CSCChamber endcap=\"%s\" station=\"%s\" ring=\"%s\" chamber=\"%s\" />\n" % (endcap,disk,ring,sector) )
          f_cov_APEs_allXml.write( "  <setape xx=\"%s\" xy=\"%s\" xz=\"%s\" yy=\"%s\" yz=\"%s\" zz=\"%s\" xa=\"%s\" xb=\"%s\" xc=\"%s\" ya=\"%s\" yb=\"%s\" yc=\"%s\" za=\"%s\" zb=\"%s\" zc=\"%s\" aa=\"%s\" ab=\"%s\" ac=\"%s\" bb=\"%s\" bc=\"%s\" cc=\"%s\" />\n" % (xx, xy, xz, yy, yz, zz, xphix, xphiy, xphiz, yphix, yphiy, yphiz, zphix, zphiy, zphiz, phixphix, phixphiy, phixphiz, phiyphiy, phiyphiz, phizphiz) )
          f_cov_APEs_allXml.write("</operation>\n\n")
          #From Histograms  
          if not isData:
            xx       = cov_fromH[endcap-1][disk-1][ring-1][sector-1][0][0]
            xy       = cov_fromH[endcap-1][disk-1][ring-1][sector-1][0][1]
            xz       = cov_fromH[endcap-1][disk-1][ring-1][sector-1][0][2]
            yy       = cov_fromH[endcap-1][disk-1][ring-1][sector-1][1][1]
            yz       = cov_fromH[endcap-1][disk-1][ring-1][sector-1][1][2]
            zz       = cov_fromH[endcap-1][disk-1][ring-1][sector-1][2][2]
            xphix    = cov_fromH[endcap-1][disk-1][ring-1][sector-1][0][3]
            xphiy    = cov_fromH[endcap-1][disk-1][ring-1][sector-1][0][4]
            xphiz    = cov_fromH[endcap-1][disk-1][ring-1][sector-1][0][5]
            yphix    = cov_fromH[endcap-1][disk-1][ring-1][sector-1][1][3]
            yphiy    = cov_fromH[endcap-1][disk-1][ring-1][sector-1][1][4]
            yphiz    = cov_fromH[endcap-1][disk-1][ring-1][sector-1][1][5]
            zphix    = cov_fromH[endcap-1][disk-1][ring-1][sector-1][2][3]
            zphiy    = cov_fromH[endcap-1][disk-1][ring-1][sector-1][2][4]
            zphiz    = cov_fromH[endcap-1][disk-1][ring-1][sector-1][2][5]
            phixphix = cov_fromH[endcap-1][disk-1][ring-1][sector-1][3][3]
            phixphiy = cov_fromH[endcap-1][disk-1][ring-1][sector-1][3][4]
            phixphiz = cov_fromH[endcap-1][disk-1][ring-1][sector-1][3][5]
            phiyphiy = cov_fromH[endcap-1][disk-1][ring-1][sector-1][4][4]
            phiyphiz = cov_fromH[endcap-1][disk-1][ring-1][sector-1][4][5]
            phizphiz = cov_fromH[endcap-1][disk-1][ring-1][sector-1][5][5]
            f_cov_fromHistXml.write("<operation>\n")
            f_cov_fromHistXml.write( "  <CSCChamber endcap=\"%s\" station=\"%s\" ring=\"%s\" chamber=\"%s\" />\n" % (endcap,disk,ring,sector) )
            f_cov_fromHistXml.write( "  <setape xx=\"%s\" xy=\"%s\" xz=\"%s\" yy=\"%s\" yz=\"%s\" zz=\"%s\" xa=\"%s\" xb=\"%s\" xc=\"%s\" ya=\"%s\" yb=\"%s\" yc=\"%s\" za=\"%s\" zb=\"%s\" zc=\"%s\" aa=\"%s\" ab=\"%s\" ac=\"%s\" bb=\"%s\" bc=\"%s\" cc=\"%s\" />\n" % (xx, xy, xz, yy, yz, zz, xphix, xphiy, xphiz, yphix, yphiy, yphiz, zphix, zphiy, zphiz, phixphix, phixphiy, phixphiz, phiyphiy, phiyphiz, phizphiz) )
            f_cov_fromHistXml.write("</operation>\n\n")
  #Closing files
  f_cov_APEsXml.write("</MuonAlignment>")
  f_cov_APEsXml.close()
  f_cov_APEs_t2Xml.write("</MuonAlignment>")
  f_cov_APEs_t2Xml.close()
  f_cov_APEs_allXml.write("</MuonAlignment>")
  f_cov_APEs_allXml.close()
  if not isData:
    f_cov_fromHistXml.write("</MuonAlignment>")
    f_cov_fromHistXml.close()
    f_cov_APEs_resizedXml.write("</MuonAlignment>")
    f_cov_APEs_resizedXml.close()
  print "You have",NfitFailed,"fits that have FAILED (if more than 0 be carefull because APE will be 0 for those)!"
