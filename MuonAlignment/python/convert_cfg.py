
from Alignment.MuonAlignment.convertXMLtoSQLite_cfg import *
process.MuonGeometryDBConverter.fileName = "MCScenario_CSA14.xml"
process.PoolDBOutputService.connect = "sqlite_file:MCScenario_CSA14.db"
