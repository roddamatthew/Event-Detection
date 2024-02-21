from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
# from sklearn.linear_model import RidgeClassifier, SGDClassifier
# from sklearn.svm import SVC, LinearSVC
# from xgboost import XGBClassifier
from sklearn.metrics import classification_report, accuracy_score, precision_score, recall_score
from sklearn.model_selection import train_test_split
from sklearn.feature_selection import VarianceThreshold
from sklearn.pipeline import Pipeline
from sklearn.multioutput import MultiOutputClassifier
from sklearn.preprocessing import MinMaxScaler
import joblib
from sklearn.model_selection import KFold
import time
import numpy as np
import os

classical_model_names = [
    'KNearestNeighbors',
    # 'DecisionTree',
    # 'RandomForest',
    # 'ExtremeGradientBoosted',
    # 'SupportVectorMachine',
    # 'SupportVectorMachineCS',
    # 'RBFSupportVectorMachine',
]


classical_models = [
    KNeighborsClassifier( weights = 'distance', metric = 'manhattan', n_neighbors = 10 ),
    # DecisionTreeClassifier(),
    # RandomForestClassifier(),
    # XGBClassifier(),
    # LinearSVC( C = 20, class_weight = 'balanced', max_iter = int( 1e4 ), verbose = True ),
    # LinearSVC( C = 20, class_weight = 'balanced', max_iter = int( 1e4 ), multi_class = 'crammer_singer', verbose = True ),
    # SVC( C = 20, class_weight = 'balanced', max_iter = int( 1e4 ), verbose = True, cache_size = 4096 ),
]

def run_experiment( model_name, window_size, encoding = 'bits', noise = False, lag = False ):
    path = str( window_size )
    if lag:
        path += '_lag'
    
    if noise:
        path += '_noise'

    print( model_name + '_' + path, encoding )

    max_length = 44
    if encoding == 'bits':
        max_length *= 8
        
    # if os.path.isfile( '/srv/shared/Artemis/processed_datasets/results/' + model_name + '_' + encoding + '_' + path ): return

    X = joblib.load( '/srv/shared/Artemis/processed_datasets/features/' + encoding + '_' + str( window_size ) )
    y = joblib.load( '/srv/shared/Artemis/processed_datasets/labels/' + path )
    
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
    }
    
    kf = KFold( n_splits = 3, shuffle = False )
    for i, ( train_index, test_index ) in enumerate( kf.split( X ) ):
        X_train = X[train_index]
        X_test = X[test_index]
        y_train = y[train_index]
        y_test = y[test_index]

        print( y_train.shape )

        if model_name in classical_model_names:
            start_time = time.time()
            
            if model_name in [ 'SupportVectorMachine', 'RBFSupportVectorMachine', 'SupportVectorMachineCS' ] and window_size > 1:
                model = Pipeline( [
                    ( 'varianceThreshold', VarianceThreshold() ),
                    ( 'minMaxScaler', MinMaxScaler() ),
                    ( 'model', MultiOutputClassifier( classical_models[classical_model_names.index( model_name )] ) )
                ] )
            else:
                model = Pipeline( [
                    ( 'varianceThreshold', VarianceThreshold() ),
                    ( 'minMaxScaler', MinMaxScaler() ),
                    ( 'model', classical_models[classical_model_names.index( model_name )] )
                ] )
                
            model.fit(
                X_train,
                y_train,
            )
            training_time = time.time() - start_time
            start_time = time.time()
            train_predictions = model.predict( X_train )
            test_predictions = model.predict( X_test )
            inference_time = time.time() - start_time
        else:
            raise Exception( 'Model Name not found!!!' )

        results['train_predictions'].append( train_predictions )
        results['test_predictions'].append( test_predictions )
        results['training_times'].append( training_time )
        results['inference_times'].append( inference_time )
        
    joblib.dump( results, '/srv/shared/Artemis/processed_datasets/results/' + model_name + '_' + encoding + '_' + path )
    return