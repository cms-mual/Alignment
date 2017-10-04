#! /usr/bin/env python
"""
Created:       27 September 2017
Last Updated:  27 September 2017

Dan Marley
daniel.edison.marley@cernSPAMNOT.ch
Texas A&M University
-----

Submit jobs for track-based muon alignment
"""
import os
import sys
import json
import commands

import util
from config import Config


pwd  = commands.getoutput("pwd")
prog = sys.argv[0]

## Setup configuration object
cfg  = Config(sys.argv[1],script=prog)  # configuration
cfg.initialize()

## Setup VERBOSE object
vb = util.VERBOSE()
vb.level = cfg.verbose_level()
vb.name  = "SUBMITJOBS"        # nickname of this script for the VERBOSE output

## Different files for submitting jobs, storing output/job IDs
submitJobsFile = cfg.submitJobsFile()
outputFile     = submitJobsFile.replace(".sh",".out.txt")
jobIDsFile     = cfg.jobIDsFile() # submitJobsFile.replace(".sh","-jobIDs.json")

vb.INFO("Submit jobs from {0}".format(submitJobsFile))
output = os.system("./{0} > {1}".format(submitJobsFile,outputFile))

vb.INFO("Retrieve job IDs from {0}".format(outputFile))
jobIDs = util.getJobIDs(outputFile)  # dictionary of {"batchID":"gatherID"}

vb.INFO("Write jobIDs to file {0}".format(jobIDsFile))
with open(jobIDsFile,'w') as outfile:
    json.dump(jobIDs,outfile)

vb.INFO("End submitting jobs")

## THE END ##
