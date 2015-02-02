#ifndef Alignment_MuonAlignmentAlgorithms_MuonResidualsFromTrack_H
#define Alignment_MuonAlignmentAlgorithms_MuonResidualsFromTrack_H

/** \class MuonResidualsFromTrack
 *  $Id: MuonResidualsFromTrack.h,v 1.4 2011/10/12 23:40:24 khotilov Exp $
 *  \author J. Pivarski - Texas A&M University <pivarski@physics.tamu.edu>
 */

#include "FWCore/Framework/interface/ESHandle.h"
#include "FWCore/Utilities/interface/Exception.h"
#include "Alignment/CommonAlignment/interface/AlignableNavigator.h"
#include "Geometry/CommonDetUnit/interface/GlobalTrackingGeometry.h"
#include "TrackingTools/PatternTools/interface/Trajectory.h"
#include "TrackingTools/TrackFitters/interface/TrajectoryStateCombiner.h"
#include "DataFormats/DetId/interface/DetId.h"
#include "DataFormats/MuonDetId/interface/DTChamberId.h"
#include "DataFormats/MuonDetId/interface/DTSuperLayerId.h"
#include "DataFormats/MuonDetId/interface/CSCDetId.h"
#include "DataFormats/SiStripDetId/interface/StripSubdetector.h"
#include "DataFormats/MuonReco/interface/Muon.h"
#include "DataFormats/MuonReco/interface/MuonFwd.h"
#include "DataFormats/TrackReco/interface/Track.h"

#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"

#include "TrackingTools/Records/interface/TrackingComponentsRecord.h"
#include "TrackingTools/TrackFitters/interface/TrajectoryFitter.h"
#include "TrackingTools/PatternTools/interface/TrajectorySmoother.h"

#include "TrackingTools/TrajectoryState/interface/TrajectoryStateOnSurface.h"
#include "TrackingTools/TransientTrack/interface/TransientTrack.h"
#include "TrackingTools/TransientTrackingRecHit/interface/TransientTrackingRecHitBuilder.h"
#include "TrackingTools/Records/interface/TransientRecHitRecord.h"
//#include "TrackingTools/PatternTools/interface/Trajectory.h"
#include "TrackingTools/GeomPropagators/interface/Propagator.h"

#include "DataFormats/TrackReco/interface/Track.h"
#include "DataFormats/TrackReco/interface/TrackFwd.h"
#include "DataFormats/DetId/interface/DetId.h"

#include "TMatrixDSym.h"
#include "TMatrixD.h"

#include <vector>
#include <map>

#include "Alignment/MuonAlignmentAlgorithms/interface/MuonChamberResidual.h"

class MuonResidualsFromTrack {
public:
  // residuals from global muon trajectories
  MuonResidualsFromTrack( const edm::EventSetup& iSetup,
                          edm::ESHandle<MagneticField> magneticField,
                          edm::ESHandle<GlobalTrackingGeometry> globalGeometry,
                          edm::ESHandle<Propagator> prop,
                          const Trajectory *traj,
                          const reco::Track* recoTrack,
                          AlignableNavigator *navigator,
                          double maxResidual );

  // residuals from tracker muons
  MuonResidualsFromTrack(edm::ESHandle<GlobalTrackingGeometry> globalGeometry,
                         const reco::Muon *recoMuon,
                         AlignableNavigator *navigator,
                         double maxResidual);

  ~MuonResidualsFromTrack();
  void clear();

  const reco::Track *getTrack() { return m_recoTrack; } // FIXME check if we need this method
  const reco::Muon  *getMuon()  { return m_recoMuon;  } // FIXME check if we need this method
  
  const std::vector<DetId> chamberIds() const { return m_chamberIds; }
  MuonChamberResidual *chamberResidual(DetId chamberId, int type);

  bool contains_TIDTEC() const { return m_contains_TIDTEC; }

  int    trackerNumHits() const { return m_tracker_numHits; }
  double trackerChi2()    const { return m_tracker_chi2; }
  double trackerRedChi2() const;
  double normalizedChi2() const;
  
  TMatrixDSym covMatrix(DetId chamberId);
  TMatrixDSym corrMatrix(DetId chamberId);
  TMatrixD    choleskyCorrMatrix(DetId chamberId);

private:
  // pointer to its track
  const reco::Track *m_recoTrack;
  // pointer to its muon
  const reco::Muon *m_recoMuon;

  TrajectoryStateCombiner m_tsoscomb;
  
  std::vector<DetId> m_chamberIds;
  std::map<DetId,MuonChamberResidual*> m_dt13;
  std::map<DetId,MuonChamberResidual*> m_dt2;
  std::map<DetId,MuonChamberResidual*> m_csc;

  bool   m_contains_TIDTEC;
  int    m_tracker_numHits;
  double m_tracker_chi2;

  std::map<DetId,TMatrixDSym> m_trkCovMatrix;
  void addTrkCovMatrix(DetId, TrajectoryStateOnSurface &);
};

#endif // Alignment_MuonAlignmentAlgorithms_MuonResidualsFromTrack_H
