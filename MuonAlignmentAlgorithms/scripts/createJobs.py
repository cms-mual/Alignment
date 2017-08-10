#! /usr/bin/env python
"""
2 August 2017

Dan Marley

Create jobs for track based muon alignment
"""
import os
import sys
import math
import commands

import util
from config import Config

prog = sys.argv[0]
cfg  = Config(sys.argv[1],script=prog)  # configuration
cfg.initialize()

## Set variables to different configurations ##

DIRNAME     = cfg.dirname()
ITERATIONS  = cfg.iterations()
INITIALGEOM = cfg.initial_geometry()
INPUTFILES  = cfg.inputfiles()

createLayerNtupleDT  = cfg.createLayerNtupleDT()
createLayerNtupleCSC = cfg.createLayerNtupleCSC()

if createLayerNtupleDT and createLayerNtupleCSC:
    util.WARNING("CREATEJOBS : You Cannot create DEBUG Ntuples for DT and CSC at the same time.")
    sys.exit(0)

doCSC = cfg.doCSC
doDT  = cfg.doDT

if not cfg.doCSC and not cfg.doDT:
    util.ERROR("CREATEJOBS : Must do either CSC or DT!")
    sys.exit()

trackerAPE = cfg.trackerAPE()
globaltag  = cfg.globaltag()
user_mail  = cfg.user_mail()
cscparams  = cfg.cscparams()
gprcd      = cfg.gprcd()
iscosmics  = cfg.iscosmics()
json_file  = cfg.json()
minTrackPt = cfg.minTrackPt()
maxTrackPt = cfg.maxTrackPt()
minTrackP  = cfg.minTrackP()
maxTrackP  = cfg.maxTrackP()
maxDxy     = cfg.maxDxy()
twoBin     = cfg.twoBin()
doCleanUp  = cfg.doCleanUp()
T0_Corr    = cfg.T0_Corr()
is_MC      = cfg.is_MC()
njobs      = cfg.subjobs()
maxEvents  = cfg.maxEvents()
skipEvents = cfg.skipEvents()
theNSigma  = cfg.motionPolicyNSigma()
peakNSigma = cfg.peakNSigma()
preFilter  = cfg.preFilter()
extraPlots = cfg.extraPlots()

combineME11  = cfg.notCombineME11()
trackerBows  = cfg.trackerBows()
gprcdconnect = cfg.gprcdconnect()
allowTIDTEC  = cfg.allowTIDTEC()
is_Alcareco  = cfg.is_Alcareco()
maxResSlopeY = cfg.maxResSlopeY()
useResiduals = cfg.useResiduals()

trackerconnect  = cfg.trackerconnect()
weightAlignment = cfg.weightAlignment()
validationLabel = cfg.validationLabel()
residualsModel  = cfg.residualsModel()
createMapNtuple = cfg.createMapNtuple()
station4params  = cfg.station4params()

createAlignNtuple = cfg.createAlignNtuple()
minAlignmentHits  = cfg.minAlignmentHits()
trackeralignment  = cfg.trackeralignment()
trackerAPEconnect = cfg.trackerAPEconnect()
station123params  = cfg.station123params()
muonCollectionTag = cfg.muonCollectionTag()
minTrackerHits    = cfg.minTrackerHits()
maxTrackerRedChi2 = cfg.maxTrackerRedChi2()

minNCrossedChambers = cfg.minNCrossedChambers()
mapplots_ingeneral  = cfg.mapplots()
trackerBowsconnect  = cfg.trackerBowsconnect()

segdiffplots_ingeneral   = cfg.segdiffplots()
curvatureplots_ingeneral = cfg.curvatureplots()


fileNames       = []
fileNamesBlocks = []
execfile(INPUTFILES)

if cfg.inputInBlocks:
    njobs = len(fileNamesBlocks)
    if not njobs:
        util.ERROR("CREATEJOBS : 'inputInBlocks' is specified but no blocks in INPUTFILES!")
        sys.exit()

stepsize = int(math.ceil(1.*len(fileNames)/cfg.subjobs))
pwd      = commands.getoutput("pwd")

