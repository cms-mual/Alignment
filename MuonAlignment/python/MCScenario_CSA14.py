# To use this script:
#     it's an ordinary Python script, not a CMSSW configuration file (though it writes and runs CMSSW configuration files)
#         * you MUST have an inertGlobalPositionRcd.db in your working directory
#         * you MUST NOT have an MCScenario_CSA14.db
#
#     to make the inertGlobalPositionRcd:
#         cmsRun Alignment/MuonAlignment/python/makeGlobalPositionRcd_cfg.py
#
#     to get rid of the MCScenario_CSA14.db:
#         rm MCScenario_CSA14.db    (naturally)
#
#     to run this script:
#         python MCScenario_CSA14.py
#
#     it will create
#         * MCScenario_CSA14.xml            the XML file with randomly-distributed values, created directly by define_scenario()
#         * convert_cfg.py                       the conversion configuration file
#         * MCScenario_CSA14.db             the SQLite database created from the XML
#         * check_cfg.py                         configuration file that converts the SQLite file back into XML
#         * MCScenario_CSA14_CHECKME.xml    converted back, so that we can check the values that were saved to the database
#
#     to check the output in Excel, do this
#         ./Alignment/MuonAlignment/python/geometryXMLtoCSV.py < MCScenario_CSA14_CHECKME.xml > MCScenario_CSA14_CHECKME.csv
#         and then open MCScenario_CSA14_CHECKME.csv in Excel

import random, os
from math import *

# set the initial seed for reproducibility!
random.seed(1234)

#### called once at the end of this script
def make_scenario_sqlite():
    scenario = define_scenario()
    write_xml(scenario, "MCScenario_CSA14.xml")
    write_conversion_cfg("convert_cfg.py", "MCScenario_CSA14.xml", "MCScenario_CSA14.db")
    cmsRun("convert_cfg.py")
    write_check_cfg("check_cfg.py", "MCScenario_CSA14.db", "MCScenario_CSA14_CHECKME.xml")
    cmsRun("check_cfg.py")
#### that's it!  everything this uses is defined below

def write_conversion_cfg(fileName, xmlFileName, dbFileName):
    outfile = file(fileName, "w")
    outfile.write("""
from Alignment.MuonAlignment.convertXMLtoSQLite_cfg import *
process.MuonGeometryDBConverter.fileName = "%(xmlFileName)s"
process.PoolDBOutputService.connect = "sqlite_file:%(dbFileName)s"
""" % vars())

def write_check_cfg(fileName, dbFileName, xmlFileName):
    outfile = file(fileName, "w")
    outfile.write("""
from Alignment.MuonAlignment.convertSQLitetoXML_cfg import *
process.PoolDBESSource.connect = "sqlite_file:%(dbFileName)s"
process.MuonGeometryDBConverter.outputXML.fileName = "%(xmlFileName)s"
process.MuonGeometryDBConverter.outputXML.relativeto = "ideal"
process.MuonGeometryDBConverter.outputXML.suppressDTChambers = False
process.MuonGeometryDBConverter.outputXML.suppressDTSuperLayers = False
process.MuonGeometryDBConverter.outputXML.suppressDTLayers = True
process.MuonGeometryDBConverter.outputXML.suppressCSCChambers = False
process.MuonGeometryDBConverter.outputXML.suppressCSCLayers = False
""" % vars())

def cmsRun(fileName):
    os.system("cmsRun %(fileName)s" % vars())

########### writing a scenario in XML ##############################################################

# only needed to make the output XML readable
DTpreferred_order = {"wheel":1, "station":2, "sector":3, "superlayer":4, "layer":5}
CSCpreferred_order = {"endcap":1, "station":2, "ring":3, "chamber":4, "layer":5}
def DTsorter(a, b): return cmp(DTpreferred_order[a], DTpreferred_order[b])
def CSCsorter(a, b): return cmp(CSCpreferred_order[a], CSCpreferred_order[b])

# an instance of this class corresponds to one <DTChamber ... /> or <CSCStation ... />, etc.
class Alignable:
    def __init__(self, alignabletype, **location):
        self.alignabletype = alignabletype
        self.location = location

    def writeXML(self):
        parameters = self.location.keys()
        if self.alignabletype[0:2] == "DT":
            parameters.sort(DTsorter)
        else:
            parameters.sort(CSCsorter)

        output = ["<", self.alignabletype, " "]
        for parameter in parameters:
            output.extend([parameter, "=\"", str(self.location[parameter]), "\" "])
        output.append("/>")

        return "".join(output)

