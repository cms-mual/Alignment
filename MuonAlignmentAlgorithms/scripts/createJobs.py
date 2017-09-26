#! /usr/bin/env python
"""
Created:       2 August 2017
Last Updated:  2 August 2017

Dan Marley
daniel.edison.marley@cernSPAMNOT.ch
Texas A&M University
Fermi National Accelerator Laboratory
-----

Create jobs for track based muon alignment
"""
import os
import sys
import math
import commands

import util
from config import Config
from writeBatchScripts import WriteBatchScripts


pwd  = commands.getoutput("pwd")
prog = sys.argv[0]

## Setup configuration object
cfg  = Config(sys.argv[1],script=prog)  # configuration
cfg.initialize()

## Setup VERBOSE object
vb = util.VERBOSE()
vb.level = cfg.verbose_level()
vb.name  = "CREATEJOBS"        # nickname of this script for the VERBOSE output

## Setup WriteBatchScripts object
wbs = WriteBatchScripts(cfg)
wbs.pwd = pwd


## Do some checks of the configuration ##
createLayerNtupleDT  = cfg.createLayerNtupleDT()
createLayerNtupleCSC = cfg.createLayerNtupleCSC()

if createLayerNtupleDT and createLayerNtupleCSC:
    vb.WARNING("You Cannot create DEBUG Ntuples for DT and CSC at the same time.")
    sys.exit(0)

doCSC = cfg.doCSC()
doDT  = cfg.doDT()

if (not doCSC and not doDT) or (doCSC and doDT):
    vb.ERROR("Must do one of CSC or DT.")
    sys.exit()



## Now do things
NAME        = cfg.name()
ITERATIONS  = cfg.iterations()
INITIALGEOM = cfg.initial_geometry()
INPUTFILES  = cfg.inputfiles()

# -- need list of filenames (stored in python file as lists)
in_files = importlib.import_module(INPUTFILES)
try:
    fileNames = in_files.fileNames
except AttributeError:
    vb.INFO("No attribute 'fileNames' in {0}".format(INPUTFILES))
    fileNames = []

try:
    fileNamesBlocks = in_files.fileNamesBlocks
except AttributeError:
    vb.INFO("No attribute 'fileNamesBlocks' in {0}".format(INPUTFILES))
    fileNamesBlocks = []


njobs = cfg.subjobs()
if cfg.inputInBlocks():
    njobs = len(fileNamesBlocks)  # redefine the 'njobs' variable
    if not njobs:
        vb.ERROR("Configuration 'inputInBlocks' is True but no blocks in {0}.".format(INPUTFILES))
        sys.exit()

stepsize = int( math.ceil( 1.*len(fileNames)/cfg.subjobs() ) )



# step 0: convert initial geometry to xml
INITIALXML = INITIALGEOM.replace('.db','')+'.xml'

vb.INFO("Converting {0} to {1}.".format(INITIALGEOM,INITIALXML))
vb.INFO("...will be done in several seconds...")

command  = "./Alignment/MuonAlignmentAlgorithms/scripts/convertSQLiteXML.py"
command += "{0} {1} --gprcdconnect {2} --gprcd {3} --noLayers ".format(INITIALGEOM,INITIALXML,cfg.gprcdconnect(),cfg.gprcd())
vb.INFO(command)

exit_code = os.system(command)
if exit_code:
    vb.ERROR("Conversion to .xml exited with code: {0}".format(exit_code))
    sys.exit()


#SUPER_SPECIAL_XY_AND_DXDZ_ITERATIONS = True
SUPER_SPECIAL_XY_AND_DXDZ_ITERATIONS = False

bsubfile   = ["#!/bin/sh", ""]
bsubnames  = []
last_align = None
directory  = ""
director   = ""

mapplots_ingeneral       = cfg.mapplots()
segdiffplots_ingeneral   = cfg.segdiffplots()
curvatureplots_ingeneral = cfg.curvatureplots()

