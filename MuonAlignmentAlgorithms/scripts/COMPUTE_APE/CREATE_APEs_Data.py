import ROOT, array, os, sys, re, math, random
from math import *
execfile("geometryXMLparser.py")
execfile("plotscripts.py")
execfile("Util_CalculateCovMatrix.py")

#xmlfileORI  = "../data_DT-1100-111111_SingleMuon_Run2016E_MuAlCalIsolatedMu_276830_277420_8_0_17_NewTrackCov_v1_03/data_DT-1100-111111_SingleMuon_Run2016E_MuAlCalIsolatedMu_276830_277420_8_0_17_NewTrackCov_v1_03.xml"
#xmlfileCOMP = "../data_DT-1100-111111_SingleMuon_Run2016E_MuAlCalIsolatedMu_276830_277420_8_0_17_NewTrackCov_v1_03/data_DT-1100-111111_SingleMuon_Run2016E_MuAlCalIsolatedMu_276830_277420_8_0_17_NewTrackCov_v1_03.xml"
#reportfile  = "../data_DT-1100-111111_SingleMuon_Run2016E_MuAlCalIsolatedMu_276830_277420_8_0_17_NewTrackCov_v1_03/data_DT-1100-111111_SingleMuon_Run2016E_MuAlCalIsolatedMu_276830_277420_8_0_17_NewTrackCov_v1_03_report.py"
xmlfileORI   = "../data_DT-1100-111111_SingleMuon_Run2016E_MuAlCalIsolatedMu_276830_277420_8_0_17_NewBase_v1_03/data_DT-1100-111111_SingleMuon_Run2016E_MuAlCalIsolatedMu_276830_277420_8_0_17_NewBase_v1_03.xml"
xmlfileCOMP  = "../data_DT-1100-111111_SingleMuon_Run2016E_MuAlCalIsolatedMu_276830_277420_8_0_17_NewBase_v1_03/data_DT-1100-111111_SingleMuon_Run2016E_MuAlCalIsolatedMu_276830_277420_8_0_17_NewBase_v1_03.xml"
reportfile   = "../data_DT-1100-111111_SingleMuon_Run2016E_MuAlCalIsolatedMu_276830_277420_8_0_17_NewBase_v1_03/data_DT-1100-111111_SingleMuon_Run2016E_MuAlCalIsolatedMu_276830_277420_8_0_17_NewBase_v1_03_report.py"
#xmlfileORI  = "../mc_DT-1100-111111_CMSSW_8_0_17_ideal_45M_8TeV_v1_03/mc_DT-1100-111111_CMSSW_8_0_17_ideal_45M_8TeV_v1_03.xml"
#xmlfileCOMP = "../mc_DT-1100-111111_CMSSW_8_0_17_ideal_45M_8TeV_v1_03/mc_DT-1100-111111_CMSSW_8_0_17_ideal_45M_8TeV_v1_03.xml"
#reportfile  = "../mc_DT-1100-111111_CMSSW_8_0_17_ideal_45M_8TeV_v1_03/mc_DT-1100-111111_CMSSW_8_0_17_ideal_45M_8TeV_v1_03_report.py"
outName = "_6DOF_NEW"
is3DOF=False # This modify the extraction of the covariance elements
execfile(reportfile)
report = reports
g1 = MuonGeometry(xmlfileORI)
g2 = MuonGeometry(xmlfileCOMP)
debug=True

#Init
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
      # FIT cov matrix 
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
            if( (index>0 and index<7) or (index>12 and index<19) or (index>24 and index<31) or (index>36 and index<43) or (index>48 and index<(6*9+1)) or (index>60 and index<(6*11+1)) ): #or (index>72 and index<(6*13+1)) or (index>84 and index<(6*15+1)) or (index>96 and index<(6*17+1)) or (index>108 and index<(6*19+1)) or (index>120 and index<(6*21+1)) or (index>132 and index<(6*23+1)) or (index>144 and index<(6*25+1)) ) :
              E_stat.append(float(covItem)) # vector with 36 elements (is 6x6)
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
      # Differece with another geometry
      D_SL = []
      d12x_cm = (g1.dt[wheel, station, sector].x - g2.dt[wheel, station, sector].x)*signConventions["DT", wheel, station, sector][0]
      D_SL.append(d12x_cm); D_SL.append(0); D_SL.append(0); D_SL.append(0); D_SL.append(0); D_SL.append(0); 
      if ( station != 4 ) : d12y_cm = (g1.dt[wheel, station, sector].y - g2.dt[wheel, station, sector].y)*signConventions["DT", wheel, station, sector][1]
      else :                d12y_cm = 0.0
      D_SL.append(0); D_SL.append(d12y_cm); D_SL.append(0); D_SL.append(0); D_SL.append(0); D_SL.append(0); 
      d12z_cm = 0.0
      D_SL.append(0); D_SL.append(0); D_SL.append(d12z_cm); D_SL.append(0); D_SL.append(0); D_SL.append(0); 
      d12phix_rad = 0.0
      D_SL.append(0); D_SL.append(0); D_SL.append(0); D_SL.append(d12phix_rad); D_SL.append(0); D_SL.append(0); 
      d12phiy_rad = 0.0
      D_SL.append(0); D_SL.append(0); D_SL.append(0); D_SL.append(0); D_SL.append(d12phiy_rad); D_SL.append(0); 
      d12phiz_rad = (g1.dt[wheel, station, sector].phiz - g2.dt[wheel, station, sector].phiz)
      D_SL.append(0); D_SL.append(0); D_SL.append(0); D_SL.append(0); D_SL.append(0); D_SL.append(d12phiz_rad)
      # Save final quantities that have to be transformed in APE
      M_FIT[wheel+2][station-1][sector-1] = E_stat
      M_DIF[wheel+2][station-1][sector-1] = D_SL

