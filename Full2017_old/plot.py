# plot configuration



# groupPlot = {}
# 
# Groups of samples to improve the plots.
# If not defined, normal plots is used
#
#'''
#groupPlot['top']  = {  
#                  'nameHR' : 'tW and t#bar{t}',
#                  'isSignal' : 0,
#                  'color': 400,   # kYellow
#                  'samples'  : ['top']
#              }

#groupPlot['WW']  = {  
#                  'nameHR' : 'WW',
#                  'isSignal' : 0,
#                  'color': 400, # kAzure -9 
#                  'samples'  : ['WW', 'ggWW', 'WWewk']
#              }

#groupPlot['Fake']  = {  
#                  'nameHR' : 'Non-prompt',
#                  'isSignal' : 0,
#                  'color': 921,    # kGray + 1
#                  'samples'  : ['Fake_em','Fake_me']
#              }


#groupPlot['DY']  = {  
#                  'nameHR' : 'DY',
#                  'isSignal' : 0,
#                  'color': 418,    # kGreen+2
#                  'samples'  : ['DY']
#              }



#groupPlot['VVV']  = {  
#                  'nameHR' : 'VVV',
#                  'isSignal' : 0,
#                  'color': 857, # kAzure -3  
#                  'samples'  : ['VVV']
#              }

'''
groupPlot['VZ']  = {  
                  'nameHR' : 'VZ',
                  'isSignal' : 0,
                  'color'    : 617,   # kViolet + 1  
                  'samples'  : ['VZ']
              }
'''
#groupPlot['Vg']  = {  
#                  'nameHR' : "V#gamma",
#                  'isSignal' : 0,
#                  'color'    : 810,   # kOrange + 10
#                  'samples'  : ['Vg']
#              }

#groupPlot['VgS']  = {
#                  'nameHR' : "V#gamma*",
#                  'isSignal' : 0,
#                  'color'    : 409,   # kGreen - 9
#                  'samples'  : ['VgS_L','VgS_H']
#              }


#'''
groupPlot['WH_hww']  = {  
                  'nameHR' : 'WH',
                  'isSignal' : 0,
                  'color': 400, # kRed 
		  #'samples'  : ['H_htt', 'H_hww', 'ZH_hww', 'ggZH_hww', 'WH_hww', 'qqH_hww', 'ggH_hww','bbH_hww','ttH_hww','ZH_htt', 'ggZH_htt', 'WH_htt', 'qqH_htt', 'ggH_htt','bbH_htt','ttH_htt' ]
                  'samples'  : ['WH_hww']
              }


#groupPlot['ggH_hww_ALT']  = {
#                      'nameHR' : 'ggH_ALT',
#                      'color' : 851,
#                      'isSignal' : 1,
#                      'samples'  : ['ggH_hww_ALT']
#                    }
#groupPlot['qqH_hww_ALT']  = {
#                      'nameHR' : 'qqH_ALT',
#                      'color' : 617,
#                      'isSignal' : 1,
#                      'samples'  : ['qqH_hww_ALT']
#                    }

'''
groupPlot['WH_hww_zerominus']  = {
                      'nameHR' : 'WH 0^{-}',
                      'color' : 632,
                      'isSignal' : 1,
                      'samples'  : ['WH_hww_zerominus']
                    }

groupPlot['WH_hww_zeroplus']  = {
                      'nameHR' : 'WH 0{+}',
                      'color' : 632+1,
                      'isSignal' : 1,
                      'samples'  : ['WH_hww_zeroplus']
                    }

groupPlot['WH_hww_zerolambda']  = {
                      'nameHR' : 'WH 0^{#Lambda 1}',
                      'color' : 632+5,
                      'isSignal' : 1,
                      'samples'  : ['WH_hww_zerolambda']
                    }
'''
groupPlot['WH_hww_mixzerominus']  = {
                      'nameHR' : 'WH h-0^{-} Int',
                      'color' : 632+6,
                      'isSignal' : 1,
                      'samples'  : ['WH_hww_mixzerominus']
                    }
'''
groupPlot['WH_hww_mixzeroplus']  = {
                      'nameHR' : 'WH h-0^{+} Int',
                      'color' : 632+3,
                      'isSignal' : 1,
                      'samples'  : ['WH_hww_mixzeroplus']
                    }

groupPlot['WH_hww_mixzerolambda']  = {
                      'nameHR' : 'WH h-0^{#Lambda 1} Int',
                      'color' : 632+4,
                      'isSignal' : 1,
                      'samples'  : ['WH_hww_mixzerolambda']
                    }
'''
#plot = {}

# keys here must match keys in samples.py    
# 
#''
#plot['ggH_hww_0PH']  = {
#                      'nameHR' : 'ggH0PH', 
#                      'color' : 999,
#                      'isSignal' : 1,
#                      'isData'   : 0,
#                      'scale'    : 1 
#                    }

