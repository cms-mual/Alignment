#!/usr/bin/env python
import os, sys, optparse

def writeSub(arg, fname):
  cTmp = """executable              = {sh}
  universe                = vanilla
  requirements            = (OpSysAndVer =?= "CentOS7")
  request_cpus            = {nCPU}
  max_transfer_output_mb  = {memory}
  +JobFlavour             = "tomorrow"
  output                  = {shN}.out
  error                   = {shN}.err
  log                     = {shN}.log
  queue
  """
  tmp = open(fname,'w')
  tmp.write(cTmp.format(**arg))
  tmp.close()

usage = "-d script DIR -t testMode -n batchName"
parser = optparse.OptionParser(usage)
parser.add_option("-d", "--tdir",
                   help="shell script dir",
                   type="string",
                   dest="tdir")
parser.add_option("-n", "--name",
                   help="bach name",
                   type="string",
                   default="muonAlignment",
                   dest="batchName")

options, args = parser.parse_args(sys.argv[1:])
cmsswdir = os.getcwd()
if not cmsswdir.startswith("/afs/cern.ch/work/"):
  print "runCondor2.py should be running on /afs/cern.ch/work/"
  exit()

if options.tdir.endswith("/"): tdir = options.tdir[:-1]
else: tdir = options.tdir
print "target DIR:",tdir
cdir = options.tdir+"_condor"
os.mkdir(cdir)
savedir = cmsswdir+"/"+tdir+"/"
# gather part
gList = [x for x in os.listdir(tdir) if x.startswith("gather") and x.endswith(".sh")]
runGather = open(cdir+"/runGather.sh",'w')
runGather.write("#!/bin/sh\n")
for x in gList:
  tmpArg = {'sh':savedir+x, 'shN':x.replace(".sh",""), 'nCPU':1, 'memory':'4000'}
  fname = x.replace(".sh", ".sub")
  writeSub(tmpArg, cdir+"/"+fname)
  runGather.write("condor_submit -batch-name align_"+options.batchName+" "+fname+"\n")
os.system("chmod +x "+cdir+"/runGather.sh")
# align part
runAlign = open(cdir+"/runAlign.sh", 'w')
tmpArg = {'sh':savedir+'align.sh', 'shN':'align', 'nCPU':4, 'memory':'4000'}
fname = "align.sub"
writeSub(tmpArg, cdir+"/"+fname)
runAlign.write("#!/bin/sh\ncondor_submit -batch-name align_"+options.batchName+" "+fname)
os.system("chmod +x "+cdir+"/runAlign.sh")
# validation part
runValidation = open(cdir+"/runValidation.sh", 'w')
tmpArg = {'sh':savedir+'validation.sh', 'shN':'validation', 'nCPU':4, 'memory':'4000'}
fname = "validation.sub"
writeSub(tmpArg, cdir+"/"+fname)
runValidation.write("#!/bin/sh\ncondor_submit -batch-name validation_"+options.batchName+" "+fname)
os.system("chmod +x "+cdir+"/runValidation.sh")
