#!/usr/bin/env python

from array import array
import ROOT
ROOT.gSystem.Load('CMSSW_7_6_3/lib/slc6_amd64_gcc493/libttH-13TeVMultiLeptonsTemplateMakers.so')

# Tree to read in (has vectors)
inFile = ROOT.TFile.Open('ttH_forKevin.root')
inTree = inFile.Get('OSTwoLepAna/summaryTree')

# Tree to write out (flat-no vectors)
outFile = ROOT.TFile.Open('ttH_flat.root','RECREATE')
outFile.cd()
outTree = ROOT.TTree('flatTree','flatTree')

Ht = array('f',[0])
outTree.Branch('Ht',Ht,'Ht/F')
# Now ROOT requires us to declare each variable we plan to store in
# the tree in this funny way.  Let's also declare the branch at the
# same time.

nJets = array('i',[0])
outTree.Branch('nJets',nJets,'nJets/I')

# Now let's make the jet vector information a little simpler with a structure
ROOT.gROOT.ProcessLine("""
struct JetStruct {
    Float_t pt;
    Float_t eta;
    Float_t phi;
};
""")
from ROOT import JetStruct

jets = [JetStruct(),JetStruct(),JetStruct(),JetStruct(),JetStruct()]
for i in range(5):
    outTree.Branch('jet{}'.format(i),
                   jets[i],
                   'jet{0}Pt/F:jet{0}Eta/F:jet{0}Phi/F'.format(i))

#set up the Leptons
nLeptons = array('i',[0])
outTree.Branch('nLeptons',nLeptons, 'nLeptons/I')

ROOT.gROOT.ProcessLine("""
struct LeptonStruct {
	Float_t pt;
	Float_t eta;
	Float_t phi;
};
""")
from ROOT import LeptonStruct

leptons = [LeptonStruct(),LeptonStruct(),LeptonStruct(),LeptonStruct(),LeptonStruct()]
for i in range(5):
    outTree.Branch('lepton{}'.format(i),
                   jets[i],
                   'lepton{0}Pt/F:lepton{0}Eta/F:lepton{0}Phi/F'.format(i))


for entry in inTree:

    # We want to make sure that any variable we store is initialized
    # in this event and not store the value from a previous event
    nJets[0] = 0
    nLeptons[0] = 0
    Ht[0] = 0
    for i in range(5):
        jets[i].pt  = -9e20
        jets[i].eta = -9e20
        jets[i].phi = -9e20
	leptons[i].pt  = -9e20
        leptons[i].eta = -9e20
        leptons[i].phi = -9e20

    #jets
    for jet in entry.preselected_jets:

        if nJets[0] < 5:
            jets[nJets[0]].pt = jet.obj.Pt()
            jets[nJets[0]].eta = jet.obj.Eta()
            jets[nJets[0]].phi = jet.obj.Phi()
        nJets[0] += 1
	Ht[0] += jet.obj.Pt()

    #leptons
    for lep in entry.preselected_leptons:

        if nLeptons[0] < 5:
            leptons[nLeptons[0]].pt = lep.obj.Pt()
            leptons[nLeptons[0]].eta = lep.obj.Eta()
            leptons[nLeptons[0]].phi = lep.obj.Phi()
        nLeptons[0] += 1
	Ht[0] += lep.obj.Pt()

    outTree.Fill()
    


outTree.Write()
outFile.Close()


