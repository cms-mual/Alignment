5 November 2017  

Luca Pernie  
Dan Marley



# Alignment


The following describes the muon alignment setup and execution.

## Setup your environment

```
SCRAM_ARCH=slc6_amd64_gcc630; export SCRAM_ARCH;
cmsrel CMSSW_10_0_0_pre2
cd CMSSW_10_0_0_pre2/src/
cmsenv

git clone https://github.com/cms-mual/Alignment.git -b $CMSSW_VERSION
git clone https://github.com/cms-mual/TrackingTools.git -b $CMSSW_VERSION
git clone https://github.com/cms-mual/MuAlSupplementaryFiles.git -b CMSSW_10_0_X
cp MuAlSupplementaryFiles/* .

ln -s Alignment/MuonAlignmentAlgorithms/scripts/createJobs.py
ln -s Alignment/MuonAlignmentAlgorithms/python/gather_cfg.py
ln -s Alignment/MuonAlignmentAlgorithms/python/align_cfg.py
ln -s Alignment/MuonAlignmentAlgorithms/scripts/submitBatchJobs.py
ln -s Alignment/MuonAlignmentAlgorithms/scripts/runBatchJobMonitor.py

scram b -j6
```


## Additional repositories

The following repositories are recommended for performing
additional tasks in muon alignment.  
Software development only occurs on the master branch.

```
git clone https://github.com/cms-mual/MuAlPhysicsValidation.git
git clone https://github.com/cms-mual/PlottingTools.git
```


### Run alignment on Data

The following commands can be used to process the muon alignment in data.  
_NB: for CSC, the `--T0` option is not needed._

```
# DT
./createJobs.py data_DT-1100-111111_2017B_CMSSW925p2_SingMu_MuAlCalIsoMuv1_92XdataRun2Promptv5_T0_ 3 data_DT-1100-111111_SingleMuon_Run2016G_MuAlCalIsolatedMu_278820_280385_8_0_24_Rerecov1_03.db SingleMuon_Run2017B-MuAlCalIsolatedMu-PromptReco-v1_297031_297723.py --json Cert_294927-297723_13TeV_PromptReco_Collisions17_JSON.txt --inputInBlocks -s data_DT-1100-111111_2017B_CMSSW925p2_SingMu_MuAlCalIsoMuv1_92XdataRun2Promptv5_T0.sh --validationLabel data_DT-1100-111111_2017B_CMSSW925p2_SingMu_MuAlCalIsoMuv1_92XdataRun2Promptv5_T0 --b --user_mail youremail --minTrackPt 30 --maxTrackPt 200 --maxDxy 0.2 --minNCrossedChambers 1 --residualsModel pureGaussian --peakNSigma 1.6 --station123params 111111 --station4params 101111 --cscparams 100001 --useResiduals 1100 --mapplots --curvatureplots --segdiffplots --extraPlots --globalTag 92X_dataRun2_Prompt_v5 --createAlignNtuple --noCleanUp --noCSC --gprcdconnect sqlite_file:GPR_July11_2017_SW924_Run2017B_dL4_iter1.db --gprcd IdealGeometry --is_Alca --T0

# CSC
./createJobs.py data_CSC-1100-100001_2017B_CMSSW925p2_SingMu_MuAlCalIsoMuv1_92XdataRun2Promptv5_ 1 data_CSC-1100-110001_SingleMuon_Run2016G_MuAlCalIsolatedMu_278820_280385_8_0_24_Rerecov1_03.db SingleMuon_Run2017B-MuAlCalIsolatedMu-PromptReco-v1_297031_297723.py --json Cert_294927-297723_13TeV_PromptReco_Collisions17_JSON.txt --inputInBlocks -s data_CSC-1100-100001_2017B_CMSSW925p2_SingMu_MuAlCalIsoMuv1_92XdataRun2Promptv5.sh --validationLabel data_CSC-1100-100001_2017B_CMSSW925p2_SingMu_MuAlCalIsoMuv1_92XdataRun2Promptv5 --b --user_mail youremail --minTrackPt 30 --maxTrackPt 200 --maxDxy 0.2 --minNCrossedChambers 1 --residualsModel pureGaussian --peakNSigma 1.6 --station123params 111111 --station4params 101111 --cscparams 100001 --useResiduals 1100 --mapplots --curvatureplots --segdiffplots --extraPlots --globalTag 92X_dataRun2_Prompt_v5 --createAlignNtuple --noCleanUp --noDT --gprcdconnect sqlite_file:GPR_July11_2017_SW924_Run2017B_dL4_iter1.db --gprcd IdealGeometry --is_Alca
```

Once the new shell script is created, simply execute the shell script to run the muon alignment.  
_The new shell script should have the same name as the `-s` argument in the command above._


### Run alignment on Simulation

```
./createJobs.py mc_DT-1100-111111_CMSSW925p2_GTasym_39M_13TeV_ 3 MuonGeometry_MC_Run2Startup_June2015_Csc2mm1mrad_DtHWUnct.DBv2.db SingleMuonGun_CMSSW_8_0_24_39M_13TeVSpectrum.py --inputInBlocks -s mc_DT-1100-111111_CMSSW925p2_GTasym_45M_13TeV.sh --validationLabel mc_DT-1100-111111_CMSSW925p2_GTasym_45M_13TeV --b --user_mail youremail --minTrackPt 20 --maxTrackPt 200 --maxDxy 0.2 --minNCrossedChambers 1 --residualsModel pureGaussian --peakNSigma 1.6 --station123params 111111 --station4params 101111 --cscparams 100001 --useResiduals 1100 --mapplots --curvatureplots --segdiffplots --extraPlots --globalTag 80X_mcRun2_asymptotic_2016_TrancheIV_v7 --createAlignNtuple --noCleanUp --noCSC --gprcdconnect sqlite_file:inertGlobalPositionRcd.StdTags.746p3.DBv2.db --gprcd inertGlobalPositionRcd --is_MC
```


