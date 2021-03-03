#version for one BSM signal model only
import os
import inspect

configurations = os.path.realpath(inspect.getfile(inspect.currentframe())) # this file
configurations = os.path.dirname(configurations) # Full2017
configurations = os.path.dirname(configurations) # ggH
configurations = os.path.dirname(configurations) # EFT
configurations = os.path.dirname(configurations) # Configurations

from LatinoAnalysis.Tools.commonTools import getSampleFiles, getBaseW, addSampleWeight

def nanoGetSampleFiles(inputDir, sample):
    try:
        if _samples_noload:
            return [sample]
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

#mcProduction = 'Fall2017_102X_nAODv4_Full2017v5'
#mcProduction = 'Fall2017_102X_nAODv5_SigOnly_Full2017v5'
mcProduction = 'Autumn18_102X_nAODv7_Full2018v7'


dataReco = 'Run2018_102X_nAODv7_Full2018v7'

#mcSteps = 'MCl1loose2017v6__MCCorr2017v6__l2loose__l2tightOR2017v6__{var}_suffix_redoMVA'
mcSteps = 'MCl1loose2018v7__MCCorr2018v7__l2loose__l2tightOR2018v7{var}'
fakeSteps = 'DATAl1loose2018v6__l2loose__fakeW'

dataSteps = 'DATAl1loose2018v6__l2loose__l2tightOR2018v6'

##############################################
###### Tree base directory for the site ######
##############################################

SITE=os.uname()[1]
if    'iihe' in SITE:
  treeBaseDir = '/pnfs/iihe/cms/store/user/xjanssen/HWW2015'
elif  'cern' in SITE:
  treeBaseDir = '/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/'

def makeMCDirectory(var=''):
    if var:
        return os.path.join(treeBaseDir, mcProduction, mcSteps.format(var='__' + var))
       #return '/afs/cern.ch/user/t/tkello/public/HWW_EFT/Fall2017/l2tightOR__{var}'.format(var=var)
    else:
        return os.path.join(treeBaseDir, mcProduction, mcSteps.format(var=''))
        #return '/afs/cern.ch/user/t/tkello/public/HWW_EFT/Fall2017/l2tightOR'

mcDirectory = makeMCDirectory()
fakeDirectory = os.path.join(treeBaseDir, dataReco, fakeSteps)
dataDirectory = os.path.join(treeBaseDir, dataReco, dataSteps)

################################################
############ DATA DECLARATION ##################
################################################

DataRun = [
            ['A','Run2018A-Nano25Oct2019-v1'] ,
            ['B','Run2018B-Nano25Oct2019-v1'] ,
            ['C','Run2018C-Nano25Oct2019-v1'] ,
            ['D','Run2018D-Nano25Oct2019_ver2-v1'] ,
          ]

DataSets = ['MuonEG','DoubleMuon','SingleMuon','EGamma']

DataTrig = {
            'MuonEG'         : 'Trigger_ElMu' ,
            'DoubleMuon'     : '!Trigger_ElMu && Trigger_dblMu' ,
            'SingleMuon'     : '!Trigger_ElMu && !Trigger_dblMu && Trigger_sngMu' ,
            'EGamma'         : '!Trigger_ElMu && !Trigger_dblMu && !Trigger_sngMu && (Trigger_sngEl || Trigger_dblEl)' ,
           }

#########################################
############ MC COMMON ##################
#########################################

# SFweight does not include btag weights
mcCommonWeight = 'XSWeight*SFweight*METFilter_MC'
mcCommonWeightMatched = 'XSWeight*SFweight*PromptGenLepMatch3l*METFilter_MC'

###########################################
#############  BACKGROUNDS  ###############
###########################################


samples['DY'] = {
    'name': nanoGetSampleFiles(mcDirectory, 'DYJetsToTT_MuEle_M-50'),
    'weight': mcCommonWeight,
    'FilesPerJob': 6,
}
addSampleWeight(samples,'DY','DYJetsToTT_MuEle_M-50', 'ptllDYW_NLO')

samples['TTbar'] = {
    'name': nanoGetSampleFiles(mcDirectory, 'TTTo2L2Nu'),
    'weight': mcCommonWeight,
    'FilesPerJob': 1
}
addSampleWeight(samples, 'TTbar', 'TTTo2L2Nu', 'Top_pTrw')

