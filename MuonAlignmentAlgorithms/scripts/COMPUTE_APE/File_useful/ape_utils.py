import numpy as np 
from File_useful.signConventions import *
from File_useful.geometryXMLparser import *
from File_useful.geometryXMLparser import MuonGeometry
from File_useful.plotscripts import *
from File_useful.Util_CalculateCovMatrix import *

wss_list = [(wheel, station, np.linspace(1,12,12, dtype='int')) if station!=4 else (wheel, station, np.linspace(1,14,14, dtype='int'))  for wheel in (-2, -1, 0, +1, +2) for station in (1, 2, 3, 4)]


def make_empty_wss_list():
  M_FIT = []
  for wheel in -2, -1, 0, +1, +2:
    M_FIT.append([])
    for station in 1, 2, 3, 4:
      M_FIT[wheel+2].append([])
      if station != 4: sectors = np.linspace(1,12,12, dtype='int')
      else: sectors = np.linspace(1,14,14, dtype='int')
      for sector in sectors:
        M_FIT[wheel+2][station-1].append(None)
  return M_FIT



def make_cov_fromH(isData, g1, gI=None):
    # Covariance from Final-Ideal geoemtry
    cov_fromH = make_empty_wss_list()
    if not isData:
      for wheel in (-2, -1, 0, 1, 2): 
        for station in (1, 2, 3, 4): 
          varx = []; vary = []; varz = []; varphix = []; varphiy = []; varphiz = []; 
          null = 0 
          cov_f = [[]]; cov_f = [[null for i in range(6)] for i in range(6)]
          if station != 4: sectors = (1,2,3,4,5,6,7,8,9,10,11,12)
          else:            sectors = (1,2,3,4,5,6,7,8,9,10,11,12,13,14)
          for sector in sectors:
            dx_cm = (g1.dt[wheel, station, sector].x - gI.dt[wheel, station, sector].x)*signConventions["DT", wheel, station, sector][0]
            dy_cm = (g1.dt[wheel, station, sector].y - gI.dt[wheel, station, sector].y)*signConventions["DT", wheel, station, sector][1]
            dz_cm = (g1.dt[wheel, station, sector].z - gI.dt[wheel, station, sector].z)*signConventions["DT", wheel, station, sector][2]
            dphix_rad = (g1.dt[wheel, station, sector].phix - gI.dt[wheel, station, sector].phix)*signConventions["DT", wheel, station,sector][0] 
            dphiy_rad = (g1.dt[wheel, station, sector].phiy - gI.dt[wheel, station, sector].phiy)*signConventions["DT", wheel, station, sector][1]
            dphiz_rad = (g1.dt[wheel, station, sector].phiz - gI.dt[wheel, station, sector].phiz)*signConventions["DT", wheel, station, sector][2]
            varx.append(dx_cm); vary.append(dy_cm); varz.append(dz_cm); varphix.append(dphix_rad); varphiy.append(dphiy_rad); varphiz.append(dphiz_rad);
          #Compute convariance
          All_vectors = np.vstack( (varx,vary,varz,varphix,varphiy,varphiz) )
          cov_f = np.cov(All_vectors)
          if station != 4: sectors = (1,2,3,4,5,6,7,8,9,10,11,12)
          else:            sectors = (1,2,3,4,5,6,7,8,9,10,11,12,13,14)
          for sector in sectors:
            cov_fromH[wheel+2][station-1][sector-1] = signConvention_cov_2D(cov_f,wheel,station,sector)
    return cov_fromH

