# pip install opencv-python mediapipe msvc-runtime
import mediapipe as mp
from mediapipe.framework.formats import landmark_pb2

import time
import json
import ast
import os
import shutil

import cv2
import random
import numpy as np
import matplotlib.pyplot as plt

from google.protobuf.internal.containers import RepeatedCompositeFieldContainer


# Grabbing the Holistic Model from Mediapipe and
# Initializing the Model
mp_holistic = mp.solutions.holistic
holistic_model = mp_holistic.Holistic(
    min_detection_confidence=0.75, min_tracking_confidence=0.5
)
# Initializing the drawing utils for drawing the facial landmarks on image
mp_drawing = mp.solutions.drawing_utils
drawing_spec_lines_r = mp_drawing.DrawingSpec(
    color=(255, 0, 0), thickness=2, circle_radius=1
)
drawing_spec_lines_l = mp_drawing.DrawingSpec(
    color=(0, 255, 0), thickness=2, circle_radius=1
)


desired_width = 1080  # 1246
desired_height = 920  # 885


def read_points(file):
    if type(file) is str:

        with open(file, "r") as f:
            data = json.load(f)
    else:
        data = file

    data_to_draw = []
    for obj in data:
        dict_to_draw = {}
        for name in obj.keys():
            landmark_list = landmark_pb2.NormalizedLandmarkList()
            for point in obj[name]:
                # Добвление NormalizedLandmark в NormalizedLandmarkList
                landmark = landmark_list.landmark.add()
                landmark.x = point["x"]
                landmark.y = point["y"]
                landmark.z = point["z"]
                # if name == 'pose':
                #     landmark.visibility = point['visibility']
            print(f"Точки прочитаны успешно! для {name}\n")
            dict_to_draw[name] = landmark_list
        data_to_draw.append(dict_to_draw)

    print("Работа завершена!")
    return data_to_draw


def show_landmarks(dict_to_draw, image, iter):
    print("Создание класса визуализации...")
    if "pose" in dict_to_draw.keys():
        # Теперь вы можете использовать pose_landmarks с функцией draw_landmarks
        mp_drawing.draw_landmarks(
            image, dict_to_draw["pose"], mp_holistic.POSE_CONNECTIONS
        )
    if "face" in dict_to_draw.keys():
        # Drawing the Facial Landmarks
        mp_drawing.draw_landmarks(
            image,
            dict_to_draw["face"],
            mp_holistic.FACEMESH_CONTOURS,
            mp_drawing.DrawingSpec(color=(255, 0, 255), thickness=1, circle_radius=1),
            mp_drawing.DrawingSpec(color=(0, 255, 255), thickness=1, circle_radius=1),
        )

    if "right_hand" in dict_to_draw.keys():
        # Drawing Right hand Land Marks
        mp_drawing.draw_landmarks(
            image,
            dict_to_draw["right_hand"],
            mp_holistic.HAND_CONNECTIONS,
            connection_drawing_spec=drawing_spec_lines_r,
        )

    if "left_hand" in dict_to_draw.keys():
        # Drawing Left hand Land Marks
        mp_drawing.draw_landmarks(
            image,
            dict_to_draw["left_hand"],
            mp_holistic.HAND_CONNECTIONS,
            connection_drawing_spec=drawing_spec_lines_l,
        )

    print("Класс создан без ошибок!\n")

    # print('Вывод изображения...')
    # cv2.imshow("Facial and Hand Landmarks", image)
    # cv2.waitKey(100)
    # # cv2.destroyAllWindows()
    # print('Работа завершена!')
    cv2.imwrite(f"./imgs_to_videos/image_{iter}.jpg", image)


# data_to_write = record_points_file(results)
result_points = read_points(
    "../test_draw/results_video_new_task_td/combined_frames.json"
)  # data_to_write


for idx, points in enumerate(result_points):
    image = np.zeros((desired_width, desired_height), np.uint8)
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    show_landmarks(points, image, idx)
# cv2.destroyAllWindows()
