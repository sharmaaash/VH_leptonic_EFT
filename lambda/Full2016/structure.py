# structure configuration for datacard

structure = {}

# keys here must match keys in samples.py    
#
structure['WH_hww_zerolambda'] = {
                  'isSignal' : 1,
                  'isData'   : 0
                  }


structure['WH_hww'] = {
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



