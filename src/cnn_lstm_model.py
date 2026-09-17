import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv1D, MaxPooling1D, LSTM, Dense, Dropout

def cnn_lstm(shape, classes):
    '''CNN-LSTM network analyzes stride to stride times
    The 1D CNN extracts local feature patterns from the gait rhythms
    The LSTM analyzes the long term chronologic dependencies.'''
    model = Sequential([
        Conv1D(filters=64, kernel_size=3, activation='relu', shape=shape),
        MaxPooling1D(pool_size=2),
        LSTM(100, return_sequences=False),
        Dropout(0.5),
        Dense(classes, activation='softmax')
    ])
    
    model.compile(loss='categorical_crossentropy', 
                  optimizer='adam', 
                  metrics=['accuracy'])
    return model
