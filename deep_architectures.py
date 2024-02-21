from keras.models import Sequential
from keras import layers
from keras import regularizers
from keras import metrics

names = [ 'DNN', '1DCNN16', '1DCNN32', '1DCNN64', 'LSTM', 'LSTM2', '1DCNN-LSTM', '2DCNN16', '2DCNN32', '2DCNN64', '2DCNN-LSTM', ]

def get_model( name, window_size, encoding = 'bits' ):
    model = None
    if encoding == 'bits':
        model = get_bits_model( name, window_size )
    elif encoding == 'bytes':
        model = get_bytes_model( name, window_size )

    if model == None:
        raise Exception( 'Called get_model incorrectly!!!! parameters:' + name + encoding )
    
    # Compile model before returning
    model.compile(
        loss = 'binary_crossentropy',
        metrics = [
            'binary_crossentropy',
            # 'binary_accuracy',
            metrics.F1Score(
                average = 'macro', threshold = 0.5,
            )
        ],
    )

    return model

def get_bits_model( name, window_size ):
    model = None
    max_length = 44 * 8
    
    if name == 'DNN':
        model = Sequential( [
            layers.Input( shape = ( window_size, max_length ) ),
            layers.Dense( 64, activation = 'relu', kernel_regularizer = regularizers.L1L2( l1=1e-5, l2 = 0 ) ),
            layers.Dense( 64, activation = 'relu', kernel_regularizer = regularizers.L1L2( l1=1e-5, l2 = 0 ) ),
            layers.Dense( 64, activation = 'relu', kernel_regularizer = regularizers.L1L2( l1=1e-5, l2 = 0 ) ),
            layers.Dense( 64, activation = 'relu', kernel_regularizer = regularizers.L1L2( l1=1e-5, l2 = 0 ) ),
            layers.Dense( 64, activation = 'relu', kernel_regularizer = regularizers.L1L2( l1=1e-5, l2 = 0 ) ),
            layers.Dense( 64, activation = 'relu', kernel_regularizer = regularizers.L1L2( l1=1e-5, l2 = 0 ) ),
            layers.Flatten(),
            layers.Dense( 32, activation = 'relu', kernel_regularizer = regularizers.L1L2( l1=1e-5, l2 = 0 ) ),
            layers.Dropout( 0.2 ),
            layers.Dense( 8, activation = 'sigmoid' ),
            layers.Flatten(),
        ] )
    elif name == '1DCNN16':
        model = Sequential( [
            layers.Input( shape = ( window_size, max_length ) ),
            layers.Reshape( ( -1, 1 ) ),
            layers.Conv1D( 128, kernel_size = ( 16 ), strides = 8, padding = 'same', activation = 'relu', kernel_regularizer = regularizers.L1L2( l1=1e-5, l2 = 0 ) ),
            layers.BatchNormalization(),
        ] )
        
        for i in range( int( window_size // 25 ) ):
            model.add( layers.Conv1D( 128, kernel_size = ( 16 ), strides = 8, padding = 'same', activation = 'relu', kernel_regularizer = regularizers.L1L2( l1=1e-5, l2 = 0 ) ) )
            model.add( layers.BatchNormalization() )
        
        model.add( layers.Flatten() )
        model.add( layers.Dense( 32, activation = 'relu', kernel_regularizer = regularizers.L1L2( l1=1e-5, l2 = 0 ) ) )
        model.add( layers.Dropout( 0.2 ) )
        model.add( layers.Dense( 8, activation = 'sigmoid' ) )
        model.add( layers.Flatten() )
    elif name == '1DCNN32':
        model = Sequential( [
            layers.Input( shape = ( window_size, max_length ) ),
            layers.Reshape( ( -1, 1 ) ),
            layers.Conv1D( 128, kernel_size = ( 32 ), strides = 16, padding = 'same', activation = 'relu', kernel_regularizer = regularizers.L1L2( l1=1e-5, l2 = 0 ) ),
            layers.BatchNormalization(),
        ] )
        
        for i in range( int( window_size // 25 ) ):
            model.add( layers.Conv1D( 128, kernel_size = ( 32 ), strides = 16, padding = 'same', activation = 'relu', kernel_regularizer = regularizers.L1L2( l1=1e-5, l2 = 0 ) ) )
            model.add( layers.BatchNormalization() )
        
        model.add( layers.Flatten() )
        model.add( layers.Dense( 32, activation = 'relu', kernel_regularizer = regularizers.L1L2( l1=1e-5, l2 = 0 ) ) )
        model.add( layers.Dropout( 0.2 ) )
        model.add( layers.Dense( 8, activation = 'sigmoid' ) )
        model.add( layers.Flatten() )
    elif name == '1DCNN64':
        model = Sequential( [
            layers.Input( shape = ( window_size, max_length ) ),
            layers.Reshape( ( -1, 1 ) ),
            layers.Conv1D( 128, kernel_size = ( 64 ), strides = 16, padding = 'same', activation = 'relu', kernel_regularizer = regularizers.L1L2( l1=1e-5, l2 = 0 ) ),
            layers.BatchNormalization(),
        ] )
        
        for i in range( int( window_size // 25 ) ):
            model.add( layers.Conv1D( 128, kernel_size = ( 64 ), strides = 16, padding = 'same', activation = 'relu', kernel_regularizer = regularizers.L1L2( l1=1e-5, l2 = 0 ) ) )
            model.add( layers.BatchNormalization() )
        
        model.add( layers.Flatten() )
        model.add( layers.Dense( 32, activation = 'relu', kernel_regularizer = regularizers.L1L2( l1=1e-5, l2 = 0 ) ) )
        model.add( layers.Dropout( 0.2 ) )
        model.add( layers.Dense( 8, activation = 'sigmoid' ) )
        model.add( layers.Flatten() )
    elif name == 'LSTM':
        model = Sequential( [
            layers.Input( shape = ( window_size, max_length ) ),
            layers.Dense( 128, activation = 'relu', kernel_regularizer = regularizers.L1L2( l1=1e-6, l2 = 0 ) ),
            layers.LSTM( 64, activation = 'tanh', kernel_regularizer = regularizers.L1L2( l1=1e-6, l2 = 0 ) ),
            layers.Dropout( 0.2 ),
            layers.Dense( 64, activation = 'relu' ),
            layers.Dropout( 0.2 ),
            layers.Dense( 32, activation = 'relu' ),
            layers.Dropout( 0.2 ),
            layers.Dense( 8, activation = 'sigmoid' ),
        ] )
    elif name == 'LSTM2':
        model = Sequential( [
            layers.Input( shape = ( window_size, max_length ) ),
            layers.Dense( 128, activation = 'relu', kernel_regularizer = regularizers.L1L2( l1=1e-5, l2 = 0 ) ),
            layers.LSTM( 64, activation = 'tanh', return_sequences = True, kernel_regularizer = regularizers.L1L2( l1=1e-6, l2 = 0 ) ),
            layers.Dropout( 0.2 ),
            layers.LSTM( 64, activation = 'tanh', kernel_regularizer = regularizers.L1L2( l1=1e-6, l2 = 0 ) ),
            layers.Dropout( 0.2 ),
            layers.Dense( 64, activation = 'relu' ),
            layers.Dropout( 0.2 ),
            layers.Dense( 32, activation = 'relu', kernel_regularizer = regularizers.L1L2( l1=1e-5, l2 = 0 ) ),
            layers.Dense( 8, activation = 'sigmoid' ),
        ] )
    elif name == '1DCNN-LSTM' :
        model = Sequential( [
            layers.Input( shape = ( window_size, max_length ) ),
            layers.Reshape( ( -1, 1 ) ),
            layers.Conv1D( 256, kernel_size = ( 4 * 8 ), strides = 2 * 8, padding = 'same', activation = 'relu', kernel_regularizer = regularizers.L1L2( l1=1e-6, l2 = 0 ) ),
            layers.BatchNormalization(),
            layers.Dropout( 0.2 ),
            layers.Reshape( ( window_size, -1 ) ),
            layers.Dense( 128, activation = 'relu', kernel_regularizer = regularizers.L1L2( l1=1e-6, l2 = 0 ) ),
            layers.LSTM( 128, kernel_regularizer = regularizers.L1L2( l1=1e-6, l2 = 0 ) ),
            layers.Dropout( 0.2 ),
            layers.Dense( 32, activation = 'relu', kernel_regularizer = regularizers.L1L2( l1=1e-6, l2 = 0 ) ),
            layers.Dropout( 0.2 ),
            layers.Dense( 8, activation = 'sigmoid' ),
        ] )
    return model


def get_bytes_model( name, window_size ):
    model = None
    max_length = 44
    
    if name == 'DNN':
        model = Sequential( [
            layers.Input( shape = ( window_size, max_length ) ),
            layers.Dense( 64, activation = 'relu', kernel_regularizer = regularizers.L1L2( l1=1e-5, l2 = 0 ) ),
            layers.Dense( 64, activation = 'relu', kernel_regularizer = regularizers.L1L2( l1=1e-5, l2 = 0 ) ),
            layers.Dense( 64, activation = 'relu', kernel_regularizer = regularizers.L1L2( l1=1e-5, l2 = 0 ) ),
            layers.Dense( 64, activation = 'relu', kernel_regularizer = regularizers.L1L2( l1=1e-5, l2 = 0 ) ),
            layers.Dense( 64, activation = 'relu', kernel_regularizer = regularizers.L1L2( l1=1e-5, l2 = 0 ) ),
            layers.Dense( 64, activation = 'relu', kernel_regularizer = regularizers.L1L2( l1=1e-5, l2 = 0 ) ),
            layers.Flatten(),
            layers.Dense( 32, activation = 'relu', kernel_regularizer = regularizers.L1L2( l1=1e-5, l2 = 0 ) ),
            layers.Dropout( 0.2 ),
            layers.Dense( 8, activation = 'sigmoid' ),
            layers.Flatten(),
        ] )
    elif name == '1DCNN16':
        model = Sequential( [
            layers.Input( shape = ( window_size, max_length ) ),
            layers.Reshape( ( -1, 1 ) ),
            layers.Conv1D( 128, kernel_size = ( 2 ), strides = 2, padding = 'valid', activation = 'relu', kernel_regularizer = regularizers.L1L2( l1=1e-6, l2 = 0 ) ),
            layers.BatchNormalization(),
            layers.Conv1D( 128, kernel_size = ( 2 ), strides = 2, padding = 'valid', activation = 'relu', kernel_regularizer = regularizers.L1L2( l1=1e-6, l2 = 0 ) ),
            layers.BatchNormalization(),
        ] )
        
        for i in range( int( window_size // 25 ) ):
            model.add( layers.Conv1D( 128, kernel_size = ( 2 ), strides = 1, padding = 'same', activation = 'relu', kernel_regularizer = regularizers.L1L2( l1=1e-6, l2 = 0 ) ) )
            model.add( layers.BatchNormalization() )
        
        model.add( layers.Flatten() )
        model.add( layers.Dense( 32, activation = 'relu', kernel_regularizer = regularizers.L1L2( l1=1e-5, l2 = 0 ) ) )
        model.add( layers.Dropout( 0.2 ) )
        model.add( layers.Dense( 8, activation = 'sigmoid' ) )
        model.add( layers.Flatten() )
    elif name == '1DCNN32':
        model = Sequential( [
            layers.Input( shape = ( window_size, max_length ) ),
            layers.Reshape( ( -1, 1 ) ),
            layers.Conv1D( 128, kernel_size = ( 4 ), strides = 2, padding = 'valid', activation = 'relu', kernel_regularizer = regularizers.L1L2( l1=1e-6, l2 = 0 ) ),
            layers.BatchNormalization(),
            layers.Conv1D( 128, kernel_size = ( 4 ), strides = 2, padding = 'valid', activation = 'relu', kernel_regularizer = regularizers.L1L2( l1=1e-6, l2 = 0 ) ),
            layers.BatchNormalization(),
        ] )
        
        for i in range( int( window_size // 25 ) ):
            model.add( layers.Conv1D( 128, kernel_size = ( 4 ), strides = 2, padding = 'same', activation = 'relu', kernel_regularizer = regularizers.L1L2( l1=1e-6, l2 = 0 ) ) )
            model.add( layers.BatchNormalization() )
        
        model.add( layers.Flatten() )
        model.add( layers.Dense( 32, activation = 'relu', kernel_regularizer = regularizers.L1L2( l1=1e-5, l2 = 0 ) ) )
        model.add( layers.Dropout( 0.2 ) )
        model.add( layers.Dense( 8, activation = 'sigmoid' ) )
        model.add( layers.Flatten() )
    elif name == '1DCNN64':
        model = Sequential( [
            layers.Input( shape = ( window_size, max_length ) ),
            layers.Reshape( ( -1, 1 ) ),
            layers.Conv1D( 128, kernel_size = ( 8 ), strides = 2, padding = 'valid', activation = 'relu', kernel_regularizer = regularizers.L1L2( l1=1e-6, l2 = 0 ) ),
            layers.BatchNormalization(),
            layers.Conv1D( 128, kernel_size = ( 8 ), strides = 2, padding = 'valid', activation = 'relu', kernel_regularizer = regularizers.L1L2( l1=1e-6, l2 = 0 ) ),
            layers.BatchNormalization(),
        ] )
        
        for i in range( int( window_size // 25 ) ):
            model.add( layers.Conv1D( 128, kernel_size = ( 8 ), strides = 2, padding = 'same', activation = 'relu', kernel_regularizer = regularizers.L1L2( l1=1e-6, l2 = 0 ) ) )
            model.add( layers.BatchNormalization() )
        
        model.add( layers.Flatten() )
        model.add( layers.Dense( 32, activation = 'relu', kernel_regularizer = regularizers.L1L2( l1=1e-5, l2 = 0 ) ) )
        model.add( layers.Dropout( 0.2 ) )
        model.add( layers.Dense( 8, activation = 'sigmoid' ) )
        model.add( layers.Flatten() )
    elif name == 'LSTM':
        model = Sequential( [
            layers.Input( shape = ( window_size, max_length ) ),
            layers.Dense( 128, activation = 'relu', kernel_regularizer = regularizers.L1L2( l1=1e-6, l2 = 0 ) ),
            layers.LSTM( 64, activation = 'tanh', kernel_regularizer = regularizers.L1L2( l1=1e-6, l2 = 0 ) ),
            layers.Dropout( 0.2 ),
            layers.Dense( 64, activation = 'relu' ),
            layers.Dropout( 0.2 ),
            layers.Dense( 32, activation = 'relu' ),
            layers.Dropout( 0.2 ),
            layers.Dense( 8, activation = 'sigmoid' ),
        ] )
    elif name == 'LSTM2':
        model = Sequential( [
            layers.Input( shape = ( window_size, max_length ) ),
            layers.Dense( 128, activation = 'relu', kernel_regularizer = regularizers.L1L2( l1=1e-5, l2 = 0 ) ),
            layers.LSTM( 64, activation = 'tanh', return_sequences = True, kernel_regularizer = regularizers.L1L2( l1=1e-6, l2 = 0 ) ),
            layers.Dropout( 0.2 ),
            layers.LSTM( 64, activation = 'tanh', kernel_regularizer = regularizers.L1L2( l1=1e-6, l2 = 0 ) ),
            layers.Dropout( 0.2 ),
            layers.Dense( 64, activation = 'relu' ),
            layers.Dropout( 0.2 ),
            layers.Dense( 32, activation = 'relu', kernel_regularizer = regularizers.L1L2( l1=1e-5, l2 = 0 ) ),
            layers.Dense( 8, activation = 'sigmoid' ),
        ] )
    elif name == '1DCNN-LSTM' :
        model = Sequential( [
            layers.Input( shape = ( window_size, max_length ) ),
            layers.Reshape( ( -1, 1 ) ),
            layers.Conv1D( 256, kernel_size = ( 4 ), strides = 2, padding = 'same', activation = 'relu', kernel_regularizer = regularizers.L1L2( l1=1e-6, l2 = 0 ) ),
            layers.BatchNormalization(),
            layers.Dropout( 0.2 ),
            layers.Reshape( ( window_size, -1 ) ),
            layers.Dense( 128, activation = 'relu', kernel_regularizer = regularizers.L1L2( l1=1e-6, l2 = 0 ) ),
            layers.LSTM( 128, kernel_regularizer = regularizers.L1L2( l1=1e-6, l2 = 0 ) ),
            layers.Dropout( 0.2 ),
            layers.Dense( 32, activation = 'relu', kernel_regularizer = regularizers.L1L2( l1=1e-6, l2 = 0 ) ),
            layers.Dropout( 0.2 ),
            layers.Dense( 8, activation = 'sigmoid' ),
        ] )
    return model