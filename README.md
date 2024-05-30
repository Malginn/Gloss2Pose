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
![plans](https://github.com/Malginn/Gloss2Pose/assets/89131328/0f844cab-8ba8-40ea-989a-11a8053a15ce)

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
- [RailSem19: A Dataset for Semantic Rail Scene Understanding](https://openaccess.thecvf.com/content_CVPRW_2019/papers/WAD/Zendel_RailSem19_A_Dataset_for_Semantic_Rail_Scene_Understanding_CVPRW_2019_paper.pdf)
- [Сегментация железнодорожных путей современными сверточными нейронными сетями](https://www.researchgate.net/publication/371681469_Segmentacia_zeleznodoroznyh_putej_sovremennymi_svertocnymi_nejronnymi_setami)