copytrackerdb = ""
if trackerconnect[0:12]     == "sqlite_file:": copytrackerdb += trackerconnect[12:]
if trackerAPEconnect[0:12]  == "sqlite_file:": copytrackerdb += trackerAPEconnect[12:]
if trackerBowsconnect[0:12] == "sqlite_file:": copytrackerdb += trackerBowsconnect[12:]
if gprcdconnect[0:12]       == "sqlite_file:": copytrackerdb += gprcdconnect[12:]


#####################################################################
# step 0: convert initial geometry to xml
INITIALXML = INITIALGEOM+'.xml'
if INITIALGEOM.endswith('.db'):
    INITIALXML = INITIALGEOM.replace('.db','.xml')

util.INFO("CREATEJOBS : Converting {0} to {1}.".format(INITIALGEOM,INITIALXML))
util.INFO("CREATEJOBS : ...will be done in several seconds...")

command = "./Alignment/MuonAlignmentAlgorithms/scripts/convertSQLiteXML.py  {0} {1} --gprcdconnect {2} --gprcd {3} --noLayers ".format(INITIALGEOM,INITIALXML,gprcdconnect,gprcd)
util.INFO("CREATEJOBS : {0}".format(command))

exit_code = os.system(command)
if exit_code:
    util.ERROR("CREATEJOBS : Problem!! Conversion exited with code: {0}".format(exit_code))
    sys.exit()

#####################################################################

def writeGatherCfg(fname, my_vars):
    file(fname, "w").write("""#/bin/sh
# %(commandline)s

export ALIGNMENT_CAFDIR=`pwd`

cd %(pwd)s
eval `scramv1 run -sh`
export ALIGNMENT_AFSDIR=`pwd`

export ALIGNMENT_INPUTFILES='%(inputfiles)s'
export ALIGNMENT_ITERATION=%(iteration)d
export ALIGNMENT_JOBNUMBER=%(jobnumber)d
export ALIGNMENT_MAPPLOTS=%(mapplots)s
export ALIGNMENT_SEGDIFFPLOTS=%(segdiffplots)s
export ALIGNMENT_CURVATUREPLOTS=%(curvatureplots)s
export ALIGNMENT_GLOBALTAG=%(globaltag)s
export ALIGNMENT_INPUTDB=%(inputdb)s
export ALIGNMENT_TRACKERCONNECT=%(trackerconnect)s
export ALIGNMENT_TRACKERALIGNMENT=%(trackeralignment)s
export ALIGNMENT_TRACKERAPECONNECT=%(trackerAPEconnect)s
export ALIGNMENT_TRACKERAPE=%(trackerAPE)s
export ALIGNMENT_TRACKERBOWSCONNECT=%(trackerBowsconnect)s
export ALIGNMENT_TRACKERBOWS=%(trackerBows)s
export ALIGNMENT_GPRCDCONNECT=%(gprcdconnect)s
export ALIGNMENT_GPRCD=%(gprcd)s
export ALIGNMENT_ISCOSMICS=%(iscosmics)s
export ALIGNMENT_STATION123PARAMS=%(station123params)s
export ALIGNMENT_STATION4PARAMS=%(station4params)s
export ALIGNMENT_CSCPARAMS=%(cscparams)s
export ALIGNMENT_MUONCOLLECTIONTAG=%(muonCollectionTag)s
export ALIGNMENT_MINTRACKPT=%(minTrackPt)s
export ALIGNMENT_MAXTRACKPT=%(maxTrackPt)s
export ALIGNMENT_MINTRACKP=%(minTrackP)s
export ALIGNMENT_MAXTRACKP=%(maxTrackP)s
export ALIGNMENT_MAXDXY=%(maxDxy)s
export ALIGNMENT_MINTRACKERHITS=%(minTrackerHits)s
export ALIGNMENT_MAXTRACKERREDCHI2=%(maxTrackerRedChi2)s
export ALIGNMENT_MINNCROSSEDCHAMBERS=%(minNCrossedChambers)s
export ALIGNMENT_ALLOWTIDTEC=%(allowTIDTEC)s
export ALIGNMENT_TWOBIN=%(twoBin)s
export ALIGNMENT_WEIGHTALIGNMENT=%(weightAlignment)s
export ALIGNMENT_MINALIGNMENTHITS=%(minAlignmentHits)s
export ALIGNMENT_COMBINEME11=%(combineME11)s
export ALIGNMENT_MAXEVENTS=%(maxEvents)s
export ALIGNMENT_SKIPEVENTS=%(skipEvents)s
export ALIGNMENT_MAXRESSLOPEY=%(maxResSlopeY)s
export ALIGNMENT_DO_DT=%(doDT)s
export ALIGNMENT_DO_CSC=%(doCSC)s
export ALIGNMENT_JSON=%(json_file)s
export ALIGNMENT_CREATEMAPNTUPLE=%(createMapNtuple)s
#export ALIGNMENT_CREATEALIGNNTUPLE=%(createAlignNtuple)s
export ALIGNMENT_PREFILTER=%(preFilter)s
export ALIGNMENT_T0CORR=%(T0_Corr)s
export ALIGNMENT_ISALCARECO=%(is_Alcareco)s
export ALIGNMENT_ISMC=%(is_MC)s
export ALIGNMENT_STORELAYERDT=%(createLayerNtupleDT)s
export ALIGNMENT_STORELAYERCSC=%(createLayerNtupleCSC)s

if [ \"zzz$ALIGNMENT_JSON\" != \"zzz\" ]; then
  cp -f $ALIGNMENT_JSON $ALIGNMENT_CAFDIR/
fi

cp -f %(directory)sgather_cfg.py %(inputdbdir)s%(inputdb)s %(copytrackerdb)s $ALIGNMENT_CAFDIR/
cd $ALIGNMENT_CAFDIR/
ls -l
cmsRun gather_cfg.py
ls -l
cp -f *.tmp %(copyplots)s $ALIGNMENT_AFSDIR/%(directory)s
""" % my_vars)

