gather_cfg_str = """#/bin/sh
export ALIGNMENT_CAFDIR=`pwd`
cd {pwd}
eval `scramv1 run -sh`
export ALIGNMENT_AFSDIR=`pwd`
export ALIGNMENT_INPUTFILES='{inputfiles}'
export ALIGNMENT_ITERATION={iteration}
export ALIGNMENT_JOBNUMBER={jobnumber}
export ALIGNMENT_MAPPLOTS={mapplots}
export ALIGNMENT_SEGDIFFPLOTS={segdiffplots}
export ALIGNMENT_CURVATUREPLOTS={curvatureplots}
export ALIGNMENT_GLOBALTAG={globaltag}
export ALIGNMENT_INPUTDB={inputdb}
export ALIGNMENT_TRACKERCONNECT={trackerconnect}
export ALIGNMENT_TRACKERALIGNMENT={trackeralignment}
export ALIGNMENT_TRACKERAPECONNECT={trackerAPEconnect}
export ALIGNMENT_TRACKERAPE={trackerAPE}
export ALIGNMENT_TRACKERBOWSCONNECT={trackerBowsconnect}
export ALIGNMENT_TRACKERBOWS={trackerBows}
export ALIGNMENT_GPRCDCONNECT={gprcdconnect}
export ALIGNMENT_GPRCD={gprcd}
export ALIGNMENT_ISCOSMICS={iscosmics}
export ALIGNMENT_STATION123PARAMS={station123params}
export ALIGNMENT_STATION4PARAMS={station4params}
export ALIGNMENT_CSCPARAMS={cscparams}
export ALIGNMENT_MUONCOLLECTIONTAG={muonCollectionTag}
export ALIGNMENT_MINTRACKPT={minTrackPt}
export ALIGNMENT_MAXTRACKPT={maxTrackPt}
export ALIGNMENT_MINTRACKP={minTrackP}
export ALIGNMENT_MAXTRACKP={maxTrackP}
export ALIGNMENT_MAXDXY={maxDxy}
export ALIGNMENT_MINTRACKERHITS={minTrackerHits}
export ALIGNMENT_MAXTRACKERREDCHI2={maxTrackerRedChi2}
export ALIGNMENT_MINNCROSSEDCHAMBERS={minNCrossedChambers}
export ALIGNMENT_ALLOWTIDTEC={allowTIDTEC}
export ALIGNMENT_TWOBIN={twoBin}
export ALIGNMENT_WEIGHTALIGNMENT={weightAlignment}
export ALIGNMENT_MINALIGNMENTHITS={minAlignmentHits}
export ALIGNMENT_COMBINEME11={combineME11}
export ALIGNMENT_MAXEVENTS={maxEvents}
export ALIGNMENT_SKIPEVENTS={skipEvents}
export ALIGNMENT_MAXRESSLOPEY={maxResSlopeY}
export ALIGNMENT_DO_DT={doDT}
export ALIGNMENT_DO_CSC={doCSC}
export ALIGNMENT_JSON={json}
export ALIGNMENT_CREATEMAPNTUPLE={createMapNtuple}
#export ALIGNMENT_CREATEALIGNNTUPLE={createAlignNtuple}
export ALIGNMENT_PREFILTER={preFilter}
export ALIGNMENT_T0CORR={T0_Corr}
export ALIGNMENT_ISALCARECO={is_Alcareco}
export ALIGNMENT_ISMC={is_MC}
export ALIGNMENT_STORELAYERDT={createLayerNtupleDT}
export ALIGNMENT_STORELAYERCSC={createLayerNtupleCSC}
if [ \"zzz$ALIGNMENT_JSON\" != \"zzz\" ]; then
  cp -f $ALIGNMENT_JSON $ALIGNMENT_CAFDIR/
fi
cp -f {directory}gather_cfg.py {inputdbdir}{inputdb} {copytrackerdb} $ALIGNMENT_CAFDIR/
cd $ALIGNMENT_CAFDIR/
cmsRun gather_cfg.py
cp -f *.tmp {copyplots} $ALIGNMENT_AFSDIR/{directory}
"""

