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

mcProduction = 'Autumn18_102X_nAODv7_Full2018v7'

mcSteps = 'MCl1loose2018v7__MCCorr2018v7__l2loose__l2tightOR2018v7{var}'

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

#########################################
############ MC COMMON ##################
#########################################

# SFweight does not include btag weights
mcCommonWeightNoMatch = 'XSWeight*SFweight*METFilter_MC'
mcCommonWeight = 'XSWeight*SFweight*PromptGenLepMatch3l*METFilter_MC'

###########################################
#############  BACKGROUNDS  ###############
###########################################

################### WH_hww #############################

files = nanoGetSampleFiles(mcDirectory, 'HWplusJ_HToWW_LNu_M125') + \
    nanoGetSampleFiles(mcDirectory, 'HWminusJ_HToWW_LNu_M125')

samples['WH_hww18'] = {
    'name':   files,
    'weight': mcCommonWeight,
    'FilesPerJob': 4
}


###########################################
#############   SIGNALS  ##################
###########################################

signals = []

samples['WH_hww_zerominus18'] = {
    'name': nanoGetSampleFiles(mcDirectory, 'WH_H0M_ToWWTo2L2Nu'),
    'weight': mcCommonWeight+'*'+'EFTaBDT_trainingWeight'+'*WH_H0M_W',
    'FilesPerJob': 3
}

signals.append('WH_hww_zerominus18')
