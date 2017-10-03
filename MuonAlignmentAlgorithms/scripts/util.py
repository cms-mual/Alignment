"""
Created:       14 August 2017
Last Updated:  14 August 2017

Dan Marley
daniel.edison.marley@cernSPAMNOT.ch
Texas A&M University
Fermi National Accelerator Laboratory
-----

Basic utility functions for the framework
"""


def extract(data,begin="(",end=")"):
    """
        Given a string and two symbols, extract the text in between the symbols.
        Check for multiple occurances!
    """
    text2return = ""
    if begin==end:
        print " ERROR :: EXTRACT : Same 'begin' and 'end' symbols {0}".format(begin)
        return text2return

    beginnings = []
    endings    = []
    for i,e in enumerate(data):
        if e==begin:
            beginnings.append(i)
        elif e==end:
            endings.append(i)


    if len(beginnings)>1:
        # nested brackets: 
        # https://stackoverflow.com/questions/38456603/extract-string-inside-nested-brackets
        text2return = []
        stack = []
        for char in data:
            if char == begin:
                stack.append([])
            elif char == end:
                text2return.append(''.join(stack.pop()))
            else:
                stack[-1].append(char)
    else:
        b = beginnings[0]+1
        e = endings[0]
        text2return = data[b:e]  # return the text in between the symbols

    return text2return


def str2bool( value ):
    """Turn string into boolean"""
    valueBoolean = False

    if value == "True" or value == "true" or value == "1":
        valueBoolean = True
    else:
        valueBoolean = False

    return valueBoolean


def file2list(filename):
    """Load text file and dump contents into a list"""
    listOfFiles = open( filename,'r').readlines()
    listOfFiles = [i.rstrip('\n') for i in listOfFiles]
    return listOfFiles


def getJobIDs(outputFile):
    """
       Get the job IDs from lxbatch output when job submitted.
        'Job <557650> is submitted to queue <1nw>.'
    """
    jobIDs  = {}
    alldata = file2list(outputFile)
    for d,data in enumerate(alldata):
        if not data.startswith("Job"): continue
        id = extract(data,begin="<",end=">")
        gatherID = data[d-1].split(" ")[-1]

        jobIDs[gatherID] = id

    return jobIDs


class VERBOSE(object):
    """
        Object for handling output to terminal

        @description Multiple "levels" for verbose output.
                     The higher the level, the less output is printed.
                     New level "MUTE" will silence all outputs.
    """
    def __init__(self,level="INFO"):
        self.verboseMap = {"DEBUG":0,
                           "INFO": 1,
                           "WARNING":2,
                           "ERROR":  3,
                           "MUTE":   4};
        self.level = level
        self.name  = None

    def DEBUG(self,message):
        """Debug level - most verbose"""
        self.verbose("DEBUG",message)
        return

    def INFO(self,message):
        """Info level - standard output"""
        self.verbose("INFO",message)
        return

    def WARNING(self,message):
        """Warning level - if something seems wrong but code can continue"""
        self.verbose("WARNING",message)
        return

    def ERROR(self,message):
        """Error level - something is wrong"""
        self.verbose("ERROR",message)
        return

    def verbose(self,level,message):
        if self.verboseMap[level] >= self.verboseMap[self.level]:
            msg = "{0} : {1}".format(self.name,message) if self.name is not None else message
            print " {0} :: {1}".format(level,msg)

        return