for iteration in range(1, ITERATIONS+1):
    wbs.inputdb    = director+".db" if iteration!=1 else INITIALGEOM
    wbs.inputdbdir = directory

    # set the directories and some files
    directory   = "{0}_{1:02d}/".format(NAME,iteration)
    director    = directory[:-1]   # all but the last "/"
    script_path = "Alignment/MuonAlignmentAlgorithms/python/"

    os.system( "rm -rf {0}; mkdir {0}  ".format(directory) )
    os.system( "cp {0}gather_cfg.py {1}".format(script_path,directory) )
    os.system( "cp {0}align_cfg.py {1} ".format(script_path,directory) )

    bsubfile.append("cd {0}".format(directory))

    # set parameters for the wbs object
    mapplots = False
    if mapplots_ingeneral and any( [iteration==i for i in [1,3,5,7,9,ITERATIONS]] ):
        mapplots = True

    segdiffplots = False
    if segdiffplots_ingeneral and (iteration==1 or iteration==ITERATIONS):
        segdiffplots = True

    curvatureplots = False
    if curvatureplots_ingeneral and (iteration==1 or iteration==ITERATIONS):
        curvatureplots = True

    wbs.directory      = directory
    wbs.mapplots       = mapplots
    wbs.segdiffplots   = segdiffplots
    wbs.curvatureplots = curvatureplots


    ### gather.sh runners for njobs
    for jobnumber in range(njobs):

        if cfg.inputInBlocks():
            inputfiles = " ".join(fileNamesBlocks[jobnumber])
        else:
            inputfiles = " ".join(fileNames[jobnumber*stepsize:(jobnumber+1)*stepsize])

        wbs.inputfiles = inputfiles
        copyplots      = "plotting*.root" if any( [mapplots,segdiffplots,curvatureplots] ) else ""

        if len(inputfiles) > 0:
            gather_fileName = "{0}gather{1:03d}.sh".format(directory, jobnumber)
            wbs.writeGatherCfg(gather_fileName)
            os.system("chmod +x {0}".format(gather_fileName)
            bsubfile.append("echo {0}".format(gather_filename))

            waiter = "" if last_align is None else "-w \"ended({0})\"".format(last_align)          
            queue  = "cmscaf1nd" if cfg.big() else "cmscaf1nh"

            bsubfile.append("bsub -R \"type==SLC6_64\" -q %s -J \"%s_gather%03d\" -u youremail.tamu.edu %s gather%03d.sh" % (queue, director, jobnumber, waiter, jobnumber))

            bsubnames.append("ended(%s_gather%03d)" % (director, jobnumber))


    ### align.sh
    if SUPER_SPECIAL_XY_AND_DXDZ_ITERATIONS:
        # reset some parameters
        if ( iteration<10 and iteration%2!=0 ):   # 1,3,5,7,9
            wbs.station123params = "000010"
            wbs.station123params = "000010"
            wbs.useResiduals     = "0010"
        elif ( iteration<=10 and iteration%2==0 ): # 2,4,6,8,10
            wbs.station123params = "110001"
            wbs.station123params = "100001"
            wbs.useResiduals     = "1100"

    wbs.writeHaddCfg("{0}hadd.sh".format(directory))
    wbs.writeAlignCfg("{0}align.sh".format(directory))

    os.system("chmod +x {0}hadd.sh".format(directory))
    os.system("chmod +x {0}align.sh".format(directory))


    base_command = "bsub -R \"type==SLC6_64\" -q cmscaf1nd -J \"{0}_{1}\" -w \"{2}\" {1}.sh"

    # hadd
    bsubfile.append("echo %shadd.sh" % directory)
    hadd_command = base_command.format(director,"hadd"," && ".join(bsubnames))
    if user_mail:
        hadd_command.replace("-q cmscaf1nd","-q cmscaf1nd -u {0}".format(user_mail))
    bsubfile.append(hadd_command)

    # align
    bsubfile.append("echo {0}align.sh".format(directory))
    align_command = base_command.format(director,"align"," && ".join(bsubnames))
    bsubfile.append(align_command)

    bsubnames  = []
    last_align = "{0}_align) && ended({0}_hadd".format(director)

    ### after the last iteration (optionally) do diagnostics run
    if NAME and iteration==ITERATIONS:
        # do we have plotting files created?
        directory1 = "{0}_01/".format(NAME)
        director1  = directory1[:-1]

        wbs.writeValidationCfg("{0}validation.sh".format(directory))
        os.system("chmod +x {0}validation.sh".format(directory))
        
        bsubfile.append("echo {0}validation.sh".format(directory))
        bsub_args = base_command.format(director,"validation","ended({0})".format(last_align))
        if user_mail:
            bsub_args.replace("-q cmscaf1nd","-q cmscaf1nd -u {0}".format(user_mail))
        bsubfile.append(bsub_args)

    bsubfile.append("cd ..")
    bsubfile.append("")


## Change the permissions of the script to submit the jobs!
submitJobs = cfg.submitJobs()
file(submitJobs,"w").write("\n".join(bsubfile))
os.system("chmod +x {0}".format(submitJobs))


## THE END ##