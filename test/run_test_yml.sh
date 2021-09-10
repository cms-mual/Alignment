#!/bin/bash
cmsrel CMSSW_12_1_0_pre2
cd  CMSSW_12_1_0_pre2/src
git clone git@github.com:cms-mual/Alignment.git -b CMSSW_12_1_X
git clone https://github.com/cms-mual/TrackingTools.git -b CMSSW_11_3_X
git clone https://github.com/cms-mual/MuAlSupplementaryFiles.git -b CMSSW_10_1_X
cp MuAlSupplementaryFiles/* .
ln -s Alignment/MuonAlignmentAlgorithms/scripts/createJobs.py
ln -s Alignment/MuonAlignmentAlgorithms/scripts/create_job_cfg_assets.py
ln -s Alignment/MuonAlignmentAlgorithms/python/gather_cfg.py
ln -s Alignment/MuonAlignmentAlgorithms/python/align_cfg.py
ln -s Alignment/MuonAlignmentAlgorithms/scripts/submitBatchJobs.py
ln -s Alignment/MuonAlignmentAlgorithms/scripts/runBatchJobMonitor.py
ln -s Alignment/test/* .
scram b -j8
python3 createJobs.py -y job_stuff.yml
cd run3MC_test_1
condor_submit_dag condor_run3MC_test_1.dag
