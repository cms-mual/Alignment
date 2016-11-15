#ifndef Alignment_MuonAlignmentAlgorithms_DTTTree_H
#define Alignment_MuonAlignmentAlgorithms_DTTTree_H

#define BADVAL -999.0
typedef struct DTLayerData {

    UChar_t wheel;
    UChar_t station;
    UChar_t sector;

    UInt_t nlayers;
    UInt_t nDT;
    UInt_t nCSC;
    UInt_t nTracker;

    Int_t charge;
    Int_t nEvent;

    Bool_t select;

    Float_t pt;
    Float_t pz;
    Float_t eta;
    Float_t phi;
     
    Float_t v_hitx[8], v_hity[4];
    Float_t v_trackx[8], v_tracky[4], v_tracky_x_layer[8];
    
    //std::vector <Float_t> made_up_array(8);

    // not in ttree, but for other purposes
    Bool_t doFill;
    std::string cutType;

    DTLayerData()
    {
        charge = 0;
        wheel = 0;
        station = 0;
        sector = 0;
        nlayers = 0;
        nDT = 0;
        nCSC = 0;
        nTracker = 0;
        select = true;
        pt = BADVAL;
        pz = BADVAL;
        eta = BADVAL;
        phi = BADVAL;
        doFill = false;
        cutType = "";
       // for(int i = 0; i < 2; i++) {
       //     v_layer_hitx[i] = BADVAL;
       //     v_layer_resx[i] = BADVAL;
       // }
       // for(int i = 0; i < 1; i++) {
       //     v_layer_hity[i] = BADVAL;
       //     v_layer_resy[i] = BADVAL;
       // }
    } 

    DTLayerData & operator = (DTLayerData x)
    {
        charge = x.charge;
        wheel = x.wheel;
        station = x.station;
        sector = x.sector;
        nlayers = x.nlayers;
        nDT = x.nDT;
        nCSC = x.nCSC;
        nTracker = x.nTracker;
        select = x.select;
        pt = x.pt;
        pz = x.pz;
        eta = x.eta;
        phi = x.phi;
        doFill = x.doFill;
        cutType = x.cutType;
        
       //for(int i = 0; i < 2; i++) {
       //     v_layer_hitx[i] = x.v_layer_hitx[i];
       //     v_layer_resx[i] = x.v_layer_resx[i];
       // }
       // for(int i = 0; i < 1; i++) {
       //     v_layer_hity[i] = x.v_layer_hity[i];
       //     v_layer_resy[i] = x.v_layer_resy[i];
       // }
        return *this;
    }
} DTLayerData;
// RDM based on nja work

#endif
