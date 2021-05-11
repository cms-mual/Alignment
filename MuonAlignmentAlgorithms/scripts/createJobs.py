#! /usr/bin/env python

import os, sys, optparse, math
from optparse import OptionParser
import yaml
import pprint
import random
from create_job_cfg_assets import hadd_cfg_str, align_cfg_str, validation_cfg_str, gather_cfg_str, condor_template,condor_gather_template


def load_yml(file_name):
    with open(file_name, 'r') as stream:
        try:
            return yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)
class cfg_object:
  def __init__(self,job_config):
    for key in job_config:
      dest = job_config[key]['dest']
      value = job_config[key]['value']
      self.add_value(dest,value)
  def add_value(self,name,value):
    v_type = type(value)
    if value is None:
      exec("self.{} = ''".format(name))
    elif v_type != str:
      exec("self.{} = {}".format(name, value))
    else:
      exec("self.{} = '{}'".format(name, value))
def write_file(fname, my_vars, file_string):
  with open("{}".format(fname), 'w') as f:
    f.write(file_string.format(**my_vars))

def remove_last_char(l_string,l_char):
  if l_string[-1] == l_char: return l_string[:-1]
  else: return l_string

#parse command line options
parser = OptionParser()
parser.add_option("-y", "--yml", dest="filename",
                  help="yml filename", metavar="YAML")
parser.add_option("-x", "--xml_geom",
                  action="store_true", dest="xml_geom", default=False,
                  help="Convert the db alignment geometry to xml.")
parser.add_option("-v", "--verbose",
                  action="store_true", dest="verbose", default=False,
                  help="Print out config and so on.")

(options, args) = parser.parse_args()

#create cfg object
job_config = load_yml(options.filename)
print(options.filename)
cfg = cfg_object(job_config)
#store starting variables
cfg.vars = vars(cfg)
if options.verbose:
  print("######################config######################")
  pprint.pprint(cfg.vars)

#must only align over DTs or CSCs
assert cfg.doCSC+cfg.doDT==1, "Must be CSC xor DT."
assert cfg.createLayerNtupleDT+cfg.createLayerNtupleCSC<=1, "WARNING! You Cannot create DEBUG Ntuples for DT and CSC at the same time."

##
##load and format file list
##
#load file list
print(cfg.INPUTFILES)
with open(cfg.INPUTFILES, 'r') as f:
  cfg.file_list = [line.replace('\n','') for line in f.readlines()]
#shuffle files
random.shuffle(cfg.file_list)

def chunks(l_list,n):
  for i in range(0, len(l_list), n):
    yield l_list[i:i + n]
cfg.file_list = list(chunks(cfg.file_list, cfg.block_size))
if options.verbose:
  print("######################filelist######################")
  pprint.pprint((cfg.file_list))

# get local dir
cfg.pwd = str(os.getcwd())
cfg.pwd_DIRNAME = "{}/{}".format(cfg.pwd,cfg.DIRNAME)

#create string of tracker dbs
cfg.copytrackerdb = ""
for db_str in [cfg.trackerconnect,cfg.trackerAPEconnect,cfg.trackerBowsconnect,cfg.gprcdconnect]:
  if db_str: cfg.copytrackerdb+= " {}".format(db_str.replace("sqlite_file:",""))

#####################################################################
# step 0: convert initial geometry to xml
cfg.INITIALXML = "{}.xml".format(cfg.INITIALGEOM.replace('.db', ''))
if options.xml_geom:
  print( "Converting",cfg.INITIALGEOM,"to",cfg.INITIALXML," ...will be done in several seconds...")
  print( "./Alignment/MuonAlignmentAlgorithms/scripts/convertSQLiteXML.py  %s %s --gprcdconnect %s --gprcd %s --noLayers " % (cfg.INITIALGEOM,cfg.INITIALXML,cfg.gprcdconnect,cfg.gprcd))
  exit_code = os.system("./Alignment/MuonAlignmentAlgorithms/scripts/convertSQLiteXML.py  %s %s --gprcdconnect %s --gprcd %s --noLayers " % (cfg.INITIALGEOM,cfg.INITIALXML,cfg.gprcdconnect,cfg.gprcd))
  if exit_code>0:
    print( "problem: conversion exited with code:", exit_code)
    sys.exit()

