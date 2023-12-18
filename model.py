import os
from tensorflow.keras.models import load_model
from tensorflow.keras.applications.resnet50 import preprocess_input
from tensorflow.keras.preprocessing import image
import numpy as np
from PIL import Image


# 以下の処理を関数化
def predict(input_filename):
    classes = [
        "alaba",
        "bellingham",
        "camavinga",
        "carvajal",
        "ceballos",
        "courtois",
        "joselu",
        "kroos",
        "militao",
        "modric",
        "nacho",
        "rodrygo",
        "taa",
        "valverde",
        "vazquez",
        "vinicius",
    ]

    # 認識させたい画像の読み込み
    input_image = image.load_img(input_filename, target_size=(224, 224))

    # 画像の前処理
    input_image = image.img_to_array(input_image)
    input_image = np.expand_dims(input_image, axis=0)
    input_image = preprocess_input(input_image)

    model = load_model("./model/ResNet50_conv4_16.h5", compile=False)

    result = model.predict(input_image)

    label = classes[np.argmax(result[0])]
    probability = result[0][np.argmax(result[0])] * 100

    return label, probability
