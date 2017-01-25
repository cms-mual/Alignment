import FWCore.ParameterSet.Config as cms
import sys

process = cms.Process('CONVERT')
process.source = cms.Source('EmptySource',firstRun = cms.untracked.uint32(1))
process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(1))

process.load('Configuration.Geometry.GeometryIdeal_cff')
process.load('Geometry.MuonNumbering.muonNumberingInitialization_cfi')

process.MuonGeometryDBConverter = cms.EDAnalyzer('MuonGeometryDBConverter',
    input = cms.string('xml'),
    fileName = cms.string('data_DT-1100-110001_SingleMuon_Run2016E_MuAlCalIsolatedMu_276830_277420_8_0_17_NewTrack_v1_03_NOGPR_Z15mm.xml'),
    shiftErr = cms.double(1000.),
    angleErr = cms.double(6.28),
    output = cms.string('db'))

process.load('CondCore.DBCommon.CondDBSetup_cfi')
process.PoolDBOutputService = cms.Service('PoolDBOutputService',
    process.CondDBSetup,
    connect = cms.string('sqlite_file:data_DT-1100-110001_SingleMuon_Run2016E_MuAlCalIsolatedMu_276830_277420_8_0_17_NewTrack_v1_03_NOGPR_Z15mm.db'),
    toPut = cms.VPSet(
        cms.PSet(record = cms.string('DTAlignmentRcd'), tag = cms.string('DTAlignmentRcd')),
        cms.PSet(record = cms.string('DTAlignmentErrorExtendedRcd'), tag = cms.string('DTAlignmentErrorExtendedRcd')),
        cms.PSet(record = cms.string('CSCAlignmentRcd'), tag = cms.string('CSCAlignmentRcd')),
        cms.PSet(record = cms.string('CSCAlignmentErrorExtendedRcd'), tag = cms.string('CSCAlignmentErrorExtendedRcd'))))

process.inertGlobalPositionRcd = cms.ESSource('PoolDBESSource',
    process.CondDBSetup,
    connect = cms.string('sqlite_file:inertGlobalPositionRcd.StdTags.746p3.DBv2.db'),
#    connect = cms.string('sqlite_file:GPR_May24_2016_SW808_gprGT_Tk_MP_Run2016B_v2_dL4_iter1.db'),
    toGet = cms.VPSet(cms.PSet(record = cms.string('GlobalPositionRcd'), tag = cms.string('inertGlobalPositionRcd'))))
#    toGet = cms.VPSet(cms.PSet(record = cms.string('GlobalPositionRcd'), tag = cms.string('IdealGeometry'))))

process.Path = cms.Path(process.MuonGeometryDBConverter)
