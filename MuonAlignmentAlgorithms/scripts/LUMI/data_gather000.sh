#/bin/sh
# ./createJobs.py data_DT-1100-110001_SingleMuon_Run2015D-PromptReco-v3_RECO_7_4_6_patch3_pt20_v1_MuAlSummer15b_ 3 MuonAlignment_July2015_746p3_data-Run2015B-Prompt_v1_IOV-1-inf_StdLabels.db SingleMuon_Run2015D-PromptReco-v3_RECO.py --inputInBlocks --json Cert_246908-259891_13TeV_PromptReco_Collisions15_25ns_JSON_MuonPhys.txt -s data_DT-1100-110001_SingleMuon_Run2015D-PromptReco-v3_RECO_7_4_6_patch3_pt20_v1_MuAlSummer15b.sh --validationLabel data_DT-1100-110001_SingleMuon_Run2015D-PromptReco-v3_RECO_7_4_6_patch3_pt20_v1_MuAlSummer15b --b --user_mail youremail --minTrackPt 20 --maxTrackPt 200 --maxDxy 0.2 --minNCrossedChambers 1 --residualsModel pureGaussian --peakNSigma 2. --station123params 110001 --station4params 100001 --cscparams 100001 --useResiduals 1100 --mapplots --curvatureplots --segdiffplots --extraPlots --globalTag 74X_dataRun2_Prompt_v0 --createAlignNtuple --noCleanUp --noCSC --trackerconnect sqlite_file:2015-07-15_PseudoPCLupdate_TkAlignment.db --trackeralignment testTag --gprcdconnect sqlite_file:GPR_July24_2015_Run2015B_74X_dataRun2_Prompt_v0_Tk150715_dL4_iter1.db --gprcd IdealGeometry

export ALIGNMENT_CAFDIR=`pwd`

cd /afs/cern.ch/work/l/lpernie/MuonAlign/WD/CMSSW_7_4_6_patch3/src
eval `scramv1 run -sh`
export ALIGNMENT_AFSDIR=`pwd`