preferred_order = {"x":1, "y":2, "z":3, "phix":4, "phiy":5, "phiz":6}
def sorter(a, b): return cmp(preferred_order[a], preferred_order[b])

# an instance of this class corresponds to one <setposition ... />
class Position:
    def __init__(self, **location):
        self.location = location

    def writeXML(self):
        parameters = self.location.keys()
        parameters.sort(sorter)

        output = ["<setposition relativeto=\"ideal\" "]
        for parameter in parameters:
            output.extend([parameter, "=\"", str(self.location[parameter]), "\" "])
        output.append("/>")

        return "".join(output)

# an instance of this class corresponds to one <operation> ... </operation> in the XML file
class Operation:
    def __init__(self, alignable, position):
        self.alignable = alignable
        self.position = position

    def writeXML(self):
        output = ["<operation> ", self.alignable.writeXML(), " ", self.position.writeXML(), " </operation>\n"]
        return "".join(output)

def write_xml(scenario, fileName):
    # a scenario is an ordered list of Operations
    XMLlist = ["<MuonAlignment>\n"]
    for operation in scenario:
        XMLlist.append(operation.writeXML())
    XMLlist.append("</MuonAlignment>\n")
    XMLstring = "".join(XMLlist)
        
    outfile = file(fileName, "w")
    outfile.write(XMLstring)

class DTChamber:
    def __init__(self, **location):
        self.__dict__.update(location)

class CSCChamber:
    def __init__(self, **location):
        self.__dict__.update(location)

########### defining the actual scenario ##############################################################

# this is the interesting part: where we define a scenario for CRAFT1 MC
def define_scenario():
    # this will be a list of operations to write to an XML file
    scenario = []

    # Uncertainty in CSC chamber positions comes in 5 parts:
    #    1. isotropic photogrammetry uncertainty of 0.03 cm (x, y, z) and 0.00015 rad in phiz
    #    2. 0.1438 cm z and 0.00057 rad phix uncertainty between rings from SLM (from comparison in 0T data with PG)
    #    3. 0.05 cm (x, y, z) disk misalignments and 0.0001 rad rotation around beamline

    # Before starting, let's build a list of chambers
    CSCchambers = []
    for endcap in 1, 2:
        for station, ring in (1, 1), (1, 2), (1, 3), (1, 4), (2, 1), (2, 2), (3, 1), (3, 2), (4, 1), (4, 2):
            if station > 1 and ring == 1:
                nchambers = 18
            else:
                nchambers = 36

            for chamber in range(1, nchambers+1):
                CSCchambers.append(CSCChamber(endcap = endcap, station = station, ring = ring, chamber = chamber))
            
    # First, the ring errors from DCOPS (derived from comparison with photogrammetry)
    CSCrings = []
    for endcap in 1, 2:
        for station, ring in (1, 1), (1, 2), (1, 3), (1, 4), (2, 1), (2, 2), (3, 1), (3, 2), (4, 1), (4, 2):
            CSCrings.append(CSCChamber(endcap = endcap, station = station, ring = ring, z = random.gauss(0, 0.1438), phix = random.gauss(0, 0.00057)))

    # Next, the chamber errors
    for chamber in CSCchambers:
        errx = random.gauss(0, 0.03)
        erry = random.gauss(0, 0.03)
        errz = random.gauss(0, 0.03)
        errphix = random.gauss(0, 0.000)
        errphiy = random.gauss(0, 0.000)
        errphiz = random.gauss(0, 0.00015)
        
        for ring in CSCrings:
            if ring.endcap == chamber.endcap and ring.station == chamber.station and ring.ring == chamber.ring:
                errz += ring.z
                errphix += ring.phix
                break

        alignable = Alignable("CSCChamber", endcap = chamber.endcap, station = chamber.station, ring = chamber.ring, chamber = chamber.chamber)
        position = Position(x = errx, y = erry, z = errz, phix = errphix, phiy = errphiy, phiz = errphiz)
        scenario.append(Operation(alignable, position))

    # Finally, the disk errors
    for endcap in 1, 2:
        for station in 1, 2, 3, 4:
            alignable = Alignable("CSCStation", endcap = endcap, station = station)
            position = Position(x = random.gauss(0, 0.05), y = random.gauss(0, 0.05), z = random.gauss(0, 0.05), phix = 0., phiy = 0., phiz = random.gauss(0, 0.0001))
            scenario.append(Operation(alignable, position))

    return scenario

# run it all!
make_scenario_sqlite()
