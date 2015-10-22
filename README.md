# Alignment

Setup Muon Alignment in 74X for early Run2 data:

    cmsrel CMSSW_7_4_6_patch3
    cd CMSSW_7_4_6_patch3/src/
    cmsenv
    
    git clone https://github.com/cms-mual/Alignment.git -b CMSSW_7_4_X_DATA
    git clone https://github.com/cms-mual/TrackingTools.git -b CMSSW_7_4_X
    git clone https://github.com/cms-mual/MuAlSupplementaryFiles.git -b CMSSW_7_4_X_DATA
    
    cp MuAlSupplementaryFiles/* .
    ln -s Alignment/MuonAlignmentAlgorithms/scripts/createJobs.py
    ln -s Alignment/MuonAlignmentAlgorithms/python/gather_cfg.py
    ln -s Alignment/MuonAlignmentAlgorithms/python/align_cfg.py
    scram b -j 16
    
How to change fiductial cuts:

    vim Alignment/MuonAlignmentAlgorithms/interface/MuonResidualsFitter.h 
    find this line:
    208 void fiducialCuts(double xMin = -80.0, double xMax = 80.0, double yMin = -80.0, double yMax = 80.0, bool fidcut1=false);  // "new" fiducial cut
    change fidcut1=false to true

Run DT alignment:

    ./createJobs.py data_DT-1100-110001_SingleMuon_Run2015B-PromptReco-v1_RECO_7_4_6_patch3_pt20_v1_ 3 \
    74X_dataRun2_Prompt_v0_AlignmentRcd.db SingleMuon_Run2015B-PromptReco-v1_RECO.py \
    --inputInBlocks \
    --json Cert_246908-255031_13TeV_PromptReco_Collisions15_50ns_JSON_MuonPhys_v2.txt \
    -s data_DT-1100-110001_SingleMuon_Run2015B-PromptReco-v1_RECO_7_4_6_patch3_pt20_v1.sh \
    --validationLabel data_DT-1100-110001_SingleMuon_Run2015B-PromptReco-v1_RECO_7_4_6_patch3_pt20_v1 \
    --b --user_mail youremail --minTrackPt 20 --maxTrackPt 200 --maxDxy 0.2 \
    --minNCrossedChambers 1 --residualsModel pureGaussian --peakNSigma 2. \
    --station123params 110001 --station4params 100001 --cscparams 100001 --useResiduals 1100 \
    --mapplots --curvatureplots --segdiffplots --extraPlots \
    --globalTag 74X_dataRun2_Prompt_v0 \
    --createAlignNtuple --noCleanUp --noCSC \
    --trackerconnect sqlite_file:2015-07-15_PseudoPCLupdate_TkAlignment.db --trackeralignment testTag \
    --gprcdconnect sqlite_file:GPR_July24_2015_Run2015B_74X_dataRun2_Prompt_v0_Tk150715_dL4_iter1.db \
    --gprcd IdealGeometry
    
    source data_DT-1100-110001_SingleMuon_Run2015B-PromptReco-v1_RECO_7_4_6_patch3_pt20_v1.sh

Run CSC Alignment:

    ./createJobs.py data_CSC-1100-110001_SingleMuon_Run2015B-PromptReco-v1_RECO_7_4_6_patch3_pt20_v1_ 3 \
    74X_dataRun2_Prompt_v0_AlignmentRcd.db SingleMuon_Run2015B-PromptReco-v1_RECO.py \
    --inputInBlocks \
    --json Cert_246908-255031_13TeV_PromptReco_Collisions15_50ns_JSON_MuonPhys_v2.txt \
    -s data_CSC-1100-110001_SingleMuon_Run2015B-PromptReco-v1_RECO_7_4_6_patch3_pt20_v1.sh \
    --validationLabel data_CSC-1100-110001_SingleMuon_Run2015B-PromptReco-v1_RECO_7_4_6_patch3_pt20_v1 \
    --b --user_mail youremail --minTrackPt 20 --maxTrackPt 200 --maxDxy 0.2 \
    --minNCrossedChambers 1 --residualsModel pureGaussian --peakNSigma 2. \
    --station123params 110001 --station4params 100001 --cscparams 100001 --useResiduals 1100 \
    --mapplots --curvatureplots --segdiffplots --extraPlots \
    --globalTag 74X_dataRun2_Prompt_v0 \
    --createAlignNtuple --noCleanUp --noDT \
    --trackerconnect sqlite_file:2015-07-15_PseudoPCLupdate_TkAlignment.db --trackeralignment testTag \
    --gprcdconnect sqlite_file:GPR_July24_2015_Run2015B_74X_dataRun2_Prompt_v0_Tk150715_dL4_iter1.db \
    --gprcd IdealGeometry
    
    source data_CSC-1100-110001_SingleMuon_Run2015B-PromptReco-v1_RECO_7_4_6_patch3_pt20_v1.sh

Add validation plots to the validation browser:

    cd /afs/cern.ch/cms/CAF/CMSALCA/ALCA_MUONALIGN/www/browser_plots/validation
    ./add_tarballs.sh [PATH_TO_TARBALL_MADE_BY_ALIGNMENT_JOB]
