#ifndef Alignment_MuonAlignmentAlgorithms_MuonResiduals3DOFrphiFitter_H
#define Alignment_MuonAlignmentAlgorithms_MuonResiduals3DOFrphiFitter_H

/** \class MuonResiduals3DOFrphiFitter
 *  $Date: Thu Apr 16 21:29:15 CDT 2009
 *  $Revision: 1.5 $ 
 *  \author J. Pivarski - Texas A&M University <pivarski@physics.tamu.edu>
 */

#ifdef STANDALONE_FITTER
#include "MuonResidualsFitter.h"
#else
#include "Alignment/MuonAlignmentAlgorithms/interface/MuonResidualsFitter.h"
#include "Geometry/GEMGeometry/interface/GEMGeometry.h"
#endif

class TTree;

class MuonResiduals3DOFrphiFitter : public MuonResidualsFitter {
public:
  enum {
    kAlignX = 0,
    kAlignY,
    kAlignPhiZ,
    kResidSigma,
    kResSlopeSigma,
    kAlpha,
    kResidGamma,
    kResSlopeGamma,
    kNPar
  };

  enum { kResid = 0, kResSlope, kPositionX, kPositionY, kAngleX, kAngleY, kRedChi2, kPz, kPt, kCharge, kNData };

  MuonResiduals3DOFrphiFitter(int residualsModel, int minHits, int useResiduals, bool weightAlignment = true)
      : MuonResidualsFitter(residualsModel, minHits, useResiduals, weightAlignment) {}

#ifndef STANDALONE_FITTER
  MuonResiduals3DOFrphiFitter(
      int residualsModel, int minHits, int useResiduals, const GEMGeometry *GEMGeometry, bool weightAlignment = true)
      : MuonResidualsFitter(residualsModel, minHits, useResiduals, weightAlignment) {}
#endif

  ~MuonResiduals3DOFrphiFitter() override {}

  int type() const override { return MuonResidualsFitter::k3DOFrphi; }

  int npar() override {
    if (residualsModel() == kPureGaussian || residualsModel() == kPureGaussian2D ||
        residualsModel() == kGaussPowerTails)
      return kNPar - 2;
    else if (residualsModel() == kPowerLawTails)
      return kNPar;
    else if (residualsModel() == kROOTVoigt)
      return kNPar;
    else
      assert(false);
  }
  int ndata() override { return kNData; }

  double sumofweights() override;
  bool fit(Alignable *ali) override;
  double plot(std::string name, TFileDirectory *dir, Alignable *ali) override;

  void correctBField() override;

  TTree *readNtuple(std::string fname,
                    unsigned int endcap,
                    unsigned int station,
                    unsigned int ring,
                    unsigned int chamber,
                    unsigned int preselected = 1);

protected:
  void inform(TMinuit *tMinuit) override;

private:
  //const GEMGeometry *m_GEMGeometry;
};

#endif  // Alignment_MuonAlignmentAlgorithms_MuonResiduals3DOFrphiFitter_H
