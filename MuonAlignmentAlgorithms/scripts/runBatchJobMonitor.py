"""
Created:       14 August    2017
Last Updated:  13 September 2017
Dan Marley
daniel.edison.marley@cernSPAMNOT.ch
Texas A&M University
-----
Running script for batch job monitor
"""
import sys
import json
import util
import commands

from configuration import Configuration
from batchJobMonitor import BatchJobMonitor

pwd  = commands.getoutput("pwd")
prog = sys.argv[0]

## Setup configuration object
cfg  = Configuration(sys.argv[1],script=prog)  # configuration
cfg.initialize()

## verbose output
vb  = util.VERBOSE()
vb.level = cfg.verbose_level()
vb.name  = "RUN_MONITOR"

## get configuration options
failedJobIDsFile   = cfg.failedJobIDsFile()    # file to store a dictionary of failed jobs {LSF ID: script}
resubmitFailedJobs = cfg.resubmitFailedJobs()  # boolean to resubmit failed jobs


vb.INFO("Setup job monitor tool")
bjm = BatchJobMonitor(cfg,verbose=cfg.verbose_level())

vb.INFO("Get the list of failed jobs")
listOfFailedJobs = bjm.failedJobs()    # get the failed jobs (main function that collects the failed jobs)


# copied submission command from `createJobs.py`
queue = "cmscaf1nd" if cfg.big() else "cmscaf1nh"
resubmitCommand = "bsub -R \"type==SLC6_64\" -q "+queue+" -J \"{0}\" -u youremail.tamu.edu {1}"

for i in listOfFailedJobs:
    vb.ERROR("Job ID {0} failed".format(i))

    # automatically resubmit failed jobs
    if resubmitFailedJobs:
        vb.INFO("Re-submitting failed job {0}".format(i))
        thisJob = jobIDs[i]
        thisJobDir,thisJobScript = thisJob.split("/")
        resubmitJobCommand = resubmitCommand.format(thisJob.replace("/","_").rstrip(".sh"),thisJobScript)

        os.system("cd {0}".format(thisJobDir))
        os.system("{0}".format(resubmitJobCommand))
        os.system("cd ../")


jobIDs = bjm.jobIDsDict()   # dict of {key=LSF IDs, item=script that was submitted}
dictOfFailedJobIDs = dict( (k,jobIDs[str(k)]) for k in listOfFailedJobs ) # store failed jobs in a dictionary


vb.INFO("Writing failed job IDs to {0}".format(failedJobIDsFile) )
with open(failedJobIDsFile,'w') as outfile:
    json.dump(dictOfFailedJobIDs,outfile)

vb.INFO("End batch job monitoring")


## THE END ##
