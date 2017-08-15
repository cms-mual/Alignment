"""
Created:       14 August 2017
Last Updated:  14 August 2017

Dan Marley
daniel.edison.marley@cernSPAMNOT.ch
Texas A&M University
Fermi National Accelerator Laboratory
-----

Running script for batch job monitor
"""
import util
from batchJobMonitor import BatchJobMonitor

verbose_level = "INFO"

vb  = util.VERBOSE()
vb.level = verbose_level
vb.name  = "RUN_MONITOR"

bjm = BatchJobMonitor(jobIDs,verbose=verbose_level)
# ...can set other options for bjm here...
listOfFailedJobs = bjm.failedJobs()

for i in listOfFailedJobs:
    vb.ERROR("Job ID {0} failed".format(i))


## THE END ##