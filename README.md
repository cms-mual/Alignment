# Alignment

This is alignmnet code version that we used for Run 1 and MC alingnment in 2012-2014.

Linux version: SL5
architecture:  slc5_amd64_gcc462
CMSSW version: CMSSW_5_3_6_patch1

# How to run:

 1. Set architecture:

`export SCRAM_ARCH=slc5_amd64_gcc462`

 2. Set CMSSW area:

`cmsrel CMSSW_5_3_6_patch1`
`cd CMSSW_5_3_6_patch1/src/`

 3. Check out repositories with muon alignmnet code:

`git clone git@github.com:cms-mual/Alignment.git`
`git clone git@github.com:cms-mual/TrackingTools.git`

 4. Compile:

`scram b -j8`
