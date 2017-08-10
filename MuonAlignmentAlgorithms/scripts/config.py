"""
Created:       2 August 2017
Last Updated:  2 August 2017

Dan Marley
daniel.edison.marley@cernSPAMNOT.ch
University of Michigan, Ann Arbor, MI 48109
-----

Configuration class for getting/setting parameters
to use in the alignment.
"""
import os
import sys
import util


class Config(object):
    """Configuration object that handles the setup"""
    def __init__(self,configfile,script='createJobs.py'):
        self.filename = configfile

        self.configuration = {}      # hold all values in dictionary (as strings)
        self.script        = script  # the script that calls this class (e..g, createJobs.py)

        self.set_defaults()


    def initialize(self):
        """Initialize the configuration"""
        self.setConfigurations()     # set the configuration options

        return


    def setConfigurations(self):
        """Read the configuration file and set arguments"""
        file = open(self.filename,'r').readlines()
        for line in file:
            param,value = line.split(' ')
            value       = value.rstrip('\n')

            self.configuration[param] = value

        return


    def get(self,param):
        """Return values of the configuration to the user"""
        value = None

        try:
            value = self.configuration[param]
        except KeyError:
            util.WARNING("CONFIG : The configuration file does not contain {0}".format(param))
            util.WARNING("CONFIG : Using default value.")
            try:
                value = self.defaults[param]
            except KeyError:
                raise KeyError("There is no default value for {0}.\n"
                               "Please set this parameter in the configuration file.".format(param))

        return value


    def set_defaults(self):
        """Set default values for configurations"""
        self.configuration = {
            'jobs':50,
            'submitJobs':'submitJobs.sh',
            'big':False,
            'user_mail':None,
            'mapplots':False,
        }

        return defaults


    def dirname(self):
        """Directory name"""
        return self.get("dirname")
        
    def iterations(self):
        """Number of fit iterations"""
        return self.get("iterations")
    
    def initial_geometry(self):
        """Initial geometry used for the fit"""
        return self.get("initial_geometry")

    def inputfiles(self):
        """Input files for the alignment"""
        return self.get("inputfiles")

    def subjobs(self):
        """Approximate number of 'gather' subjobs"""
        return int(self.get("jobs"))

    def submitJobs(self):
        """
           Alternate name of submitJobs.sh script (please include .sh extension).
           A file with this name will be OVERWRITTEN
        """
        return self.get("submitJobs")

    def big(self):
        """Subjobs will be run on queue 'cmscaf1nd'"""
        return util.str2bool( self.get("big") )

    def user_mail(self):
        """Send email to specified address.
           Default: destination LSB_MAILTO in lsf.conf
        """
        return self.get('user_mail')

    def mapplots(self):
        """Draw 'map plots'"""
        return util.str2bool( self.get('mapplots') )

    def segdiffplots(self):
        """Draw 'segment-difference plots'"""
        return util.str2bool( self.get('segdiffplots') )

    def curvatureplots(self):
        """Draw curvature plots"""
        return util.str2bool( self.get('curvatureplots') )

    def globaltag(self):
        """GlobalTag for Alca conditions"""
        return self.get('globaltag')
                  default="CRAFT0831X_V1::All",

    def trackerconnect(self):
        """Connect string for tracker alignment (frontier://FrontierProd/CMS_COND_310X_ALIGN, sqlite_file, etc.)"""
        return self.get('trackerconnect')

    def trackeralignment(self):
        """Name of the TrackerAlignmentRcd tag"""
        return self.get('trackeralignment')

    def trackerAPEconnect(self):
        """Connect string for tracker APEs (frontier://..., sqlite_file:, etc.)"""
        return self.get('trackerAPEconnect')

    def trackerAPE(self):
        """Name of the TrackerAlignmentErrorExtendedRcd tag"""
        return self.get('trackerAPE')


    def trackerBowsconnect(self):
        """
           Connect string for tracker Surface Deformations 
           (frontier://... or sqlite_file:...)
        """
        return self.get("trackerBowsconnect")

    def trackerBows(self):
        """Name of TrackerSurfaceDeformationRcd tag"""
        return self.get("trackerBows")

    def gprcdconnect(self):
        """Connect string for GlobalPositionRcd (frontier://... or sqlite_file:...)"""
        return self.get("gprcdconnect")

    def gprcd(self):
        """Name of GlobalPositionRcd tag"""
        return self.get("gprcd")

    def iscosmics(self):
        """if invoked, use cosmic track refitter instead of the standard one"""
                  action="store_true",
        return self.get("iscosmics")

    def station123params(self):
        """
            Alignable parameters for DT stations 1, 2, 3 
            (see SWGuideAlignmentAlgorithms#Selection_of_what_to_align)
        """
        return self.get("station123params")

    def station4params(self):
        """Alignable parameters for DT station 4"""
        return self.get("station4params")

    def cscparams(self):
        """Alignable parameters for CSC chambers"""
        return self.get("cscparams")

    def minTrackPt(self):
        """Minimum allowed track transverse momentum (in GeV)"""
        return self.get("minTrackPt")

    def maxTrackPt(self):
        """Maximum allowed track transverse momentum (in GeV)"""
        return self.get("maxTrackPt")

    def minTrackP(self):
        """Minimum allowed track momentum (in GeV)"""
        return self.get("minTrackP")
    def maxTrackP(self):
        """Maximum allowed track momentum (in GeV)"""
        return self.get("maxTrackP")

    def minTrackerHits(self):
        """Minimum number of tracker hits"""
        return int( self.get("minTrackerHits") )

    def maxTrackerRedChi2(self):
        """Maximum tracker chi^2 per degrees of freedom"""
        return self.get("maxTrackerRedChi2")

    def allowTIDTEC(self):
        """
            Allow tracks that pass through the tracker's 
            TID||TEC region (not recommended)
        """
        return util.str2bool( self.get("notAllowTIDTEC") )

    def twoBin(self):
        """Apply the 'two-bin method' to control charge-antisymmetric errors"""
        return util.str2bool( self.get("twoBin") )

    def weightAlignment(self):
        """Segments will be weighted by ndf/chi^2 in the alignment"""
        return util.str2bool( self.get("weightAlignment") )

    def minAlignmentSegments(self):
        """Minimum number of segments required to align a chamber"""
        return int( self.get("minAlignmentHits") )

    def notCombineME11(self):
        """Treat ME1/1a and ME1/1b as separate objects"""
        return util.str2bool( self.get("notCombineME11") )

    def maxEvents(self):
        """Maximum number of events"""
        return self.get("maxEvents")

    def skipEvents(self):
        """Number of events to be skipped"""
        return self.get("skipEvents")

    def validationLabel(self):
        """
            If given nonempty string RUNLABEL, diagnostics and creation of 
            plots will be run in the end of the last iteration; 
            the RUNLABEL will be used to mark a run; the results will be put into a 
            RUNLABEL_DATESTAMP.tgz tarball
        """
        return self.get("validationLabel")

    def maxResSlopeY(self):
        """Maximum residual slope y component"""
        return self.get("maxResSlopeY")

    def motionPolicyNSigma(self):
        """
            Minimum nsigma(deltax) position displacement to move a chamber 
            for the final alignment result.
        """
        return int( self.get("motionPolicyNSigma") )

    def doCleanUp(self):
        """Temporary plotting*.root and *.tmp files not removed at the end of each align job"""
        return util.str2bool( self.get("doCleanUp") )

    def doCSC(self):
        """Process the CSC endcap chambers"""
        return util.str2bool( self.get("doCSC") )

    def doDT(self):
        """if invoked, DT barrel chambers would not be processed"""
        return util.str2bool( self.get("doDT") )

    def createMapNtuple(self):
        """If mapplots are switched on, a special ntuple is created"""
        return util.str2bool( self.get("createMapNtuple") )

    def inputInBlocks(self):
        """
            Assume that INPUTFILES provides a list of files already 
            groupped into job blocks (`-j` has no effect)
        """
        return util.str2bool( self.get("inputInBlocks") )

    def json(self):
        """If present with JSON file as argument, use JSON file for good lumi mask.
            'The latest JSON file is available at 
            /afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions11/7TeV/Prompt/
        """
        return self.get("json")

    def createAlignNtuple(self):
        """Debug ntuples with residuals created during gather jobs"""
        return util.str2bool( self.get("createAlignNtuple") )

    def residualsModel(self):
        """
            Functional residuals model. 
            Possible vaslues: 
              pureGaussian2D (default), pureGaussian, 
              GaussPowerTails, ROOTVoigt, powerLawTails
        """
        return self.get("residualsModel")

    def useResiduals(self):
        """
            Select residuals to use, possible values: 
              1111, 1110, 1100, 1010, 0010 
            that correspond to x y dxdz dydz residuals
        """
        return self.get("useResiduals")

    def peakNSigma(self):
        """
            If >0, only residuals peaks within n-sigma multidimentional 
            ellipsoid considered in the alignment fit
        """
        return self.get("peakNSigma")

    def preFilter(self):
        """
            MuonAlignmentPreFilter module would be invoked in the Path's beginning. 
            Can significantly speed up gather jobs.
        """
        return util.str2bool( self.get("preFilter") )

    def muonCollectionTag(self):
        """
            If empty, use trajectories. 
            Else, it's InputTag of muons collection to use in 
            tracker muons based approach, e.g., 'newmuons' or 'muons'
        """
        return self.get("muonCollectionTag")

    def maxDxy(self):
        """Maximum track impact parameter with relation to beamline"""
        return self.get("maxDxy")

    def minNCrossedChambers(self):
        """Minimum number of muon chambers that a track is required to cross"""
        return self.get("minNCrossedChambers")

    def extraPlots(self):
        """
            Produce additional plots with geometry, reports differences, 
            and corrections visulizations
        """
        return util.str2bool( self.get("extraPlots") )

    def T0(self):
        """
            Includes T0 correction into DT muon segments 
            (safer to have them, even if usually there is no visible difference). 
            It implies the re-reconstruction of global muons.
        """
        return util.str2bool( self.get("T0_Corr") )

    def is_Alca(self):
        """Use if you are running on ALCARECO. DO NOT USE for RECO"""
        return util.str2bool( self.get("is_Alcareco") )

    def is_MC(self):
        """Use if running on MC"""
        return util.str2bool( self.get("is_MC") )

    def createLayerNtupleDT(self):
        """Add a TTree with DT layer per layer information"""
        return util.str2bool( self.get("createLayerNtupleDT") )

    def createLayerNtupleCSC(self):
        """Add a TTree with CSC layer per layer information"""
        return util.str2bool( self.get("createLayerNtupleCSC") )



    def __str__(self):
        """Specialized print statement for this class"""
        command = """ Track-Based Muon Alignment : Configuration

./%(prog)s <configuration>

Creates (overwrites) a directory for each of the iterations and creates (overwrites)
submitJobs.sh with the submission sequence and dependencies.
""" % {'prog': self.source}

        keys = configuration.keys()
        keys.sort()
        max_len = max( len(i) for i in keys )+2


        for i in keys:
            neededlength = max_len-len(i)
            whitespace   = ' '*neededlength

            try:
                command+="   ** {0}{1}= {2:.4f}\n".format(i,whitespace,self.__dict__[i])
            except ValueError:
                continue

        return command
