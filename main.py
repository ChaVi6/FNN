from keras.layers import Dense, Activation, Dropout, Convolution2D, MaxPooling2D, Flatten
from keras.models import Sequential

def build_model(hidden_layers, shape):
    if hidden_layers < 1:
        hidden_layers = 1
    structure = [Convolution2D(filters=32, kernel_size=(3, 3),
                               strides=(1, 1), padding='same',
                               input_shape=shape[1:]),
                 Activation('relu'),
                 MaxPooling2D(pool_size=(2, 2), strides=2),
                 Dropout(0.25), Flatten()]
    for i in range(1, hidden_layers + 1):
        structure.append(Dense(int(512 / (2 * i)), activation="relu"))
        structure.append(Dropout(0.5))
    structure.append(Dense(6, activation="sigmoid"))
    return Sequential(structure)

def normalize_prediction(pred):
    max1, max2 = sorted(pred)[4:]
    for i in range(0, 6):
        if pred[i] == max1 or pred[i] == max2:
            pred[i] = 1
        else:
            pred[i] = 0
    return pred
