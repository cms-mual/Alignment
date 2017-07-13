import ROOT, array, os, sys, re, math, random
from math import *
sys.path.insert(0, '../Alignment/MuonAlignmentAlgorithms/scripts/')
from ShiftCSCGeometry_Fn import *

# Inputs
DbFile       = "data_CSC-1100-110001_SingleMuon_Run2016G_MuAlCalIsolatedMu_278820_280385_8_0_24_Rerecov1_03" #DB you used to start alignment (before shut down)
# We should use always inert in order to do not double count GPR
gprcdconnect = "inertGlobalPositionRcd.StdTags.746p3.DBv2.db"#"GPR_July3_2017_SW924_Run2017B_dL4_iter1.db"
gprcd        = "inertGlobalPositionRcd"#"IdealGeometry"

Run          = "1"
Tag_ToGlobal = "_ToGlobal"
xmlfile1     = DbFile + Tag_ToGlobal + ".xml"
OutDB        = "data_CSC-1100-110001_SingleMuon_Run2016G_MuAlCalIsolatedMu_278820_280385_8_0_24_Rerecov1_03_CSCRingAlignment.db" #Final .DB to use in next alignment

#Creating a XML from the initial geom.DB that is referred to Global.
comm1 = '../Alignment/MuonAlignmentAlgorithms/scripts/convertSQLiteXML.py ' + DbFile + '.db ' + DbFile + Tag_ToGlobal + '.xml --gprcdconnect sqlite_file:'+ gprcdconnect + ' --gprcd ' + gprcd + ' --relativeTo none'
print 'Executing: ' + comm1
Conv_comm = subprocess.Popen([comm1], stdout=subprocess.PIPE, shell=True);
Conv_comm.wait()
print "You just created: " + DbFile + Tag_ToGlobal + ".xml, that is the new XML referred to global position."

#Now I'm creating the shifed XML file
execfile("../Alignment/MuonAlignmentAlgorithms/scripts/geometryXMLparser.py")
g1 = MuonGeometry(xmlfile1)

with open("ShiftList.txt") as f:
    content = f.readlines()

#*******************************************************************************
# Endcap 1                                                                      
#-------------------------------------------------------------------------------
# First Iron Disk
sinPhi_1_1_1 = float(content[1].split()[1])
cosPhi_1_1_1 = float(content[1].split()[2])
sinPhi_1_1_2 = float(content[2].split()[1])
cosPhi_1_1_2 = float(content[2].split()[2])
sinPhi_1_1_3 = float(content[3].split()[1])
cosPhi_1_1_3 = float(content[3].split()[2])
#sinPhi_1_1_2 = sinPhi_1_1_1
#cosPhi_1_1_2 = cosPhi_1_1_1
#sinPhi_1_1_3 = sinPhi_1_1_1
#cosPhi_1_1_3 = cosPhi_1_1_1

#-------------------------------------------------------------------------------
# Second Iron Disk
sinPhi_1_2_1 = float(content[5].split()[1])
cosPhi_1_2_1 = float(content[5].split()[2])
sinPhi_1_2_2 = float(content[6].split()[1])
cosPhi_1_2_2 = float(content[6].split()[2])
sinPhi_1_3_1 = float(content[7].split()[1])
cosPhi_1_3_1 = float(content[7].split()[2])
sinPhi_1_3_2 = float(content[8].split()[1])
cosPhi_1_3_2 = float(content[8].split()[2])
#sinPhi_1_2 = (sinPhi_1_2_1 + sinPhi_1_3_1)/2.0
#cosPhi_1_2 = (cosPhi_1_2_1 + cosPhi_1_3_1)/2.0
#sinPhi_1_2_1 = sinPhi_1_2
#cosPhi_1_2_1 = cosPhi_1_2
#sinPhi_1_2_2 = sinPhi_1_2
#cosPhi_1_2_2 = cosPhi_1_2
#sinPhi_1_3_1 = sinPhi_1_2
#cosPhi_1_3_1 = cosPhi_1_2
#sinPhi_1_3_2 = sinPhi_1_2
#cosPhi_1_3_2 = cosPhi_1_2

