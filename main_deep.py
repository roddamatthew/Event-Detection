from run_experiment_deep import run_experiment
from multiprocessing import Pool
import random
from numba import cuda
import keras.backend as K
import tensorflow as tf
import sys

def get_deep_parameters():
    parameters = []
    
    # window_sizes = [ 45, 50 ]
    window_sizes = [ 5, 10, 15, 20, 25, 30, 35, 40, 45, 50 ]
    window_sizes.reverse()
    model_names = [
        # 'DNN',
        '1DCNN16',
        '1DCNN32',
        '1DCNN64',
        # 'LSTM',
        # 'LSTM2',
        # '1DCNN-LSTM',
        # '1DCNN-LSTM-Dropout'
    ]

    for encoding in [ 'bits' ]:
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

# if __name__ == '__main__':
#     parameters = get_deep_parameters()
    
#     with Pool( 1 ) as p:
#         p.starmap( run_experiment, parameters )


if __name__ == '__main__':
    print( sys.argv )
    p = [
        sys.argv[1],
        int( sys.argv[2] ),
        sys.argv[3],
        False if sys.argv[4] == 'False' else True,
        False if sys.argv[5] == 'False' else True,
    ]
    
    gpu_devices = tf.config.experimental.list_physical_devices("GPU")
    for device in gpu_devices:
        tf.config.experimental.set_memory_growth(device, True)
    
    print( p )
        
    run_experiment( *p )