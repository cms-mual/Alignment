#!/usr/bin/env python
import numpy as np
import pandas as pd
import uproot
import ROOT, array, os, sys, re, math, random
from math import *
import argparse

sys.path.append('./File_useful/')
from File_useful.signConventions import *
from File_useful.geometryXMLparser import *
from File_useful.geometryXMLparser import MuonGeometry
from File_useful.plotscripts import *
from File_useful.Util_CalculateCovMatrix import *
from File_useful.ape_utils import wss_list, make_empty_wss_list, make_cov_fromH, get_cov_fit_from_fit, make_average_cov, write_xml

parser = argparse.ArgumentParser(description='Calculate APEs from alignment')
parser.add_argument('outname', help='output name')
parser.add_argument('xml', help='xml file from alignment')
parser.add_argument('report', help='report file from alignment')
parser.add_argument('--compgeom', default='Geom/muonGeometry_IDEAL_AllZeroes.Ape6x6.StdTags.746p3.DBv2.xml', help='Comparison geometry for MC')
parser.add_argument('--debug', default=False, action='store_true', help='print debug information')
parser.add_argument('--isDT', default=False, action='store_true', help='compute APEs for DTs') 
parser.add_argument('--isCSC', default=False, action='store_true', help='compute APEs for CSCs') 
parser.add_argument('--isData', default=False, action='store_true', help='compute APEs for Data') 
parser.add_argument('--is3DOF', default=False, action='store_true', help='compute 3DOF APEs') 
args = parser.parse_args()

assert args.isDT != args.isCSC, "Must be either isDT or isCSC"

#options
outName = args.outname
isDT = args.isDT
isData = args.isData
is3DOF = args.is3DOF
outname = args.outname
xmlfileORI = args.xml 
reportfile = args.report
xmfileIdealGeom = args.compgeom
debug = args.debug

# read geometry
exec(open(reportfile).read())
report = reports
g1 = MuonGeometry(xmlfileORI)
if not isData:
    gI = MuonGeometry(xmfileIdealGeom)

# calculate ideal ape
if isDT:
  # Covariance from Final-Ideal geoemtry
  if not isData:
    cov_fromH = make_cov_fromH(isData, g1, gI=gI)
    
  # APE from MINUIT and from comparing 2 geometries
  #For chamber that is an object described in the report file
  E_stat, M_FIT, NfitFailed = get_cov_fit_from_fit(report, is3DOF, debug=debug)

  #Now we have the Covariance matrix that give us: sigma_x(stat), sigma_y(stat)... and off-diagonal terms sigma_xy(stat), sigma_xz(stat)...
  #Off-diagonal terms can be written in term of correlation: rho_xy, rho_xz... where rho_xy=sigma_xy(stat)/(sigma_x(stat)*sigma_y(stat))
  cov_only, cov_only_times2, cov_only_all = make_average_cov(M_FIT)

  # Take the size from the APEs from the histogram and give it to one from MINUIT
  if not isData:
    cov_only_resizedFromH = resizeAPEs(cov_only,cov_fromH)

  write_xml('output/APEs_COV_DT_' + outName + '.xml', cov_only)
  write_xml('output/APEs_COV_t2_DT_' + outName + '.xml', cov_only_times2)
  write_xml('output/APEs_COVall_DT_' + outName + '.xml', cov_only_all)
  if not isData:
      write_xml('output/APEs_COVfromH_DT_' + outName + '.xml', cov_fromH)
      write_xml('output/APEs_COV_resized_DT_' + outName + '.xml', cov_only_resizedFromH)
      
  print("You have",NfitFailed,"fits that have FAILED (if more than 0 be carefull because APE will be 0 for those)!")