export ALIGNMENT_INPUTFILES='/store/data/Run2015D/SingleMuon/RECO/PromptReco-v3/000/257/487/00000/9A455067-8A65-E511-9CD5-02163E01438F.root /store/data/Run2015D/SingleMuon/RECO/PromptReco-v4/000/258/440/00000/C44BFB40-776E-E511-92A5-02163E0138CE.root /store/data/Run2015D/SingleMuon/RECO/PromptReco-v3/000/257/751/00000/82D38DD9-5C68-E511-9B3C-02163E014130.root /store/data/Run2015D/SingleMuon/RECO/PromptReco-v4/000/259/686/00000/6A74DFEC-A27A-E511-BC9D-02163E01432E.root /store/data/Run2015D/SingleMuon/RECO/PromptReco-v4/000/258/177/00000/84E51580-A76C-E511-B0E4-02163E011ADE.root /store/data/Run2015D/SingleMuon/RECO/PromptReco-v4/000/258/448/00000/5228DAA9-E76E-E511-9EC7-02163E011D0D.root /store/data/Run2015D/SingleMuon/RECO/PromptReco-v4/000/259/862/00000/D623EC98-DC7B-E511-A368-02163E01477E.root /store/data/Run2015D/SingleMuon/RECO/PromptReco-v4/000/258/214/00000/A8250E31-086D-E511-B5FE-02163E01410A.root /store/data/Run2015D/SingleMuon/RECO/PromptReco-v3/000/257/645/00000/B8B13633-9767-E511-9202-02163E013501.root /store/data/Run2015D/SingleMuon/RECO/PromptReco-v3/000/257/613/00000/88FCF073-B966-E511-9E6E-02163E014525.root /store/data/Run2015D/SingleMuon/RECO/PromptReco-v3/000/256/734/00000/E48244E1-BD5F-E511-9B94-02163E0144D0.root /store/data/Run2015D/SingleMuon/RECO/PromptReco-v3/000/257/822/00000/283074FE-DF68-E511-A277-02163E011DB5.root /store/data/Run2015D/SingleMuon/RECO/PromptReco-v4/000/258/712/00000/BCC591CE-5B71-E511-A7FF-02163E0141A1.root /store/data/Run2015D/SingleMuon/RECO/PromptReco-v3/000/257/599/00000/E4A8D5E2-5366-E511-B824-02163E014186.root /store/data/Run2015D/SingleMuon/RECO/PromptReco-v3/000/256/734/00000/DE139893-AA5F-E511-8D63-02163E013588.root /store/data/Run2015D/SingleMuon/RECO/PromptReco-v4/000/258/440/00000/2280FCEC-786E-E511-BC5A-02163E0135AE.root /store/data/Run2015D/SingleMuon/RECO/PromptReco-v4/000/258/742/00000/26F62252-1572-E511-A0A2-02163E01436C.root /store/data/Run2015D/SingleMuon/RECO/PromptReco-v3/000/257/969/00000/DCD0F114-B569-E511-9B20-02163E01367E.root /store/data/Run2015D/SingleMuon/RECO/PromptReco-v4/000/258/445/00000/76636C9A-D86E-E511-AC71-02163E0136F2.root /store/data/Run2015D/SingleMuon/RECO/PromptReco-v4/000/258/177/00000/44CE8051-866C-E511-BFCC-02163E0145C3.root'
export ALIGNMENT_ITERATION=1
export ALIGNMENT_JOBNUMBER=0
export ALIGNMENT_MAPPLOTS=True
export ALIGNMENT_SEGDIFFPLOTS=True
export ALIGNMENT_CURVATUREPLOTS=True
export ALIGNMENT_GLOBALTAG=74X_dataRun2_Prompt_v0
export ALIGNMENT_INPUTDB=MuonAlignment_July2015_746p3_data-Run2015B-Prompt_v1_IOV-1-inf_StdLabels.db
export ALIGNMENT_TRACKERCONNECT=sqlite_file:2015-07-15_PseudoPCLupdate_TkAlignment.db
export ALIGNMENT_TRACKERALIGNMENT=testTag
export ALIGNMENT_TRACKERAPECONNECT=
export ALIGNMENT_TRACKERAPE=AlignmentErrorsExtended
export ALIGNMENT_TRACKERBOWSCONNECT=
export ALIGNMENT_TRACKERBOWS=TrackerSurfaceDeformations
export ALIGNMENT_GPRCDCONNECT=sqlite_file:GPR_July24_2015_Run2015B_74X_dataRun2_Prompt_v0_Tk150715_dL4_iter1.db
export ALIGNMENT_GPRCD=IdealGeometry
export ALIGNMENT_ISCOSMICS=None
export ALIGNMENT_STATION123PARAMS=110001
export ALIGNMENT_STATION4PARAMS=100001
export ALIGNMENT_CSCPARAMS=100001
export ALIGNMENT_MUONCOLLECTIONTAG=
export ALIGNMENT_MINTRACKPT=20
export ALIGNMENT_MAXTRACKPT=200
export ALIGNMENT_MINTRACKP=0
export ALIGNMENT_MAXTRACKP=10000
export ALIGNMENT_MAXDXY=0.2
export ALIGNMENT_MINTRACKERHITS=15
export ALIGNMENT_MAXTRACKERREDCHI2=10
export ALIGNMENT_MINNCROSSEDCHAMBERS=1
export ALIGNMENT_ALLOWTIDTEC=True
export ALIGNMENT_TWOBIN=None
export ALIGNMENT_WEIGHTALIGNMENT=None
export ALIGNMENT_MINALIGNMENTHITS=5
export ALIGNMENT_COMBINEME11=True
export ALIGNMENT_MAXEVENTS=-1
export ALIGNMENT_SKIPEVENTS=0
export ALIGNMENT_MAXRESSLOPEY=10
export ALIGNMENT_DO_DT=True
export ALIGNMENT_DO_CSC=False
export ALIGNMENT_JSON=Cert_246908-259891_13TeV_PromptReco_Collisions15_25ns_JSON_MuonPhys.txt
export ALIGNMENT_CREATEMAPNTUPLE=False
#export ALIGNMENT_CREATEALIGNNTUPLE=True
export ALIGNMENT_PREFILTER=False


if [ "zzz$ALIGNMENT_JSON" != "zzz" ]; then
  cp -f $ALIGNMENT_JSON $ALIGNMENT_CAFDIR/
fi

cp -f data_DT-1100-110001_SingleMuon_Run2015D-PromptReco-v3_RECO_7_4_6_patch3_pt20_v1_MuAlSummer15b_01/gather_cfg.py MuonAlignment_July2015_746p3_data-Run2015B-Prompt_v1_IOV-1-inf_StdLabels.db 2015-07-15_PseudoPCLupdate_TkAlignment.db GPR_July24_2015_Run2015B_74X_dataRun2_Prompt_v0_Tk150715_dL4_iter1.db  $ALIGNMENT_CAFDIR/
cd $ALIGNMENT_CAFDIR/
ls -l
cmsRun gather_cfg.py
ls -l
cp -f *.tmp plotting*.root $ALIGNMENT_AFSDIR/data_DT-1100-110001_SingleMuon_Run2015D-PromptReco-v3_RECO_7_4_6_patch3_pt20_v1_MuAlSummer15b_01/
