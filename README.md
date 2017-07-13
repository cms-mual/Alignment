# Alignment
**Notes for the future releases**
1. CommonAlignmentMonitor can be always taken from the new cmssw release
2. Check if there are any changes you need to take from TrackingTools and Alignment
3. Our version "Alignment/MuonAlignment/python/geometryXMLparser.py" is in Alignment/MuonAlignmentAlgorithms/scripts and it has a line commented otherwise it crash. I believe it is done to be used inside cmssw, and we use in standalone macros.

**Setup your environment:**   
```
SCRAM_ARCH=slc6_amd64_gcc530; export SCRAM_ARCH;
cmsrel CMSSW_9_2_6
cd CMSSW_9_2_6/src/
cmsenv
git clone https://github.com/cms-mual/Alignment.git -b CMSSW_9_2_6
git clone https://github.com/cms-mual/TrackingTools.git -b CMSSW_9_2_6
git clone https://github.com/cms-mual/MuAlSupplementaryFiles.git -b CMSSW_9_0_X
cp MuAlSupplementaryFiles/* .
ln -s Alignment/MuonAlignmentAlgorithms/scripts/createJobs.py
ln -s Alignment/MuonAlignmentAlgorithms/python/gather_cfg.py
ln -s Alignment/MuonAlignmentAlgorithms/python/align_cfg.py
scram b -j 6
```

**Run alignment on MC (DT example):**   
```
1. ./createJobs.py mc_DT-1100-111111_CMSSW_9_1_0_GTasym_39M_13TeV_ 3 MuonGeometry_MC_Run2Startup_June2015_Csc2mm1mrad_DtHWUnct.DBv2.db SingleMuonGun_CMSSW_8_0_24_39M_13TeVSpectrum.py --inputInBlocks -s mc_DT-1100-111111_CMSSW_9_0_1_GTasym_45M_13TeV.sh --validationLabel mc_DT-1100-111111_CMSSW_9_0_1_GTasym_45M_13TeV --b --user_mail youremail --minTrackPt 20 --maxTrackPt 200 --maxDxy 0.2 --minNCrossedChambers 1 --residualsModel pureGaussian --peakNSigma 1.6 --station123params 111111 --station4params 101111 --cscparams 100001 --useResiduals 1100 --mapplots --curvatureplots --segdiffplots --extraPlots --globalTag 80X_mcRun2_asymptotic_2016_TrancheIV_v7 --createAlignNtuple --noCleanUp --noCSC --gprcdconnect sqlite_file:inertGlobalPositionRcd.StdTags.746p3.DBv2.db --gprcd inertGlobalPositionRcd --is_MC
```

**Run alignment on Data (DT example, for CSC you can remove the --T0 option):**
```
1. ./createJobs.py data_DT-1100-111111_CMSSW_926_SingMu_MuAlCalIsoMuv1_294927_297723_92X_dataRun2_Prompt_v5_T0_ 3 data_DT-1100-111111_SingleMuon_Run2016G_MuAlCalIsolatedMu_278820_280385_8_0_24_Rerecov1_03.db SingleMuon_Run2017B-MuAlCalIsolatedMu-PromptReco-v1_297031_297723.py --json Cert_294927-297723_13TeV_PromptReco_Collisions17_JSON.txt --inputInBlocks -s data_DT-1100-111111_CMSSW_926_SingMu_MuAlCalIsoMuv1_294927_297723_92X_dataRun2_Prompt_v5_T0.sh --validationLabel data_DT-1100-111111_CMSSW_926_SingMu_MuAlCalIsoMuv1_294927_297723_92X_dataRun2_Prompt_v5_T0 --b --user_mail youremail --minTrackPt 30 --maxTrackPt 200 --maxDxy 0.2 --minNCrossedChambers 1 --residualsModel pureGaussian --peakNSigma 1.6 --station123params 111111 --station4params 101111 --cscparams 100001 --useResiduals 1100 --mapplots --curvatureplots --segdiffplots --extraPlots --globalTag 92X_dataRun2_Prompt_v5 --createAlignNtuple --noCleanUp --noCSC --gprcdconnect sqlite_file:GPR_July11_2017_SW924_Run2017B_dL4_iter1.db --gprcd IdealGeometry --is_Alca --T0
```

**Additional folders (you can use still old branches):**   
```
git clone https://github.com/cms-mual/MuAlPhysicsValidation.git
git clone https://github.com/cms-mual/PlottingTools.git
```

**Add validation plots to the validation browser:**   
```
cd /afs/cern.ch/cms/CAF/CMSALCA/ALCA_MUONALIGN/www/browser_plots/validation    
./add_tarballs.sh [PATH_TO_TARBALL_MADE_BY_ALIGNMENT_JOB]
```

**Json File location:**   
```
cp /afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions17/13TeV/PromptReco/Cert_294927-297723_13TeV_PromptReco_Collisions17_JSON.txt .
```