hadd_cfg_str = """#!/bin/sh

export ALIGNMENT_CAFDIR=`pwd`

cd {pwd}
eval `scramv1 run -sh`
export ALIGNMENT_AFSDIR=`pwd`
export ALIGNMENT_INPUTDB={inputdb}
export ALIGNMENT_ITERATION={iteration}
export ALIGNMENT_GLOBALTAG={globaltag}
export ALIGNMENT_TRACKERCONNECT={trackerconnect}
export ALIGNMENT_TRACKERALIGNMENT={trackeralignment}
export ALIGNMENT_TRACKERAPECONNECT={trackerAPEconnect}
export ALIGNMENT_TRACKERAPE={trackerAPE}
export ALIGNMENT_TRACKERBOWSCONNECT={trackerBowsconnect}
export ALIGNMENT_TRACKERBOWS={trackerBows}
export ALIGNMENT_GPRCDCONNECT={gprcdconnect}
export ALIGNMENT_GPRCD={gprcd}
export ALIGNMENT_ISCOSMICS={iscosmics}
export ALIGNMENT_STATION123PARAMS={station123params}
export ALIGNMENT_STATION4PARAMS={station4params}
export ALIGNMENT_CSCPARAMS={cscparams}
export ALIGNMENT_MINTRACKPT={minTrackPt}
export ALIGNMENT_MAXTRACKPT={maxTrackPt}
export ALIGNMENT_MINTRACKP={minTrackP}
export ALIGNMENT_MAXTRACKP={maxTrackP}
export ALIGNMENT_MINTRACKERHITS={minTrackerHits}
export ALIGNMENT_MAXTRACKERREDCHI2={maxTrackerRedChi2}
export ALIGNMENT_ALLOWTIDTEC={allowTIDTEC}
export ALIGNMENT_TWOBIN={twoBin}
export ALIGNMENT_WEIGHTALIGNMENT={weightAlignment}
export ALIGNMENT_MINALIGNMENTHITS={minAlignmentHits}
export ALIGNMENT_COMBINEME11={combineME11}
export ALIGNMENT_MAXRESSLOPEY={maxResSlopeY}
export ALIGNMENT_CLEANUP={doCleanUp}
export ALIGNMENT_CREATEALIGNNTUPLE={createAlignNtuple}
export ALIGNMENT_RESIDUALSMODEL={residualsModel}
export ALIGNMENT_PEAKNSIGMA={peakNSigma}
export ALIGNMENT_USERESIDUALS={useResiduals}
export ALIGNMENT_DO_DT={doDT}
export ALIGNMENT_DO_CSC={doCSC}

cp -f {directory}align_cfg.py {inputdbdir}{inputdb} {directory}*.tmp  {copytrackerdb} $ALIGNMENT_CAFDIR/

export ALIGNMENT_PLOTTINGTMP=`find {directory}plotting*.root -maxdepth 1 -size +0 -print( 2> /dev/null`)

# if it's 1st or last iteration, combine _plotting.root files into one:
if [ \"$ALIGNMENT_ITERATION\" != \"111\" ] || [ \"$ALIGNMENT_ITERATION\" == \"{ITERATIONS}\" ]; then
  #nfiles=$(ls {directory}plotting*.root 2> /dev/null | wc -l)
  if [ \"zzz$ALIGNMENT_PLOTTINGTMP\" != \"zzz\" ]; then
    hadd -f1 -k {directory}{director}_plotting.root {directory}plotting*.root
    #if [ $? == 0 ] && [ \"$ALIGNMENT_CLEANUP\" == \"True\" ]; then rm {directory}plotting*.root; fi
  fi
fi
if [ \"$ALIGNMENT_CLEANUP\" == \"True\" ] && [ \"zzz$ALIGNMENT_PLOTTINGTMP\" != \"zzz\" ]; then
  rm $ALIGNMENT_PLOTTINGTMP
fi
"""


