30 October 2017  
Luca Pernie  
Dan Marley  


# Alignment

## Setup your environment:

```
# Build CMSSW Environment
SCRAM_ARCH=slc6_amd64_gcc530; export SCRAM_ARCH;
export RELEASE=CMSSW_9_2_6

cmsrel $RELEASE
cd $RELEASE/src/
cmsenv

# Add packages for alignment
git cms-addpkg Alignment/CommonAlignmentMonitor
cd Alignment
git clone https://github.com/demarley/Alignment.git -b $RELEASE

# To obtain the actual code, you will lose the git repo in this step, needs to be revisited...
mv Alignment/MuonAlignmentAlgorithms/ .
rm -rf Alignment
cd ../
git clone https://github.com/cms-mual/TrackingTools.git -b $RELEASE
git clone https://github.com/cms-mual/MuAlSupplementaryFiles.git -b CMSSW_9_0_X

# link files
ln -s Alignment/MuonAlignmentAlgorithms/scripts/createJobs.py
ln -s Alignment/MuonAlignmentAlgorithms/scripts/submitJobs.py
ln -s Alignment/MuonAlignmentAlgorithms/scripts/runBatchJobMonitor.py
ln -s Alignment/MuonAlignmentAlgorithms/python/gather_cfg.py
ln -s Alignment/MuonAlignmentAlgorithms/python/align_cfg.py
scram b -j6
```

### Additional folders (single branch)
```
git clone https://github.com/cms-mual/MuAlPhysicsValidation.git
git clone https://github.com/cms-mual/PlottingTools.git
```



## Data Alignment

_Note: for CSC, the `--T0` option is not needed_

```
./createJobs.py config.txt
./submitJobs.py config.txt
```

where `config.txt` is the configuration file that maintains the list of 
options you need when running the alignment.


### Add validation plots to the validation browser:

```
cd /afs/cern.ch/cms/CAF/CMSALCA/ALCA_MUONALIGN/www/browser_plots/validation    
./add_tarballs.sh <PATH_TO_TARBALL_MADE_BY_ALIGNMENT_JOB>
```

### JSON File location:**   
```
ls /afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions17/13TeV/PromptReco/Cert_294927-297723_13TeV_PromptReco_Collisions17_JSON.txt #json files
ls /afs/cern.ch/cms/CAF/CMSALCA/ALCA_MUONALIGN/www/muonGeometries/ #official muon geoemtries
```

## Notes for the changing release

Check the differences between your code and the release.

If you are not sure about what should be different, 
compare the old release and the code you have locally.

It should have only one file, where hits in muon system are neglected, and you do the fit 3 times.

```
diff -r TrackingTools/TrackRefitter/ $CMSSW_RELEASE_BASE/src/TrackingTools/TrackRefitter/ > diff_TrackingTools.txt
diff -r Alignment/CommonAlignmentMonitor/ $CMSSW_RELEASE_BASE/src/Alignment/CommonAlignmentMonitor/ > diff_CommonAlignmentMonitor.txt
diff -r Alignment/MuonAlignmentAlgorithms/ /cvmfs/cms.cern.ch/slc6_amd64_gcc530/cms/cmssw-patch/CMSSW_9_2_5_patch2/src/Alignment/MuonAlignmentAlgorithms/ > diff_MuonAlignmentAlgorithms.txt
diff -r $CMSSW_RELEASE_BASE/src/Alignment/MuonAlignmentAlgorithms/  /cvmfs/cms.cern.ch/slc6_amd64_gcc530/cms/cmssw-patch/CMSSW_9_2_5_patch2/src/Alignment/MuonAlignmentAlgorithms/ > diff_MuonAlignmentAlgorithms.txt
```

5. Many dfferences here. You can check one by one if they are expected, 
or you can compare old release and new release, and make the changes in your code



