# Computing APEs

1) CREATE_APEs.py
  -> From the _report.py file we extract the covariance matrix and we compute the APEs. In simulation we also can take the ideal geoemtry and the final one and we can extract the APEs from the correlation among the coordinates

Calculate APEs from alignment output. (DT only for now)

Help string:

```
Calculate APEs from alignment

positional arguments:
  outname              output name
  xml                  xml file from alignment
  report               report file from alignment

optional arguments:
  -h, --help           show this help message and exit
  --compgeom COMPGEOM  Comparison geometry for MC
  --debug DEBUG        print debug information
  --isDT ISDT          compute APEs for DTs
  --isCSC ISCSC        compute APEs for CSCs
  --isData ISDATA      compute APEs for Data
  --is3DOF IS3DOF      compute 3DOF APEs
```
Example usage:
```
python3 CREATE_APEs.py test test_data/run3MC_DT_large_01.xml test_data/run3MC_DT_large_01_report.py --isDT
```

or

```
python3 CREATE_APEs.py test test_data/run3MC_DT_large_01.xml test_data/run3MC_DT_large_01_report.py --isDT --isData
```


2) TEST_APEs.py
  -> We test the coverage of the APEs, that should return a chi2 distribution for 6DOF. In the case of the APEs extracted from the correlation plots, this should be true by construction.
  -> The macro draw the coverage for xmlfileAPE, and overimpose mxmlfileAPE and xmlfileAPE_comp to the Histogram correlation plots

3) Display_APE.py
  -> The APEs, and the correlation among the coordinates can be placed into a single plots. Also 2 different APEs can be compared.

4) ConvertXMLtoSQLite_cfg.py
  -> Convert APE from xml to db (so we can use them)
