# structure configuration for datacard

structure = {}

# keys here must match keys in samples.py    
#
structure['WH_hww_zerominus16'] = {
                  'isSignal' : 1,
                  'isData'   : 0
                  }

structure['WH_hww_zerominus17'] = {
                  'isSignal' : 1,
                  'isData'   : 0
                  }

structure['WH_hww_zerominus18'] = {
                  'isSignal' : 1,
                  'isData'   : 0
                  }

structure['WH_hww16'] = {
                  'isSignal' : 0,
                  'isData'   : 0
                  }

structure['WH_hww17'] = {
                  'isSignal' : 0,
                  'isData'   : 0
                  }

structure['WH_hww18'] = {
                  'isSignal' : 0,
                  'isData'   : 0
                  }


structure['DATA']  = { 
                  'isSignal' : 0,
                  'isData'   : 1 
              }

#print "INSTRUCTURE"
#print cuts
#print nuisances['WWresum0j']
#print "OK"

#for nuis in nuisances.itervalues():
#  if 'cutspost' in nuis:
#    nuis['cuts'] = nuis['cutspost'](nuis, cuts)

#    print nuis



