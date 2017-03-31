import FWCore.ParameterSet.Config as cms
import sys

process = cms.Process('CONVERT')
process.source = cms.Source('EmptySource',firstRun = cms.untracked.uint32(1))
process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(1))

process.load('Configuration.Geometry.GeometryIdeal_cff')
process.load('Geometry.MuonNumbering.muonNumberingInitialization_cfi')

process.MuonGeometryDBConverter = cms.EDAnalyzer('MuonGeometryDBConverter',
    input = cms.string('xml'),
    fileName = cms.string('MuonGeometry_MC_Run2Startup_June2015_Csc2mm1mrad_DtHWUnct_v1.StdTags.746p3.DBv2_ME14asME11.xml'),
    shiftErr = cms.double(1000.),
    angleErr = cms.double(6.28),
    output = cms.string('db'))

process.load('CondCore.DBCommon.CondDBSetup_cfi')
process.PoolDBOutputService = cms.Service('PoolDBOutputService',
    process.CondDBSetup,
    connect = cms.string('sqlite_file:MuonGeometry_MC_Run2Startup_June2015_Csc2mm1mrad_DtHWUnct_v1.StdTags.746p3.DBv2_ME14asME11.db'),
    toPut = cms.VPSet(
        cms.PSet(record = cms.string('DTAlignmentRcd'), tag = cms.string('DTAlignmentRcd')),
        cms.PSet(record = cms.string('DTAlignmentErrorExtendedRcd'), tag = cms.string('DTAlignmentErrorExtendedRcd')),
        cms.PSet(record = cms.string('CSCAlignmentRcd'), tag = cms.string('CSCAlignmentRcd')),
        cms.PSet(record = cms.string('CSCAlignmentErrorExtendedRcd'), tag = cms.string('CSCAlignmentErrorExtendedRcd'))))

process.inertGlobalPositionRcd = cms.ESSource('PoolDBESSource',
    process.CondDBSetup,
    connect = cms.string('sqlite_file:inertGlobalPositionRcd.StdTags.746p3.DBv2.db'),
    toGet = cms.VPSet(cms.PSet(record = cms.string('GlobalPositionRcd'), tag = cms.string('inertGlobalPositionRcd'))))

process.Path = cms.Path(process.MuonGeometryDBConverter)
