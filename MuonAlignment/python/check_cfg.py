
from Alignment.MuonAlignment.convertSQLitetoXML_cfg import *
process.PoolDBESSource.connect = "sqlite_file:MCScenario_CSA14.db"
process.MuonGeometryDBConverter.outputXML.fileName = "MCScenario_CSA14_CHECKME.xml"
process.MuonGeometryDBConverter.outputXML.relativeto = "ideal"
process.MuonGeometryDBConverter.outputXML.suppressDTChambers = False
process.MuonGeometryDBConverter.outputXML.suppressDTSuperLayers = False
process.MuonGeometryDBConverter.outputXML.suppressDTLayers = True
process.MuonGeometryDBConverter.outputXML.suppressCSCChambers = False
process.MuonGeometryDBConverter.outputXML.suppressCSCLayers = False