#####################################################################

def writeHaddCfg(fname, my_vars):
    file("%shadd.sh" % directory, "w").write("""#!/bin/sh
# %(commandline)s

export ALIGNMENT_CAFDIR=`pwd`

cd %(pwd)s
eval `scramv1 run -sh`
export ALIGNMENT_AFSDIR=`pwd`
export ALIGNMENT_INPUTDB=%(inputdb)s
export ALIGNMENT_ITERATION=%(iteration)d
export ALIGNMENT_GLOBALTAG=%(globaltag)s
export ALIGNMENT_TRACKERCONNECT=%(trackerconnect)s
export ALIGNMENT_TRACKERALIGNMENT=%(trackeralignment)s
export ALIGNMENT_TRACKERAPECONNECT=%(trackerAPEconnect)s
export ALIGNMENT_TRACKERAPE=%(trackerAPE)s
export ALIGNMENT_TRACKERBOWSCONNECT=%(trackerBowsconnect)s
export ALIGNMENT_TRACKERBOWS=%(trackerBows)s
export ALIGNMENT_GPRCDCONNECT=%(gprcdconnect)s
export ALIGNMENT_GPRCD=%(gprcd)s
export ALIGNMENT_ISCOSMICS=%(iscosmics)s
export ALIGNMENT_STATION123PARAMS=%(station123params)s
export ALIGNMENT_STATION4PARAMS=%(station4params)s
export ALIGNMENT_CSCPARAMS=%(cscparams)s
export ALIGNMENT_MINTRACKPT=%(minTrackPt)s
export ALIGNMENT_MAXTRACKPT=%(maxTrackPt)s
export ALIGNMENT_MINTRACKP=%(minTrackP)s
export ALIGNMENT_MAXTRACKP=%(maxTrackP)s
export ALIGNMENT_MINTRACKERHITS=%(minTrackerHits)s
export ALIGNMENT_MAXTRACKERREDCHI2=%(maxTrackerRedChi2)s
export ALIGNMENT_ALLOWTIDTEC=%(allowTIDTEC)s
export ALIGNMENT_TWOBIN=%(twoBin)s
export ALIGNMENT_WEIGHTALIGNMENT=%(weightAlignment)s
export ALIGNMENT_MINALIGNMENTHITS=%(minAlignmentHits)s
export ALIGNMENT_COMBINEME11=%(combineME11)s
export ALIGNMENT_MAXRESSLOPEY=%(maxResSlopeY)s
export ALIGNMENT_CLEANUP=%(doCleanUp)s
export ALIGNMENT_CREATEALIGNNTUPLE=%(createAlignNtuple)s
export ALIGNMENT_RESIDUALSMODEL=%(residualsModel)s
export ALIGNMENT_PEAKNSIGMA=%(peakNSigma)s
export ALIGNMENT_USERESIDUALS=%(useResiduals)s
export ALIGNMENT_DO_DT=%(doDT)s
export ALIGNMENT_DO_CSC=%(doCSC)s

cp -f %(directory)salign_cfg.py %(inputdbdir)s%(inputdb)s %(directory)s*.tmp  %(copytrackerdb)s $ALIGNMENT_CAFDIR/

export ALIGNMENT_PLOTTINGTMP=`find %(directory)splotting*.root -maxdepth 1 -size +0 -print 2> /dev/null`

# if it's 1st or last iteration, combine _plotting.root files into one:
if [ \"$ALIGNMENT_ITERATION\" != \"111\" ] || [ \"$ALIGNMENT_ITERATION\" == \"%(ITERATIONS)s\" ]; then
  #nfiles=$(ls %(directory)splotting*.root 2> /dev/null | wc -l()
  if [ \"zzz$ALIGNMENT_PLOTTINGTMP\" != \"zzz\" ]; then
    hadd -f1 -k %(directory)s%(director)s_plotting.root %(directory)splotting*.root
    #if [ $? == 0 ] && [ \"$ALIGNMENT_CLEANUP\" == \"True\" ]; then rm %(directory)splotting*.root; fi
  fi
fi
if [ \"$ALIGNMENT_CLEANUP\" == \"True\" ] && [ \"zzz$ALIGNMENT_PLOTTINGTMP\" != \"zzz\" ]; then
  rm $ALIGNMENT_PLOTTINGTMP
fi
""" % my_vars)

