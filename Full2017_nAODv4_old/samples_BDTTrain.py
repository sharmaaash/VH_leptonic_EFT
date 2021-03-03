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
#mcProduction17  = 'Fall2017_102X_nAODv5_Full2017v6'
mcProduction17  = 'Fall2017_102X_nAODv7_Full2017v7'
#mcSteps17 = 'MCl1loose2017v6__MCCorr2017v6__l2loose__l2tightOR2017v6__EFTaBDTsplit'
mcSteps17 = 'MCl1loose2017v7__MCCorr2017v7__l2loose__l2tightOR2017v7__EFTskim4BDT'
##############################################
###### Tree base directory for the site ######
##############################################

SITE=os.uname()[1]
if    'iihe' in SITE:
  treeBaseDir = '/pnfs/iihe/cms/store/user/xjanssen/HWW2015'
elif  'cern' in SITE:
  treeBaseDir = '/eos/user/s/sharmaa/'
#  treeBaseDir = '/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano'

def makeMCDirectory17(var=''):
    if var:
        return os.path.join(treeBaseDir, mcProduction17, mcSteps17.format(var='__' + var))
    else:
        return os.path.join(treeBaseDir, mcProduction17, mcSteps17.format(var=''))

mcDirectory17 = makeMCDirectory17()



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


files17 = nanoGetSampleFiles(mcDirectory17, 'HWplusJ_HToWW_M125') + \
    nanoGetSampleFiles(mcDirectory17, 'HWminusJ_HToWW_M125')


samples['WH_hww17'] = {
    'name':   files17,
    'weight': mcCommonWeight,
    'FilesPerJob': 4
}
###########################################
#############   SIGNALS  ##################
###########################################

signals = []


samples['WH_hww_zerominus17'] = {
    'name': nanoGetSampleFiles(mcDirectory17, 'WH_H0M_ToWWTo2L2Nu'),
    'weight': mcCommonWeight,
    'FilesPerJob': 3
}

signals.append('WH_hww_zerominus17')

