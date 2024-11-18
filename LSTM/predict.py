from LSTM.DataProcess import *
import numpy as np


def pred(input_data,model):
    feature_dim = input_data.shape[1]
    data = Norm(input_data)
    input = data.reshape(1,10,feature_dim)
    res = model.predict(input)
    return num2label(np.argmax(res))