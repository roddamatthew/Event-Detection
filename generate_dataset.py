import numpy as np
import pandas as pd
from joblib import load
from numpy.lib.stride_tricks import sliding_window_view

# Randomly sample reaction time from normal distribution
def noise_time( mean = 0.45, std = 0.03 ):
    return np.random.normal( mean, std )

def match_timestamps( dataset, targets ):
    labels = []
    
    for j, sample in enumerate( dataset ):
        print( j, '  ', end = '\r' )
        for i in range( len( targets ) ):
            if sample['time'] < targets[i]['time']:
                labels.append( targets[i]['label'] )
                break
    return labels

def match_timestamps_windowed( dataset, targets, window_size ):
    labels = []
    for i in range( len( dataset[:-window_size + 1] ) ):
        window_start = dataset[i]['time']
        window_end = dataset[i + window_size - 1]['time']

        label = [ 0, 0, 0, 0, 0, 0, 0, 0 ]
        for j in range( len( targets ) ):
            if targets[j]['time'] >= window_start:
                # Now j is within the packet window
                k = j
                while targets[k]['time'] <= window_end:
                    if targets[k]['label'] > 0:
                        label[targets[k]['label'] - 1] += 1
                    k += 1

                labels.append( label )
                break
    assert len( labels ) == ( len( dataset ) - window_size + 1 )
    return labels


import random

# Single packet classification noise.
# Only one type of noise can be applied at a time
# 1. If there is no event, randomly apply a random event
# 2. If there is an event, randomly remove it
# 3. If there is an event, randomly confuse it for another
def noise_single( label, fp = 0.02, fn = 0.05, confusion = 0.05 ):
    val = random.uniform( 0, 1 )
    
    # False Positive
    if label == 0 and val <= fp:
        return random.randint( 1, 8 )
    # False Negative
    elif label != 0 and val <= fn:
        return 0
    elif label != 0 and val <= fn + confusion:
        return random.randint( 1, 8 )
    return label

def noise_multi( label, fp = 0.02, fn = 0.05, confusion = 0.05 ):
    val = random.uniform( 0, 1 )
    
    # False Positive
    if label[0] == 1 and val <= fp:
        label[0] = 0
        label[random.randint( 1, 7 )] = 1
        return label
    # False Negative
    elif label[0] != 1 and val <= fn:
        label = [ 0 for i in range( len( label ) ) ]
        label[0] = 1
        return label
    elif label[0] != 1 and val <= fn + confusion:
        label = [ 0 for i in range( len( label ) ) ]
        label[random.randint( 1, 7 )] = 1
        return label
    return label

def load_datasets( paths ):
    datasets = []
    for path in paths:
        datasets.append( pd.read_pickle( path ) )
    
    k = 2.0 # 1.0 for client and server, 2.0 for client
    # Filter client packets
    for i in range( len( datasets ) ):
        datasets[i] = datasets[i][datasets[i]['artemissbs.origin'] >= k]
    
    return datasets

# Load labels of dataset using the columns in the DataFrame
def load_labels( dataset ):
    targets = []

    events = [ 'helmsetwarp.warp_factor', 'helmsetimpulse.throttle', 'helmsetsteering.rudder', 'loadtube.tube_index', 'firetube.tube_index' ]
    classes = [ 'None', 'Slow', 'Fast', 'Warp', 'Stop Warp', 'Left', 'Right', 'Load', 'Fire' ]

    # 0: No Event
    # 1: Slow: Impulse < 50
    # 2: Fast: Impulse >= 50
    # 3: Warp: Warp > 0
    # 4: Stop Warp: Warp == 0
    # 5: Left: Steer < 50
    # 6: Right: Steer > 50
    # 7: Load
    # 8: Fire

    labels = []

    for event, time in zip( dataset[ events ].values, dataset['time'] ):
        time = time.timestamp()
        if np.isnan( event ).all():
            labels.append( {
                'label': 0,
                'time': time,
            } )
        else:
            for i, value in enumerate( event ):
                if not np.isnan( value ):
                    if i == 0: # Warp
                        if value > 0: labels.append( { 'label': 3, 'time': time, } )
                        else: labels.append( { 'label': 4, 'time': time, } )
                    elif i == 1: # Impulse
                        if value >= 0.5: labels.append( { 'label': 2, 'time': time, } )
                        else: labels.append( { 'label': 1, 'time': time, } )
                    elif i == 2: # Steering
                        if value > 0.5: labels.append( { 'label': 6, 'time': time, } )
                        elif value < 0.5: labels.append( { 'label': 5, 'time': time, } )
                        else: labels.append( { 'label': 0, 'time': time, } )
                    elif i == 3: # Loading
                        labels.append( { 'label': 7, 'time': time, } )
                    elif i == 4: # Firing
                        labels.append( { 'label': 8, 'time': time, } )
                    else:
                        # Uh oh
                        print( 'Error in target evaluation', i )
    return labels

