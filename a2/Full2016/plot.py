# plot configuration



# groupPlot = {}
# 
# Groups of samples to improve the plots.
# If not defined, normal plots is used
#
groupPlot['WH_hww']  = {  
                  'nameHR' : 'WH',
                  'isSignal' : 0,
                  'color': 400, # kRed 
		  #'samples'  : ['H_htt', 'H_hww', 'ZH_hww', 'ggZH_hww', 'WH_hww', 'qqH_hww', 'ggH_hww','bbH_hww','ttH_hww','ZH_htt', 'ggZH_htt', 'WH_htt', 'qqH_htt', 'ggH_htt','bbH_htt','ttH_htt' ]
                  'samples'  : ['WH_hww']
              }

groupPlot['WH_hww_zeroplus']  = {
                      'nameHR' : 'WH 0^{+}',
                      'color' : 632+1,
                      'isSignal' : 1,
                      'samples'  : ['WH_hww_zeroplus']
                    }

groupPlot['TTbar']  = {
                  'nameHR' : 'tW and t#bart',
                  'isSignal' : 0,
                  'color': 401,   # kYellow+1
                  'samples'  : ['TTbar']
              }
groupPlot['DY']  = {
                  'nameHR' : 'DY',
                  'isSignal' : 0,
                  'color': 635,    # kGreen+3
                  'samples'  : ['DY']
              }
groupPlot['WW']  = {
                  'nameHR' : 'WW',
                  'isSignal' : 0,
                  'color': 431,    # kGreen+3
                  'samples'  : ['WW']
              }
plot['WW']  = {
                  'color': 431,
                  'isSignal' : 0,
                  'isData'   : 0,
                  'scale'    : 1,
                 }
plot['DY']  = {
                  'color': 635,
                  'isSignal' : 0,
                  'isData'   : 0,
                  'scale'    : 1,
                 }
plot['TTbar']  = {
                  'color': 401,
                  'isSignal' : 0,
                  'isData'   : 0,
                  'scale'    : 1,
                 }

groupPlot['WH_hww_mixzeroplus']  = {
                      'nameHR' : 'WH h-0^{+} Int',
                      'color' : 632,
                      'isSignal' : 1,
                      'samples'  : ['WH_hww_mixzeroplus']
                    }
plot['WH_hww_zeroplus']  = {
                      'color' : 632+1,
                      'isSignal' : 1,
                      'isData'   : 0,
                      'scale'    : 1.0
                    } 
plot['WH_hww_mixzeroplus']  = {
                      'color' : 632,
                      'isSignal' : 1,
                      'isData'   : 0,
                      'scale'    : 1.0
                    }


plot['WH_hww'] = {
                  'nameHR' : 'WH',
                  'color': 400, # kRed+2 
                  'isSignal' : 0,
                  'isData'   : 0,    
                  'scale'    : 1    #
                  }




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

legend['lumi'] = 'L = 35.9/fb'

legend['sqrt'] = '#sqrt{s} = 13 TeV'