#-------------------------------------------------------------------------------
# Third Iron Disk
sinPhi_1_4_1 = float(content[9].split()[1])
cosPhi_1_4_1 = float(content[9].split()[2])
# Align ME4/2 independently from ME4/1 because ME4/2 newly installed chambers
sinPhi_1_4_2 = float(content[10].split()[1])
cosPhi_1_4_2 = float(content[10].split()[2])
#*******************************************************************************
# Endcap 2                                                                      
#-------------------------------------------------------------------------------
# First Iron Disk
sinPhi_2_1_1 = float(content[11].split()[1])
cosPhi_2_1_1 = float(content[11].split()[2])
sinPhi_2_1_2 = float(content[12].split()[1])
cosPhi_2_1_2 = float(content[12].split()[2])
sinPhi_2_1_3 = float(content[13].split()[1])
cosPhi_2_1_3 = float(content[13].split()[2])
#sinPhi_2_1_2 = sinPhi_2_1_1
#cosPhi_2_1_2 = cosPhi_2_1_1
#sinPhi_2_1_3 = sinPhi_2_1_1
#cosPhi_2_1_3 = cosPhi_2_1_1

#-------------------------------------------------------------------------------
# Second Iron Disk
sinPhi_2_2_1 = float(content[15].split()[1])
cosPhi_2_2_1 = float(content[15].split()[2])
sinPhi_2_2_2 = float(content[16].split()[1])
cosPhi_2_2_2 = float(content[16].split()[2])
sinPhi_2_3_1 = float(content[17].split()[1])
cosPhi_2_3_1 = float(content[17].split()[2])
sinPhi_2_3_2 = float(content[18].split()[1])
cosPhi_2_3_2 = float(content[18].split()[2])
#sinPhi_2_2 = (sinPhi_2_2_1 + sinPhi_2_3_1)/2.0
#cosPhi_2_2 = (cosPhi_2_2_1 + cosPhi_2_3_1)/2.0
#sinPhi_2_2_1 = sinPhi_2_2
#cosPhi_2_2_1 = cosPhi_2_2
#sinPhi_2_2_2 = sinPhi_2_2
#cosPhi_2_2_2 = cosPhi_2_2
#sinPhi_2_3_1 = sinPhi_2_2
#cosPhi_2_3_1 = cosPhi_2_2
#sinPhi_2_3_2 = sinPhi_2_2
#cosPhi_2_3_2 = cosPhi_2_2

#-------------------------------------------------------------------------------
# Third Iron Disk
sinPhi_2_4_1 = float(content[19].split()[1])
cosPhi_2_4_1 = float(content[19].split()[2])
# Align ME4/2 independently from ME4/1 because ME4/2 newly installed chambers
sinPhi_2_4_2 = float(content[20].split()[1])
cosPhi_2_4_2 = float(content[20].split()[2])
#*******************************************************************************

outFileName = xmlfile1 + ".CSC_Shifted.xml"
outFile = open(outFileName, 'w')

outFile.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n")
outFile.write("<?xml-stylesheet type=\"text/xml\" href=\"MuonAlignment.xsl\"?>\n")
outFile.write("<MuonAlignment>\n")
outFile.write("\n")

