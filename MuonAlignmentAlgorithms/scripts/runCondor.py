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

homePath = "/".join(os.environ['CMSSW_BASE'].split("/")[:-1])
cmsswName = os.environ['CMSSW_BASE'].split("/")[-1]
print "home path: ",homePath
print "CMSSW project name: ",cmsswName
os.chdir(homePath)
os.system("tar cf "+cmsswName+".tar "+cmsswName)
tarball = cmsswName+".tar"
os.chdir(cmsswName+"/src/")

tdir = options.tdir
cDir = options.tdir+"_condor"
os.mkdir(cDir)
os.system("mv "+homePath+"/"+tarball+" "+homePath+"/"+cmsswName+"/src/"+cDir)

sList = [x for x in os.listdir(tdir) if x.startswith("gather") and x.endswith(".sh")]

cTmp = """executable              = {sh}
universe                = vanilla
requirements            = (OpSysAndVer =?= "CentOS7")
request_cpus            = {nCPU}
max_transfer_output_mb  = {memory}
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

# gather part
outGatherList = []
for x in sList:
  tmpJ = open(cDir+"/"+x.replace(".sh", ".sub"),'w')
  data = {'sh':x, 'shN':x.replace(".sh", ""), 'tarBall':tarball, 'outN':'out'+x[6:9]+".tar", 'nCPU':1, 'memory':'4000'}
  outGatherList.append('out'+x[6:9]+".tar")
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
  
# align part
tmpAlign = open(cDir+"/align.sub",'w')
tmpAlignV = {'sh':'align.sh', 'shN':'align', 'tarBall':'{}, outGather.tar'.format(tarball), 'outN':'outAlign', 'nCPU':4, 'memory':'4000'}
tmpAlign.write(cTmp.format(**tmpAlignV))
tmpAlign.close()
os.system("chmod +x "+cDir+"/align.sub")

tmpAlignSh = open(cDir+"/align.sh", 'w')
alignSh = open(tdir+"/align.sh")
for x in alignSh:
  if x.startswith("cd /") and x.endswith(cmsswName+"/src\n"):
    tmpAlignSh.write("tar xf "+tarball)
    tmpAlignSh.write("\nrm "+tarball)
    tmpAlignSh.write("\ncd "+cmsswName+"/src/"+tdir)
    tmpAlignSh.write("\nmv $ALIGNMENT_CAFDIR/outGather.tar .\n")
    tmpAlignSh.write("tar xf outGather.tar\n")
    tmpAlignSh.write("cd ..\n")
    tmpAlignSh.write("scram build ProjectRename\n")
  else:
    tmpAlignSh.write(x)
tmpAlignSh.write("cd $ALIGNMENT_CAFDIR\n")
tmpAlignSh.write("mkdir -p outAlign\n")
tmpAlignSh.write("cp -f $ALIGNMENT_AFSDIR/"+tdir+"/*report.py outAlign\n")
tmpAlignSh.write("cp -f $ALIGNMENT_AFSDIR/"+tdir+"/"+tdir+".root outAlign\n")
tmpAlignSh.write("cp -f $ALIGNMENT_AFSDIR/"+tdir+"/"+tdir+"_plotting.root outAlign\n")
tmpAlignSh.write("cp -f $ALIGNMENT_AFSDIR/"+tdir+"/*.xml outAlign\n")
tmpAlignSh.close()
os.system("chmod +x "+cDir+"/align.sh")
tmpAlignRun = open(cDir+"/runAlign.sh", 'w')
tmpAlignRun.write("#!/bin/bash\n")
tmpAlignRun.write("mkdir tmpGather\n")
tmpAlignRun.write("mv out*.tar tmpGather\n")
tmpAlignRun.write("cd tmpGather\n")
for x in outGatherList:
  tmpAlignRun.write("tar xf {}\n".format(x))
tmpAlignRun.write("tar cf outGather.tar *.root *.tmp\n")
tmpAlignRun.write("mv outGather.tar ..\n")
tmpAlignRun.write("cd ..\n")
tmpAlignRun.write("condor_submit -batch-name align align.sub\n")
tmpAlignRun.write("rm -rf tmpGather")
tmpAlignRun.close()
os.system("chmod +x "+cDir+"/runAlign.sh")
tmpAlignRun.close()

# validation part
tmpVal = open(cDir+"/validation.sub",'w')
tmpValV = {'sh':'validation.sh', 'shN':'validation', 'tarBall':'{}, outAlign.tar'.format(tarball), 'outN':'outValidation.tar', 'nCPU':4, 'memory':'4000'}
tmpVal.write(cTmp.format(**tmpValV))
tmpVal.close()
os.system("chmod +x "+cDir+"/validation.sub")

tmpValSh = open(cDir+"/validation.sh", 'w')
valSh = open(tdir+"/validation.sh")
for x in valSh:
  if x.startswith("export ALIGNMENT_CAFDIR=`pwd`"):
    tmpValSh.write("mkdir outValidation\n")
    tmpValSh.write("export ALIGNMENT_node=`pwd`\n")
    tmpValSh.write("cd outValidation\n")
    tmpValSh.write(x)
    tmpValSh.write("mv ../{} .\n".format(tarball))
    tmpValSh.write("tar xf "+tarball)
    tmpValSh.write("\nrm {}\n".format(tarball))
  elif x.startswith("cd /") and x.endswith(cmsswName+"/src\n"):
    tmpValSh.write("cd "+cmsswName+"/src/"+tdir)
    tmpValSh.write("\nmv $ALIGNMENT_node/outAlign.tar .\n")
    tmpValSh.write("tar xf outAlign.tar\n")
    tmpValSh.write("rm outAlign.tar\n")
    tmpValSh.write("cd ..\n")
    tmpValSh.write("scram build ProjectRename\n")
  else:
    tmpValSh.write(x)
tmpValSh.write("cd $ALIGNMENT_node\n")
tmpValSh.write("tar cf outValidation.tar outValidation")
tmpValSh.close()
os.system("chmod +x "+cDir+"/validation.sh")

tmpValRun = open(cDir+"/runValidation.sh", 'w')
tmpValRun.write("#!/bin/bash\n")
tmpValRun.write("cd outAlign\n")
tmpValRun.write("tar cf outAlign.tar *\n")
tmpValRun.write("mv outAlign.tar ..\n")
tmpValRun.write("cd ..\n")
tmpValRun.write("condor_submit -batch-name validation validation.sub")
tmpValRun.close()
os.system("chmod +x "+cDir+"/runValidation.sh")

# submit gather
os.chdir(cDir)
cList = [x for x in os.listdir(".") if x.endswith(".sub")]
for i, x in enumerate(cList):
  os.system("chmod +x "+x.replace(".sh", ".sub"))
  os.system("chmod +x "+x)
  print "condor submit {}/{}".format(i,len(cList))
  os.system("condor_submit -batch-name "+options.batchName+" "+x.replace(".sh", ".sub"))
  if options.testRun: break
