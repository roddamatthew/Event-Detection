from run_experiment import run_experiment
from multiprocessing import Pool
import random
import os

def get_deep_parameters():
    parameters = []
    
    window_sizes = [ 1, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50 ]
    model_names = [
        'DNN',
        '1DCNN16',
        '1DCNN32',
        '1DCNN64',
        'LSTM',
        'LSTM2',
        '1DCNN-LSTM'
    ]

    for encoding in [ 'bits', 'bytes' ]:
        for window_size in window_sizes:
            for lag in [ False, True ]:
                for noise in [ False, True ]:
                    for model_name in model_names:
                        parameters.append( [
                            model_name,
                            window_size,
                            encoding,
                            noise,
                            lag,
                        ] )
    return parameters


def get_parameters():
    parameters = []
    
    window_sizes = [ 1, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50 ]
    model_names = [
        'DecisionTree',
        'RandomForest',
        'ExtremeGradientBoosted',
        'KNearestNeighbors',
        'SupportVectorMachine',
        'RBFSupportVectorMachine',
    ]

    for encoding in [ 'bits', 'bytes' ]:
        for window_size in window_sizes:
            for lag in [ False, True ]:
                for noise in [ False, True ]:
                    for model_name in model_names:
                        parameters.append( [
                            model_name,
                            window_size,
                            encoding,
                            noise,
                            lag,
                        ] )
    return parameters



if __name__ == '__main__':    
    parameters = get_parameters()
    random.shuffle( parameters )

    with Pool( 16 ) as p:
        p.starmap( run_experiment, parameters )
        
        # for param in parameters:
        #     path = param[0]
        #     path += '_' + param[2]
        #     path += '_' + str( param[1] )
        #     if param[4]:
        #         path += '_lag'
        #     if param[3]:
        #         path += '_noise'
            
        #     if path not in completed:
        #         print( path )
        #         print( param )
        #         p.starmap( run_experiment, param )
