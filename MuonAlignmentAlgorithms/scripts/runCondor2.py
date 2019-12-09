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
  tmw.write(cTmp.format(**arg))
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
  print "runCondor2.py should be running in /afs/cern.ch/work/"
  exit()

if options.tdir.endswith("/"): tdir = options.tdir[:-1]
else: tdir = options.tdir
print "target DIR:",tdir
cdir = options.tdir+"_condor"
os.mkdir(cdir)

# gather part
gList = [x for x in os.listdir(tdir) if x.startswith("gather") and x.endswith(".sh")]
runGather = open(cdir+"/runGather.sh",'w')
for x in gList:
  tmpArg = {'sh':cmsswdir+"/"+cdir+"/"+x, 'shN':x.replace(".sh",""), 'nCPU':1, 'memory':'4000'}
  fname = x.replace(".sh", ".sub")
  writeSub(tmpArg, cdir+"/"+fname)
  runGather.write("condor_submit -batch-name align_"+options.batchName+" "+fname)

# align part
runAlign = open(cdir+"/runAlign.sh", 'w')
tmpArg = {'sh':cmsswdir+"/"+cdir+'/align.sh', 'shN':'align', 'nCPU':4, 'memory':'4000'}
fname = "align.sub"
writeSub(tmpArg, cdir+"/"+fname)
runAlign.write("condor_submit -batch-name "+options.batchName+" "+fname)

# validation part
runValidation = open(cdir+"/runValidation.sh", 'w')
tmpArg = {'sh':cmsswdir+"/"+cdir+'/validation.sh', 'shN':'validation', 'nCPU':4, 'memory':'4000'}
fname = "validation.sub"
writeSub(tmpArg, cdir+"/"+fname)
runValidation.write("condor_submit -batch-name validation_"+options.batchName+" "+fname)