# Preprocess a dataset to make features
def make_features( dataset, encoding = 'bits', window_size = 1 ):
    # Max packet length is 44 bytes
    max_length = 44
    if encoding == 'bits':
        max_length *= 8
    
    packets = []
    if encoding == 'bits':
        for packet, time in zip( dataset['udp.payload'], dataset['time'] ):
            blank_packet = np.zeros( max_length )
            blank_packet[:len( packet ) * 8] += np.unpackbits( np.frombuffer( packet, dtype = 'uint8' ) )
            packets.append( {
                'payload': blank_packet,
                'time': time.timestamp(), # 
            } )
    elif encoding == 'bytes':
        for packet, time in zip( dataset['udp.payload'], dataset['time'] ):
            blank_packet = np.zeros( max_length )
            blank_packet[:len( packet )] += np.frombuffer( packet, dtype = 'uint8' )
            packets.append( {
                'payload': blank_packet,
                'time': time.timestamp(),
            } )
    else:
        print( 'ERROR IN ENCODING: MUST BE ONE OF "bits" OR "BYTES"' )
        return

    print( 'Preprocessed packets with', encoding, 'encoding' )
    print( 'Found', len( packets ), 'packets' )

    # Aggregate packets and samples into windows:
    if window_size == 1:
        X = np.zeros( ( len( packets ), max_length ) )
        for i in range( len( packets ) ):
            X[i] += packets[i]['payload']
    else:
        X = np.zeros( ( len( packets ), max_length ) )
        
        for i in range( len( packets ) ):
            X[i] += packets[i]['payload']
        X = sliding_window_view( X, ( window_size ), axis = 0 ).reshape( -1, max_length * window_size )

    print( 'Final feature is shape: ', X.shape )
    return X


# Preprocess dataset to make labels
def make_labels( dataset, window_size = 1, lag = False, noise = False ):
    labels = load_labels( dataset )
    print( 'Loaded', len( labels ), 'single packet labels' )

    # Add timing noise
    if lag:
        for i in range( len( labels ) ):
            labels[i]['time'] += np.random.normal( 0.45, 0.03 )

        # Verify noise was added correctly
        labels_ = load_labels( dataset )
        delta = []
        for true, noisey in zip( labels_, labels ):
            delta.append( noisey['time'] - true['time'] )
        print( 'Measured added noise was N(', np.mean( delta ), ',', np.std( delta ), ')' )

    # Load packet times
    packets = []
    for time in dataset['time']:
        packets.append( {
            'time': time.timestamp(),
        } )

    # Aggregate packets and samples into windows:
    if window_size == 1:
        y = []
        for label in labels:
            y.append( label['label'] )

        if lag:
            y = match_timestamps( packets, labels )
            y_ = match_timestamps( packets, labels_ )
            
            diff = 0
            for s1, s2 in zip( y, y_ ):
                if s1 != s2:
                    diff += 1
            print( 'Number of differences from timing lag was: ', diff )
    else:
        y = []
        for label in labels:
            sample = np.zeros( ( 8 ) )
            if label['label'] > 0:
                sample[label['label'] - 1] += 1
            y.append( sample )
        
        y = sliding_window_view( y, ( window_size ), axis = 0 )
        y = np.sum( y, axis = 2 )
        
        if lag:
            y = match_timestamps_windowed( packets, labels, window_size )
            y = np.array( y )
        y[y>0] = 1

    total_changes = 0
    # Add noise to labels
    if noise:
        total_changes = 0
        if window_size == 1:
            for i in range( len( y ) ):
                noisey_label = noise_single( y[i] )
                total_changes += 1 if y[i] != noisey_label else 0
                y[i] = noisey_label
        else:
            for i in range( len( y ) ):
                noisey_label = noise_multi( y[i] )
                total_changes += np.sum( np.abs( y[i] - noisey_label ) )
                y[i] = noisey_label
    print( 'After adding noise np.sum( y )', np.sum( y ) )
    print( 'Total changes due to noise:', total_changes )
    print( 'Final targets shape:', len( y ) )
    return y