def get_cov_fit_from_fit(report, is3DOF, debug=False):
  M_FIT = make_empty_wss_list()
  NfitFailed=0
  for r in report:
    index=1
    if ( r.postal_address[0] == "DT" and r.status == "PASS") :
        wheel   = r.postal_address[1]
        station = r.postal_address[2]
        sector  = r.postal_address[3]
        if(station==4 and (sector==10 or sector==14 or sector==4 or sector==13)):
          print( "SKIPPING BAD SECTORS")
          continue
        if(debug): print( "0)", wheel, station, sector)
        # Extract the covariance matrix and place it in the list E_stat
        E_stat=[]
        Cov_M = r.CovMatrix
        for covItem in Cov_M:
          #STATION 1 2 3
          if ( station != 4 ): #In station 1,2,3 are 144 numbers, because there are 12 params, but we want the first six (three): xx, xy, xz, xphix, xphiy, xphiz, A, B, 0, 0, 0, 0; yx, yy, yz... (xx, xy, xphiz, xA, xB, 0, 0, 0, 0, 0, 0, 0, yx, yy...)
            #3DOF
            if(is3DOF):
              if( index==25 ):
                E_stat.append(float(0)); E_stat.append(float(0)); E_stat.append(float(0)); E_stat.append(float(0)); E_stat.append(float(0)); E_stat.append(float(0)); #add a raw of 0
                E_stat.append(float(0)); E_stat.append(float(0)); E_stat.append(float(0)); E_stat.append(float(0)); E_stat.append(float(0)); E_stat.append(float(0));
                E_stat.append(float(0)); E_stat.append(float(0)); E_stat.append(float(0)); E_stat.append(float(0)); E_stat.append(float(0)); E_stat.append(float(0));
              if( index==1 or index==2 or index==13 or index==14 or index==25 or index==26 ):
                E_stat.append(float(covItem))
              if( index==3 or index==15 or index==27 ):
                E_stat.append(float(0)); E_stat.append(float(0)); E_stat.append(float(0)); E_stat.append(float(covItem));  # add 0 to Y component that is not there
            #6DOF
            else:
              if( (index>0 and index<7) or (index>12 and index<19) or (index>24 and index<31) or (index>36 and index<43) or (index>48 and index<(6*9+1)) or (index>60 and index<(6*11+1)) ):
                E_stat.append(float(covItem)) 
          #STATION 4
          else:                 #In station 4 there are 64 numbers, because there are 8 params, but we want the first five (two): xx, xz, xphix, xphiy, xphiz, A, 0, 0; zx, zz, zphix... (xx, xphiz, xA, 0, 0, 0, 0, 0, phizx, phizphiz...)
            #3DOF
            if(is3DOF):
              if( index==1 or index==9 ):
                E_stat.append(float(covItem))
              if( index==2 or index==10 ): 
                E_stat.append(float(0)); E_stat.append(float(0)); E_stat.append(float(0)); E_stat.append(float(0)); E_stat.append(float(covItem));  # add 0 to Y component that is not there
              if( index==3 ):
                E_stat.append(float(0)); E_stat.append(float(0)); E_stat.append(float(0)); E_stat.append(float(0)); E_stat.append(float(0)); E_stat.append(float(0)); #add a raw of 0
                E_stat.append(float(0)); E_stat.append(float(0)); E_stat.append(float(0)); E_stat.append(float(0)); E_stat.append(float(0)); E_stat.append(float(0));
                E_stat.append(float(0)); E_stat.append(float(0)); E_stat.append(float(0)); E_stat.append(float(0)); E_stat.append(float(0)); E_stat.append(float(0));
                E_stat.append(float(0)); E_stat.append(float(0)); E_stat.append(float(0)); E_stat.append(float(0)); E_stat.append(float(0)); E_stat.append(float(0));          
            #6DOF
            else:
              if( index==2 or index==10 or index==18 or index==26 or index==34 ):
                E_stat.append(float(0)) # add 0 to Y component that is not there
              if( index==8 ):
                E_stat.append(float(0)); E_stat.append(float(0)); E_stat.append(float(0)); E_stat.append(float(0)); E_stat.append(float(0)); E_stat.append(float(0)); #add a raw of 0
              if( (index>0 and index<6) or (index>8 and index<14) or (index>16 and index<22) or (index>24 and index<30) or (index>32 and index<38) ):#or (index>40 and index<46) or (index>48 and index<54) or (index>56 and index<62) or (index>64 and index<70) ) :
                E_stat.append(float(covItem)) # vector with 25 elements
          index=index+1
        if(debug): print("1)", len(E_stat), " -> ", E_stat)
        # Save final quantities in a map that for each chamber has a 6x6 matrix
        M_FIT[wheel+2][station-1][sector-1] = E_stat
    if ( r.postal_address[0] == "DT" and r.status != "PASS") :
      wheel   = r.postal_address[1]
      station = r.postal_address[2]
      sector  = r.postal_address[3]
      NfitFailed=NfitFailed+1
      m_null = []
      for iN in range(36): m_null.append(0)
      M_FIT[wheel+2][station-1][sector-1] = m_null
 
  #Apply Sign Convention to M_FIT (so that you can average different sectors correctly)
  M_FIT = signConvention(M_FIT)
  return E_stat, M_FIT, NfitFailed

