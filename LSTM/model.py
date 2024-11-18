from keras.models import Sequential
from keras.layers import Flatten, Dense, LSTM


def lstm(timestep,feature_dim,output_size):
    model = Sequential()
    model.add(LSTM(activation='relu', units=128,
                   input_shape=(timestep, feature_dim)))
    model.add(Dense(units=output_size,activation = "softmax"))
    return model