import random
import re
random.seed(123456)

fileName="data_DT-1100-110001_SingleMuon_Run2016E_MuAlCalIsolatedMu_276830_277420_8_0_17_NewTrack_v1_03_NOGPR"
fileName_NEW=fileName+"_Z15mm"
sigmax = 0.0 #in cm
sigmay = 0.0
sigmaz = 1.5
sigmaphix = 0.00000 #in mrad
sigmaphiy = 0.00000
sigmaphiz = 0.00000
out_f=open(fileName_NEW+'.xml','w')

with open(fileName+'.xml','r') as f:
  for line in f:
    newLine = line
    if '" z="' in line:
      print newLine
      z = random.gauss(0., sigmaz)
      #Find the old Z value
      index_init = line.find('" z="')
      index_init = int(index_init) + 5
      index_end  = line.find('" phix="')
      index_end  = int(index_end) 
      old_z = line[index_init:index_end]
      num_decimals=old_z[::-1].find('.')
      print old_z
      #Now smear it
      new_z = round(float(old_z) + z,num_decimals)
      print new_z
      newLine = line[0:index_init] + str(new_z) + line[index_end:]
      print newLine
      out_f.write(newLine)
    else:
      out_f.write(newLine)
out_f.close()
