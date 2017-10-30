"""
Created:       14 August 2017
Last Updated:  15 August 2017
Dan Marley
daniel.edison.marley@cernSPAMNOT.ch
Texas A&M University
Fermi National Accelerator Laboratory
-----
Class used to write generic scripts used in batch jobs
"""
import os
import sys
from configuration import Configuration


class WriteBatchScripts(object):
    """Write batch scripts using functions and pre-formatted text"""
    def __init__(self,cfg):
        self.config      = cfg

        self.dirname     = cfg.name()
        self.commandline = cfg.filename
        self.ITERATIONS  = cfg.iterations()
        self.INITIALGEOM = cfg.initial_geometry()
        self.INITIALXML  = self.INITIALGEOM.replace('.db','')+'.xml'

        self.createLayerNtupleDT  = cfg.createLayerNtupleDT()
        self.createLayerNtupleCSC = cfg.createLayerNtupleCSC()

        self.doCSC = cfg.doCSC()
        self.doDT  = cfg.doDT()
        
        self.trackerAPE = cfg.trackerAPE()
        self.globaltag  = cfg.globaltag()
        self.user_mail  = cfg.user_mail()
        self.cscparams  = cfg.cscparams()
        self.gprcd      = cfg.gprcd()
        self.iscosmics  = cfg.iscosmics()
        self.json_file  = cfg.json()
        self.minTrackPt = cfg.minTrackPt()
        self.maxTrackPt = cfg.maxTrackPt()
        self.minTrackP  = cfg.minTrackP()
        self.maxTrackP  = cfg.maxTrackP()
        self.maxDxy     = cfg.maxDxy()
        self.twoBin     = cfg.twoBin()
        self.doCleanUp  = cfg.doCleanUp()
        self.T0_Corr    = cfg.T0()
        self.is_MC      = cfg.is_MC()
        self.njobs      = cfg.subjobs()
        self.maxEvents  = cfg.maxEvents()
        self.skipEvents = cfg.skipEvents()
        self.theNSigma  = cfg.motionPolicyNSigma()
        self.peakNSigma = cfg.peakNSigma()
        self.preFilter  = cfg.preFilter()
        self.extraPlots = cfg.extraPlots()

        self.combineME11  = not cfg.notCombineME11()
        self.trackerBows  = cfg.trackerBows()
        self.gprcdconnect = cfg.gprcdconnect()
        self.allowTIDTEC  = cfg.allowTIDTEC()
        self.is_Alcareco  = cfg.is_Alca()
        self.maxResSlopeY = cfg.maxResSlopeY()
        self.useResiduals = cfg.useResiduals()

        self.trackerconnect  = cfg.trackerconnect()
        self.weightAlignment = cfg.weightAlignment()
        self.validationLabel = cfg.validationLabel()
        self.residualsModel  = cfg.residualsModel()
        self.createMapNtuple = cfg.createMapNtuple()
        self.station4params  = cfg.station4params()

        self.createAlignNtuple = cfg.createAlignNtuple()
        self.minAlignmentHits  = cfg.minAlignmentSegments()
        self.trackeralignment  = cfg.trackeralignment()
        self.trackerAPEconnect = cfg.trackerAPEconnect()
        self.station123params  = cfg.station123params()
        self.muonCollectionTag = cfg.muonCollectionTag()
        self.minTrackerHits    = cfg.minTrackerHits()
        self.maxTrackerRedChi2 = cfg.maxTrackerRedChi2()

        self.minNCrossedChambers = cfg.minNCrossedChambers()
        self.mapplots_ingeneral  = cfg.mapplots()
        self.trackerBowsconnect  = cfg.trackerBowsconnect()

        self.segdiffplots_ingeneral   = cfg.segdiffplots()
        self.curvatureplots_ingeneral = cfg.curvatureplots()

        sqlite_tag = "sqlite_file:"
        self.copytrackerdb = ""
        if self.trackerconnect.startswith(sqlite_tag):
            self.copytrackerdb += self.trackerconnect[12:]
        if self.trackerAPEconnect.startswith(sqlite_tag): 
            self.copytrackerdb += self.trackerAPEconnect[12:]
        if self.trackerBowsconnect.startswith(sqlite_tag): 
            self.copytrackerdb += self.trackerBowsconnect[12:]
        if self.gprcdconnect.startswith(sqlite_tag): 
            self.copytrackerdb += self.gprcdconnect[12:]

        # ** parameters that need to be set by user ** #
        self.inputdbdir = ""
        self.inputdb    = ""
        self.directory  = "{0}_{1:02d}/".format(cfg.name(),1)
        self.director   = self.directory
        self.mapplots       = False
        self.segdiffplots   = False
        self.curvatureplots = False
        self.inputfiles     = ""
        self.iteration   = 1
        self.jobumber    = 0
        self.copyplots   = ""
        self.directory1  = ""
        self.director1   = ""



    #####################################################################
    def writeGatherCfg(self,fname):
        file(fname,"w").write("""#/bin/sh
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
""" % self.__dict__)

        return



    #####################################################################
    def writeHaddCfg(self,fname):
        file(fname,"w").write("""#!/bin/sh
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
""" % self.__dict__)

        return


    #####################################################################
    def writeAlignCfg(self,fname):
        file(fname,"w").write("""#!/bin/sh
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
""" % self.__dict__)

        return


    #####################################################################
    def writeValidationCfg(self,fname):
        file(fname,"w").write("""#!/bin/sh
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
  ./wrapperExtraPlots.sh -n $ALIGNMENT_ITERATION -i $ALIGNMENT_AFSDIR -0 g0.xml -z -w %(station123params)s %(dirname)s
  mkdir out/extra
  cd %(dirname)s
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
""" % self.__dict__)

        return


## THE END ##
