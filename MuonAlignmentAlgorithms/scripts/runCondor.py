import os, sys, optparse

usage = "-d script DIR -t testMode -n batchName"
parser = optparse.OptionParser(usage)
parser.add_option("-d", "--tdir",
                   help="shell script dir",
                   type="string",
                   dest="tdir")
parser.add_option("-t", "--test",
                   help="test run submit only one job",
                   default=False,
                   dest="testRun")
parser.add_option("-n", "--name",
                   help="bach name",
                   type="string",
                   default="muonAlignment",
                   dest="batchName")

options, args = parser.parse_args(sys.argv[1:])
print "target DIR:",options.tdir

cDir = options.tdir+"_condor"
os.mkdir(cDir)

homePath = "/".join(os.environ['CMSSW_BASE'].split("/")[:-1])
cmsswName = os.environ['CMSSW_BASE'].split("/")[-1]
os.chdir(homePath)
os.system("tar cf "+cmsswName+".tar "+cmsswName)
tarball = cmsswName+".tar"
os.system("mv "+tarball+" "+cmsswName+"/src/"+cDir)
os.chdir(cmsswName+"/src/")

sList = [x for x in os.listdir(options.tdir) if x.startswith("gather") and x.endswith(".sh")]

cTmp = """executable              = {sh}
universe                = vanilla
requirements            = (OpSysAndVer =?= "CentOS7")
+JobFlavour             = "tomorrow"
output                  = {shN}.out
error                   = {shN}.err
log                     = {shN}.log
transfer_input_files    = {tarBall}
should_transfer_files   = YES
when_to_transfer_output = ON_EXIT
transfer_output_files   = {outN}
queue
"""

cpJson = """if [ "zzz$ALIGNMENT_JSON" != "zzz" ]; then
  cp -f $ALIGNMENT_JSON $ALIGNMENT_CAFDIR/
fi
"""

for x in sList:
  tmpJ = open(cDir+"/"+x.replace(".sh", ".sub"),'w')
  data = {'sh':x, 'shN':x.replace(".sh", ""), 'tarBall':tarball, 'outN':'out'+x[6:9]+".tar"}
  tmpJ.write(cTmp.format(**data))
  tmpJ.close()

  tmpS = open(cDir+"/"+x, 'w')
  tmpS.write("#!/bin/bash\n")
  tmp = open(options.tdir+"/"+x, 'r')
  for l in tmp:
    if l.startswith("export ALIGNMENT_CAFDIR=`pwd`\n"):
      tmpS.write(l)
      tmpS.write("tar xf "+tarball)
      tmpS.write("\ncd "+tarball.replace(".tar","/src"))
      tmpS.write("\nscram build ProjectRename")
      tmpS.write("\neval `scramv1 run -sh`\n")
    elif l.startswith("export"): tmpS.write(l)
    elif l.startswith("cp -f"):
      tmpS.write(l)
      tmpS.write(cpJson)
      tmpS.write("cd $ALIGNMENT_CAFDIR/\n")
      tmpS.write("cmsRun gather_cfg.py\n")
      tmpS.write("tar cf out"+x[6:9]+".tar *.root *.tmp\n")
      break
  tmpS.close()

os.chdir(cDir)
cList = [x for x in os.listdir(".") if x.endswith(".sub")]
for i, x in enumerate(cList):
  os.system("chmod 755 "+x.replace(".sh", ".sub"))
  os.system("chmod 755 "+x)
  print "condor submit {}/{}".format(i,len(cList))
  os.system("condor_submit -batch-name "+options.batchName+" "+x.replace(".sh", ".sub"))
  if options.testRun: break
