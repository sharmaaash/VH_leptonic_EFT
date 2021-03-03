# plot configuration



# groupPlot = {}
# 
# Groups of samples to improve the plots.
# If not defined, normal plots is used
#


#'''
groupPlot['WH_hww']  = {  
                  'nameHR' : 'WH',
                  'isSignal' : 0,
                  'color': 400, # kRed 
                  'samples'  : ['WH_hww']
              }

groupPlot['WH_hww_zeroplus']  = {
                      'nameHR' : 'WH h-0^{+}',
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
                  'color': 636,    # kGreen+3
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
                  'color': 636,
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
                      'color' : 632+3,
                      'isSignal' : 1,
                      'samples'  : ['WH_hww_mixzeroplus']
                    }
#plot = {}


plot['WH_hww_zeroplus']  = {
                      'color' : 632+1,
                      'isSignal' : 1,
                      'isData'   : 0,
                      'scale'    : 1.0
                    } 
plot['WH_hww_mixzeroplus']  = {
                      'color' : 635,
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

legend['lumi'] = 'L = 59.74/fb'

legend['sqrt'] = '#sqrt{s} = 13 TeV'




