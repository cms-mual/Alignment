import ROOT, array, os, sys, re, math, random
from math import *

reportfile   = "mc_DT-1100-111111_CMSSW_8_0_24_GTasym_45M_8TeV_misall_03_report.py"
outName = "mc_DT-1100-111111_CMSSW_8_0_24_GTasym_45M_8TeV_misall_03_sigmas.txt"
outFile = open(outName,'w')
execfile(reportfile)
report = reports
debug=True

# Initialize my sigma container
Sigma_c = []
for wheel in -2, -1, 0, +1, +2:
  Sigma_c.append([])
  for station in 1, 2, 3, 4:
    Sigma_c[wheel+2].append([])
    if station != 4:
      for sector in 1,2,3,4,5,6,7,8,9,10,11,12:
        Sigma_c[wheel+2][station-1].append(None)
    else:
      for sector in 1,2,3,4,5,6,7,8,9,10,11,12,13,14:
        Sigma_c[wheel+2][station-1].append(None)
# Now exctract them from the reportfile
NfitFailed=0
for r in report:
  index=1
  if ( r.postal_address[0] == "DT" and r.status == "PASS") :
    wheel   = r.postal_address[1]
    station = r.postal_address[2]
    sector  = r.postal_address[3]
    if(debug): print "0)", wheel, station, sector
    sig = []
    if(station!=4):
      if(debug): print "1a)", r.sigmax, r.sigmay
      sx = str(r.sigmax).split()[0]; sy = str(r.sigmay).split()[0];
      if(debug): print "1b)", sx, sy
      sig.append(sx); sig.append(sy);
      outFile.write(str(wheel) + "_" + str(station) + "_" + str(sector) + " " + str(sx) + " " + str(sy) + "\n" )
    else:
      if(debug): print "1a)", r.sigmaresid
      si = str(r.sigmaresid).split()[0]
      if(debug): print "1b)", si
      sig.append(si)
      outFile.write(str(wheel) + "_" + str(station) + "_" + str(sector) + " " + str(si) + "\n" )
    Sigma_c[wheel+2][station-1][sector-1] = sig
  elif( r.postal_address[0] == "DT" and r.status != "PASS" ):
    NfitFailed=NfitFailed+1

outFile.close()
print "You have",NfitFailed,"fits that have FAILED (if more than 0 be carefull because APE will be 0 for those)!"
