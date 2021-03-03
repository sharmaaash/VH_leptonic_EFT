# example of configuration file

import os

configDir = os.path.expandvars("../FullRun2_nAODv4")

tagName = ''

# luminosity to normalize to (in 1/fb)
lumi = 137.1

# file with list of cuts
cutsFile = os.path.join(configDir,'cuts_BDTTrain.py' )

# file with list of samples
samplesFile = os.path.join(configDir,'samples_BDTTrain.py' )

# structure file for datacard
structureFile = os.path.join(configDir,'structure.py')