#####################################################################

def writeAlignCfg(fname, my_vars):
    file("%salign.sh" % directory, "w").write("""#!/bin/sh
# %(commandline)s

export ALIGNMENT_CAFDIR=`pwd`

cd %(pwd)s
eval `scramv1 run -sh`
export ALIGNMENT_AFSDIR=`pwd`
export ALIGNMENT_INPUTDB=%(inputdb)s
export ALIGNMENT_ITERATION=%(iteration)d
export ALIGNMENT_GLOBALTAG=%(globaltag)s
export ALIGNMENT_TRACKERCONNECT=%(trackerconnect)s
export ALIGNMENT_TRACKERALIGNMENT=%(trackeralignment)s
export ALIGNMENT_TRACKERAPECONNECT=%(trackerAPEconnect)s
export ALIGNMENT_TRACKERAPE=%(trackerAPE)s
export ALIGNMENT_TRACKERBOWSCONNECT=%(trackerBowsconnect)s
export ALIGNMENT_TRACKERBOWS=%(trackerBows)s
export ALIGNMENT_GPRCDCONNECT=%(gprcdconnect)s
export ALIGNMENT_GPRCD=%(gprcd)s
export ALIGNMENT_ISCOSMICS=%(iscosmics)s
export ALIGNMENT_STATION123PARAMS=%(station123params)s
export ALIGNMENT_STATION4PARAMS=%(station4params)s
export ALIGNMENT_CSCPARAMS=%(cscparams)s
export ALIGNMENT_MINTRACKPT=%(minTrackPt)s
export ALIGNMENT_MAXTRACKPT=%(maxTrackPt)s
export ALIGNMENT_MINTRACKP=%(minTrackP)s
export ALIGNMENT_MAXTRACKP=%(maxTrackP)s
export ALIGNMENT_MINTRACKERHITS=%(minTrackerHits)s
export ALIGNMENT_MAXTRACKERREDCHI2=%(maxTrackerRedChi2)s
export ALIGNMENT_ALLOWTIDTEC=%(allowTIDTEC)s
export ALIGNMENT_TWOBIN=%(twoBin)s
export ALIGNMENT_WEIGHTALIGNMENT=%(weightAlignment)s
export ALIGNMENT_MINALIGNMENTHITS=%(minAlignmentHits)s
export ALIGNMENT_COMBINEME11=%(combineME11)s
export ALIGNMENT_MAXRESSLOPEY=%(maxResSlopeY)s
export ALIGNMENT_CLEANUP=%(doCleanUp)s
export ALIGNMENT_CREATEALIGNNTUPLE=%(createAlignNtuple)s
export ALIGNMENT_RESIDUALSMODEL=%(residualsModel)s
export ALIGNMENT_PEAKNSIGMA=%(peakNSigma)s
export ALIGNMENT_USERESIDUALS=%(useResiduals)s
export ALIGNMENT_DO_DT=%(doDT)s
export ALIGNMENT_DO_CSC=%(doCSC)s
export ALIGNMENT_ISMC=%(is_MC)s

cp -f %(directory)salign_cfg.py %(inputdbdir)s%(inputdb)s %(directory)s*.tmp  %(copytrackerdb)s $ALIGNMENT_CAFDIR/

export ALIGNMENT_PLOTTINGTMP=`find %(directory)splotting*.root -maxdepth 1 -size +0 -print 2> /dev/null`

cd $ALIGNMENT_CAFDIR/
export ALIGNMENT_ALIGNMENTTMP=`find alignment*.tmp -maxdepth 1 -size +1k -print 2> /dev/null`
ls -l

cmsRun align_cfg.py
cp -f MuonAlignmentFromReference_report.py $ALIGNMENT_AFSDIR/%(directory)s%(director)s_report.py
cp -f MuonAlignmentFromReference_outputdb.db $ALIGNMENT_AFSDIR/%(directory)s%(director)s.db
cp -f MuonAlignmentFromReference_plotting.root $ALIGNMENT_AFSDIR/%(directory)s%(director)s.root

cd $ALIGNMENT_AFSDIR
./Alignment/MuonAlignmentAlgorithms/scripts/convertSQLiteXML.py %(directory)s%(director)s.db %(directory)s%(director)s.xml --noLayers --gprcdconnect $ALIGNMENT_GPRCDCONNECT --gprcd $ALIGNMENT_GPRCD

export ALIGNMENT_ALIGNMENTTMP=`find %(directory)salignment*.tmp -maxdepth 1 -size +1k -print 2> /dev/null`
if [ \"$ALIGNMENT_CLEANUP\" == \"True\" ] && [ \"zzz$ALIGNMENT_ALIGNMENTTMP\" != \"zzz\" ]; then
  rm $ALIGNMENT_ALIGNMENTTMP
  echo " "
fi

# if it's not 1st or last iteration, do some clean up:
if [ \"$ALIGNMENT_ITERATION\" != \"1\" ] && [ \"$ALIGNMENT_ITERATION\" != \"%(ITERATIONS)s\" ]; then
  if [ \"$ALIGNMENT_CLEANUP\" == \"True\" ] && [ -e %(directory)s%(director)s.root ]; then
    rm %(directory)s%(director)s.root
  fi
fi

# if it's last iteration, apply chamber motion policy
if [ \"$ALIGNMENT_ITERATION\" == \"%(ITERATIONS)s\" ]; then
  # convert this iteration's geometry into detailed xml
  ./Alignment/MuonAlignmentAlgorithms/scripts/convertSQLiteXML.py %(directory)s%(director)s.db %(directory)s%(director)s_extra.xml --gprcdconnect $ALIGNMENT_GPRCDCONNECT --gprcd $ALIGNMENT_GPRCD
  echo "Perform motion policy "
  echo "/Alignment/MuonAlignmentAlgorithms/scripts/motionPolicyChamber.py %(INITIALXML)s  %(directory)s%(director)s_extra.xml %(directory)s%(director)s_report.py %(directory)s%(director)s_final.xml --nsigma %(theNSigma)s"
  ./Alignment/MuonAlignmentAlgorithms/scripts/motionPolicyChamber.py \
      %(INITIALXML)s  %(directory)s%(director)s_extra.xml \
      %(directory)s%(director)s_report.py \
      %(directory)s%(director)s_final.xml \
      --nsigma %(theNSigma)s
  echo "Convert the resulting xml into the final sqlite geometry "
  echo "./Alignment/MuonAlignmentAlgorithms/scripts/convertSQLiteXML.py %(directory)s%(director)s_final.xml %(directory)s%(director)s_final.db --gprcdconnect $ALIGNMENT_GPRCDCONNECT --gprcd $ALIGNMENT_GPRCD"
  ./Alignment/MuonAlignmentAlgorithms/scripts/convertSQLiteXML.py %(directory)s%(director)s_final.xml %(directory)s%(director)s_final.db --gprcdconnect $ALIGNMENT_GPRCDCONNECT --gprcd $ALIGNMENT_GPRCD
fi

""" % my_vars)