samples['WW'] = {
    'name': nanoGetSampleFiles(mcDirectory, 'WWTo2L2Nu'),
    'weight': mcCommonWeight + '*nllW',
    'FilesPerJob': 3
}


files = nanoGetSampleFiles(mcDirectory, 'HWplusJ_HToWW_M125') + \
    nanoGetSampleFiles(mcDirectory, 'HWminusJ_HToWW_M125')

samples['WH_hww'] = {
    'name':   files,
    'weight': mcCommonWeight,
}

###########################################
#############   SIGNALS  ##################
###########################################

signals = []

'''
############ WH H0M->WW ############
samples['WH_hww_zerominus'] = {
    'name': nanoGetSampleFiles(mcDirectory, 'WH_H0M_ToWWTo2L2Nu'),
    'weight': mcCommonWeight+'*'+'EFTaBDT_analysisWeight',
    'FilesPerJob': 3
}

signals.append('WH_hww_zerominus')
'''
############ WH H0P->WW ############
samples['WH_hww_zeroplus'] = {
    'name': nanoGetSampleFiles(mcDirectory, 'WH_H0PH_ToWWTo2L2Nu'),
    'weight': mcCommonWeight+'*'+'EFTaBDT_analysisWeight'+ '*WH_H0PH_W',
    'FilesPerJob': 3
}

signals.append('WH_hww_zeroplus') 
############ WH H0L1->WW ############
'''
samples['WH_hww_zerolambda'] = {
    'name': nanoGetSampleFiles(mcDirectory, 'WH_H0L1_ToWWTo2L2Nu'),
    'weight': mcCommonWeight,
    'FilesPerJob': 3
}

signals.append('WH_hww_zerolambda')

######### mix of SM and BSM #####################

samples['WH_hww_mixzerominus'] = {
    'name': nanoGetSampleFiles(mcDirectory, 'WH_H0Mf05_ToWWTo2L2Nu'),
    'weight': mcanalysisweight,
    'FilesPerJob': 3
}

signals.append('WH_hww_mixzerominus')
''' 
############ WH mixH0P->WW ############
samples['WH_hww_mixzeroplus'] = {
    'name': nanoGetSampleFiles(mcDirectory, 'WH_H0PHf05_ToWWTo2L2Nu'),
    'weight': mcCommonWeight+'*'+'EFTaBDT_analysisWeight'+ '*WH_H0PHf05_W',
    'FilesPerJob': 3
}

signals.append('WH_hww_mixzeroplus')
'''
############ WH mixH0L1->WW ############
samples['WH_hww_mixzerolambda'] = {
    'name': nanoGetSampleFiles(mcDirectory, 'WH_H0L1f05_ToWWTo2L2Nu'),
    'weight': mcCommonWeight,
    'FilesPerJob': 3
}

signals.append('WH_hww_mixzerolambda')

'''


###########################################
################## FAKE ###################
###########################################
'''
samples['Fake'] = {
  'name': [],
  'weight': 'METFilter_DATA*fakeW',
  'weights': [],
  'isData': ['all'],
  'FilesPerJob': 30
}

for _, sd in DataRun:
  for pd in DataSets:
    files = nanoGetSampleFiles(fakeDirectory, pd + '_' + sd)
    samples['Fake']['name'].extend(files)
    samples['Fake']['weights'].extend([DataTrig[pd]] * len(files))

samples['Fake']['subsamples'] = {
  'em': 'abs(Lepton_pdgId[0]) == 11',
  'me': 'abs(Lepton_pdgId[0]) == 13'
}
'''
###########################################
################## DATA ###################
###########################################
'''
samples['DATA'] = {
  'name': [],
  'weight': 'METFilter_DATA*LepWPCut',
  'weights': [],
  'isData': ['all'],
  # 'FilesPerJob': 100
  'FilesPerJob': 200
}

for _, sd in DataRun:
  for pd in DataSets:
    files = nanoGetSampleFiles(dataDirectory, pd + '_' + sd)
    samples['DATA']['name'].extend(files)
    samples['DATA']['weights'].extend([DataTrig[pd]] * len(files))
'''