align_cfg_str = """#!/bin/sh

export ALIGNMENT_CAFDIR=`pwd`

cd {pwd}
eval `scramv1 run -sh`
export ALIGNMENT_AFSDIR=`pwd`
export ALIGNMENT_INPUTDB={inputdb}
export ALIGNMENT_ITERATION={iteration}
export ALIGNMENT_GLOBALTAG={globaltag}
export ALIGNMENT_TRACKERCONNECT={trackerconnect}
export ALIGNMENT_TRACKERALIGNMENT={trackeralignment}
export ALIGNMENT_TRACKERAPECONNECT={trackerAPEconnect}
export ALIGNMENT_TRACKERAPE={trackerAPE}
export ALIGNMENT_TRACKERBOWSCONNECT={trackerBowsconnect}
export ALIGNMENT_TRACKERBOWS={trackerBows}
export ALIGNMENT_GPRCDCONNECT={gprcdconnect}
export ALIGNMENT_GPRCD={gprcd}
export ALIGNMENT_ISCOSMICS={iscosmics}
export ALIGNMENT_STATION123PARAMS={station123params}
export ALIGNMENT_STATION4PARAMS={station4params}
export ALIGNMENT_CSCPARAMS={cscparams}
export ALIGNMENT_MINTRACKPT={minTrackPt}
export ALIGNMENT_MAXTRACKPT={maxTrackPt}
export ALIGNMENT_MINTRACKP={minTrackP}
export ALIGNMENT_MAXTRACKP={maxTrackP}
export ALIGNMENT_MINTRACKERHITS={minTrackerHits}
export ALIGNMENT_MAXTRACKERREDCHI2={maxTrackerRedChi2}
export ALIGNMENT_ALLOWTIDTEC={allowTIDTEC}
export ALIGNMENT_TWOBIN={twoBin}
export ALIGNMENT_WEIGHTALIGNMENT={weightAlignment}
export ALIGNMENT_MINALIGNMENTHITS={minAlignmentHits}
export ALIGNMENT_COMBINEME11={combineME11}
export ALIGNMENT_MAXRESSLOPEY={maxResSlopeY}
export ALIGNMENT_CLEANUP={doCleanUp}
export ALIGNMENT_CREATEALIGNNTUPLE={createAlignNtuple}
export ALIGNMENT_RESIDUALSMODEL={residualsModel}
export ALIGNMENT_PEAKNSIGMA={peakNSigma}
export ALIGNMENT_USERESIDUALS={useResiduals}
export ALIGNMENT_DO_DT={doDT}
export ALIGNMENT_DO_CSC={doCSC}
export ALIGNMENT_ISMC={is_MC}

cp -f {directory}align_cfg.py {inputdbdir}{inputdb} {directory}*.tmp  {copytrackerdb} $ALIGNMENT_CAFDIR/

export ALIGNMENT_PLOTTINGTMP=`find {directory}plotting*.root -maxdepth 1 -size +0 -print( 2> /dev/null`)

cd $ALIGNMENT_CAFDIR/
export ALIGNMENT_ALIGNMENTTMP=`find alignment*.tmp -maxdepth 1 -size +1k -print( 2> /dev/null`)
ls -l

cmsRun align_cfg.py
cp -f MuonAlignmentFromReference_report.py $ALIGNMENT_AFSDIR/{directory}{director}_report.py
cp -f MuonAlignmentFromReference_outputdb.db $ALIGNMENT_AFSDIR/{directory}{director}.db
cp -f MuonAlignmentFromReference_plotting.root $ALIGNMENT_AFSDIR/{directory}{director}.root

cd $ALIGNMENT_AFSDIR
./Alignment/MuonAlignmentAlgorithms/scripts/convertSQLiteXML.py {directory}{director}.db {directory}{director}.xml --noLayers --gprcdconnect $ALIGNMENT_GPRCDCONNECT --gprcd $ALIGNMENT_GPRCD

export ALIGNMENT_ALIGNMENTTMP=`find {directory}alignment*.tmp -maxdepth 1 -size +1k -print( 2> /dev/null`)
if [ \"$ALIGNMENT_CLEANUP\" == \"True\" ] && [ \"zzz$ALIGNMENT_ALIGNMENTTMP\" != \"zzz\" ]; then
  rm $ALIGNMENT_ALIGNMENTTMP
  echo " "
fi

# if it's not 1st or last iteration, do some clean up:
if [ \"$ALIGNMENT_ITERATION\" != \"1\" ] && [ \"$ALIGNMENT_ITERATION\" != \"{ITERATIONS}\" ]; then
  if [ \"$ALIGNMENT_CLEANUP\" == \"True\" ] && [ -e {directory}{director}.root ]; then
    rm {directory}{director}.root
  fi
fi

# if it's last iteration, apply chamber motion policy
if [ \"$ALIGNMENT_ITERATION\" == \"{ITERATIONS}\" ]; then
  # convert this iteration's geometry into detailed xml
  ./Alignment/MuonAlignmentAlgorithms/scripts/convertSQLiteXML.py {directory}{director}.db {directory}{director}_extra.xml --gprcdconnect $ALIGNMENT_GPRCDCONNECT --gprcd $ALIGNMENT_GPRCD
  echo "Perform motion policy "
  echo "/Alignment/MuonAlignmentAlgorithms/scripts/motionPolicyChamber.py {INITIALXML}  {directory}{director}_extra.xml {directory}{director}_report.py {directory}{director}_final.xml --nsigma {theNSigma}"
  ./Alignment/MuonAlignmentAlgorithms/scripts/motionPolicyChamber.py \
      {INITIALXML}  {directory}{director}_extra.xml \
      {directory}{director}_report.py \
      {directory}{director}_final.xml \
      --nsigma {theNSigma}
  echo "Convert the resulting xml into the final sqlite geometry "
  echo "./Alignment/MuonAlignmentAlgorithms/scripts/convertSQLiteXML.py {directory}{director}_final.xml {directory}{director}_final.db --gprcdconnect $ALIGNMENT_GPRCDCONNECT --gprcd $ALIGNMENT_GPRCD"
  ./Alignment/MuonAlignmentAlgorithms/scripts/convertSQLiteXML.py {directory}{director}_final.xml {directory}{director}_final.db --gprcdconnect $ALIGNMENT_GPRCDCONNECT --gprcd $ALIGNMENT_GPRCD
fi

"""

