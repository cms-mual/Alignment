# Alignment

This is alignmnet code version that we used for Run 1 and MC alingnment in 2012-2014.

Linux version: SL6
architecture:  slc6_amd64_gcc472
CMSSW version: CMSSW_5_3_28_patch1

# How to run:

 1. Set architecture:
    export SCRAM_ARCH=slc6_amd64_gcc472
 2. Set CMSSW area:
    cmsrel CMSSW_5_3_28_patch1
    cd CMSSW_5_3_28_patch1/src/
 3. Check out repositories with muon alignmnet code:
    git clone git@github.com:cms-mual/Alignment.git -b CMSSW_5_3_X
    git clone git@github.com:cms-mual/TrackingTools.git -b CMSSW_5_3_X
    git clone https://github.com/cms-mual/MuAlSupplementaryFiles.git
    cp MuAlSupplementaryFiles/* .
    ln -s Alignment/MuonAlignmentAlgorithms/scripts/createJobs.py
    ln -s Alignment/MuonAlignmentAlgorithms/python/gather_cfg.py
    ln -s Alignment/MuonAlignmentAlgorithms/python/align_cfg.py
 4. Compile:
    `scram b -j 16`
