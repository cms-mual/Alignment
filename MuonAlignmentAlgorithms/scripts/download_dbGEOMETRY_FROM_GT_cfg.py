#TAKEN FROM Alignment/MuonAlignment/python/download_sqlite_cfg.py
import FWCore.ParameterSet.Config as cms
#globalTag = "80X_mcRun2_asymptotic_2016_TrancheIV_v7" #!
globalTag = "MCRUN2_74_V9" #!
#outputFile = "geo_80X_mcRun2_asymptotic_2016_TrancheIV_v7.db" #!
outputFile = "geo_80X_MCRUN2_74_V9.db" #!

process = cms.Process("CONVERT")
process.source = cms.Source("EmptySource")
process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(1))

process.load("Configuration.Geometry.GeometryIdeal_cff")
process.load("Geometry.MuonNumbering.muonNumberingInitialization_cfi")
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.GlobalTag.globaltag = globalTag

process.MuonGeometryDBConverter = cms.EDAnalyzer("MuonGeometryDBConverter",
                                                 input = cms.string("db"),
                                                 dtLabel = cms.string(""),
                                                 cscLabel = cms.string(""),
                                                 shiftErr = cms.double(1000.),
                                                 angleErr = cms.double(6.28),
                                                 getAPEs = cms.bool(True),                                                
                                                 output = cms.string("db")
                                                 )

from CondCore.CondDB.CondDB_cfi import *
CondDBSetup = CondDB.clone()
CondDBSetup.__delattr__('connect')
process.PoolDBOutputService = cms.Service("PoolDBOutputService",
                                          CondDBSetup,
                                          connect = cms.string("sqlite_file:%s" % outputFile),
                                          toPut = cms.VPSet(cms.PSet(record = cms.string("DTAlignmentRcd"), tag = cms.string("DTAlignmentRcd")),
                                                            cms.PSet(record = cms.string("DTAlignmentErrorExtendedRcd"), tag = cms.string("DTAlignmentErrorExtendedRcd")),
                                                            cms.PSet(record = cms.string("CSCAlignmentRcd"), tag = cms.string("CSCAlignmentRcd")),
                                                            cms.PSet(record = cms.string("CSCAlignmentErrorExtendedRcd"), tag = cms.string("CSCAlignmentErrorExtendedRcd"))))
process.Path = cms.Path(process.MuonGeometryDBConverter)