# Preprocess a dataset returning features and labels:
# features is an np.array of shape: n_samples, window_size, 44 * encoding
# labels is an np.array of shape: n_samples OR n_samples, n_classes if window_size > 1
def process_dataset( dataset, encoding = 'bits', window_size = 1, lag = ( 0.45, 0.03 ), noise = False ):
    # Max packet length is 44 bytes
    max_length = 44
    if encoding == 'bits':
        max_length *= 8
    
    packets = []
    if encoding == 'bits':
        for packet, time in zip( dataset['udp.payload'], dataset['time'] ):
            blank_packet = np.zeros( max_length )
            blank_packet[:len( packet ) * 8] += np.unpackbits( np.frombuffer( packet, dtype = 'uint8' ) )
            packets.append( {
                'payload': blank_packet,
                'time': time.timestamp(), # 
            } )
    elif encoding == 'bytes':
        for packet, time in zip( dataset['udp.payload'], dataset['time'] ):
            blank_packet = np.zeros( max_length )
            blank_packet[:len( packet )] += np.frombuffer( packet, dtype = 'uint8' )
            packets.append( {
                'payload': blank_packet,
                'time': time.timestamp(),
            } )
    else:
        print( 'ERROR IN ENCODING: MUST BE ONE OF "bits" OR "BYTES"' )
        return
    
    print( 'Preprocessed packets with', encoding, 'encoding' )
    print( 'Found', len( packets ), 'packets' )
    
    labels = load_labels( dataset )
    print( 'Loaded', len( labels ), 'single packet labels' )
    
    # Add timing noise
    total_noise = 0
    for i in range( len( labels ) ):
        reaction_time = noise_time( lag[0], lag[1] )
        total_noise += reaction_time
        labels[i]['time'] += reaction_time
    
    # Verify noise was added correctly
    labels_ = load_labels( dataset )
    delta = []
    for true, noisey in zip( labels_, labels ):
        delta.append( noisey['time'] - true['time'] )
            
    print( 'Added noise to labels according to distribution N(', lag[0], ',', lag[1], ')' )
    print( 'Total added noise was', total_noise, 'seconds' )
    print( 'Measured added noise was N(', np.mean( delta ), ',', np.std( delta ), ')' )
    
    # Aggregate packets and samples into windows:
    if window_size == 1:
        y = match_timestamps( packets, labels )
        X = np.zeros( ( len( packets ), max_length ) )

        if lag:
            y_ = match_timestamps( packets, labels_ )
            
            diff = 0
            for s1, s2 in zip( y, y_ ):
                if s1 != s2:
                    diff += 1
            print( '### Number of differences was: ', diff )
        
        for i in range( len( packets ) ):
            X[i] += packets[i]['payload']
    else:
        y = match_timestamps_windowed( packets, labels, window_size )
        y = np.array( y )
        y[y>0] = 1
        X = np.zeros( ( len( packets ), max_length ) )
        
        for i in range( len( packets ) ):
            X[i] += packets[i]['payload']
        X = sliding_window_view( X, ( window_size ), axis = 0 ).reshape( -1, max_length * window_size )
    
    print( 'X.shape:', X.shape, ', should be ( n_samples, max_length * window_size )' )
    print( 'y.shape:', len( y ), ', should be ( n_samples, )' )
    print( 'y contains the following unique values' )
    print( np.unique( y ) )
    
    print( 'np.sum( y ):', np.sum( y ) )

    total_changes = 0
    # Add noise to labels
    if noise:
        total_changes = 0
        if window_size == 1:
            for i in range( len( y ) ):
                noisey_label = noise_single( y[i] )
                total_changes += 1 if y[i] != noisey_label else 0
                y[i] = noisey_label
        else:
            for i in range( len( y ) ):
                noisey_label = noise_multi( y[i] )
                total_changes += np.sum( np.abs( y[i] - noisey_label ) )
                y[i] = noisey_label
    print( 'After adding noise np.sum( y )', np.sum( y ) )
    print( 'Total changes due to noise:', total_changes )
    
    return X, y





# def match_timestamps( dataset, targets ):
#     labels = []
    
#     for sample in dataset:
#         # For each sample, iterate through the targets until finding the minimum positive value
#         label = None
#         for i in range( len( targets ) ):
#             label = None

#             # Always update if the time is equal
#             if targets[i]['time'] == sample['time']:
#                 label = targets[i]

#             # Only update if the time is greater, if there isn't already a label
#             elif targets[i]['time'] > sample['time']:
#                 if label == None:
#                     label = targets[i]
#                 elif label != None:
#                     labels.append( label['label'] )
#                     break
#     # If we get to the end of this loop, we ran out of targets
#     if len( labels ) == len( dataset ):
#         print( 'LABELS AND DATASET DIFFERENT SIZE AFTER TIME MATCH' )
#         print( 'ADDING NO EVENT TO CORRECT SIZE', len( dataset ) - len( labels ) )
#         while len( labels ) < len( dataset ):
#             labels.append( 0 )
#     return labels