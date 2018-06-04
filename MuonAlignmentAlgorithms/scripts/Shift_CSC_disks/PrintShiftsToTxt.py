import subprocess, time, sys, os
from ShiftCSCGeometry_Fn import *

# First alignment provided after shut down
file = "../data_CSC-1100-100001_CMSSW_9_2_1_SingleMuon_MuAlCalIsolatedMuv1_294927_297723_GPRv1_01/data_CSC-1100-100001_CMSSW_9_2_1_SingleMuon_MuAlCalIsolatedMuv1_294927_297723_GPRv1_01_plotting.root"
# Outputs
outFileName = "ShiftList.txt"

# Get the shifts to insert
corr_1_1_1 = get_Corr(file,"p","+","1","1")
corr_1_1_2 = get_Corr(file,"p","+","1","2")
corr_1_1_3 = get_Corr(file,"p","+","1","3")
corr_1_1_4 = corr_1_1_1
corr_1_2_1 = get_Corr(file,"p","+","2","1")
corr_1_2_2 = get_Corr(file,"p","+","2","2")
corr_1_3_1 = get_Corr(file,"p","+","3","1")
corr_1_3_2 = get_Corr(file,"p","+","3","2")
corr_1_4_1 = get_Corr(file,"p","+","4","1")
corr_1_4_2 = get_Corr(file,"p","+","4","2")
corr_2_1_1 = get_Corr(file,"m","-","1","1")
corr_2_1_2 = get_Corr(file,"m","-","1","2")
corr_2_1_3 = get_Corr(file,"m","-","1","3")
corr_2_1_4 = corr_2_1_1
corr_2_2_1 = get_Corr(file,"m","-","2","1")
corr_2_2_2 = get_Corr(file,"m","-","2","2")
corr_2_3_1 = get_Corr(file,"m","-","3","1")
corr_2_3_2 = get_Corr(file,"m","-","3","2")
corr_2_4_1 = get_Corr(file,"m","-","4","1")
corr_2_4_2 = get_Corr(file,"m","-","4","2")

# Now Print them to the txt file
txtfile = open(outFileName, 'w')
txtfile.write('  Chamber   DX  -DY\n')
txtfile.write('corr_1_1_1 ' + str(corr_1_1_1[0]) + " " + str(corr_1_1_1[1]) + '\n')
txtfile.write('corr_1_1_2 ' + str(corr_1_1_2[0]) + " " + str(corr_1_1_2[1]) + '\n')
txtfile.write('corr_1_1_3 ' + str(corr_1_1_3[0]) + " " + str(corr_1_1_3[1]) + '\n')
txtfile.write('corr_1_1_4 ' + str(corr_1_1_4[0]) + " " + str(corr_1_1_4[1]) + '\n')
txtfile.write('corr_1_2_1 ' + str(corr_1_2_1[0]) + " " + str(corr_1_2_1[1]) + '\n')
txtfile.write('corr_1_2_2 ' + str(corr_1_2_2[0]) + " " + str(corr_1_2_2[1]) + '\n')
txtfile.write('corr_1_3_1 ' + str(corr_1_3_1[0]) + " " + str(corr_1_3_1[1]) + '\n')
txtfile.write('corr_1_3_2 ' + str(corr_1_3_2[0]) + " " + str(corr_1_3_2[1]) + '\n')
txtfile.write('corr_1_4_1 ' + str(corr_1_4_1[0]) + " " + str(corr_1_4_1[1]) + '\n')
txtfile.write('corr_1_4_2 ' + str(corr_1_4_2[0]) + " " + str(corr_1_4_2[1]) + '\n')
txtfile.write('corr_2_1_1 ' + str(corr_2_1_1[0]) + " " + str(corr_2_1_1[1]) + '\n')
txtfile.write('corr_2_1_2 ' + str(corr_2_1_2[0]) + " " + str(corr_2_1_2[1]) + '\n')
txtfile.write('corr_2_1_3 ' + str(corr_2_1_3[0]) + " " + str(corr_2_1_3[1]) + '\n')
txtfile.write('corr_2_1_4 ' + str(corr_2_1_4[0]) + " " + str(corr_2_1_4[1]) + '\n')
txtfile.write('corr_2_2_1 ' + str(corr_2_2_1[0]) + " " + str(corr_2_2_1[1]) + '\n')
txtfile.write('corr_2_2_2 ' + str(corr_2_2_2[0]) + " " + str(corr_2_2_2[1]) + '\n')
txtfile.write('corr_2_3_1 ' + str(corr_2_3_1[0]) + " " + str(corr_2_3_1[1]) + '\n')
txtfile.write('corr_2_3_2 ' + str(corr_2_3_2[0]) + " " + str(corr_2_3_2[1]) + '\n')
txtfile.write('corr_2_4_1 ' + str(corr_2_4_1[0]) + " " + str(corr_2_4_1[1]) + '\n')
txtfile.write('corr_2_4_2 ' + str(corr_2_4_2[0]) + " " + str(corr_2_4_2[1]) + '\n')
txtfile.close()