#####################################################################

last_align = None
cfg.directory  = ""
directories = []
for iteration in range(1, cfg.ITERATIONS+1):
    cfg.iteration = iteration

    #create directory strings
    if iteration == 1:
        cfg.inputdb = cfg.INITIALGEOM
        cfg.inputdbdir = cfg.directory [:]
    else:
        cfg.inputdb = cfg.director + ".db"
        cfg.inputdbdir = '{}/{}'.format(cfg.DIRNAME,cfg.directory [:])
    cfg.directory  = "{0}_{1:02d}/".format(cfg.DIRNAME, iteration)
    cfg.director = remove_last_char(cfg.directory, '/')
    cfg.dir_no_ = remove_last_char(cfg.DIRNAME, '_')
    cfg.pwd_DIRNAME_directory = "{}/{}/{}".format(cfg.pwd,cfg.DIRNAME,cfg.directory)
    cfg.DIRNAME_directory = "{}/{}".format(cfg.DIRNAME,cfg.directory)

    directories.append(cfg.director)

    #create directories
    dir_name_dict = {"dirname":cfg.DIRNAME, "directory": cfg.directory }
    cfg.iteration_dirs.append("{dirname}/{directory}".format(**dir_name_dict))
    if iteration == 1: 
      os.system("rm -rf {dirname}; mkdir {dirname}".format(**dir_name_dict))
      os.system("cp {fname} {dirname}".format(**{**dir_name_dict,"fname":options.filename}))
      os.system("mkdir {dirname}/output".format(**dir_name_dict))
      os.system("mkdir {dirname}/log".format(**dir_name_dict))
      os.system("mkdir {dirname}/error".format(**dir_name_dict))
    os.system("mkdir {dirname}/{directory}".format(**dir_name_dict))
    os.system("mkdir {dirname}/output/{directory}".format(**dir_name_dict))
    os.system("mkdir {dirname}/log/{directory}".format(**dir_name_dict))
    os.system("mkdir {dirname}/error/{directory}".format(**dir_name_dict))
    os.system("cp Alignment/MuonAlignmentAlgorithms/python/gather_cfg.py {dirname}/{directory}".format(**dir_name_dict))
    os.system("cp Alignment/MuonAlignmentAlgorithms/python/align_cfg.py {dirname}/{directory}".format(**dir_name_dict))

    # I don't fully understand why  mapplots is only true for odd iters, i guess it has to do with the "special" iterations below
    if cfg.mapplots_ingeneral and ((not (iteration/2.).is_integer()) or iteration == cfg.ITERATIONS): cfg.mapplots = True
    else: cfg.mapplots = False
    if cfg.segdiffplots_ingeneral and (iteration == 1 or iteration == cfg.ITERATIONS): cfg.segdiffplots = True
    else: cfg.segdiffplots = False
    if cfg.curvatureplots_ingeneral and (iteration == 1 or iteration == cfg.ITERATIONS): cfg.curvatureplots = True
    else: cfg.curvatureplots = False

    ### gather.sh runners for njobs
    for jobnumber, files in enumerate(cfg.file_list):
      cfg.inputfiles = " ".join(files)
      cfg.jobnumber = jobnumber
      if cfg.mapplots or cfg.segdiffplots or cfg.curvatureplots: cfg.copyplots = "plotting*.root"
      else: cfg.copyplots = ""

      if len(cfg.inputfiles) > 0:
        gather_fileName = "{dirname}/{directory}gather{jobnumber:03d}.sh".format(**{**dir_name_dict, "jobnumber":jobnumber})

        vars(cfg)
        write_file(gather_fileName, vars(cfg),gather_cfg_str)

    ### align and hadd
    hadd_fname = "{dirname}/{directory}hadd.sh".format(**dir_name_dict)
    align_fname = "{dirname}/{directory}align.sh".format(**dir_name_dict)
    if cfg.SUPER_SPECIAL_XY_AND_DXDZ_ITERATIONS:
        if (not (iteration/2.).is_integer()):
            tmp = station123params, station123params, useResiduals 
            station123params, station123params, useResiduals = "000010", "000010", "0010"
            writeHaddCfg("%shadd.sh" % cfg.directory, vars())
            writeAlignCfg("%salign.sh" % cfg.directory, vars())
            station123params, station123params, useResiduals = tmp
        else:
            tmp = station123params, station123params, useResiduals 
            station123params, station123params, useResiduals = "110001", "100001", "1100"
            writeHaddCfg("%shadd.sh" % cfg.directory, vars())
            writeAlignCfg("%salign.sh" % cfg.directory, vars())
            station123params, station123params, useResiduals = tmp
    else:
      write_file(hadd_fname, vars(cfg),hadd_cfg_str)
      write_file(align_fname, vars(cfg),align_cfg_str)
    
    os.system("chmod +x {}/*".format(cfg.DIRNAME_directory))

    ### after the last iteration (optionally) do diagnostics run
    if len(cfg.validationLabel) and iteration == cfg.ITERATIONS:
        # do we have plotting files created?
        cfg.directory1 = cfg.iteration_dirs[0]
        cfg.director1 = cfg.directory1[:-1]
        
        validation_fname = "{dirname}/{directory}validation.sh".format(**dir_name_dict)
        write_file(validation_fname, vars(cfg), validation_cfg_str)
        os.system("chmod +x {}".format(validation_fname))

