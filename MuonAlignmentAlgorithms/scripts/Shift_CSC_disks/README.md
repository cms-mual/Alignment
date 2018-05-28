##Disk-level CSC Alignment

1) In the validation browser, observe if, in the first iteration of CSC alignment, a sinuosoidal behaviour is present.

2) If so, you can extract the fit parameters to print out the shifts in a txt file by setting 

```python
file = <CSC_alignment_dir>/*_plotting.root
``` 

(the ROOT file produced by the first iteration of CSC alignment), then running

```
python PrintShiftsToTxt.py
```

3) Then you can use the .txt produced by PrintShiftsToTxt.py to correct the geometry and produce a new reference geoemtry without any sinusoidal shifts; after changing the DbFile to the reference geometry, naming your OutDB, and modifying line 28 to take your .txt file from the previous step, run 

```
python PrintShiftedXML_fromTXT.py
```

4) Rerun the alignment with this geometry and verify that the validation browser shows no more sinusoidal shifting of the disks.
