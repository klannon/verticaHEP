#include "variables.h"

vector<ttH::Lepton> get_collection(vector<ttH::Muon> muObjs, vector<ttH::Electron>eleObjs)
{
  vector<ttH::Lepton> lepCollection(muObjs.begin(),muObjs.end());
  lepCollection.insert(lepCollection.end(),eleObjs.begin(),eleObjs.end());
  std::sort(lepCollection.begin(), lepCollection.end(), [] (ttH::Lepton a, ttH::Lepton b) { return a.obj.Pt() > b.obj.Pt();});
  return lepCollection;
}

bool passCommon(vector<ttH::Electron> tightEles, vector<ttH::Electron> psEles, vector<ttH::Muon> tightMus, vector<ttH::Muon> psMus, vector<ttH::Jet> psJets)
{
  auto taggedjetstight = keepTagged(psJets,"M");
  auto taggedjetsloose = keepTagged(psJets,"L");
  
  vector<ttH::Lepton> psLeps = get_collection(psMus,psEles);
  vector<ttH::Lepton> tightLeps = get_collection(tightMus,tightEles);

  //count group by
  if (!( psLeps.size() >3 || tightLeps.size()>1)) return false;
  //find min mass. Isn't the vector sorted? Why not get last entry? b/c sorted on Pt
  double mindilepmass = getTwoObjKineExtreme(psLeps,"min","mass");
  //min   
  //if (!(mindilepmass>12)) return false;
  //psLeps ordered greatest to least? 2 queries 1) select event having max(pt) > 20 2) select event group by event count(select leps where Pt >10) > 2
  if (!(psLeps[0].obj.Pt()>20 /*&& psLeps[1].obj.Pt()>10*/)) return false;
  //count group by        
  if (!((psJets).size()>1)) return false;
  //count group by
  if (!( (taggedjetsloose.size()>1) || (taggedjetstight.size()>0) )) return false;

  return true;
}

bool pass2lss(vector<ttH::Electron> tightEles, vector<ttH::Electron> psEles, vector<ttH::Muon> tightMus, vector<ttH::Muon> psMus, vector<ttH::Jet> psJets, vector<ttH::MET> met)
{
  vector<ttH::Lepton> psLeps = get_collection(psMus,psEles);
  vector<ttH::Lepton> tightLeps = get_collection(tightMus,tightEles);
  
  //count group by || count group by and 3rd psLep pt < 2nd tightLep Pt
  if ( !( (psLeps.size() ==2 && tightLeps.size() == 2) || (psLeps.size() == 3 && tightLeps.size() == 2 && psLeps[2].obj.Pt() < tightLeps[1].obj.Pt() ) ) ) return false;
  //tightLep size = 2 at this point. Same as what I've already done (charge = +/-1?)
  if (tightLeps[0].charge != tightLeps[1].charge) return false;
  //messVar = true for all. select event where count(mess) = sum(mess) group by event? (b/c true is 1)
  for (auto &ele: tightEles) if (!(ele.isGsfCtfScPixChargeConsistent)) return false;
  //min(chargeFlip) < 0.2
  for (auto &mu: tightMus) if (!(mu.chargeFlip < 0.2)) return false;
  //count group by
  if ( !( psJets.size()>3 ) ) return false;

  //need to figure out how to add Tlorentz vecs
  auto objs_for_mht = getsumTLV(psLeps,psJets);
  double MHT_handle = objs_for_mht.Pt();
  //end up with new variable at end. scalar function?
  double metLD_handle = 0.00397*(met[0].obj.Pt()) + 0.00265*MHT_handle;
  //figure out TLorentz 1st
  if ( !(metLD_handle> 0.2) ) return false;
  //tightLeps ordered greatest to least? 2 queries 1) select event having max(pt) > 20 2) select event group by event count(select leps where Pt >10) > 2
  if ( !(tightLeps[0].obj.Pt()>20 && tightLeps[1].obj.Pt()>10) ) return false;
  //max for [0]? 
  if ( !((tightLeps[0].obj.Pt() + tightLeps[1].obj.Pt() + met[0].obj.Pt())>100.) ) return false; 
  //count group by
  if (tightEles.size() ==2 )
    {
      double vetoZmass = pickFromSortedTwoObjKine(psEles,"mass",1,91.2);
      if ( !(fabs(vetoZmass-91.2)>10) ) return false;                     
    }
  return true;
}

bool pass3l(vector<ttH::Electron> tightEles, vector<ttH::Electron> psEles, vector<ttH::Muon> tightMus, vector<ttH::Muon> psMus, vector<ttH::Jet> psJets, vector<ttH::MET> met)
{
  vector<ttH::Lepton> psLeps = get_collection(psMus,psEles);
  vector<ttH::Lepton> tightLeps = get_collection(tightMus,tightEles);
  
  if ( !(tightLeps.size() >= 3) ) return false;

  auto objs_for_mht = getsumTLV(psLeps,psJets);
  double MHT_handle = objs_for_mht.Pt();
  double metLD_handle = 0.00397*(met[0].obj.Pt()) + 0.00265*MHT_handle;
  if ( !(metLD_handle> 0.2 || psJets.size()>3)  ) return false;

  if (psJets.size() < 4)
    {
      if (tightMus.size() == 2)
	{
	  if (tightMus[0].charge != tightMus[1].charge)
	    {
	      if (!(metLD_handle > 0.3)) return false;
	    }
	}
      else if (tightEles.size() == 2)
	{
	  if (tightEles[0].charge != tightEles[1].charge)
	    {
	      if (!(metLD_handle > 0.3)) return false;
	    }
	}
    }

  if ( !(tightLeps[0].obj.Pt()>20 && tightLeps[2].obj.Pt()>10) ) return false;
  double vetoZmass = pickFromSortedTwoObjKine(tightLeps,"massSFOS",1,91.2);
  if ( !(fabs(vetoZmass-91.2)>10) ) return false;                     
  
  return true;
}