for endcap in 1,2:
  for disk in 1, 2, 3, 4:
    if disk == 1: rings = (1,2,3,4)
    else:         rings = (1,2)
    for ring in rings:
      
      if (endcap == 1 and disk == 1 and (ring == 1 or ring ==4) ):
        sinPhi = sinPhi_1_1_1
        cosPhi = cosPhi_1_1_1
      if (endcap == 1 and disk == 1 and ring == 2 ):
        sinPhi = sinPhi_1_1_2
        cosPhi = cosPhi_1_1_2
      if (endcap == 1 and disk == 1 and ring == 3 ):
        sinPhi = sinPhi_1_1_3
        cosPhi = cosPhi_1_1_3
      if (endcap == 1 and disk == 2 and ring == 1 ):
        sinPhi = sinPhi_1_2_1
        cosPhi = cosPhi_1_2_1
      if (endcap == 1 and disk == 2 and ring == 2 ):
        sinPhi = sinPhi_1_2_2
        cosPhi = cosPhi_1_2_2
      if (endcap == 1 and disk == 3 and ring == 1 ):
        sinPhi = sinPhi_1_3_1
        cosPhi = cosPhi_1_3_1
      if (endcap == 1 and disk == 3 and ring == 2 ):
        sinPhi = sinPhi_1_3_2
        cosPhi = cosPhi_1_3_2
      if (endcap == 1 and disk == 4 and ring == 1 ):
        sinPhi = sinPhi_1_4_1
        cosPhi = cosPhi_1_4_1
      if (endcap == 1 and disk == 4 and ring == 2 ):
        sinPhi = sinPhi_1_4_2
        cosPhi = cosPhi_1_4_2
      
      if (endcap == 2 and disk == 1 and (ring == 1 or ring ==4) ):
        sinPhi = sinPhi_2_1_1
        cosPhi = cosPhi_2_1_1
      if (endcap == 2 and disk == 1 and ring == 2 ):
        sinPhi = sinPhi_2_1_2
        cosPhi = cosPhi_2_1_2
      if (endcap == 2 and disk == 1 and ring == 3 ):
        sinPhi = sinPhi_2_1_3
        cosPhi = cosPhi_2_1_3
      if (endcap == 2 and disk == 2 and ring == 1 ):
        sinPhi = sinPhi_2_2_1
        cosPhi = cosPhi_2_2_1
      if (endcap == 2 and disk == 2 and ring == 2 ):
        sinPhi = sinPhi_2_2_2
        cosPhi = cosPhi_2_2_2
      if (endcap == 2 and disk == 3 and ring == 1 ):
        sinPhi = sinPhi_2_3_1
        cosPhi = cosPhi_2_3_1
      if (endcap == 2 and disk == 3 and ring == 2 ):
        sinPhi = sinPhi_2_3_2
        cosPhi = cosPhi_2_3_2
      if (endcap == 2 and disk == 4 and ring == 1 ):
        sinPhi = sinPhi_2_4_1
        cosPhi = cosPhi_2_4_1
      if (endcap == 2 and disk == 4 and ring == 2 ):
        sinPhi = sinPhi_2_4_2
        cosPhi = cosPhi_2_4_2
      
      # Convert mm to cm
      sinPhi_cm = 0.1*sinPhi
      cosPhi_cm = 0.1*cosPhi
      
      if disk != 1 and ring == 1: chambers = range(1,18+1,1)
      else:                       chambers = range(1,36+1,1)
      for chamber in chambers:
        x = g1.csc[endcap, disk, ring, chamber].x + sinPhi_cm
        y = g1.csc[endcap, disk, ring, chamber].y - cosPhi_cm
        z = g1.csc[endcap, disk, ring, chamber].z
        phix = g1.csc[endcap, disk, ring, chamber].phix
        phiy = g1.csc[endcap, disk, ring, chamber].phiy
        phiz = g1.csc[endcap, disk, ring, chamber].phiz
        outFile.write("<operation>\n")
        outFile.write("  <CSCChamber endcap=\"%s\" station=\"%s\" ring=\"%s\" chamber=\"%s\" />\n" % ( endcap, disk, ring, chamber ) )
        outFile.write("  <setposition relativeto=\"none\" x=\"%.10f\" y=\"%.10f\" z=\"%.10f\" phix=\"%.10f\" phiy=\"%.10f\" phiz=\"%.10f\" />\n" % ( x, y, z, phix, phiy, phiz ) )
        outFile.write("  <setape xx=\"0.0000000000\" xy=\"0.0000000000\" xz=\"0.0000000000\" xa=\"0.0000000000\" xb=\"0.0000000000\" xc=\"0.0000000000\" yy=\"0.0000000000\" yz=\"0.0000000000\" ya=\"0.0000000000\" yb=\"0.0000000000\" yc=\"0.0000000000\" zz=\"0.0000000000\" za=\"0.0000000000\" zb=\"0.0000000000\" zc=\"0.0000000000\" aa=\"0.0000000000\" ab=\"0.0000000000\" ac=\"0.0000000000\" bb=\"0.0000000000\" bc=\"0.0000000000\" cc=\"0.0000000000\"  />\n")
        outFile.write("</operation>\n")
        outFile.write("\n")

outFile.write("</MuonAlignment>\n")

# Cretaing cfg file to convert .xml in .db
convertXMLtoSQLite = open( "CSCshift_ConvertXMLtoSQLite_cfg.py", 'w' )
writeXML_DB_Converter(convertXMLtoSQLite, outFileName, OutDB, gprcdconnect , gprcd, Run )
print 'To convert the XML to DB, please do "cmsRun CSCshift_ConvertXMLtoSQLite_cfg.py"'

sys.exit(0)
