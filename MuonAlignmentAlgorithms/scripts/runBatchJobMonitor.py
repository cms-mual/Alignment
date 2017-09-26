"""
Created:       14 August    2017
Last Updated:  13 September 2017

Dan Marley
daniel.edison.marley@cernSPAMNOT.ch
Texas A&M University

-----

Running script for batch job monitor
"""
import util
from batchJobMonitor import BatchJobMonitor

verbose_level = "INFO"

vb  = util.VERBOSE()
vb.level = verbose_level
vb.name  = "RUN_MONITOR"

jobIDs = []   # list of job IDs

bjm = BatchJobMonitor(jobIDs,verbose=verbose_level)
# ...can set other options for bjm here...
listOfFailedJobs = bjm.failedJobs()

for i in listOfFailedJobs:
    vb.ERROR("Job ID {0} failed".format(i))


## THE END ##