covTot = []
for wheel in -2, -1, 0, +1, +2:
  covTot.append([])
  for station in 1, 2, 3, 4:
    covTot[wheel+2].append(None)

for wheel in -2, -1, 0, +1, +2:
  for station in 1, 2, 3, 4:
    print "\n********************************************************************"
    print "Group of chambers: wheel = %s, station = %s" % (wheel, station)
    print "********************************************************************"
    
    #print "FIT input data for wheel = %s, station = %s" % (wheel, station)
    #printM( M_FIT[wheel+2][station-1] )
    #print "Covariance Stat for wheel = %s, station = %s" % (wheel, station)
    cov_FIT = calculateCovStatMatrix( M_FIT[wheel+2][station-1] )
    
    #print "\nDIF input data for wheel = %s, station = %s" % (wheel, station)
    #printM( M_DIF[wheel+2][station-1] )
    #print "Covariance SL for wheel = %s, station = %s" % (wheel, station)
    cov_DIF = calculateCovMatrix( M_DIF[wheel+2][station-1] )

    covTot[wheel+2][station-1] = sumMatrix(cov_FIT, cov_DIF)
    #print "Total covariance matrix for wheel = %s, station = %s" % (wheel, station)
    #printCovMatrix( covTot[wheel+2][station-1] )    
    #print "\nSqrt from total covariance matrix for wheel = %s, station = %s" % (wheel, station)
    #printSqrtCovMatrix( covTot[wheel+2][station-1] )

print "\n--------------------------------------------------------------------"
print "                              SUMMARY                               "
print "--------------------------------------------------------------------\n"

for wheel in -2, -1, 0, +1, +2:
  for station in 1, 2, 3, 4:
    print "--------------------------------------------------------------------"
    print "Group of chambers: wheel = %s, station = %s" % (wheel, station)
    print "--------------------------------------------------------------------"
    
    print "Total covariance matrix for wheel = %s, station = %s" % (wheel, station)
    printCovMatrix( covTot[wheel+2][station-1] )

#Print APEs to XML file
f_AllAPEsXml = open('APEs_DT_Data_AllContributions_AllTypesOfApes' + outName + '.xml','w')
f_AllAPEsTxt = open('APEs_DT_Data_AllContributions_AllTypesOfApes' + outName + '.txt','w')
# DE means only "diagonal elements"
f_DE_AllAPEsXml = open('APEs_DE_DT_Data_AllContributions_AllTypesOfApes' + outName + '.xml','w')
f_DE_AllAPEsTxt = open('APEs_DE_DT_Data_AllContributions_AllTypesOfApes' + outName + '.txt','w')

f_AllAPEsXml.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n")
f_AllAPEsXml.write("<?xml-stylesheet type=\"text/xml\" href=\"MuonAlignment.xsl\"?>\n")
f_AllAPEsXml.write("<MuonAlignment>\n\n")
f_AllAPEsTxt.write("wheel station sector xx xy xz yy yz zz xphix xphiy xphiz yphix yphiy yphiz zphix zphiy zphiz phixphix phixphiy phixphiz phiyphiy phiyphiz phizphiz\n")

f_DE_AllAPEsXml.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n")
f_DE_AllAPEsXml.write("<?xml-stylesheet type=\"text/xml\" href=\"MuonAlignment.xsl\"?>\n")
f_DE_AllAPEsXml.write("<MuonAlignment>\n\n")
f_DE_AllAPEsTxt.write("wheel station sector xx xy xz yy yz zz xphix xphiy xphiz yphix yphiy yphiz zphix zphiy zphiz phixphix phixphiy phixphiz phiyphiy phiyphiz phizphiz\n")

for wheel in -2, -1, 0, +1, +2:
  for station in 1, 2, 3, 4:
    if station != 4: sectors = (1,2,3,4,5,6,7,8,9,10,11,12)
    else:            sectors = (1,2,3,4,5,6,7,8,9,10,11,12,13,14)
    for sector in sectors:
      
      xx = covTot[wheel+2][station-1][0][0]
      xy = covTot[wheel+2][station-1][0][1]
      xz = covTot[wheel+2][station-1][0][2]
      yy = covTot[wheel+2][station-1][1][1]
      yz = covTot[wheel+2][station-1][1][2]
      zz = covTot[wheel+2][station-1][2][2]
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
      f_AllAPEsTxt.write( "%s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s\n" % (wheel, station, sector, xx, xy, xz, yy, yz, zz, xphix, xphiy, xphiz, yphix, yphiy, yphiz, zphix, zphiy, zphiz, phixphix, phixphiy, phixphiz, phiyphiy, phiyphiz, phizphiz) )
      
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
      f_DE_AllAPEsTxt.write( "%s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s\n" % (wheel, station, sector, xx, xy, xz, yy, yz, zz, xphix, xphiy, xphiz, yphix, yphiy, yphiz, zphix, zphiy, zphiz, phixphix, phixphiy, phixphiz, phiyphiy, phiyphiz, phizphiz) )
      
f_AllAPEsXml.write("</MuonAlignment>")
f_AllAPEsXml.close()
f_AllAPEsTxt.close()
f_DE_AllAPEsXml.write("</MuonAlignment>")
f_DE_AllAPEsXml.close()
f_DE_AllAPEsTxt.close()
