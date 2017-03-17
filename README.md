# Alignment
Setup your environment:   
```
SCRAM_ARCH=slc6_amd64_gcc530; export SCRAM_ARCH;
cmsrel CMSSW_9_0_0_pre4
cd CMSSW_9_0_0_pre4/src/
cmsenv
git clone https://github.com/cms-mual/Alignment.git -b CMSSW_9_0_X
git clone https://github.com/cms-mual/TrackingTools.git -b CMSSW_9_0_X
git clone https://github.com/cms-mual/MuAlSupplementaryFiles.git -b CMSSW_8_0_X
cp MuAlSupplementaryFiles/* .
ln -s Alignment/MuonAlignmentAlgorithms/scripts/createJobs.py
ln -s Alignment/MuonAlignmentAlgorithms/python/gather_cfg.py
ln -s Alignment/MuonAlignmentAlgorithms/python/align_cfg.py
scram b -j 16
```
Additional folders (you can use still old branches):   
```
git clone https://github.com/cms-mual/MuAlPhysicsValidation.git
git clone https://github.com/cms-mual/PlottingTools.git
```
Run DT alignment starting with ideal muon geometry:

    ./createJobs.py mc_DT-1100-110001_CMSSW_8_0_0_patch1_ideal_v1_ 3 \
    idealMuonGeometry_DESRUN2_74_V4.APEsExtd.StdTags.746p3.DBv2.db \
    SingleMuonGun_CMSSW_8_0_0_patch1_100K_35GeV_v1.py --inputInBlocks \
    -s mc_DT-1100-110001_CMSSW_8_0_0_patch1_ideal_v1.sh \
    --validationLabel mc_DT-1100-110001_CMSSW_8_0_0_patch1_ideal_v1 \
    --b --user_mail youremail --minTrackPt 30 --maxTrackPt 200 --maxDxy 0.2 \
    --minNCrossedChambers 1 --residualsModel pureGaussian --peakNSigma 2. \
    --station123params 110001 --station4params 100001 --cscparams 100001 --useResiduals 1100 \
    --mapplots --curvatureplots --segdiffplots --extraPlots \
    --globalTag 80X_mcRun2_design_v5 \
    --createAlignNtuple --noCleanUp --noCSC \
    --gprcdconnect sqlite_file:inertGlobalPositionRcd.StdTags.746p3.DBv2.db \
    --gprcd inertGlobalPositionRcd
    
    source mc_DT-1100-110001_CMSSW_8_0_0_patch1_ideal_v1.sh

Run CSC Alignment starting with ideal muon geometry:

    ./createJobs.py mc_CSC-1100-110001_CMSSW_8_0_0_patch1_ideal_v1_ 3 \
    idealMuonGeometry_DESRUN2_74_V4.APEsExtd.StdTags.746p3.DBv2.db \
    SingleMuonGun_CMSSW_8_0_0_patch1_100K_35GeV_v1.py --inputInBlocks \
    -s mc_CSC-1100-110001_CMSSW_8_0_0_patch1_ideal_v1.sh \
    --validationLabel mc_CSC-1100-110001_CMSSW_8_0_0_patch1_ideal_v1 \
    --b --user_mail youremail --minTrackPt 30 --maxTrackPt 200 --maxDxy 0.2 \
    --minNCrossedChambers 1 --residualsModel pureGaussian --peakNSigma 2. \
    --station123params 110001 --station4params 100001 --cscparams 100001 --useResiduals 1100 \
    --mapplots --curvatureplots --segdiffplots --extraPlots \
    --globalTag 80X_mcRun2_design_v5 \
    --createAlignNtuple --noCleanUp --noDT \
    --gprcdconnect sqlite_file:inertGlobalPositionRcd.StdTags.746p3.DBv2.db \
    --gprcd inertGlobalPositionRcd
    
    source mc_CSC-1100-110001_CMSSW_8_0_0_patch1_ideal_v1.sh
    
Run DT alignment starting with misaligned muon geometry:

    ./createJobs.py mc_DT-1100-110001_CMSSW_8_0_0_patch1_misaligned_v1_ 3 \
    MuonGeometry_MC_Run2Startup_June2015_Csc2mm1mrad_DtHWUnct_v1.StdTags.746p3.DBv2.db \
    SingleMuonGun_CMSSW_8_0_0_patch1_100K_35GeV_v1.py --inputInBlocks \
    -s mc_DT-1100-110001_CMSSW_8_0_0_patch1_misaligned_v1.sh \
    --validationLabel mc_DT-1100-110001_CMSSW_8_0_0_patch1_misaligned_v1 \
    --b --user_mail youremail --minTrackPt 30 --maxTrackPt 200 --maxDxy 0.2 \
    --minNCrossedChambers 1 --residualsModel pureGaussian --peakNSigma 2. \
    --station123params 110001 --station4params 100001 --cscparams 100001 --useResiduals 1100 \
    --mapplots --curvatureplots --segdiffplots --extraPlots \
    --globalTag 80X_mcRun2_design_v5 \
    --createAlignNtuple --noCleanUp --noCSC \
    --gprcdconnect sqlite_file:inertGlobalPositionRcd.StdTags.746p3.DBv2.db \
    --gprcd inertGlobalPositionRcd
    
    source mc_DT-1100-110001_CMSSW_8_0_0_patch1_misaligned_v1.sh

Run CSC Alignment starting with misaligned muon geometry:

    ./createJobs.py mc_CSC-1100-110001_CMSSW_8_0_0_patch1_misaligned_v1_ 3 \
    MuonGeometry_MC_Run2Startup_June2015_Csc2mm1mrad_DtHWUnct_v1.StdTags.746p3.DBv2.db \
    SingleMuonGun_CMSSW_8_0_0_patch1_100K_35GeV_v1.py --inputInBlocks \
    -s mc_CSC-1100-110001_CMSSW_8_0_0_patch1_misaligned_v1.sh \
    --validationLabel mc_CSC-1100-110001_CMSSW_8_0_0_patch1_misaligned_v1 \
    --b --user_mail youremail --minTrackPt 30 --maxTrackPt 200 --maxDxy 0.2 \
    --minNCrossedChambers 1 --residualsModel pureGaussian --peakNSigma 2. \
    --station123params 110001 --station4params 100001 --cscparams 100001 --useResiduals 1100 \
    --mapplots --curvatureplots --segdiffplots --extraPlots \
    --globalTag 80X_mcRun2_design_v5 \
    --createAlignNtuple --noCleanUp --noDT \
    --gprcdconnect sqlite_file:inertGlobalPositionRcd.StdTags.746p3.DBv2.db \
    --gprcd inertGlobalPositionRcd
    
    source mc_CSC-1100-110001_CMSSW_8_0_0_patch1_misaligned_v1.sh

Add validation plots to the validation browser:   
```
cd /afs/cern.ch/cms/CAF/CMSALCA/ALCA_MUONALIGN/www/browser_plots/validation    
./add_tarballs.sh [PATH_TO_TARBALL_MADE_BY_ALIGNMENT_JOB]
```
Json File location:   
    /afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions16/13TeV/Cert_271036-274421_13TeV_PromptReco_Collisions16_JSON_MuonPhys.txt 