def make_job_name(dir_dict, job_name):
  job_name = "{job_name}_{iter_dir}.sub".format(**{**dir_dict,"job_name": job_name})
  job_w_path = "./{top_dir}/{job_name}".format(**{**dir_dict,"job_name": job_name})
  return job_name, job_w_path

class Job:
  def __init__(self, name, path,):
    self.name = name.replace(".sub","")
    self.path = path
  def __repr__(self):
    return "JOB {} {}\n".format(self.name,self.path)
  def __str__(self):
    return "JOB {} {}\n".format(self.name,self.path)

class Dag:
  def __init__(self):
    self.jobs = []
    self.connections = []
  def add_job(self,job,parents=[]):
    self.jobs.append(job)
    if len(parents) > 0 and parents[0]:
      self.connections.append([job,parents])
  def __str__(self):
    dag_string = ""
    for job in self.jobs:
      dag_string += str(job)
    for (child, parents) in self.connections:
      par_string = ""
      for parent in parents:
        par_string += " {}".format(parent.name)
      dag_string += "PARENT {} CHILD {}\n".format(par_string, child.name)
    return dag_string

#make condor jobs
#the loop for the next iter starts with the last align job, so we set the default align job to 0
align = 0
dag = Dag()
for directory in directories:
  dir_name_dict = {"top_dir":cfg.DIRNAME, "iter_dir": directory }
  gather_fname = make_job_name(dir_name_dict, "gather")
  hadd_fname = make_job_name(dir_name_dict, "hadd")
  align_fname = make_job_name(dir_name_dict, "align")
  validate_fname = make_job_name(dir_name_dict, "validate")

  write_file(gather_fname[1], dir_name_dict, condor_gather_template)
  gather = Job(gather_fname[0],gather_fname[0])
  dag.add_job(gather,parents=[align])

  write_file(hadd_fname[1], {**dir_name_dict, "job_sh": "hadd.sh"}, condor_template)
  hadd = Job(hadd_fname[0],hadd_fname[0])
  dag.add_job(hadd,parents=[gather])

  write_file(align_fname[1], {**dir_name_dict, "job_sh": "align.sh"}, condor_template)
  align = Job(align_fname[0],align_fname[0])
  dag.add_job(align,parents=[hadd])

  #only run validation for last iter
  if directory == directories[-1]:
    write_file(validate_fname[1], {**dir_name_dict, "job_sh": "validate.sh"}, condor_template)
    validate = Job(validate_fname[0],validate_fname[0])
    dag.add_job(validate,parents=[hadd,align])

with open('{top_dir}/condor_{top_dir}.dag'.format(top_dir=cfg.DIRNAME), 'w') as f:
  f.write(str(dag))

os.system("chmod +x {}/*".format(cfg.DIRNAME))

