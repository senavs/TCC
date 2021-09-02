import numpy as np
from keras import Model
from keras.layers import Input, Conv2D, MaxPooling2D, Dense, Flatten, Dropout

from api import settings
from api.modules.preprocessing import pre_processing

TARGET_DECODER = {
    0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
    10: 'div', 11: 'minus', 12: 'parenthesis-closed', 13: 'parenthesis-opened', 14: 'plus', 15: 'times'
}


def build_model() -> Model:
    input_ = Input(shape=settings.preprocessing.IMAGE_SHAPE)

    x = Conv2D(32, kernel_size=(3, 3), padding='same', activation='relu')(input_)
    x = MaxPooling2D(pool_size=(2, 2), padding='same')(x)
    x = Dropout(0.25)(x)

    x = Flatten()(x)

    x = Dense(64, activation='relu')(x)
    x = Dropout(0.5)(x)
    output = Dense(16, activation='softmax')(x)

    model = Model(input_, output)
    model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=["accuracy"])

    return model


def load_model() -> Model:
    model = build_model()
    model.load_weights(settings.model.MODEL_WEIGHTS)

    return model


def predict(model: Model, image: np.ndarray) -> str:
    prediction = model.predict(pre_processing(image))
    return TARGET_DECODER[np.argmax(prediction)]
