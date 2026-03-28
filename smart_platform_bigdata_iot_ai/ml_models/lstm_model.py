import numpy as np
from keras.models import Sequential
from keras.layers import LSTM, Dense

def create_model():
    model = Sequential()
    model.add(LSTM(50, input_shape=(10, 1)))
    model.add(Dense(1))
    model.compile(optimizer='adam', loss='mse')
    return model