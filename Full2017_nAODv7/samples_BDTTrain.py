import os
import inspect

configurations = os.path.realpath(inspect.getfile(inspect.currentframe())) # this file
configurations = os.path.dirname(configurations) # ggH2016
configurations = os.path.dirname(configurations) # Differential
configurations = os.path.dirname(configurations) # Configurations

from LatinoAnalysis.Tools.commonTools import getSampleFiles, getBaseW, addSampleWeight

def nanoGetSampleFiles(inputDir, sample):
    try:
        if _samples_noload:
            return []
    except NameError:
        pass

    return getSampleFiles(inputDir, sample, True, 'nanoLatino_')

# samples

try:
    len(samples)
except NameError:
    import collections
    samples = collections.OrderedDict()

################################################
################# SKIMS ########################
################################################

#mcProduction = 'Summer16_102X_nAODv4_Full2016v5'
# mcProduction = 'Summer16_102X_nAODv5_SigOnly_Full2016v5'
mcProduction = 'Fall2017_102X_nAODv7_Full2017v7'
#mcProductionSigOnly = 'Summer16_102X_nAODv5_SigOnly_Full2016v5'

#mcSteps = 'MCl1loose2016v5__MCCorr2016v5__l2loose__l2tightOR2016v5'
mcSteps = 'MCl1loose2017v7__MCCorr2017v7__l2loose__l2tightOR2017v7{var}'
##############################################
###### Tree base directory for the site ######
##############################################

SITE=os.uname()[1]
if    'iihe' in SITE:
  treeBaseDir = '/pnfs/iihe/cms/store/user/xjanssen/HWW2015'
elif  'cern' in SITE:
#  treeBaseDir = '/eos/cms/store/group/phys_higgs/cmshww/sharmaa'
  treeBaseDir = '/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano'

def makeMCDirectory(var=''):
    if var:
        return os.path.join(treeBaseDir, mcProduction, mcSteps.format(var='__' + var))
    else:
        return os.path.join(treeBaseDir, mcProduction, mcSteps.format(var=''))

mcDirectory = makeMCDirectory()
#mcSigOnlyDirectory = os.path.join(treeBaseDir, mcProductionSigOnly, mcSteps.format(var=''))

#########################################
############ MC COMMON ##################
#########################################

# SFweight does not include btag weights
mcCommonWeightNoMatch = 'XSWeight*SFweight*METFilter_MC'
mcCommonWeight = 'XSWeight*SFweight*PromptGenLepMatch3l*METFilter_MC'

###########################################
#############  BACKGROUNDS  ###############
###########################################

files = nanoGetSampleFiles(mcDirectory, 'HWplusJ_HToWW_LNu_M125') + \
    nanoGetSampleFiles(mcDirectory, 'HWminusJ_HToWW_LNu_M125')

samples['WH_hww16'] = {
    'name':   files,
    'weight': mcCommonWeight,
    'FilesPerJob': 4
}



###########################################
#############   SIGNALS  ##################
###########################################

signals = []

############ WH H->WW0M ############
samples['WH_hww_zerominus16'] = {
    'name': nanoGetSampleFiles(mcDirectory, 'WH_H0M_ToWWTo2L2Nu'),
    'weight': mcCommonWeight+'*'+'EFTaBDT_trainingWeight',
    'FilesPerJob': 3
}

signals.append('WH_hww_zerominus16')