### Add validation plots to the validation browser

```
cd /afs/cern.ch/cms/CAF/CMSALCA/ALCA_MUONALIGN/www/browser_plots/validation    
./add_tarballs.sh [PATH_TO_TARBALL_MADE_BY_ALIGNMENT_JOB]
```

### JSON File location

```
ls /afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions17/13TeV/PromptReco/Cert_294927-297723_13TeV_PromptReco_Collisions17_JSON.txt #json files
ls /afs/cern.ch/cms/CAF/CMSALCA/ALCA_MUONALIGN/www/muonGeometries/ #official muon geoemtries
```

## Batch Job Monitoring

Many batch jobs are submitted to successfully run the muon alignment.
New additions to the framework allow the user to check the (many) batch job outputs to determine if there
were any failures that need to be re-submitted.

New scripts in `MuonAlignmentAlgorithms/scripts/`:

Script | Description
------ | -----------
`createBatchJobs.py`    | Create batch jobs.  This mimics the setup above, but is still being developed.
`writeBatchScripts.py`  | Class that contains information for writing batch scripts automatically.
`submitBatchJobs.py`    | Submit batch jobs.  Recommended method because it saves the LSF ID with the script that was submitted.
`configuration.py`      | Configuration class.  Necessary for creating/submitting/monitoring batch jobs.
`util.py`               | Utility functions used in the framework.
`runBatchJobMonitor.py` | Running script that uses the `batchJobMonitor` class.
`batchJobMonitor.py`    | Class responsible for performing the tasks to determine if a batch job failed.

Using the setup described above (with `createJobs.py`), submit batch jobs to run the muon alignment.
If you submit jobs by just executing the batch script, the batch monitoring tool can still determine which jobs have failed,
but it will not be able to link failed batch jobs with the script that was executed.  
Instead, it is recommended to create batch jobs using the setup above, and use the `submitBatchJobs.py` script to submit the jobs.

To do this, simply:
```
./createJobs.py ... # described above
python submitBatchJobs.py config.txt
```
where `config.txt` is a configuration file that contains arguments similar to the command line arguments above.
An example is located in `MuonAlignmentAlgorithms/scripts/config.txt`.  
The `name` and `iterations` arguments are the only necessary configuration settings for submitting batch jobs.  
_('name' is the same as the first argument above with the last `_`)_

Once the batch jobs have been submitted, the LSF ID numbers and corresponding scripts are saved to a file.  
To check the successes or failures of batch jobs, run the following command:

```
python runBatchJobMonitor.py config.txt
```

The failed jobs will be saved to a text file (for reference later) and also printed to the screen.
Check the `STDOUT` files from the LSF jobs to make sure the jobs actually failed!
Jobs can be re-submitted by the user.  
_There is temporary functionality built-in to the batchJobMonitor to automatically resubmit jobs, 
but it is not currently active_.

Please investigate the `batchJobMonitor` class and `runBatchJobMonitor` script to check other options and configurations.


## Notes for the changing CMSSW release

For new releases of CMSSW, it is important to keep relevant code up-to-date.
Currently, the muon alignment framework relies on CMSSW packages that aren't centrally maintained,
but need to remain consistent with the official release.  

First, get the correct architecture, checkout the release, if needed:
```
SCRAM_ARCH=slc6_amd64_gcc630
export SCRAM_ARCH
cmsrel CMSSW_9_3_0_pre5
cd CMSSW_9_3_0_pre5/src/
cmsenv
```

Now, check the differences between your code and the one in the release.  
If you are not sure about what should be different, 
check the difference in the old release and the code you have locally there. 

Those should be the the only difference you also have with the following command:

```
diff -r TrackingTools/TrackRefitter/ $CMSSW_RELEASE_BASE/src/TrackingTools/TrackRefitter/ > diff_TrackingTools.txt
```
In `TrackingTools` there should have only be one file with differences (where hits in muon system are neglected, and you do the fit 3 times).  
Next, check the `CommonAlignmentMonitor`:

```
diff -r Alignment/CommonAlignmentMonitor/ $CMSSW_RELEASE_BASE/src/Alignment/CommonAlignmentMonitor/ > diff_CommonAlignmentMonitor.txt
```

This package should be identical.  
_For some reason this package must be mainted in `cms-mual`, so just check your version is identical to the one in the repository._

Finally, the `MuonAlignmentAlgorithms` package needs to be checked.
```
 diff -r ../../CMSSW_9_2_6/src/Alignment/MuonAlignmentAlgorithms/ /cvmfs/cms.cern.ch/slc6_amd64_gcc530/cms/cmssw-patch/CMSSW_9_2_5_patch2/src/Alignment/MuonAlignmentAlgorithms/ > diff_MuonAlignmentAlgorithms.txt
```

There should be many dfferences here. 
Check one by one if they are expected!  
You can compare old release and new releases, and make the relevant changes in your code:

```
diff -r $CMSSW_RELEASE_BASE/src/Alignment/MuonAlignmentAlgorithms/  /cvmfs/cms.cern.ch/slc6_amd64_gcc530/cms/cmssw-patch/CMSSW_9_2_6/src/Alignment/MuonAlignmentAlgorithms/ > diff_MuonAlignmentAlgorithms.txt
```


# Contact

Contact the authors with any questions.
