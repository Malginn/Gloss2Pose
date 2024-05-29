import mediapipe as mp
from mediapipe.framework.formats import landmark_pb2

import time
import ast
import json
import os

import cv2
import random
import numpy as np
import matplotlib.pyplot as plt

from google.protobuf.internal.containers import RepeatedCompositeFieldContainer


file_path_to_write = "path_to_empty.json"
# img_path = r"C:\Users\ivano\Desktop\SBER\demo2.jpg"


def record_points_file(data_to_draw, results, file_name):
    """
    Записываем результаты в файл для добавления в БД
    """
    names_landmarks = {}
    if results.face_landmarks is not None:
        names_landmarks["face"] = results.face_landmarks.landmark
    if results.right_hand_landmarks is not None:
        names_landmarks["right_hand"] = results.right_hand_landmarks.landmark
    if results.left_hand_landmarks is not None:
        names_landmarks["left_hand"] = results.left_hand_landmarks.landmark
    if results.pose_landmarks is not None:
        names_landmarks["pose"] = results.pose_landmarks.landmark

    data_to_write = {}
    for name in names_landmarks.keys():
        points = []
        for landmark in names_landmarks[name]:
            points.append(
                {"x": landmark.x, "y": landmark.y, "z": landmark.z, "visibility": 1}
            )

        data_to_write[name] = points

    data_to_draw.append(data_to_write)

    return data_to_draw


# def calculate_average_fps(current_fps, fps_buffer):
#     # Добавляем текущее значение в буфер
#     fps_buffer.pop(0)
#     fps_buffer.append(current_fps)

#     # Вычисляем среднее значение в буфере
#     average_fps = sum(fps_buffer) / len(fps_buffer)

#     return average_fps, fps_buffer


# Grabbing the Holistic Model from Mediapipe and
# Initializing the Model
mp_holistic = mp.solutions.holistic
holistic_model = mp_holistic.Holistic(
    min_detection_confidence=0.75, min_tracking_confidence=0.5
)


# (0) in VideoCapture is used to connect to your computer's default camera
capture = cv2.VideoCapture("videopath")

data_to_draw = []
while capture.isOpened():
    ret, frame = capture.read()
    if not ret:
        print("Конец видефайла")
        break

    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    image.flags.writeable = False
    results = holistic_model.process(image)
    data_to_write = record_points_file(data_to_draw, results, file_path_to_write)


with open(file_path_to_write, "w") as file:
    json.dump(data_to_write, file)
print("Файл успешно записан!")
