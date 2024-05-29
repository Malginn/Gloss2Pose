import cv2
import os


def images_to_video(input_folder, output_video, fps):
    image_files = [
        input_folder + f"image_{i}.jpg" for i in range(len(os.listdir(input_folder)))
    ]

    frame = cv2.imread(image_files[0])
    height, width, _ = frame.shape

    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    video_writer = cv2.VideoWriter(output_video, fourcc, fps, (width, height))

    for image_path in image_files:
        frame = cv2.imread(image_path)
        video_writer.write(frame)

    video_writer.release()


# Укажите папку с изображениями, выходное видео и частоту кадров (FPS)
input_folder = "./imgs_to_videos/"
output_video = "./result_video/update10.mp4"
fps = 30

images_to_video(input_folder, output_video, fps)