## Former Setup
```
1. ./createJobs.py data_DT-1100-111111_2017B_CMSSW925p2_SingMu_MuAlCalIsoMuv1_92XdataRun2Promptv5_T0_ 3 data_DT-1100-111111_SingleMuon_Run2016G_MuAlCalIsolatedMu_278820_280385_8_0_24_Rerecov1_03.db SingleMuon_Run2017B-MuAlCalIsolatedMu-PromptReco-v1_297031_297723.py --json Cert_294927-297723_13TeV_PromptReco_Collisions17_JSON.txt --inputInBlocks -s data_DT-1100-111111_2017B_CMSSW925p2_SingMu_MuAlCalIsoMuv1_92XdataRun2Promptv5_T0.sh --validationLabel data_DT-1100-111111_2017B_CMSSW925p2_SingMu_MuAlCalIsoMuv1_92XdataRun2Promptv5_T0 --b --user_mail youremail --minTrackPt 30 --maxTrackPt 200 --maxDxy 0.2 --minNCrossedChambers 1 --residualsModel pureGaussian --peakNSigma 1.6 --station123params 111111 --station4params 101111 --cscparams 100001 --useResiduals 1100 --mapplots --curvatureplots --segdiffplots --extraPlots --globalTag 92X_dataRun2_Prompt_v5 --createAlignNtuple --noCleanUp --noCSC --gprcdconnect sqlite_file:GPR_July11_2017_SW924_Run2017B_dL4_iter1.db --gprcd IdealGeometry --is_Alca --T0
2. ./createJobs.py data_CSC-1100-100001_2017B_CMSSW925p2_SingMu_MuAlCalIsoMuv1_92XdataRun2Promptv5_ 1 data_CSC-1100-110001_SingleMuon_Run2016G_MuAlCalIsolatedMu_278820_280385_8_0_24_Rerecov1_03.db SingleMuon_Run2017B-MuAlCalIsolatedMu-PromptReco-v1_297031_297723.py --json Cert_294927-297723_13TeV_PromptReco_Collisions17_JSON.txt --inputInBlocks -s data_CSC-1100-100001_2017B_CMSSW925p2_SingMu_MuAlCalIsoMuv1_92XdataRun2Promptv5.sh --validationLabel data_CSC-1100-100001_2017B_CMSSW925p2_SingMu_MuAlCalIsoMuv1_92XdataRun2Promptv5 --b --user_mail youremail --minTrackPt 30 --maxTrackPt 200 --maxDxy 0.2 --minNCrossedChambers 1 --residualsModel pureGaussian --peakNSigma 1.6 --station123params 111111 --station4params 101111 --cscparams 100001 --useResiduals 1100 --mapplots --curvatureplots --segdiffplots --extraPlots --globalTag 92X_dataRun2_Prompt_v5 --createAlignNtuple --noCleanUp --noDT --gprcdconnect sqlite_file:GPR_July11_2017_SW924_Run2017B_dL4_iter1.db --gprcd IdealGeometry --is_Alca
```

## Run alignment on Simulation:
```
1. ./createJobs.py mc_DT-1100-111111_CMSSW925p2_GTasym_39M_13TeV_ 3 MuonGeometry_MC_Run2Startup_June2015_Csc2mm1mrad_DtHWUnct.DBv2.db SingleMuonGun_CMSSW_8_0_24_39M_13TeVSpectrum.py --inputInBlocks -s mc_DT-1100-111111_CMSSW925p2_GTasym_45M_13TeV.sh --validationLabel mc_DT-1100-111111_CMSSW925p2_GTasym_45M_13TeV --b --user_mail youremail --minTrackPt 20 --maxTrackPt 200 --maxDxy 0.2 --minNCrossedChambers 1 --residualsModel pureGaussian --peakNSigma 1.6 --station123params 111111 --station4params 101111 --cscparams 100001 --useResiduals 1100 --mapplots --curvatureplots --segdiffplots --extraPlots --globalTag 80X_mcRun2_asymptotic_2016_TrancheIV_v7 --createAlignNtuple --noCleanUp --noCSC --gprcdconnect sqlite_file:inertGlobalPositionRcd.StdTags.746p3.DBv2.db --gprcd inertGlobalPositionRcd --is_MC
```

