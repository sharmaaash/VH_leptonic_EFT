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
mcProduction16 = 'Summer16_102X_nAODv5_Full2016v6'
mcProduction17 = 'Fall2017_102X_nAODv5_Full2017v6'
mcProduction18 = 'Autumn18_102X_nAODv6_Full2018v6'
#mcProductionSigOnly = 'Fall2017_102X_nAODv5_SigOnly_Full2017v5'
mcSteps16 = 'MCl1loose2016v6__MCCorr2016v6__l2loose__l2tightOR2016v6'
mcSteps17 = 'MCl1loose2017v6__MCCorr2017v6__l2loose__l2tightOR2017v6'
mcSteps18 = 'MCl1loose2018v6__MCCorr2018v6__l2loose__l2tightOR2018v6'
##############################################
###### Tree base directory for the site ######
##############################################

SITE=os.uname()[1]
if    'iihe' in SITE:
  treeBaseDir = '/pnfs/iihe/cms/store/user/xjanssen/HWW2015'
elif  'cern' in SITE:
  treeBaseDir = '/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano'

def makeMCDirectory16(var=''):
    if var:
        return os.path.join(treeBaseDir, mcProduction16, mcSteps16.format(var='__' + var))
    else:
        return os.path.join(treeBaseDir, mcProduction16, mcSteps16.format(var=''))

mcDirectory16 = makeMCDirectory16()


def makeMCDirectory17(var=''):
    if var:
        return os.path.join(treeBaseDir, mcProduction17, mcSteps17.format(var='__' + var))
    else:
        return os.path.join(treeBaseDir, mcProduction17, mcSteps17.format(var=''))

mcDirectory17 = makeMCDirectory17()

def makeMCDirectory18(var=''):
    if var:
        return os.path.join(treeBaseDir, mcProduction18, mcSteps18.format(var='__' + var))
    else:
        return os.path.join(treeBaseDir, mcProduction17, mcSteps17.format(var=''))

mcDirectory18 = makeMCDirectory18()


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

files16 = nanoGetSampleFiles(mcDirectory16, 'HWplusJ_HToWW_M125') + \
    nanoGetSampleFiles(mcDirectory16, 'HWminusJ_HToWW_M125')


samples['WH_hww16'] = {
    'name':   files16,
    'weight': mcCommonWeight,
    'FilesPerJob': 4
}


files17 = nanoGetSampleFiles(mcDirectory17, 'HWplusJ_HToWW_M125') + \
    nanoGetSampleFiles(mcDirectory17, 'HWminusJ_HToWW_M125')


samples['WH_hww17'] = {
    'name':   files17,
    'weight': mcCommonWeight,
    'FilesPerJob': 4
}

files18 = nanoGetSampleFiles(mcDirectory18, 'HWplusJ_HToWW_M125') + \
    nanoGetSampleFiles(mcDirectory18, 'HWminusJ_HToWW_M125')


samples['WH_hww18'] = {
    'name':   files18,
    'weight': mcCommonWeight,
    'FilesPerJob': 4
}

###########################################
#############   SIGNALS  ##################
###########################################

signals = []

samples['WH_hww_zerolambda16'] = {
    'name': nanoGetSampleFiles(mcDirectory16, 'WH_H0L1_ToWWTo2L2Nu'),
    'weight': mcCommonWeight+'*'+'EFTaBDT_trainingWeight',
    'FilesPerJob': 3
}

signals.append('WH_hww_zerolambda16')


samples['WH_hww_zerolambda17'] = {
    'name': nanoGetSampleFiles(mcDirectory17, 'WH_H0L1_ToWWTo2L2Nu'),
    'weight': mcCommonWeight+'*'+'EFTaBDT_trainingWeight',
    'FilesPerJob': 3
}

signals.append('WH_hww_zerolambda17')

samples['WH_hww_zerolambda18'] = {
    'name': nanoGetSampleFiles(mcDirectory18, 'WH_H0L1_ToWWTo2L2Nu'),
    'weight': mcCommonWeight+'*'+'EFTaBDT_trainingWeight',
    'FilesPerJob': 3
}

signals.append('WH_hww_zerolambda18')
