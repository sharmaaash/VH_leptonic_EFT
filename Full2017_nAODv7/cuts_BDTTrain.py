# cuts

supercut = 'MinIf$( WH3l_mOSll[], WH3l_mOSll[Iteration$] > 0) > 12 \
            && Alt$(Lepton_pt[0],0)>25 \
            && Alt$(Lepton_pt[1],0)>15 \
            && Alt$(Lepton_pt[2],0)>10 \
            && (nLepton>=3 && Alt$(Lepton_pt[3],0)<10) \
            && abs(WH3l_chlll) == 1 \
           '
#            && Alt$( CleanJet_pt[0], 0) < 40 \
#            && Sum$( CleanJet_pt > 20. && abs(CleanJet_eta)<2.5 && Jet_btagDeepB[CleanJet_jetIdx] > 0.2217) == 0\
#           '

#cuts['Preselection'] = 1
'''
cuts['wh3l_13TeV_sssf']  = 'WH3l_njet == 0 \
                       && Alt$( CleanJet_pt[0], 0) < 30 \
                       && Sum$( CleanJet_pt > 20. && abs(CleanJet_eta)<2.5 && Jet_btagDeepB[CleanJet_jetIdx] > 0.2217) == 0\
                       && WH3l_dphilllmet > 2.5 \
                       && MinIf$(WH3l_mOSll[], WH3l_mOSll[Iteration$] > 0) < 100\
                       && WH3l_flagOSSF == 0\
                       && nLepton == 3 \
                       '
cuts['wh3l_13TeV_ossf']  = 'WH3l_njet == 0 \
                       && Alt$( CleanJet_pt[0], 0) < 30 \
                       && Sum$( CleanJet_pt[] < 20 || Jet_btagDeepB[CleanJet_jetIdx[]] < 0.2217 ) == nCleanJet  \
                       && WH3l_dphilllmet > 2.2 \
                       && PuppiMET_pt > 50\
                       && WH3l_ZVeto > 25\
                       && MinIf$(WH3l_mOSll[], WH3l_mOSll[Iteration$] > 0) < 100\
                       && WH3l_flagOSSF == 1\
                       && nLepton == 3 \
                       '
cuts['wh3l_13TeV_ossfmtWWW']  = 'WH3l_njet == 0 \
                       && Alt$( CleanJet_pt[0], 0) < 30 \
                       && Sum$( CleanJet_pt[] < 20 || Jet_btagDeepB[CleanJet_jetIdx[]] < 0.2217 ) == nCleanJet  \
                       && WH3l_dphilllmet > 2.2 \
                       && PuppiMET_pt > 50\
                       && WH3l_ZVeto > 25\
                       && MinIf$(WH3l_mOSll[], WH3l_mOSll[Iteration$] > 0) < 100\
                       && WH3l_flagOSSF == 1\
                       && nLepton == 3 \
                       && WH3l_mtWWW > 80\
                       '
cuts['wh3l_13TeV_ossfptlll20']  = 'WH3l_njet == 0 \
                       && Alt$( CleanJet_pt[0], 0) < 30 \
                       && Sum$( CleanJet_pt[] < 20 || Jet_btagDeepB[CleanJet_jetIdx[]] < 0.2217 ) == nCleanJet  \
                       && WH3l_dphilllmet > 2.2 \
                       && PuppiMET_pt > 50\
                       && WH3l_ZVeto > 25\
                       && MinIf$(WH3l_mOSll[], WH3l_mOSll[Iteration$] > 0) < 100\
                       && WH3l_flagOSSF == 1\
                       && WH3l_ptlll > 20\
                       && nLepton == 3 \
                       '
cuts['wh3l_13TeV_ossfptlll40']  = 'WH3l_njet == 0 \
                       && Alt$( CleanJet_pt[0], 0) < 30 \
                       && Sum$( CleanJet_pt[] < 20 || Jet_btagDeepB[CleanJet_jetIdx[]] < 0.2217 ) == nCleanJet  \
                       && WH3l_dphilllmet > 2.2 \
                       && PuppiMET_pt > 50\
                       && WH3l_ZVeto > 25\
                       && MinIf$(WH3l_mOSll[], WH3l_mOSll[Iteration$] > 0) < 100\
                       && WH3l_flagOSSF == 1\
                       && WH3l_ptlll > 40\
                       && nLepton == 3 \
                       '

cuts['wh3l_wz_13TeV'] = 'WH3l_njet == 0\
                         && Sum$(CleanJet_pt > 20. && abs(CleanJet_eta)<2.5 && Jet_btagDeepB[CleanJet_jetIdx] > 0.2217) == 0\
                         && PuppiMET_pt > 45\
                         && WH3l_ZVeto < 20\
                         && WH3l_mlll > 100\
                        '

cuts['wh3l_zg_13TeV'] = 'WH3l_njet == 0\
                         && Sum$(CleanJet_pt > 20. && abs(CleanJet_eta)<2.5 && Jet_btagDeepB[CleanJet_jetIdx] > 0.2217) == 0\
                         && PuppiMET_pt < 40\
                         && WH3l_mlll > 80\
                         && WH3l_mlll < 100\
                        '
'''
# 11 = e
# 13 = mu
# 15 = tau

