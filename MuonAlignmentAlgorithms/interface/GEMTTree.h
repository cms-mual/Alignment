#ifndef Alignment_MuonAlignmentAlgorithms_CSCTTree_H
#define Alignment_MuonAlignmentAlgorithms_CSCTTree_H
#define BADVAL -999.0

typedef struct GEMChamberData {

    UChar_t endcap;
    UChar_t station;
    UChar_t ring;
    UChar_t superChamber;

    UInt_t nChambers;
    UInt_t nDT;
    UInt_t nCSC;
    UInt_t nGEM;
    UInt_t nTracker;

    Int_t charge;
    Int_t nEvent;

    Float_t pt;
    Float_t pz;
    Float_t eta;
    Float_t phi;

    Float_t v_hitx[6], v_hity[6];
    Float_t v_resx[6], v_resy[6];

    // not in ttree, but for other purposes
    Bool_t doFill;
    std::string cutType;

    GEMChamberData(){
        charge = 0;
        endcap = 0;
        station = 0;
        ring = 0;
        superChamber = 0;
        nChambers = 0;
        nDT = 0;
        nCSC = 0;
        nGEM = 0;
        nTracker = 0;
        pt = BADVAL;
        pz = BADVAL;
        eta = BADVAL;
        phi = BADVAL;
        doFill = false;
        cutType = "";
        for(int i = 0; i < 6; i++) {
            v_hitx[i] = BADVAL;
            v_hity[i] = BADVAL;
            v_resx[i] = BADVAL;
            v_resy[i] = BADVAL;
        }
    } 

    CSCLayerData & operator = (CSCLayerData x)
    {
        charge = x.charge;
        endcap = x.endcap;
        ring = x.ring;
        superChamber = x.superChamber;
        nChambers = x.nChambers;
        nDT = x.nDT;
        nCSC = x.nCSC;
        nGEM = x.nGEM;
        nTracker = x.nTracker;
        pt = x.pt;
        pz = x.pz;
        eta = x.eta;
        phi = x.phi;
        doFill = x.doFill;
        cutType = x.cutType;

        for(int i = 0; i < 6; i++) {
            v_hitx[i] = x.v_hitx[i];
            v_hity[i] = x.v_hity[i];
            v_resx[i] = x.v_resx[i];
            v_resy[i] = x.v_resy[i];
        }
        return *this;
    }
} GEMChamberData;

#endif
