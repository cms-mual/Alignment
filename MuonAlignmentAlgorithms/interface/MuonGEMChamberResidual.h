#ifndef Alignment_MuonAlignmentAlgorithms_MuonGEMChamberResidual_H
#define Alignment_MuonAlignmentAlgorithms_MuonGEMChamberResidual_H

/** \class MuonGEMChamberResidual
 * 
 * Implementation of muon chamber residuals for GEM
 * 
 * $Id: $
 */

#include "Alignment/MuonAlignmentAlgorithms/interface/MuonHitsChamberResidual.h"
#include "TrackingTools/GeomPropagators/interface/Propagator.h"

class MuonGEMChamberResidual : public MuonHitsChamberResidual {
public:
  MuonGEMChamberResidual(edm::ESHandle<GlobalTrackingGeometry> globalGeometry,
                         AlignableNavigator *navigator,
                         DetId chamberId,
                         AlignableDetOrUnitPtr chamberAlignable);

  // for GEM, the residual is chamber local x, projected by the strip measurement direction
  // for GEM, the resslope is dresx/dz, or tan(phi_y)
  void addResidual(edm::ESHandle<Propagator> prop,
                   const TrajectoryStateOnSurface *tsos,
                   const TrackingRecHit *hit,
                   double,
                   double) override;

  // dummy method
  void setSegmentResidual(const reco::MuonChamberMatch *, const reco::MuonSegmentMatch *) override {}
};

#endif  // Alignment_MuonAlignmentAlgorithms_MuonGEMChamberResidual_H
