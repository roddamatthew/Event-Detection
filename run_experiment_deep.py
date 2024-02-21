from sklearn.metrics import classification_report, accuracy_score, precision_score, recall_score, f1_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.multioutput import MultiOutputClassifier
from sklearn.preprocessing import MinMaxScaler
import joblib
from sklearn.model_selection import KFold
import time
import numpy as np
import os
import tensorflow as tf
from deep_architectures import get_model

deep_model_names = [ 
    'DNN',
    '1DCNN16',
    '1DCNN32',
    '1DCNN64',
    'LSTM',
    'LSTM2',
    '1DCNN-LSTM',
    '2DCNN16',
    '2DCNN32',
    '2DCNN64',
    '2DCNN-LSTM',
]

def run_experiment( model_name, window_size, encoding = 'bits', noise = False, lag = False ):
    path = str( window_size )
    if lag:
        path += '_lag'
    
    if noise:
        path += '_noise'

    print( model_name + '_' + path, encoding )

    # if os.path.isfile( '/srv/shared/Artemis/processed_datasets/results/' + model_name + '_' + encoding + '_' + path ): return

    max_length = 44
    if encoding == 'bits':
        max_length *= 8

    X = joblib.load( '/srv/shared/Artemis/processed_datasets/features/' + encoding + '_' + str( window_size ) )
    y = joblib.load( '/srv/shared/Artemis/processed_datasets/labels/' + path )
    gt = joblib.load( '/srv/shared/Artemis/processed_datasets/labels/' + str( window_size ) )
    
    if window_size > 1:
        y[y>0] = 1

    results = {
        'model': model_name,
        'window_size': window_size,
        'encoding': encoding,
        'noise': noise,
        'lag': lag,
        'train_predictions': [],
        'test_predictions': [],
        'training_times': [],
        'inference_times': [],
        'history': [],
    }
    
    kf = KFold( n_splits = 3, shuffle = False )
    for i, ( train_index, test_index ) in enumerate( kf.split( X ) ):
        X_train = np.transpose( X[train_index].reshape( -1, 44, window_size ), axes = ( 0, 2, 1 ) )
        X_test = np.transpose( X[test_index].reshape( -1, 44, window_size ), axes = ( 0, 2, 1 ) )
        y_train = y[train_index]
        y_test = y[test_index]
        
        print( '###########################', model_name + '_' + path, encoding, '###########################', )
        
        print( 'X_train', X_train.shape )
        print( 'y_train', y_train.shape )
        print( 'X_test', X_test.shape )
        print( 'y_test', y_test.shape )
        
        if model_name in deep_model_names:
            start_time = time.time()
            model = get_model( model_name, window_size, encoding )
            model.summary()
            history = model.fit( 
                X_train.reshape( -1, window_size, max_length ), np.array( y_train, dtype = np.float32 ),
                validation_data = ( X_test.reshape( -1, window_size, max_length ), np.array( gt[test_index], dtype = np.float32 ) ),
                batch_size = 32,
                epochs = 200,
                # class_weight = 'balanced',
                callbacks = [
                    tf.keras.callbacks.EarlyStopping(
                        monitor = 'val_f1_score',
                        patience = 15,
                        restore_best_weights = True,
                        start_from_epoch = 10,
                        mode = 'max', # Bigger F1 is better!
                    )
                ]
            )
            training_time = time.time() - start_time
            start_time = time.time()
            train_predictions = model.predict( X_train.reshape( -1, window_size, max_length ) )
            test_predictions = model.predict( X_test.reshape( -1, window_size, max_length ) )
            inference_time = time.time() - start_time
            # results['history'] = history
        else:
            raise Exception( 'Model Name not found!!!', model_name, deep_model_names )

        results['train_predictions'].append( train_predictions )
        results['test_predictions'].append( test_predictions )
        results['training_times'].append( training_time )
        results['inference_times'].append( inference_time )
        results['history'].append( history.history )
        
        model.save( '/srv/shared/Artemis/processed_datasets/' + model_name + '_' + encoding + '_' + path + '_' + str( i ) + '.keras' )
        
        
        print( 'Train:' )
        print( 'Accuracy', accuracy_score( gt[train_index], np.round( train_predictions ) ) )
        print( 'Precision', precision_score( gt[train_index], np.round( train_predictions ), average = 'macro' ) )
        print( 'Recall', recall_score( gt[train_index], np.round( train_predictions ), average = 'macro' ) )
        print( 'F1-Score', f1_score( gt[train_index], np.round( train_predictions ), average = 'macro' ) )
        print( 'Test:' )
        print( 'Accuracy', accuracy_score( gt[test_index], np.round( test_predictions ) ) )
        print( 'Precision', precision_score( gt[test_index], np.round( test_predictions ), average = 'macro' ) )
        print( 'Recall', recall_score( gt[test_index], np.round( test_predictions ), average = 'macro' ) )
        print( 'F1-Score', f1_score( gt[test_index], np.round( test_predictions ), average = 'macro' ) )
    
        print( classification_report( gt[test_index], np.round( test_predictions ) ) )
        # Delete model to free up space
        del model
        
    # joblib.dump( results, '/srv/shared/Artemis/processed_datasets/results/' + model_name + '_' + encoding + '_' + path )
    
    from numba import cuda
    cuda.select_device( 0 )
    cuda.close()
    
    return