# variables

#variables = {}
    
#'fold' : # 0 = not fold (default), 1 = fold underflowbin, 2 = fold overflow bin, 3 = fold underflow and overflow


variables['events']  = {'name'  : '1',
                        'range' : (1,0,2),
                        'xaxis' : 'events',
                        'fold'  : 3
                        }
variables['pt1']  = {   'name': 'Alt$(Lepton_pt[0],0)',            #   variable name    
                        'range' : (10,0.,200),    #   variable range
                        # 'range' : (60,0.,300),    #   variable range
                        'xaxis' : 'lept1_p_{T} [GeV]',  #   x axis name
                         'fold' : 0
                        }

variables['pt2']  = {   'name': 'Alt$(Lepton_pt[1],0)',
                        'range' : (10,0.,200),    #   variable range
                        # 'range' : (40,0.,200),    #   variable range
                        'xaxis' : 'lept2_p_{T} [GeV]',  #   x axis name
                         'fold' : 0
                        }

variables['pt3']  = {   'name': 'Alt$(Lepton_pt[2],0)',
                        # 'range' : (40,0.,200),    #   variable range
                        'range' : (7,0.,100),    #   variable range
                       'xaxis' : 'lept3_p_{T} [GeV]',  #   x axis name
                        'fold' : 0
                       }

variables['WH3l_drOSll_min']  = {   'name': 'MinIf$( WH3l_drOSll[], WH3l_drOSll[Iteration$] > 0)',
                         'range' : ([0.,0.75,1.0,1.25,1.5,1.75,2.5,4.0],),    #   variable range
                         'xaxis' : 'min #Delta R_{ll}',  #   x axis name
                         'fold' : 0
                        }

variables['BDTG_OSSF'] = { 'name': 'hww_WH3l_OSSF_mvaBDTG(Entry$,0)',
                        'range' : ([-1.0,-0.5,0.,0.3,0.45,0.6,0.7,0.8,0.85,0.9,0.95,1.0],),    #   variable range
                        'xaxis' : 'MVA discriminant',
                        'fold' : 3,
                        'linesToAdd' : ['.L %s/src/PlotsConfigurations/Configurations/EFT/WH3l/BDT_analysis/BDT_config/v7/Full2017/hww_WH3l_OSSF_mvaBDTG.C+' % os.getenv('CMSSW_BASE')]
                      }

variables['BDTG_OSSF_10bin'] = { 'name': 'hww_WH3l_OSSF_mvaBDTG(Entry$,0)',
                        'range' : (10,-1,1),
                        'xaxis' : 'MVA discriminant',
                        'fold' : 3,
                        'linesToAdd' : ['.L %s/src/PlotsConfigurations/Configurations/EFT/WH3l/BDT_analysis/BDT_config/v7/Full2017/hww_WH3l_OSSF_mvaBDTG.C+' % os.getenv('CMSSW_BASE')] 
                       }

variables['BDTG_OSSF_20bin'] = { 'name': 'hww_WH3l_OSSF_mvaBDTG(Entry$,0)',
                        'range' : (20,-1,1),
                        'xaxis' : 'MVA discriminant',
                        'fold' : 3,
                      'linesToAdd' : ['.L %s/src/PlotsConfigurations/Configurations/EFT/WH3l/BDT_analysis/BDT_config/v7/Full2017/hww_WH3l_OSSF_mvaBDTG.C+' % os.getenv('CMSSW_BASE')] 
                       }


