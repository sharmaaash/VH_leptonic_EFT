# preselections

preselections = {}

#preselections['ALL']  = "\
#    WH3l_flagOSSF == 0 || WH3l_flagOSSF == 1\
#"

# preselections['SSSF']  = "\
    # Alt$(Lepton_pt[0],0)>25 \
    # && Alt$(Lepton_pt[1],0)>15 \
    # && Alt$(Lepton_pt[2],0)>10 \
    # && (nLepton>=3 && Alt$(Lepton_pt[3],0)<10) \
    # && abs(WH3l_chlll) == 1 \
    # && WH3l_flagOSSF == 0\
    # && Alt$( CleanJet_pt[0], 0) < 40 \
# "
# preselections['SSSF']  = "\
    # Alt$(Lepton_pt[0],0)>25 \
    # && Alt$(Lepton_pt[1],0)>20 \
    # && Alt$(Lepton_pt[2],0)>15 \
    # && (nLepton>=3 && Alt$(Lepton_pt[3],0)<10) \
    # && abs(WH3l_chlll) == 1 \
    # && WH3l_flagOSSF == 0\
# "

# preselections['OSSF']  = "\
    # WH3l_flagOSSF == 1\
# "

# preselections['OSSF']  = "\
    # WH3l_flagOSSF == 1\
# "
'''
preselections['SSSF']  = 'WH3l_flagOSSF == 0\
                            && Alt$( CleanJet_pt[0], 0) < 30 \
                            && Sum$( CleanJet_pt > 20. && abs(CleanJet_eta)<2.5 && Jet_btagDeepB[CleanJet_jetIdx] > 0.2217) == 0\
                            && MinIf$( WH3l_mOSll[], WH3l_mOSll[Iteration$] > 0) > 12\
                            && Alt$(Lepton_pt[0],0)>25 \
                            && Alt$(Lepton_pt[1],0)>20 \
                            && Alt$(Lepton_pt[2],0)>15 \
                            && (nLepton>=3 && Alt$(Lepton_pt[3],0)<10) \
                            && abs(WH3l_chlll) == 1 \
                       '
'''
# preselections['OSSF']  = 'WH3l_flagOSSF == 1\
                            # && WH3l_ZVeto > 20\
                            # && Alt$( CleanJet_pt[0], 0) < 30 \
                            # && Sum$( CleanJet_pt > 20. && abs(CleanJet_eta)<2.5 && Jet_btagDeepB[CleanJet_jetIdx] > 0.2217) == 0\
                            # && MinIf$( WH3l_mOSll[], WH3l_mOSll[Iteration$] > 0) > 12\
                            # && Alt$(Lepton_pt[0],0)>25 \
                            # && Alt$(Lepton_pt[1],0)>20 \
                            # && Alt$(Lepton_pt[2],0)>15 \
                            # && (nLepton>=3 && Alt$(Lepton_pt[3],0)<10) \
                            # && abs(WH3l_chlll) == 1 \
                       # '
preselections['all']  = 'Alt$( CleanJet_pt[0], 0) < 30 \
                            && Sum$( CleanJet_pt > 20. && abs(CleanJet_eta)<2.5 && Jet_btagDeepB[CleanJet_jetIdx] > 0.2217) == 0\
                            && MinIf$( WH3l_mOSll[], WH3l_mOSll[Iteration$] > 0) > 12\
                            && Alt$(Lepton_pt[0],0)>25 \
                            && Alt$(Lepton_pt[1],0)>20 \
                            && Alt$(Lepton_pt[2],0)>15 \
                            && (nLepton>=3 && Alt$(Lepton_pt[3],0)<10) \
                            && abs(WH3l_chlll) == 1 \
                       '
