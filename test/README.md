```
cp Alignment/test/* .
python3 createJobs.py -y job_stuff.yml
cd run3MC_test
condor_submit_dag *.dag
```
