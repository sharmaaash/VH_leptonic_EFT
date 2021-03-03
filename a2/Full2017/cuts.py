# cuts
supercut = 'MinIf$( WH3l_mOSll[], WH3l_mOSll[Iteration$] > 0) > 12 \
            && Alt$(Lepton_pt[0],0)>25 \
            && Alt$(Lepton_pt[1],0)>20 \
            && Alt$(Lepton_pt[2],0)>15 \
            && (nLepton>=3 && Alt$(Lepton_pt[3],0)<10) \
            && abs(WH3l_chlll) == 1 \
           '
cuts['Preselection'] = '1'
'''
cuts['wh3l_13TeV_sssf']  = 'WH3l_flagOSSF == 0\
                            && Alt$( CleanJet_pt[0], 0) < 30 \
                            && Sum$( CleanJet_pt > 20. && abs(CleanJet_eta)<2.5 && Jet_btagDeepB[CleanJet_jetIdx] > 0.6321) == 0\
                       '
cuts['wh3l_13TeV_ossf']  = 'WH3l_flagOSSF == 1\
                            && WH3l_ZVeto > 20\
                            && Alt$( CleanJet_pt[0], 0) < 30 \
                            && PuppiMET_pt > 40 \
                            && Sum$( CleanJet_pt > 20. && abs(CleanJet_eta)<2.5 && Jet_btagDeepB[CleanJet_jetIdx] > 0.6321) == 0\
                       '
cuts['wh3l_wz_13TeV'] = 'WH3l_flagOSSF == 1\
                         && PuppiMET_pt > 45\
                         && WH3l_ZVeto < 20\
                         && WH3l_mlll > 100\
                         && Alt$( CleanJet_pt[0], 0) < 30 \
                         && Sum$( CleanJet_pt > 20. && abs(CleanJet_eta)<2.5 && Jet_btagDeepB[CleanJet_jetIdx] > 0.6321) == 0\
                        '

cuts['wh3l_zg_13TeV'] = 'WH3l_ZVeto < 20\
                         && PuppiMET_pt < 40\
                         && WH3l_mlll > 80\
                         && WH3l_mlll < 100\
                         && Alt$( CleanJet_pt[0], 0) < 30 \
                         && Sum$( CleanJet_pt > 20. && abs(CleanJet_eta)<2.5 && Jet_btagDeepB[CleanJet_jetIdx] > 0.6321) == 0\
                        '
'''
# 11 = e
# 13 = mu
# 15 = tau