#####################################################################

def writeValidationCfg(fname, my_vars):
    file(fname, "w").write("""#!/bin/sh
# %(commandline)s

export ALIGNMENT_CAFDIR=`pwd`
mkdir files
mkdir out

cd %(pwd)s
eval `scramv1 run -sh`
ALIGNMENT_AFSDIR=`pwd`
ALIGNMENT_ITERATION=%(iteration)d
ALIGNMENT_MAPPLOTS=None
ALIGNMENT_SEGDIFFPLOTS=None
ALIGNMENT_CURVATUREPLOTS=None
ALIGNMENT_EXTRAPLOTS=%(extraPlots)s
export ALIGNMENT_GPRCDCONNECT=%(gprcdconnect)s
export ALIGNMENT_GPRCD=%(gprcd)s
export ALIGNMENT_DO_DT=%(doDT)s
export ALIGNMENT_DO_CSC=%(doCSC)s


# copy the scripts to CAFDIR
cd Alignment/MuonAlignmentAlgorithms/scripts/
cp -f plotscripts.py $ALIGNMENT_CAFDIR/
cp -f mutypes.py $ALIGNMENT_CAFDIR/
cp -f alignmentValidation.py $ALIGNMENT_CAFDIR/
cp -f phiedges_fitfunctions.C $ALIGNMENT_CAFDIR/
cp -f createTree.py $ALIGNMENT_CAFDIR/
cp -f signConventions.py $ALIGNMENT_CAFDIR/
cp -f convertSQLiteXML.py $ALIGNMENT_CAFDIR/
cp -f wrapperExtraPlots.sh $ALIGNMENT_CAFDIR/
cd -
cp Alignment/MuonAlignmentAlgorithms/test/browser/tree* $ALIGNMENT_CAFDIR/out/

# copy the results to CAFDIR
cp -f %(directory1)s%(director1)s_report.py $ALIGNMENT_CAFDIR/files/
cp -f %(directory)s%(director)s_report.py $ALIGNMENT_CAFDIR/files/
cp -f %(directory1)s%(director1)s.root $ALIGNMENT_CAFDIR/files/
cp -f %(directory)s%(director)s.root $ALIGNMENT_CAFDIR/files/
if [ -e %(directory1)s%(director1)s_plotting.root ] && [ -e %(directory)s%(director)s_plotting.root ]; then
  cp -f %(directory1)s%(director1)s_plotting.root $ALIGNMENT_CAFDIR/files/
  cp -f %(directory)s%(director)s_plotting.root $ALIGNMENT_CAFDIR/files/
  ALIGNMENT_MAPPLOTS=%(mapplots)s
  ALIGNMENT_SEGDIFFPLOTS=%(segdiffplots)s
  ALIGNMENT_CURVATUREPLOTS=%(curvatureplots)s
fi

dtcsc=""
if [ $ALIGNMENT_DO_DT == \"True\" ]; then
  dtcsc="--dt"
fi
if [ $ALIGNMENT_DO_CSC == \"True\" ]; then
  dtcsc="${dtcsc} --csc"
fi


cd $ALIGNMENT_CAFDIR/
echo \" ### Start running ###\"
date

# do fits and median plots first 
./alignmentValidation.py -l %(validationLabel)s -i $ALIGNMENT_CAFDIR --i1 files --iN files --i1prefix %(director1)s --iNprefix %(director)s -o $ALIGNMENT_CAFDIR/out  --createDirSructure --dt --csc --fit --median

if [ $ALIGNMENT_MAPPLOTS == \"True\" ]; then
  ./alignmentValidation.py -l %(validationLabel)s -i $ALIGNMENT_CAFDIR --i1 files --iN files --i1prefix %(director1)s --iNprefix %(director)s -o $ALIGNMENT_CAFDIR/out  $dtcsc --map
fi

if [ $ALIGNMENT_SEGDIFFPLOTS == \"True\" ]; then
  ./alignmentValidation.py -l %(validationLabel)s -i $ALIGNMENT_CAFDIR --i1 files --iN files --i1prefix %(director1)s --iNprefix %(director)s -o $ALIGNMENT_CAFDIR/out  $dtcsc --segdiff
fi                   

if [ $ALIGNMENT_CURVATUREPLOTS == \"True\" ]; then
  ./alignmentValidation.py -l %(validationLabel)s -i $ALIGNMENT_CAFDIR --i1 files --iN files --i1prefix %(director1)s --iNprefix %(director)s -o $ALIGNMENT_CAFDIR/out  $dtcsc --curvature
fi

if [ $ALIGNMENT_EXTRAPLOTS == \"True\" ]; then
  if [ \"zzz%(copytrackerdb)s\" != \"zzz\" ]; then
    cp -f $ALIGNMENT_AFSDIR/%(copytrackerdb)s $ALIGNMENT_CAFDIR/
  fi
  cp $ALIGNMENT_AFSDIR/inertGlobalPositionRcd.db .
  ./convertSQLiteXML.py $ALIGNMENT_AFSDIR/%(INITIALGEOM)s g0.xml --noLayers  --gprcdconnect $ALIGNMENT_GPRCDCONNECT --gprcd $ALIGNMENT_GPRCD
  ./wrapperExtraPlots.sh -n $ALIGNMENT_ITERATION -i $ALIGNMENT_AFSDIR -0 g0.xml -z -w %(station123params)s %(dir_no_)s
  mkdir out/extra
  cd %(dir_no_)s
  mv MB ../out/extra/
  mv ME ../out/extra/
  cd -
fi

# run simple diagnostic
./alignmentValidation.py -l %(validationLabel)s -i $ALIGNMENT_CAFDIR --i1 files --iN files --i1prefix %(director1)s --iNprefix %(director)s -o $ALIGNMENT_CAFDIR/out --dt --csc --diagnostic

# fill the tree browser structure: 
./createTree.py -i $ALIGNMENT_CAFDIR/out

timestamp=`date \"+%%y-%%m-%%d %%H:%%M:%%S\"`
echo \"%(validationLabel)s.plots (${timestamp})\" > out/label.txt

ls -l out/
timestamp=`date +%%Y%%m%%d%%H%%M%%S`
tar czf %(validationLabel)s_${timestamp}.tgz out
cp -f %(validationLabel)s_${timestamp}.tgz $ALIGNMENT_AFSDIR/

""" % my_vars)


