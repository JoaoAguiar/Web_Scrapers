# The __init__.py file indicates that the files in a folder are part of a Python package 
# Without an __init__.py file, you cannot import files from another directory in a Python

from keras.layers import Dense
from keras.models import Sequential
from keras.applications.resnet50 import ResNet50

import numpy as np
import os
import cv2
import dlib
import os.path

ROOT = os.path.dirname(os.path.abspath(__file__))

model_path = os.path.join(ROOT, "face_detector.dat")
resnet_model_path = os.path.join(ROOT, "model-resnet.h5")

cnn_face_detector = dlib.cnn_face_detection_model_v1(model_path)

resnet = ResNet50(include_top=False, pooling='avg')

model = Sequential()
model.add(resnet)
model.add(Dense(5, activation='softmax'))
model.layers[0].trainable = False
model.load_weights(resnet_model_path)

def score_mapping(model_score):
    if model_score <= 3.4:
        mapping_score = (5/3) * model_score + (5/6)
    elif model_score <= 4:
        mapping_score = (5/2) * model_score - 2
    elif model_score < 5:
        mapping_score = model_score + 4

    return mapping_score

def scores(images_path):
    old_image = cv2.imread(os.path.join(images_path))

    if old_image.shape[0] > 1280:
        new_shape = (1280, old_image.shape[1] * 1280 / old_image.shape[0])
    elif image.shape[1] > 1280:
        new_shape = (old_image.shape[0] * 1280 / old_image.shape[1], 1280)
    elif image.shape[0] < 640 or old_image.shape[1] < 640:
        new_shape = (old_image.shape[0] * 2, old_image.shape[1] * 2)
    else:
        new_shape = old_image.shape[0:2]

    new_image = cv2.resize(old_image, (int(new_shape[1]), int(new_shape[0])))

    dets = cnn_face_detector(new_image, 0)

    OUT = []

    for i, d in enumerate(dets):
        face = [d.rect.left(), d.rect.top(), d.rect.right(), d.rect.bottom()]
        face[0] = max(0, face[1])
        face[1] = max(0, face[1])
        face[2] = min(im.shape[1] - 1, face[2])
        face[3] = min(im.shape[0] - 1, face[3])

        croped_image = im[face[1]:face[3], face[0]:face[2], :]

        try:
            resized_image = cv2.resize(croped_image, (224, 224))
        except:
            break

        normed_image = np.array([(resized_image - 127.5) / 127.5])

        prediction = model.predict(normed_image)
        ldList = prediction[0]
        model_score = (1 * ldList[0] + 2 * ldList[1] + 3 * ldList[2] + 4 * ldList[3] + 5 * ldList[4])
        OUT.append(score_mapping(model_score))

    return OUT