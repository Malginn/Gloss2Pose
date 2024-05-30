# Translation of lemmatized text into Russian Sign language video
Russian had no open analogues at the time of the development of this project, and we would like other teams to be able to use our work in their projects and promote the topic of creating animations of Russian sign language, since there are many nuances in this area, ranging from transitions between gestures and ending up to the transmission of the correct intonation using gestures.

✅On support.

## Contents
- [Technologies](#Technologies)
- [Usage](#Usage)
- [Development](#Development)
- [Demo](#Demo)
- [TODO](#TODO)
- [Sources](#Sources)

## <a name="Technologies">Technologies</a>
- [MediaPipe](https://mediapipe.readthedocs.io/en/latest/)
- [OpenCV](https://opencv.org/)
## <a name="Usage">Usage</a>
To install the project, just ___clone the project___ and install the dependencies from the ___requirement.txt___ file

```sh
pip install -r requirements.txt
```

To run, configure the paths for the `code/model/inference.ipynb` file and run the code for training or forward pass

To view the metric values ​​that the model received during training, view the `results` folder


## <a name="Development">Development</a>
During development, the version of CUDA 12.1 for pytorch was used, so the same version is indicated in the requirements file
```
torch==2.2.1+cu121
torcaudio==2.2.1+cu121
torchvision==0.17.1+cu121
```
Check if these cuda and __cuDNN__ drivers match

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
