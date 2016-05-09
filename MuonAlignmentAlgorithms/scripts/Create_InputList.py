import subprocess, time, sys, os, string

# Inputs
ListDas = "InputList_DAS_2015D_PromotRecov3"          # no .list (list of paths fo the files)
removeUseless = True                                  # remove files not included in the json files from the list 
randomList = True                                     # randomize the list, it mixes files if they are sorted by size
OutName = "SingleMuon_Run2015D-PromptReco-v3_RECO.py"
fileJson = "Cert_246908-257599_13TeV_PromptReco_Collisions15_25ns_JSON_MuonPhys.txt"
FilePerJob = 20

#Remove useles files
fileIs=0
fileIsNot=0
if(removeUseless):
    ListDas_red = ListDas + '_red'
    Filelist_f = open( ListDas + '.list' )
    Jsonlist_f = open( fileJson )
    NEW_f = open( ListDas_red + ".list", 'w' )
    Filelistbase_v = Filelist_f.readlines()
    Jsonlistbase_v = Jsonlist_f.readlines()
    for Nline in range(len(Filelistbase_v)):
      IsThere=False
      line = Filelistbase_v[Nline]
      num = line.index('000')               #assume .../v1/000/251/028/...
      newLine  = line[int(num+4):int(num+7)]
      newLine += line[int(num+8):int(num)+11]
      for NlineJson in range(len(Jsonlistbase_v)):
          JsonLine = str(Jsonlistbase_v[NlineJson]).strip('\n')
          if( string.find(str(JsonLine),str(newLine))>0 ): IsThere=True
      if(IsThere):
         fileIs += 1
         NEW_f.write(Filelistbase_v[Nline])
      else:
         fileIsNot += 1
    print "File in the JSON files are " + str(fileIs) + "/" + str(float(fileIsNot+fileIs)) + " (" + str(float(fileIs/float(fileIs+fileIsNot))*100) + "%)"
    ListDas = ListDas_red
    Filelist_f.close()
    Jsonlist_f.close()
    NEW_f.close()

#Randomize
if(randomList):
     ListDas_ran = ListDas + "_random"
     command = "cat " + ListDas + ".list | shuf > " + ListDas_ran + ".list"
     print "Executing:"
     print command
     comm = subprocess.Popen([command], stdout=subprocess.PIPE, shell=True);
     comm.communicate()
     ListDas = ListDas_ran

#Initial lines
fout = open(OutName, 'w')
num_lines = sum(1 for line in open(ListDas+ ".list"))
fout.write('fileNamesBlocks = [\n')
#Main body
nLine = 1
oldpost = ""
with open(ListDas+ ".list", 'r') as f:
    for line in f:
        Myfile = line.strip()
        pre = ""
        if(nLine==1):
            pre = "["
        post = ""
        if(nLine%(FilePerJob)==0 and nLine!=1):
            post = "],"
        else:
            if(nLine != num_lines):
                post = ","
            else:
                post = "]"
        if(nLine!=1 and oldpost=="],"):
            pre = "["
        body = pre + "'" + str(Myfile) + "'" + post
        fout.write( body + '\n' )
        nLine += 1
        oldpost = post
#Final line
fout.write(']')
fout.close()
