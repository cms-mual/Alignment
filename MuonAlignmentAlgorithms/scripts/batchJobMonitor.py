"""
Created:       14 August 2017
Last Updated:  14 August 2017

Dan Marley
daniel.edison.marley@cernSPAMNOT.ch
Texas A&M University
Fermi National Accelerator Laboratory
-----

Class to monitor batch jobs for successful completion.
Setup for lxplus, but this can be extended to other batch systems.
"""
import os
import sys
import json
import util
import commands


class BatchJobMonitor(object):
    """Monitor batch jobs on lxplus"""
    def __init__(self,config,verbose="INFO"):
        """
            Initialize the batch job monitor object.

            @param jobIDs    Dictionary of "jobID":"gatherID"
        """
        self.config = config
        self.jobIDsFile = config.jobIDsFile()
        self.jobIDs     = json.load( open(self.jobIDsFile,'r') )
        self.listOfJobIDs = [int(i) for i in self.jobIDs.keys()]

        self.lsfDirectory = ["{0}_{1:02d}/".format(config.name(),iteration) for iteration in range(config.iterations())]
        self.failedJobIDs = []

        self.vb = util.VERBOSE()
        self.vb.level = verbose
        self.vb.name  = "MONITOR"  # simple name of this script to recognize the output

        self.failed_keywords = ["error","fail","crash","command not found"]


    def getListOfJobIDs(self,jobIDs):
        """Take the text file and parse it correctly to have a list of Job IDs"""
        full_list = util.file2list(jobIDs)
        id_list   = []

        for i in full_list:
            if i.startswith("Job <"): #72126848> is submitted to queue <cmscaf1nd>
                data = util.extract(i,begin="<",end=">")
                id_list.append( int(data) )

        return id_list


    def isSuccessful(self,jobID):
        """Check if an individual job is successful"""
        if not self.failedJobIDs:
            # if the list of failed jobs is empty, check for failed jobs
            self.getFailedJobs()

        if jobID in self.failedJobIDs:
            self.vb.ERROR("Job ID {0} appears to have failed.".format(jobID))
            self.vb.ERROR("Please check the LSF output to confirm.")
            self.vb.ERROR("Fix any issues and resubmit job, if necessary.")

        return False


    def getStatus(self,jobID):
        """Get the status of a specific job"""
        status = commands.getoutput("bjobs {0}".format(jobID))

        return status

    def jobIDsDict(self):
        """Return the job IDs"""
        return self.jobIDs


    def failedJobs(self):
        """Return the failed job IDs"""
        if not self.failedJobIDs:
            self.getFailedJobs()

        return self.failedJobIDs


    def getFailedJobs(self):
        """Determine the job IDs of failed jobs"""
        self.failedJobIDs = []  # reset

        # add any failed jobs to the list of failed job IDs
        for j in self.listOfJobIDs:
            if self.jobFailed(j,self.jobIDs[str(j)]):  self.failedJobIDs.append(j)

        return


    def jobFailed(self,jobID,directory):
        """Read through LSF output to determine if job failed or succeeded"""
        directory = directory.split("/")[0]
        filename  = "{0}/LSFJOB_{1}/STDOUT".format(directory,jobID)
        filedata  = util.file2list(filename)

        # check the output exists
        if not os.path.isfile(filename):
            vb.ERROR("The file {0} does not exist".format(filename))

        # read through output looking for "ERROR" or something like it
        failed = False
        for line in filedata:
            lin = line.lower()
            if any( [i in lin for i in self.failed_keywords] ):
                failed = True
                break

        return failed


## THE END ##
