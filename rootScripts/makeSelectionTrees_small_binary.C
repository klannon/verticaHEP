//Charlie Mueller 2/24/2016
#include <iostream>
#include "TSystem.h"
#include <vector>
#include "TH1.h"
#include "TChain.h"
#include <string>
#include "TString.h"
#include "TH1D.h"
#include "TFile.h"
#include <cmath>
#include "TLorentzVector.h"
#include "ttH-13TeVMultiLeptons/TemplateMakers/src/classes.h"
#include "TMVA/Config.h"
#include "TMVA/Tools.h"
#include "TMVA/Reader.h"
#include "TMVA/MethodCuts.h"
#include "selection.h"
//#include "loadSamples.h"
#include <fstream>
#include <time.h>

/////////////////////////////////////////
///
/// usage: root -l makeSelectionTrees.C+
///
/////////////////////////////////////////


void run_it(TChain* chain, TString output_file)
{

  double startAddress = get_wall_time();
  int chainentries = chain->GetEntries();   
  cout << "# events in tree: "<< chainentries << endl;  

  //int passCommonCount = 0;
  
  double mcwgt_intree = -999.;
  double wgt_intree = -999.;
  double wallTimePerEvent_intree = -99.;  
  int eventnum_intree = -999;
  int higgs_decay_intree = -9999;
  int lumiBlock_intree = -999;
  int runNumber_intree = -999;
  
  vector<ttH::Lepton> *preselected_leptons_intree=0;
  //vector<ttH::Electron> *raw_electrons_intree=0;               
  vector<ttH::Electron> *preselected_electrons_intree=0;
  //vector<ttH::Muon> *raw_muons_intree=0;
  vector<ttH::Muon> *preselected_muons_intree=0;
  vector<ttH::Jet> *preselected_jets_intree=0;
  vector<ttH::MET> *met_intree=0;
  vector<ttH::GenParticle> *pruned_genParticles_intree=0;
  vector<ttH::Lepton> *tight_leptons_intree=0;
  vector<ttH::Electron> *tight_electrons_intree=0;
  vector<ttH::Muon> *tight_muons_intree=0;
  //vector<ttH::Lepton> *tight_leptons_sortedByMiniIso_intree=0;  
  

  chain->SetBranchAddress("mcwgt", &mcwgt_intree);
  chain->SetBranchAddress("wgt", &wgt_intree);
  chain->SetBranchAddress("wallTimePerEvent", &wallTimePerEvent_intree);
  chain->SetBranchAddress("eventnum", &eventnum_intree);
  chain->SetBranchAddress("lumiBlock", &lumiBlock_intree);
  chain->SetBranchAddress("runNumber", &runNumber_intree);
  chain->SetBranchAddress("higgs_decay", &higgs_decay_intree);
  chain->SetBranchAddress("preselected_leptons", &preselected_leptons_intree);

  chain->SetBranchAddress("preselected_electrons", &preselected_electrons_intree);
  chain->SetBranchAddress("preselected_muons", &preselected_muons_intree);

  chain->SetBranchAddress("tightMvaBased_leptons", &tight_leptons_intree);
  chain->SetBranchAddress("tightMvaBased_electrons", &tight_electrons_intree);
  chain->SetBranchAddress("tightMvaBased_muons", &tight_muons_intree);    
  chain->SetBranchAddress("preselected_jets", &preselected_jets_intree);
  chain->SetBranchAddress("met", &met_intree);
  chain->SetBranchAddress("pruned_genParticles", &pruned_genParticles_intree); 

  chain->SetBranchStatus("*", 0);  

  double addressTime = get_wall_time() - startAddress;
  //double num_fake_jets_intree = 0.;
  int numEntries = 0;
  int numTightMu = 0;
  int numTightElec = 0;
  int numEvent = 0;
  vector<ttH::Electron> tightElec;
  vector<ttH::Muon> tightMu;
  TFile *copiedfile = new TFile(output_file, "RECREATE"); //"UPDATE"); // #, 'test' ) // "RECREATE");
  // TTree *three_lep_tree = (TTree*)chain->CloneTree(0);
  // three_lep_tree->SetName("threelep_tree");
  // three_lep_tree->Branch("lepTop_score", &lepTop_BDT_intree);
  // three_lep_tree->Branch("bJet", &bJet_intree);
  // three_lep_tree->Branch("lep", &lepton_intree);
  // three_lep_tree->Branch("isLepTopPresent", &isLepTopPresent_intree);
  // three_lep_tree->Branch("isCorrectLepTopMatch", &correctLepTopMatch_intree);

/*
  TTree *two_lep_tree = (TTree*)chain->CloneTree(0);
  two_lep_tree->SetName("ss2l_tree");
  two_lep_tree->Branch("num_fake_jets", &num_fake_jets_intree);
*/

  chain->SetBranchStatus("preselected_muons*", 1);
  chain->SetBranchStatus("preselected_electrons*", 1);
  chain->SetBranchStatus("preselected_jets*", 1);
  chain->SetBranchStatus("met*", 1);

  TTree *event_selection_tree = (TTree*)chain->CloneTree(0);
  event_selection_tree->SetName("eventSelection_tree");

  TTree *object_selection_tree = new TTree("object selection", "objects after skimming");
  object_selection_tree->SetName("objectSelection_tree");
  object_selection_tree->Branch("tightMuons", &tightMu);
  object_selection_tree->Branch("tightElectrons", &tightElec);
  
  Int_t cachesize = 250000000;   //250 MBytes
  chain->SetCacheSize(cachesize);
  chain->SetCacheLearnEntries(20); 
  
  double starttime = get_wall_time();
  //time_t start,end;
  //time (&start);
  //  chainentries = 100000;
/*
  chain->SetBranchStatus("preselected_muons*", 1);
  chain->SetBranchStatus("preselected_electrons*", 1);
  chain->SetBranchStatus("preselected_jets*", 1);
  chain->SetBranchStatus("met*", 1);
*/
  for (int i=0; i<chainentries; i++)
    {
      
      if (i%10000 == 0)
	{
	  float fraction = 100.*i/chainentries;
	  cout << fraction << " % complete" << endl;
	  cout << i << endl;
	}
      chain->GetEntry(i);

      //////////////////////////
      ////
      //// selection, vetos etc
      ////
      //////////////////////////

      //      if ( (*preselected_jets_intree).size() < 3) continue; 
      //bool passesCommon = passCommon(*tight_electrons_intree, *preselected_electrons_intree, *tight_muons_intree, *preselected_muons_intree, *preselected_jets_intree);
      //if (!passesCommon) continue;
      //bool passes2lss = pass2lss(*tight_electrons_intree, *preselected_electrons_intree, *tight_muons_intree, *preselected_muons_intree, *preselected_jets_intree, *met_intree);
      // bool passes3l = pass3l(*tight_electrons_intree, *preselected_electrons_intree, *tight_muons_intree, *preselected_muons_intree, *preselected_jets_intree, *met_intree);
      // if ( !(passes2lss || passes3l) ) continue;

      //////////////////////////
      ////
      //// calculation of new vars etc
      ////
      //////////////////////////
      //num_fake_jets_intree = 0.;
      double segCom = 0.;
      for (const auto & muon : *preselected_muons_intree)
	{
	  if (muon.validFrac >= 0.8 && muon.lepMVA > 0.75) {

	     if (muon.isGlobalMuon && muon.normalizedChi2 < 3 && muon.localChi2 < 12 && muon.trKink < 20) {
 		segCom = 0.303;
	     } else { segCom = 0.451;}

	     if (muon.segCompatibility > segCom){
	        numEntries += 1;
		tightMu.push_back(muon);
	     }
	  } 
	}

      for (const auto & elec : *preselected_electrons_intree) {

         if (elec.lepMVA > 0.75 && elec.numMissingInnerHits == 0 && elec.passConversioVeto){ //used for event selection
         //if (elec.lepMVA > 0.75 ){
 	    numEntries += 1;
	    tightElec.push_back(elec);
	 }
      }

      bool passesCommon = passCommon(tightElec, *preselected_electrons_intree, tightMu, *preselected_muons_intree, *preselected_jets_intree);
      bool passes2lss = pass2lss(tightElec, *preselected_electrons_intree, tightMu, *preselected_muons_intree, *preselected_jets_intree, *met_intree);

      numTightMu += tightMu.size();
      numTightElec += tightElec.size();
      //passCommonCount += 1;

      if (passesCommon && passes2lss){
         event_selection_tree->Fill();
	 numEvent +=1;
      }

      //if ( passes2lss ) two_lep_tree->Fill();
      //      else if ( passes3l ) three_lep_tree->Fill();

      object_selection_tree->Fill();

      tightElec.erase(tightElec.begin(), tightElec.end() );
      tightMu.erase(tightMu.begin(), tightMu.end() );
    }
  
  
  double endtime = get_wall_time();
  //time (&end);
  //double dif = difftime (end,start);
  double totalLoop = endtime - starttime;
  cout << "Address time: " << addressTime << endl;
  cout << "Loop time: " << totalLoop << " seconds, " << endl;
  if (chainentries>0) cout << "an average of " << totalLoop / chainentries << " per event." << endl;
  cout << "numEntries: " << numEntries << endl;
  cout << "event selection: " << numEvent << endl;
  
  //  three_lep_tree->Write();
  object_selection_tree->Write();
  event_selection_tree->Write();
  copiedfile->Close();

}