#####################################################################

#SUPER_SPECIAL_XY_AND_DXDZ_ITERATIONS = True
SUPER_SPECIAL_XY_AND_DXDZ_ITERATIONS = False

bsubfile   = ["#!/bin/sh", ""]
bsubnames  = []
last_align = None
directory  = ""

for iteration in range(1, ITERATIONS+1):
    if iteration == 1:
        inputdb    = INITIALGEOM
        inputdbdir = directory[:]
    else:
        inputdb    = director+".db"
        inputdbdir = directory[:]

    directory   = "{0}_{1:02d}".format(DIRNAME,iteration)
    director    = directory
    dir_no_     = DIRNAME
    script_path = "Alignment/MuonAlignmentAlgorithms/python/"
 
    os.system( "rm -rf {0}; mkdir {0}".format(directory) )
    os.system( "cp {0}/gather_cfg.py {0}".format(script_path,directory) )
    os.system( "cp {0}/align_cfg.py {0}".format(script_path,directory) )

    bsubfile.append("cd {0}".format(directory))

    mapplots = False
    if mapplots_ingeneral and any( [iteration==i for i in [1,3,5,7,9,ITERATIONS]] ):
        mapplots = True

    segdiffplots = False
    if segdiffplots_ingeneral and (iteration == 1 or iteration == ITERATIONS):
        segdiffplots = True

    curvatureplots = False
    if curvatureplots_ingeneral and (iteration == 1 or iteration == ITERATIONS):
        curvatureplots = True


    ### gather.sh runners for njobs
    for jobnumber in range(njobs):
        if not cfg.inputInBlocks:
            inputfiles = " ".join(fileNames[jobnumber*stepsize:(jobnumber+1)*stepsize])
        else:
            inputfiles = " ".join(fileNamesBlocks[jobnumber])
        
        if mapplots or segdiffplots or curvatureplots:
            copyplots = "plotting*.root"
        else:
            copyplots = ""

        if len(inputfiles) > 0:
            gather_fileName = "{0}/gather{1:03d}.sh".format(directory, jobnumber)
            writeGatherCfg(gather_fileName, vars())
            os.system("chmod +x {0}".format(gather_fileName)
            bsubfile.append("echo {0}".format(gather_filename))

            waiter = "" if last_align is None else "-w \"ended({0})\"".format(last_align)          
            queue  = "cmscaf1nd" if cfg.big else "cmscaf1nh"

            bsubfile.append("bsub -R \"type==SLC6_64\" -q %s -J \"%s_gather%03d\" -u youremail.tamu.edu %s gather%03d.sh" % (queue, director, jobnumber, waiter, jobnumber))

            bsubnames.append("ended(%s_gather%03d)" % (director, jobnumber)()


    ### align.sh
    if SUPER_SPECIAL_XY_AND_DXDZ_ITERATIONS:
        if ( 0 < iteration <= 10 and iteration%2!=0 ): # 1,3,5,7,9
            tmp = station123params, station123params, useResiduals 
            station123params, station123params, useResiduals = "000010", "000010", "0010"
            writeHaddCfg("%shadd.sh" % directory, vars()()
            writeAlignCfg("%salign.sh" % directory, vars()()
            station123params, station123params, useResiduals = tmp
        elif ( 0 < iteration <= 10 and iteration%2==0 ): # 2,4,6,8
            tmp = station123params, station123params, useResiduals 
            station123params, station123params, useResiduals = "110001", "100001", "1100"
            writeHaddCfg("%shadd.sh" % directory, vars())
            writeAlignCfg("%salign.sh" % directory, vars())
            station123params, station123params, useResiduals = tmp
    else:
        writeHaddCfg("%shadd.sh" % directory, vars())
        writeAlignCfg("%salign.sh" % directory, vars())
    
    os.system("chmod +x %shadd.sh" % directory)
    os.system("chmod +x %salign.sh" % directory)

    bsubfile.append("echo %shadd.sh" % directory)

    
    if user_mail:
        bsubfile.append("bsub -R \"type==SLC6_64\" -q cmscaf1nd -J \"%s_hadd\" -u %s -w \"%s\" hadd.sh" % (director, user_mail, " && ".join(bsubnames)))
    else: 
        bsubfile.append("bsub -R \"type==SLC6_64\" -q cmscaf1nd -J \"%s_hadd\" -w \"%s\" hadd.sh" % (director, " && ".join(bsubnames)))

    bsubfile.append("echo %salign.sh" % directory()

    if user_mail:
        bsubfile.append("bsub -R \"type==SLC6_64\" -q cmscaf1nd -J \"%s_align\" -u %s -w \"%s\" align.sh" % (director, user_mail, " && ".join(bsubnames)))
    else: 
        bsubfile.append("bsub -R \"type==SLC6_64\" -q cmscaf1nd -J \"%s_align\" -w \"%s\" align.sh" % (director, " && ".join(bsubnames)))
    
    #bsubfile.append("cd .."()
    bsubnames = []
    last_align = "%s_align) && ended(%s_hadd" % (director, director)
    

    ### after the last iteration (optionally) do diagnostics run
    if validationLabel and iteration == ITERATIONS:
        # do we have plotting files created?
        directory1 = "{0}_01/".format(DIRNAME)
        director1  = directory1[:-1]

        writeValidationCfg("{0}validation.sh".format(directory, vars()))
        os.system("chmod +x {0}validation.sh".format(directory))
        
        bsubfile.append("echo {0}validation.sh".format(directory))

        bsub_args = "bsub -R \"type==SLC6_64\" -q cmscaf1nd -J \"{0}_validation\" -w \"ended({1})\" validation.sh".format(director,last_align)
        if user_mail:
            bsub_args += " -u {0}".format(user_mail)
        bsubfile.append(bsub_args)

    bsubfile.append("cd ..")
    bsubfile.append("")


file(cfg.submitJobs, "w").write("\n".join(bsubfile))
os.system("chmod +x {0}".format(cfg.submitJobs))
