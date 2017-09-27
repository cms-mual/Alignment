"""
Created:       14 August    2017
Last Updated:  13 September 2017

Dan Marley
daniel.edison.marley@cernSPAMNOT.ch
Texas A&M University

-----

Running script for batch job monitor
"""
import json
import util
from batchJobMonitor import BatchJobMonitor

pwd  = commands.getoutput("pwd")
prog = sys.argv[0]

## Setup configuration object
cfg  = Config(sys.argv[1],script=prog)  # configuration
cfg.initialize()


vb  = util.VERBOSE()
vb.level = cfg.verbose_level()
vb.name  = "RUN_MONITOR"


jobIDsFile         = cfg.jobIDsFile()
failedJobIDsFile   = cfg.failedJobIDsFile() 
resubmitFailedJobs = cfg.resubmitFailedJobs()


vb.INFO("Load list of job IDs")
jobIDs = json.load( open(jobIDsFile,'r') ) # dictionary

vb.INFO("Setup job monitor tool")
bjm = BatchJobMonitor(jobIDs,verbose=verbose_level)
# ...can set other options for bjm here...

vb.INFO("Get the list of failed jobs")
listOfFailedJobs = bjm.failedJobs()

# hard-coded submission command from `createJobs.py`
queue = "cmscaf1nd" if cfg.big() else "cmscaf1nh"
resubmitCommand = "bsub -R \"type==SLC6_64\" -q "+queue+" -J \"{0}\" -u youremail.tamu.edu {1}"

for i in listOfFailedJobs:
    vb.ERROR("Job ID {0} failed".format(i))
    if resubmitFailedJobs:
        vb.INFO("Re-submitting failed job {0}".format(i))
        thisJob = jobIDs[i]
        thisJobDir,thisJobScript = thisJob.split("/")
        resubmitJobCommand = resubmitCommand.format(thisJob.replace("/","_").rstrip(".sh"),thisJobScript)

        os.system("cd {0}".format(thisJobDir))
        os.system("{0}".format(resubmitJobCommand))
        os.system("cd ../")

dictOfFailedJobIDs = dict( (k,jobIDs[k]) for k in listOfFailedJobs )

vb.INFO("Writing failed job IDs to {0}".format(failedJobIDsFile) )
with open(failedJobIDsFile,'w') as outfile:
    json.dump(dictOfFailedJobIDs,outfile)

vb.INFO("End batch job monitoring")


## THE END ##
