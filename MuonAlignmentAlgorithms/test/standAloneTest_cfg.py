import FWCore.ParameterSet.Config as cms

process = cms.Process("TEST")
process.source = cms.Source("PoolSource", fileNames = cms.untracked.vstring(
    "/store/data/Run2018D/SingleMuon/ALCARECO/TkAlMuonIsolated-PromptReco-v2/000/325/000/00000/DD35CEF5-7EB9-D746-A0B3-0DC25007D6E6.root",
    #"/store/data/Run2018D/SingleMuon/RAW-RECO/ZMu-PromptReco-v2/000/325/114/00000/7DFF4F39-9B1F-CA4A-87FD-93D283065E12.root"
    ))
process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(100))

process.StandAloneTest = cms.EDAnalyzer("StandAloneTest", Tracks = cms.InputTag(""))

process.load("Configuration.StandardSequences.MagneticField_cff")
process.load("Geometry.CMSCommonData.cmsIdealGeometryXML_cfi")
process.load("Geometry.CommonDetUnit.bareGlobalTrackingGeometry_cfi")
process.load("Geometry.MuonNumbering.muonNumberingInitialization_cfi")
process.load("Geometry.DTGeometry.dtGeometry_cfi")
process.load("Geometry.CSCGeometry.cscGeometry_cfi")
process.load("Geometry.RPCGeometry.rpcGeometry_cfi")
process.load("Geometry.TrackerNumberingBuilder.trackerNumberingGeometry_cfi")
process.load("Geometry.TrackerGeometryBuilder.trackerGeometry_cfi")

#### for cosmic rays (only use one)
#process.load("TrackingTools.TrackRefitter.globalCosmicMuonTrajectories_cff")
#process.TrackRefitter = process.globalCosmicMuons.clone()
#process.TrackRefitter.Tracks = cms.InputTag("globalCosmicMuons")
#process.StandAloneTest.Tracks = cms.InputTag("globalCosmicMuons")

# for collisions (only use one)
process.load("TrackingTools.TrackRefitter.globalMuonTrajectories_cff")
process.TrackRefitter = process.globalMuons.clone()
process.TrackRefitter.Tracks = cms.InputTag("globalMuons")
process.StandAloneTest.Tracks = cms.InputTag("globalMuons")

process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.GlobalTag.globaltag = cms.string("102X_dataRun2_v7")

from CondCore.CondDB.CondDB_cfi import *
CondDBSetup = CondDB.clone()
CondDBSetup.__delattr__('connect')

### for assigning a custom muon alignment
# process.MuonAlignment = cms.ESSource("PoolDBESSource",
#                                      CondDBSetup,
#                                      connect = cms.string("sqlite_file:customMuonAlignment.db"),
#                                      toGet = cms.VPSet(cms.PSet(record = cms.string("DTAlignmentRcd"), tag = cms.string("DTAlignmentRcd")),
#                                                        cms.PSet(record = cms.string("CSCAlignmentRcd"), tag = cms.string("CSCAlignmentRcd"))))
# process.es_prefer_MuonAlignment = cms.ESPrefer("PoolDBESSource", "MuonAlignment")

### it is important to refit with zero weights ("infinite" APEs)
#process.MuonAlignmentErrorsExtended = cms.ESSource("PoolDBESSource",
#                                     CondDBSetup,
#                                     connect = cms.string("sqlite_file:APE1000cm.db"),
#                                     toGet = cms.VPSet(cms.PSet(record = cms.string("DTAlignmentErrorExtendedRcd"), tag = cms.string("DTAlignmentErrorExtendedRcd")),
#                                                       cms.PSet(record = cms.string("CSCAlignmentErrorExtendedRcd"), tag = cms.string("CSCAlignmentErrorExtendedRcd"))))
#process.es_prefer_MuonAlignmentErrorsExtended = cms.ESPrefer("PoolDBESSource", "MuonAlignmentErrorsExtended")

process.TFileService = cms.Service("TFileService", fileName = cms.string("standAloneTest.root"))
process.Path = cms.Path(process.TrackRefitter * process.StandAloneTest)
