# variables

#variables = {}
    


variables['events']  = {   'name': '1',      
                        'range' : (1,0,2),  
                        'xaxis' : 'events', 
                        'fold' : 3
                        }

'''
variables['genLepton_pt']  = {   'name': 'LeptonGen_pt',
                        'range' : (20,0,200),
                        'xaxis' : 'p_{T}^{Gen}',
                        'fold' : 3
                        }

variables['cosThetaS'] = { 'name': 'hww_cosTheta(Entry$,0)',
                           'range' : (20,-1.0,1.0),
                           'xaxis' : 'cos(#theta_{S})',
                           'fold'  : 3,
                           'linesToAdd' : ['.L /afs/cern.ch/user/t/tkello/workspace/MainAnalysis/HWW_AC/CMSSW_9_4_9/src/PlotsConfigurations/Configurations/EFT/ggH/Full2017/hww_cosTheta.C+'] 
                         }

variables['cosThetaOne'] = { 'name': 'hww_cosTheta(Entry$,1)',
                           'range' : (20,-1.0,1.0),
                           'xaxis' : 'cos(#theta_{1})',
                           'fold'  : 3
                           } 

variables['cosThetaTwo'] = { 'name': 'hww_cosTheta(Entry$,2)',
                           'range' : (20,-1.0,1.0),
                           'xaxis' : 'cos(#theta_{2})',
                           'fold'  : 3
                         }
'''
variables['mll'] = { 'name' : 'mll',
                     'range': (20,0,200),
                     'xaxis': 'm_{ll}',
                     'fold' : 3 
                }

variables['mth'] = { 'name' : 'mth',
                     'range': (20,0,200),
                     'xaxis': 'm_{T}^{H}',
                     'fold' : 3
                }
'''
variables['dphill'] = { 'name' : 'dphill',
                     'range': (20,0,3.14),
                     'xaxis': '#Delta#Phi_{ll}',
                     'fold' : 3
                }
'''
variables['mllVSmth'] = {   'name': 'mll:mth', 
                           'range': ([60,65,70,75,80,90,100,110,125],[10,15,20,25,30,40,50,60,70,80,100],),
                           'xaxis': 'm_{ll} : m_{T}^{H}',
                           'fold': 3
                       }
'''
variables['pTWW'] = {   'name': 'pTWW',
                           'range': (20,0,200),
                           'xaxis': 'p_{T}^{WW}',
                           'fold': 3
                       }

variables['ptll'] = {   'name': 'ptll',
                           'range': (20,0,200),
                           'xaxis': 'p_{T}^{ll}',
                           'fold': 3
                       }
'''
'''
variables['mllVSmth_pt2ge20'] = {   'name': 'mll:mth',            #   variable name    
                             'range' : ([60,80,90,100,110,120,130,150,200],[12,25,35,40,45,50,55,70,90,210],),            #   variable range
                             'xaxis' : 'm_{ll} : m_{T}^{H}',      #   x axis name
                             'fold' : 3 ,
                             # do weighted plot too
                             'doWeight' : 1,
                             'binX'     : 8,
                             'binY'     : 9
                             #
                             }

variables['mllVSmth_pt2lt20'] = {   'name': 'mll:mth',            #   variable name    
                             'range' : ([60,80,90,110,130,150,200],[12,25,40,50,70,90,210],),            #   variable range
                             'xaxis' : 'm_{ll} : m_{T}^{H}',      #   x axis name
                             'fold' : 3 ,
                             # do weighted plot too
                             'doWeight' : 1,
                             'binX'     : 6,
                             'binY'     : 6
                             #
                             }
'''
