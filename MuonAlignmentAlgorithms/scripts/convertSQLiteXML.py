#! /usr/bin/env python

import os, sys, optparse, math

prog = sys.argv[0]

usage = """%(prog)s INPUT_FILE OUTPUT_FILE [--noChambers] [--noLayers] [--ringsOnly] [--relativeTo ideal|none]

performs either sqlite-->xml or xml-->sqlite conversion following the documentation at 
https://twiki.cern.ch/twiki/bin/view/CMS/SWGuideMuonGeometryConversion

Arguments:

INPUT_FILE      is either .db SQLite or .xml file that should be converted
OUTPUT_FILE     is either .xml or .db output file, the result of conversion

Options for sqlite-->xml conversion:

--noChambers    if present, no chambers info would be written into xml
--noLayers      if present, no layers (and no DT superlayers) info would be written into xml
--relativeTo X  by default, xml conversion is done relative to ideal DDD description,
                if "none" is specified, absolute positions would be written into xml
--ringsOnly     special flag for xml dumping of CSC ring structure only, it automatically
                turns off all DTs and also CSC's chambers and layers on output and coordinates
                are relative "to none"
--runNumber N   Use run #N to extract xml from necessary IOV
""" % vars()

if len(sys.argv) < 3:
  print "Too few arguments!\n\n"+usage
  sys.exit()

parser=optparse.OptionParser(usage)

parser.add_option("--noChambers",
  help="if present, no chambers info would be written into xml",
  action="store_true",
  default=False,
  dest="noChambers")

parser.add_option("--noLayers",
  help="if present, no layers (and no DT superlayers) info would be written into xml",
  action="store_true",
  default=False,
  dest="noLayers")

parser.add_option("-l", "--relativeTo",
  help="by default, xml conversion is done relative to ideal DDD description, if \"none\" is specified, absolute positions would be written into xml",
  type="string",
  default='ideal',
  dest="relativeTo")

parser.add_option("--ringsOnly",
  help="special flag for xml dumping of CSC ring structure only, it automatically turns off all DTs and also CSC's chambers and layers",
  action="store_true",
  default=False,
  dest="ringsOnly")

parser.add_option("-r", "--runNumber",
  help="Use run #N to extract xml from necessary IOV (default is 1)",
  type="int",
  default=1,
  dest="runNumber")

parser.add_option("--gprcdconnect",
  help="connect string for GlobalPositionRcd (frontier://... or sqlite_file:...). The defailt is a trivial/inert GPR",
  type="string",
  default="sqlite_file:inertGlobalPositionRcd.db",
  dest="gprcdconnect")

parser.add_option("--gprcd",
  help="name of GlobalPositionRcd tag",
  type="string",
  default="inertGlobalPositionRcd",
  dest="gprcd")


options, args = parser.parse_args(sys.argv[3:])

supRings="True"
if options.ringsOnly: supRings="False"
supChambers="False"
if options.noChambers or options.ringsOnly: supChambers="True"
supLayers="False"
if options.noLayers or options.ringsOnly: supLayers="True"

relativeTo=options.relativeTo
if options.ringsOnly: relativeTo="none"

runNumber = options.runNumber
gprcdconnect = options.gprcdconnect
gprcd = options.gprcd

theInputFile = sys.argv[1]
theOutputFile = sys.argv[2]

ok = False

if theInputFile[-4:]==".xml" and theOutputFile[-3:]==".db":
  ok = True
  file("tmp_converter_cfg.py","w").write("""
import FWCore.ParameterSet.Config as cms
import sys

process = cms.Process('CONVERT')
process.source = cms.Source('EmptySource',firstRun = cms.untracked.uint32(1))
process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(1))

process.load('Configuration.Geometry.GeometryIdeal_cff')
process.load('Configuration.StandardSequences.DD4hep_GeometrySim_cff')

process.DTGeometryAlInputXML = cms.ESProducer("DTGeometryESModule",
    appendToDataLabel = cms.string('idealForInputXML'),
    applyAlignment = cms.bool(False),
    alignmentsLabel = cms.string(''),
    fromDDD = cms.bool(False),
    fromDD4hep = cms.bool(True)
)

process.CSCGeometryAlInputXML = cms.ESProducer("CSCGeometryESModule",
    appendToDataLabel = cms.string('idealForInputXML'),
    fromDDD = cms.bool(False),
    fromDD4hep = cms.bool(True),
    alignmentsLabel = cms.string(''),
    useRealWireGeometry = cms.bool(True),
    useOnlyWiresInME1a = cms.bool(False),
    useGangedStripsInME1a = cms.bool(True),
    useCentreTIOffsets = cms.bool(False),
    applyAlignment = cms.bool(False),
    debugV = cms.untracked.bool(False)
)

process.MuonGeometryDBConverter = cms.EDAnalyzer('MuonGeometryDBConverter',
    input = cms.string('xml'),
    fileName = cms.string('%(theInputFile)s'),
    shiftErr = cms.double(1000.),
    angleErr = cms.double(6.28),
    output = cms.string('db'))

from CondCore.CondDB.CondDB_cfi import *
CondDBSetup = CondDB.clone()
CondDBSetup.__delattr__('connect')
process.PoolDBOutputService = cms.Service('PoolDBOutputService',
    CondDBSetup,
    connect = cms.string('sqlite_file:%(theOutputFile)s'),
    toPut = cms.VPSet(
        cms.PSet(record = cms.string('DTAlignmentRcd'), tag = cms.string('DTAlignmentRcd')),
        cms.PSet(record = cms.string('DTAlignmentErrorExtendedRcd'), tag = cms.string('DTAlignmentErrorExtendedRcd')),
        cms.PSet(record = cms.string('CSCAlignmentRcd'), tag = cms.string('CSCAlignmentRcd')),
        cms.PSet(record = cms.string('CSCAlignmentErrorExtendedRcd'), tag = cms.string('CSCAlignmentErrorExtendedRcd'))))

process.inertGlobalPositionRcd = cms.ESSource('PoolDBESSource',
    CondDBSetup,
    connect = cms.string('%(gprcdconnect)s'),
    toGet = cms.VPSet(cms.PSet(record = cms.string('GlobalPositionRcd'), tag = cms.string('%(gprcd)s'))))

process.Path = cms.Path(process.MuonGeometryDBConverter)
""" % vars())