validation_cfg_str = """#!/bin/sh

export ALIGNMENT_CAFDIR=`pwd`
mkdir files
mkdir out

cd {pwd}
eval `scramv1 run -sh`
ALIGNMENT_AFSDIR=`pwd`
ALIGNMENT_ITERATION={iteration}
ALIGNMENT_MAPPLOTS=None
ALIGNMENT_SEGDIFFPLOTS=None
ALIGNMENT_CURVATUREPLOTS=None
ALIGNMENT_EXTRAPLOTS={extraPlots}
export ALIGNMENT_GPRCDCONNECT={gprcdconnect}
export ALIGNMENT_GPRCD={gprcd}
export ALIGNMENT_DO_DT={doDT}
export ALIGNMENT_DO_CSC={doCSC}


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
cp -f {directory1}{director1}_report.py $ALIGNMENT_CAFDIR/files/
cp -f {directory}{director}_report.py $ALIGNMENT_CAFDIR/files/
cp -f {directory1}{director1}.root $ALIGNMENT_CAFDIR/files/
cp -f {directory}{director}.root $ALIGNMENT_CAFDIR/files/
if [ -e {directory1}{director1}_plotting.root ] && [ -e {directory}{director}_plotting.root ]; then
  cp -f {directory1}{director1}_plotting.root $ALIGNMENT_CAFDIR/files/
  cp -f {directory}{director}_plotting.root $ALIGNMENT_CAFDIR/files/
  ALIGNMENT_MAPPLOTS={mapplots}
  ALIGNMENT_SEGDIFFPLOTS={segdiffplots}
  ALIGNMENT_CURVATUREPLOTS={curvatureplots}
fi

dtcsc=""
if [ $ALIGNMENT_DO_DT == \"True\" ]; then
  dtcsc="--dt"
fi
if [ $ALIGNMENT_DO_CSC == \"True\" ]; then
  dtcsc="${{dtcsc}} --csc"
fi


cd $ALIGNMENT_CAFDIR/
echo \" ### Start running ###\"
date

# do fits and median plots first 
./alignmentValidation.py -l {validationLabel} -i $ALIGNMENT_CAFDIR --i1 files --iN files --i1prefix {director1} --iNprefix {director} -o $ALIGNMENT_CAFDIR/out  --createDirSructure --dt --csc --fit --median

if [ $ALIGNMENT_MAPPLOTS == \"True\" ]; then
  ./alignmentValidation.py -l {validationLabel} -i $ALIGNMENT_CAFDIR --i1 files --iN files --i1prefix {director1} --iNprefix {director} -o $ALIGNMENT_CAFDIR/out  $dtcsc --map
fi

if [ $ALIGNMENT_SEGDIFFPLOTS == \"True\" ]; then
  ./alignmentValidation.py -l {validationLabel} -i $ALIGNMENT_CAFDIR --i1 files --iN files --i1prefix {director1} --iNprefix {director} -o $ALIGNMENT_CAFDIR/out  $dtcsc --segdiff
fi                   

if [ $ALIGNMENT_CURVATUREPLOTS == \"True\" ]; then
  ./alignmentValidation.py -l {validationLabel} -i $ALIGNMENT_CAFDIR --i1 files --iN files --i1prefix {director1} --iNprefix {director} -o $ALIGNMENT_CAFDIR/out  $dtcsc --curvature
fi

if [ $ALIGNMENT_EXTRAPLOTS == \"True\" ]; then
  if [ \"zzz{copytrackerdb}\" != \"zzz\" ]; then
    cp -f $ALIGNMENT_AFSDIR/{copytrackerdb} $ALIGNMENT_CAFDIR/
  fi
  cp $ALIGNMENT_AFSDIR/inertGlobalPositionRcd.db .
  ./convertSQLiteXML.py $ALIGNMENT_AFSDIR/{INITIALGEOM} g0.xml --noLayers  --gprcdconnect $ALIGNMENT_GPRCDCONNECT --gprcd $ALIGNMENT_GPRCD
  ./wrapperExtraPlots.sh -n $ALIGNMENT_ITERATION -i $ALIGNMENT_AFSDIR -0 g0.xml -z -w {station123params} {dir_no_}
  mkdir out/extra
  cd {dir_no_}
  mv MB ../out/extra/
  mv ME ../out/extra/
  cd -
fi

# run simple diagnostic
./alignmentValidation.py -l {validationLabel} -i $ALIGNMENT_CAFDIR --i1 files --iN files --i1prefix {director1} --iNprefix {director} -o $ALIGNMENT_CAFDIR/out --dt --csc --diagnostic

# fill the tree browser structure: 
./createTree.py -i $ALIGNMENT_CAFDIR/out

timestamp=`date \"+%%y-%%m-%%d %%H:%%M:%%S\"`
echo \"{validationLabel}.plots (${{timestamp}})\" > out/label.txt

ls -l out/
timestamp=`date +%%Y%%m%%d%%H%%M%%S`
tar czf {validationLabel}_${{timestamp}}.tgz out
cp -f {validationLabel}_${{timestamp}}.tgz $ALIGNMENT_AFSDIR/

"""