#plot['qqH_hww_0PH']  = {
#                      'nameHR' : 'qqH0PH',
#                      'color' : 617,
#                      'isSignal' : 1,
#                      'isData'   : 0,
#                      'scale'    : 1
#                    }

#'''
#plot['ggH_hww_ALT']  = {
#                      'color' : 851,
#                      'isSignal' : 1,
#                      'isData'   : 0,
#                      'scale'    : 1.0 
#                    }

#plot['qqH_hww_ALT']  = {
#                      'color' : 617,
#                      'isSignal' : 1,
#                      'isData'   : 0,
#                      'scale'    : 1.0
#                    }
#

'''
plot['WH_hww_zerominus']  = {
                      'color' : 632,
                      'isSignal' : 1,
                      'isData'   : 0,
                      'scale'    : 1.0
                    }
plot['WH_hww_zeroplus']  = {
                      'color' : 632+1,
                      'isSignal' : 1,
                      'isData'   : 0,
                      'scale'    : 1.0
                    } 

plot['WH_hww_zerolambda']  = {
                      'color' : 632+5,
                      'isSignal' : 1,
                      'isData'   : 0,
                      'scale'    : 1.0
                    }
'''
plot['WH_hww_mixzerominus']  = {
                      'color' : 632+6,
                      'isSignal' : 1,
                      'isData'   : 0,
                      'scale'    : 1.0
                    }
'''
plot['WH_hww_mixzeroplus']  = {
                      'color' : 632+3,
                      'isSignal' : 1,
                      'isData'   : 0,
                      'scale'    : 1.0
                    }

plot['WH_hww_mixzerolambda']  = {
                      'color' : 632+4,
                      'isSignal' : 1,
                      'isData'   : 0,
                      'scale'    : 1.0
                    }
#'''                   
#plot['DY']  = {  
#                  'color': 418,    # kGreen+2
#                  'isSignal' : 0,
#                  'isData'   : 0, 
#                  'scale'    : 1.0,
#                  #'cuts'  : {
#                       #'hww2l2v_13TeV_of0j'      : 0.95 ,
#                       #'hww2l2v_13TeV_top_of0j'  : 0.95 , 
#                       #'hww2l2v_13TeV_dytt_of0j' : 0.95 ,
#                       #'hww2l2v_13TeV_em_0j'     : 0.95 , 
#                       #'hww2l2v_13TeV_me_0j'     : 0.95 , 
#                       ##
#                       #'hww2l2v_13TeV_of1j'      : 1.08 ,
#                       #'hww2l2v_13TeV_top_of1j'  : 1.08 , 
#                       #'hww2l2v_13TeV_dytt_of1j' : 1.08 ,
#                       #'hww2l2v_13TeV_em_1j'     : 1.08 , 
#                       #'hww2l2v_13TeV_me_1j'     : 1.08 , 
#                        #},

#              }


#plot['Fake_em']  = {  
#                  'color': 921,    # kGray + 1
#                  'isSignal' : 0,
#                  'isData'   : 0,
#                  'scale'    : 1.0                  
#              }


#plot['Fake_me']  = {  
#                  'color': 921,    # kGray + 1
#                  'isSignal' : 0,
#                  'isData'   : 0,
#                  'scale'    : 1.0                  
#              }

              
#plot['top'] = {   
#                  'color': 400,   # kYellow
#                  'isSignal' : 0,
#                  'isData'   : 0, 
#                  'scale'    : 1.0,
#                  #'cuts'  : {
                       #'hww2l2v_13TeV_of0j'      : 0.94 ,
                       #'hww2l2v_13TeV_top_of0j'  : 0.94 , 
                       #'hww2l2v_13TeV_dytt_of0j' : 0.94 ,
                       #'hww2l2v_13TeV_em_0j'     : 0.94 , 
                       #'hww2l2v_13TeV_me_0j'     : 0.94 , 
                       ##
                       #'hww2l2v_13TeV_of1j'      : 0.86 ,
                       #'hww2l2v_13TeV_top_of1j'  : 0.86 , 
                       #'hww2l2v_13TeV_dytt_of1j' : 0.86 ,
                       #'hww2l2v_13TeV_em_1j'     : 0.86 , 
                       #'hww2l2v_13TeV_me_1j'     : 0.86 , 
                        #},
