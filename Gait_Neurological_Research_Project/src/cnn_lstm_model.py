import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv1D, MaxPooling1D, LSTM, Dense, Dropout

def build_cnn_lstm(input_shape, num_classes):
    '''
    Builds a CNN-LSTM network to analyze temporal stride-to-stride windows.
    The 1D CNN extracts local feature patterns from the gait rhythms, 
    and the LSTM analyzes the long-term chronologic dependencies.
    '''
    model = Sequential([
        Conv1D(filters=64, kernel_size=3, activation='relu', input_shape=input_shape),
        MaxPooling1D(pool_size=2),
        LSTM(100, return_sequences=False),
        Dropout(0.5),
        Dense(num_classes, activation='softmax')
    ])
    
    model.compile(loss='categorical_crossentropy', 
                  optimizer='adam', 
                  metrics=['accuracy'])
    return model
