# Translation of lemmatized text into Russian Sign language video
Russian had no open analogues at the time of the development of this project, and we would like other teams to be able to use our work in their projects and promote the topic of creating animations of Russian sign language, since there are many nuances in this area, ranging from transitions between gestures and ending up to the transmission of the correct intonation using gestures.

✅On support.

## Contents
- [Technologies](#Technologies)
- [Development](#Development)
- [Demo](#Demo)
- [TODO](#TODO)
- [Sources](#Sources)

## <a name="Technologies">Technologies</a>
- [MediaPipe](https://mediapipe.readthedocs.io/en/latest/)
- [OpenCV](https://opencv.org/)

## <a name="Development">Development</a>
![plans](https://github.com/Malginn/Gloss2Pose/assets/89131328/a2f84837-0d4b-486a-9fc1-eb16e6b60cc5)

"The project is designed to minimize the need for direct model inference to generate key points and images. Instead, it allows for the extraction of data directly from a pre-built database containing key points and lemmatized words. These data can then be connected using transition algorithms, which in this case operate linearly, selecting the shortest path between consecutive states.

The dev directory is the root, we have modules:
- `keypoints_creator.py` for converting videos to dots(Creating a language database)
- `combined_jsons.py` to combine json files of words into a single file for further processing
- `smooth_transition.py` to create smooth transitions between the last extreme frames (linear transition, requires revision)
- `create_show_frames.py` to create JPEG images and test the resulting skeletons
- `frames_to_video.py` to create a video from the received frames with a given fps, adjusted to the timeline of the video

### On this __drive__ you can find all the data that was used or generated in this project [Google Drive](https://drive.google.com/drive/folders/1fTvgyfbYXH-9kYn9OYU3ISHZQnuNmelm?usp=sharing)
-----------

## <a name="Demo">Demo</a>

[https://github.com/Malginn/Rail_segm/assets/89131328/8f164965-b0aa-4881-959d-b8ba9276bfdb](https://github.com/Malginn/Gloss2Pose/assets/89131328/c0706620-fa3b-4061-916b-ae01f6527095)

## <a name="TODO">TODO</a>:
- Enrich training examples to improve model accuracy
- Play with threshold values `IoU` and `Conf`


## <a name="Sources">Sources</a>
- [Dataset "Slovo"](https://developers.sber.ru/portal/products/slovo)
- [Mediapipe docs](https://mediapipe.readthedocs.io/en/latest/)
- 