if theInputFile[-3:]==".db" and theOutputFile[-4:]==".xml":
  ok = True
  file("tmp_converter_cfg.py","w").write("""# sqlite2xml conversion
from Alignment.MuonAlignment.convertSQLitetoXML_cfg import *

process.load('Configuration.Geometry.GeometryIdeal_cff')
process.load('Configuration.StandardSequences.DD4hep_GeometrySim_cff')

process.DTGeometryAlInputDB = cms.ESProducer("DTGeometryESModule",
    appendToDataLabel = cms.string('idealForInputDB'),
    applyAlignment = cms.bool(False),
    alignmentsLabel = cms.string(''),
    fromDDD = cms.bool(False),
    fromDD4hep = cms.bool(True)
)

process.CSCGeometryAlInputDB = cms.ESProducer("CSCGeometryESModule",
    appendToDataLabel = cms.string('idealForInputDB'),
    fromDDD = cms.bool(False),
    fromDD4hep = cms.bool(True),
    alignmentsLabel = cms.string(''),
    useRealWireGeometry = cms.bool(True),
    useOnlyWiresInME1a = cms.bool(False),
    useGangedStripsInME1a = cms.bool(True),
    useCentreTIOffsets = cms.bool(False),
    applyAlignment = cms.bool(False),
    debugV = cms.untracked.bool(False)
)

process.DTGeometryAlOutputXML = cms.ESProducer("DTGeometryESModule",
    appendToDataLabel = cms.string('idealForOutputXML'),
    applyAlignment = cms.bool(False),
    alignmentsLabel = cms.string(''),
    fromDDD = cms.bool(False),
    fromDD4hep = cms.bool(True)
)

process.CSCGeometryAlOutputXML = cms.ESProducer("CSCGeometryESModule",
    appendToDataLabel = cms.string('idealForOutputXML'),
    fromDDD = cms.bool(False),
    fromDD4hep = cms.bool(True),
    alignmentsLabel = cms.string(''),
    useRealWireGeometry = cms.bool(True),
    useOnlyWiresInME1a = cms.bool(False),
    useGangedStripsInME1a = cms.bool(True),
    useCentreTIOffsets = cms.bool(False),
    applyAlignment = cms.bool(False),
    debugV = cms.untracked.bool(False)
)

process.source = cms.Source("EmptySource",
    numberEventsInRun = cms.untracked.uint32(1),
    firstRun = cms.untracked.uint32(%(runNumber)d)
)

process.inertGlobalPositionRcd.connect = "%(gprcdconnect)s"
process.inertGlobalPositionRcd.toGet =  cms.VPSet(cms.PSet(record = cms.string('GlobalPositionRcd'), tag = cms.string('%(gprcd)s')))

process.PoolDBESSource.connect = "sqlite_file:%(theInputFile)s"
process.MuonGeometryDBConverter.outputXML.fileName = "%(theOutputFile)s"

process.MuonGeometryDBConverter.outputXML.relativeto = "%(relativeTo)s"

process.MuonGeometryDBConverter.outputXML.suppressDTBarrel = True
process.MuonGeometryDBConverter.outputXML.suppressDTWheels = True
process.MuonGeometryDBConverter.outputXML.suppressDTStations = True
process.MuonGeometryDBConverter.outputXML.suppressDTChambers = %(supChambers)s
process.MuonGeometryDBConverter.outputXML.suppressDTSuperLayers = %(supLayers)s
process.MuonGeometryDBConverter.outputXML.suppressDTLayers = %(supLayers)s

process.MuonGeometryDBConverter.outputXML.suppressCSCEndcaps = True
process.MuonGeometryDBConverter.outputXML.suppressCSCStations = True
process.MuonGeometryDBConverter.outputXML.suppressCSCRings = %(supRings)s
process.MuonGeometryDBConverter.outputXML.suppressCSCChambers = %(supChambers)s
process.MuonGeometryDBConverter.outputXML.suppressCSCLayers = %(supLayers)s

""" % vars())

if not ok:
  print usage
  sys.exit()

exit_code = os.system("cmsRun tmp_converter_cfg.py")

if exit_code>0:
  print "problem: cmsRun exited with code:", exit_code
else: 
  os.system("rm tmp_converter_cfg.py")