def make_average_cov(M_FIT):
  cov_only  = make_empty_wss_list()
  cov_only_times2 = make_empty_wss_list()
  cov_only_all = make_empty_wss_list()
  for wheel, station, sectors in wss_list:
      print(
'''
\n********************************************************************\n
Group of chambers: wheel = %s, station = %s
********************************************************************
''' %  (wheel, station) 
      )
      #Covariance averaging same wheel/station
      print("Covariance matrix Matrix for wheel = %s, station = %s" % (wheel, station))
      cov_FIT    = calculateCovStatMatrix( M_FIT[wheel+2][station-1] ) 
      cov_FIT_t2 = calculateCovStatMatrix_times2( M_FIT[wheel+2][station-1] )
      for sector in sectors:
        cov_only[wheel+2][station-1][sector-1]        = cov_FIT 
        cov_only_times2[wheel+2][station-1][sector-1] = cov_FIT_t2
      #Covariance not averaging same wheel/station
      for sector in sectors:
        matrix = None
        if(station==4 and (sector==4 or sector==10 or sector==13 or sector==14)): matrix = cov_FIT
        else: matrix = calculateCovStatMatrix_noAverage(M_FIT[wheel+2][station-1][sector-1])
        cov_only_all[wheel+2][station-1][sector-1] = matrix
  #Apply Sign Convention again, because this is what CMS is expecting
  cov_only = signConvention(cov_only)
  cov_only_times2 = signConvention(cov_only_times2)
  cov_only_all = signConvention(cov_only_all) 
  return cov_only, cov_only_times2, cov_only_all

def write_xml(filename, cov_obj):
    with open(filename, 'w') as f:
        f.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n")
        f.write("<?xml-stylesheet type=\"text/xml\" href=\"MuonAlignment.xsl\"?>\n")
        f.write("<MuonAlignment>\n\n")
        for wheel, station, sectors in wss_list:
            for sector in sectors:
                xx       = cov_obj[wheel+2][station-1][sector-1][0][0]
                xy       = cov_obj[wheel+2][station-1][sector-1][0][1]
                xz       = cov_obj[wheel+2][station-1][sector-1][0][2]
                yy       = cov_obj[wheel+2][station-1][sector-1][1][1]
                yz       = cov_obj[wheel+2][station-1][sector-1][1][2]
                zz       = cov_obj[wheel+2][station-1][sector-1][2][2]
                xphix    = cov_obj[wheel+2][station-1][sector-1][0][3]
                xphiy    = cov_obj[wheel+2][station-1][sector-1][0][4]
                xphiz    = cov_obj[wheel+2][station-1][sector-1][0][5]
                yphix    = cov_obj[wheel+2][station-1][sector-1][1][3]
                yphiy    = cov_obj[wheel+2][station-1][sector-1][1][4]
                yphiz    = cov_obj[wheel+2][station-1][sector-1][1][5]
                zphix    = cov_obj[wheel+2][station-1][sector-1][2][3]
                zphiy    = cov_obj[wheel+2][station-1][sector-1][2][4]
                zphiz    = cov_obj[wheel+2][station-1][sector-1][2][5]
                phixphix = cov_obj[wheel+2][station-1][sector-1][3][3]
                phixphiy = cov_obj[wheel+2][station-1][sector-1][3][4]
                phixphiz = cov_obj[wheel+2][station-1][sector-1][3][5]
                phiyphiy = cov_obj[wheel+2][station-1][sector-1][4][4]
                phiyphiz = cov_obj[wheel+2][station-1][sector-1][4][5]
                phizphiz = cov_obj[wheel+2][station-1][sector-1][5][5]        
                if(station==4): xy=0; yy = 0.01; yz=0; yphix=0; yphiy=0; yphiz=0;
                f.write("<operation>\n")
                f.write( "  <DTChamber wheel=\"%s\" station=\"%s\" sector=\"%s\" />\n" % (wheel, station, sector) )
                f.write( "  <setape xx=\"%s\" xy=\"%s\" xz=\"%s\" yy=\"%s\" yz=\"%s\" zz=\"%s\" xa=\"%s\" xb=\"%s\" xc=\"%s\" ya=\"%s\" yb=\"%s\" yc=\"%s\" za=\"%s\" zb=\"%s\" zc=\"%s\" aa=\"%s\" ab=\"%s\" ac=\"%s\" bb=\"%s\" bc=\"%s\" cc=\"%s\" />\n" % (xx, xy, xz, yy, yz, zz, xphix, xphiy, xphiz, yphix, yphiy, yphiz, zphix, zphiy, zphiz, phixphix, phixphiy, phixphiz, phiyphiy, phiyphiz, phizphiz) )
                f.write("</operation>\n\n")
        f.write("</MuonAlignment>")