void makeSelectionTrees_small(void)
{

  // TChain *tth_chain = loadFiles("ttH");  
  // run_it(tth_chain,"ttH_lepTopBDTResults.root");

  double totStart = get_wall_time();
  TString output_file = "skimSelection.root";
  TChain *chain = new TChain("OSTwoLepAna/summaryTree");
  //chain->Add("/tmpscratch/users/mlink2/rootFiles/charlie_tree_11503.root");
/*
  chain->Add("/hadoop/store/user/lannon/bdtreco_v0/tth_nonbb/charlie_tree_11503.root");
  chain->Add("/hadoop/store/user/lannon/bdtreco_v0/tth_nonbb/charlie_tree_21176.root");

  chain->Add("/hadoop/store/user/lannon/bdtreco_v0/tth_nonbb/charlie_tree_30640.root");
  chain->Add("/hadoop/store/user/lannon/bdtreco_v0/ttjets_semilep/charlie_tree_10640.root");
  chain->Add("/hadoop/store/user/lannon/bdtreco_v0/ttjets_semilep/charlie_tree_11504.root");
  chain->Add("/hadoop/store/user/lannon/bdtreco_v0/ttjets_semilep/charlie_tree_12183.root");
  chain->Add("/hadoop/store/user/lannon/bdtreco_v0/ttjets_semilep/charlie_tree_13130.root");
  chain->Add("/hadoop/store/user/lannon/bdtreco_v0/ttjets_semilep/charlie_tree_13381.root");
*/

  chain->Add("/hadoop/store/user/lannon/bdtreco_v0/ttjets_semilep/charlie_tree_10640.root");
  chain->Add("/hadoop/store/user/lannon/bdtreco_v0/ttjets_semilep/charlie_tree_11504.root");
  chain->Add("/hadoop/store/user/lannon/bdtreco_v0/ttjets_semilep/charlie_tree_12183.root");
  chain->Add("/hadoop/store/user/lannon/bdtreco_v0/ttjets_semilep/charlie_tree_13130.root");
  chain->Add("/hadoop/store/user/lannon/bdtreco_v0/ttjets_semilep/charlie_tree_13381.root");
  chain->Add("/hadoop/store/user/lannon/bdtreco_v0/ttjets_semilep/charlie_tree_14553.root");
  chain->Add("/hadoop/store/user/lannon/bdtreco_v0/ttjets_semilep/charlie_tree_15205.root");
  chain->Add("/hadoop/store/user/lannon/bdtreco_v0/ttjets_semilep/charlie_tree_16058.root");

/*
  std::ifstream infile("files_forSelection_ttjet.txt");
  TString line;
  while (infile >> line ){
     chain->Add(line );
     cout << line << endl;
  }
*/
  double chainTime = get_wall_time() - totStart;
  run_it(chain,output_file);
  double totEnd = get_wall_time();
  double totalTime = totEnd - totStart;

  cout << "total time: " << totalTime << endl;
  cout << "chain time: " << chainTime << endl; 



  // TChain *ttw_chain = loadFiles("ttW");
  // TChain *ttbar_chain = loadFiles("ttbar");

}

int main(int argc, char** argv){

makeSelectionTrees_small();

}
