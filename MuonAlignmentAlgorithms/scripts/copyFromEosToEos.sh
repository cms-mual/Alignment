#/bin/sh
# parameters
EOS="/store/caf/user/lpernie/mu_align/"
files="data_DT-1100-110001_SingleMuon_Run2015D-PromptReco-v3_RECO_7_4_6_patch3_pt20_v1.sh
data_DT-1100-110001_SingleMuon_Run2015D-PromptReco-v3_RECO_7_4_6_patch3_pt20_v1_01
data_DT-1100-110001_SingleMuon_Run2015D-PromptReco-v3_RECO_7_4_6_patch3_pt20_v1_01.root
data_DT-1100-110001_SingleMuon_Run2015D-PromptReco-v3_RECO_7_4_6_patch3_pt20_v1_01_plotting.root
data_DT-1100-110001_SingleMuon_Run2015D-PromptReco-v3_RECO_7_4_6_patch3_pt20_v1_02
data_DT-1100-110001_SingleMuon_Run2015D-PromptReco-v3_RECO_7_4_6_patch3_pt20_v1_02.root
data_DT-1100-110001_SingleMuon_Run2015D-PromptReco-v3_RECO_7_4_6_patch3_pt20_v1_03
data_DT-1100-110001_SingleMuon_Run2015D-PromptReco-v3_RECO_7_4_6_patch3_pt20_v1_03.root
data_DT-1100-110001_SingleMuon_Run2015D-PromptReco-v3_RECO_7_4_6_patch3_pt20_v1_03_plotting.root
data_DT-1100-110001_SingleMuon_Run2015D-PromptReco-v3_RECO_7_4_6_patch3_pt20_v1_20151110095912.tgz
data_DT-1100-110001_SingleMuon_Run2015D-PromptReco-v3_RECO_7_4_6_patch3_pt20_v1_MuAlSummer15b.sh
data_DT-1100-110001_SingleMuon_Run2015D-PromptReco-v3_RECO_7_4_6_patch3_pt20_v1_MuAlSummer15b_01
data_DT-1100-110001_SingleMuon_Run2015D-PromptReco-v3_RECO_7_4_6_patch3_pt20_v1_MuAlSummer15b_02
data_DT-1100-110001_SingleMuon_Run2015D-PromptReco-v3_RECO_7_4_6_patch3_pt20_v1_MuAlSummer15b_03
data_DT-1100-110001_SingleMuon_Run2015D-PromptReco-v3_RECO_7_4_6_patch3_pt20_v1_MuAlSummer15b_NOFIDCUT_01
data_DT-1100-110001_SingleMuon_Run2015D-PromptReco-v3_RECO_7_4_6_patch3_pt20_v1_MuAlSummer15b_NOFIDCUT_02
data_DT-1100-110001_SingleMuon_Run2015D-PromptReco-v3_RECO_7_4_6_patch3_pt20_v1_MuAlSummer15b_NOFIDCUT_03
data_DT-1100-110001_SingleMuon_Run2015D-PromptReco-v4_RECO_CMSSW_7_4_12_patch4_pt20_luca_v1.sh
data_DT-1100-110001_SingleMuon_Run2015D-PromptReco-v4_RECO_CMSSW_7_4_12_patch4_pt20_luca_v1_01
data_DT-1100-110001_SingleMuon_Run2015D-PromptReco-v4_RECO_CMSSW_7_4_12_patch4_pt20_luca_v1_02
data_DT-1100-110001_SingleMuon_Run2015D-PromptReco-v4_RECO_CMSSW_7_4_12_patch4_pt20_luca_v1_03
data_DT-1100-110001_SingleMuon_Run2015D-PromptReco-v4_RECO_CMSSW_7_4_12_patch4_pt20_luca_v1_20151120093630.tgz"

OUT_FOLDER="/store/group/alca_muonalign/lpernie/"
eosComm="/afs/cern.ch/project/eos/installation/0.3.84-aquamarine/bin/eos.select"

#loop
for f in $files
do
    echo FIRST IS $EOS$f
    check=`$eosComm ls -D $EOS$f`
    nLine=`echo "$check" | wc -l`
    if [ "$nLine" -eq "1" ]
    then
       echo "->Is a FILE!"
       echo "  cmsStage -f $EOS$f $OUT_FOLDER"
       stage=`cmsStage -f $EOS$f $OUT_FOLDER`
    else
       echo "->Is a DIR!"
       echo "  $eosComm mkdir -p $OUT_FOLDER/$f"
       makedir=`$eosComm mkdir -p $OUT_FOLDER/$f`
       #Now go inside the folder
       fold=`$eosComm ls $EOS$f`
       for ff in $fold
       do
           echo "  --> Descending in $ff"
           echo "      cmsStage -f $EOS$f/$ff $OUT_FOLDER/$f"
           stage=`cmsStage -f $EOS$f/$ff $OUT_FOLDER/$f`
       done
    fi
done