#                  }
'''

plot['WW']  = {
                  'color': 400, # kAzure -9 
                  'isSignal' : 0,
                  'isData'   : 0,    
                  'scale'    : 1.0   # ele/mu trigger efficiency   datadriven
                  }

#plot['ggWW']  = {
#                  'color': 850, # kAzure -10
#                  'isSignal' : 0,
#                  'isData'   : 0,    
#                  'scale'    : 1.0
#                  }

#plot['WWewk']  = {
#                  'color': 851, # kAzure -9 
#                  'isSignal' : 0,
#                  'isData'   : 0,
#                  'scale'    : 1.0   # ele/mu trigger efficiency   datadriven
#                  }


#plot['Vg']  = { 
#                  'color': 859, # kAzure -1  
#                  'isSignal' : 0,
#                  'isData'   : 0,
#                  'scale'    : 1.0
#                  }


#plot['VgS_L'] = {
#                  'color'    : 409,   # kViolet + 1  
#                  'isSignal' : 0,
#                  'isData'   : 0,
#                  'scale'    : 1.0
#                  }

#plot['VgS_H'] = {
#                  'color'    : 409,   # kViolet + 1  
#                  'isSignal' : 0,
#                  'isData'   : 0,
#                  'scale'    : 1.0
#                  }

plot['VZ']  = { 
                  'color': 858, # kAzure -2  
                  'isSignal' : 0,
                  'isData'   : 0,
                 'scale'    : 1.0
                  }
'''
#plot['VVV']  = { 
#                  'color': 857, # kAzure -3  
#                  'isSignal' : 0,
#                  'isData'   : 0,
#                  'scale'    : 1.0
#                  }
#'''
# Htautau

#plot['H_htt'] = {
#                  'nameHR' : 'Htt',
#                  'color': 632+4, # kRed+4 
#                  'isSignal' : 0,
#                  'isData'   : 0,    
#                  'scale'    : 1    #
#                  }


#plot['ZH_htt'] = {
#                  'nameHR' : 'ZHtt',
#                  'color': 632+3, # kRed+3 
#                  'isSignal' : 1,
#                  'isData'   : 0,    
#                  'scale'    : 1    #
#                  }

#plot['bbH_htt'] = {
#                  'nameHR' : 'bbHtt',
#                  'color': 632-1, # kRed-1 
#                  'isSignal' : 1,
#                  'isData'   : 0,
#                  'scale'    : 1    #
#                  }
#
#plot['ttH_htt'] = {
#                  'nameHR' : 'bbHtt',
#                  'color': 632-2, # kRed-1 
#                  'isSignal' : 1,
#                  'isData'   : 0,
#                  'scale'    : 1    #
#                  }
#
#
#plot['ggZH_htt'] = {
#                  'nameHR' : 'ggZHtt',
#                  'color': 632+4, # kRed+4
#                  'isSignal' : 1,
#                  'isData'   : 0,    
#                  'scale'    : 1    #
#                  }
#
#plot['WH_htt'] = {
#                  'nameHR' : 'WHtt',
#                  'color': 632+2, # kRed+2 
#                  'isSignal' : 1,
#                  'isData'   : 0,    
#                  'scale'    : 1    #
#                  }
#
#
#plot['qqH_htt'] = {
#                  'nameHR' : 'qqHtt',
#                  'color': 632+1, # kRed+1 
#                  'isSignal' : 1,
#                  'isData'   : 0,    
#                  'scale'    : 1    #
#                  }
#
#
#plot['ggH_htt'] = {
#                  'nameHR' : 'ggHtt',
#                  'color': 632, # kRed 
#                  'isSignal' : 1,
#                  'isData'   : 0,    
#                  'scale'    : 1    #
#                  }
#
# HWW 

#plot['H_hww'] = {
#                  'nameHR' : 'Hww',
#                  'color': 632, # kRed 
#                  'isSignal' : 1,
#                  'isData'   : 0,    
#                  'scale'    : 1    #
#                  }


#plot['ggZH_hww'] = {
#                  'nameHR' : 'ggZH',
#                  'color': 632+4, # kRed+4
#                  'isSignal' : 0,
#                  'isData'   : 0,    
#                  'scale'    : 1    #
#                  }

plot['WH_hww'] = {
                  'nameHR' : 'WH',
                  'color': 400, # kRed+2 
                  'isSignal' : 0,
                  'isData'   : 0,    
                  'scale'    : 1    #
                  }


#plot['qqH_hww'] = {
#                  'nameHR' : 'qqH',
#                  'color': 632+1, # kRed+1 
#                  'isSignal' : 0,
#                  'isData'   : 0,    
#                  'scale'    : 1    #
#                  }


#plot['ggH_hww'] = {
#                  'nameHR' : 'ggH',
#                  'color': 632, # kRed 
#                  'isSignal' : 0,
#                  'isData'   : 0,    
#                  'scale'    : 1    #
#                  }

#plot['bbH_hww'] = {
#                  'nameHR' : 'bbH',
#                  'color': 632+5, # kRed+5 
#                  'isSignal' : 1,
#                  'isData'   : 0,
#                  'scale'    : 1    #
#                  }

#plot['ttH_hww'] = {
#                  'nameHR' : 'ttH',
#                  'color': 632+6, # kRed+6
#                  'isSignal' : 0,
#                  'isData'   : 0,
#                  'scale'    : 1    #
#                  }


# data
'''
plot['DATA']  = { 
                  'nameHR' : 'Data',
                  'color': 1 ,  
                  'isSignal' : 0,
                  'isData'   : 1 ,
                  'isBlind'  : 1
              }

'''


# additional options

legend['lumi'] = 'L = 41.5/fb'

legend['sqrt'] = '#sqrt{s} = 13 TeV'




