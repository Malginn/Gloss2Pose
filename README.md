# Task Gloss2Pose
Этот проект решает задачу по переводу русского языка жестов в сгенерированные позы

✅In progress.

## Contents
- [TODO](#TODO)
- [Sources](#Sources)
  
## <a name="TODO">TODO</a>:
1) Выделение ключевых точек из кадров видео жестов датасета "Slovo"
  +  Mediapipe лучше всего справляется с этой задачей и удобна в использовании
  +  Ключевые точки рук состоят из 21 точки(см документацию mediapipe)
  +  Модель holistic в mediapipe полностью рисует скелет человека вместе с руками
  - Выводить скелет на черном фоне
  - Нужно научиться останавливаться и отрисовывать точки только на кадрах с жестами, то есть сделать поиск по видео соседних похожих кадров с каким-то пороговым значением(т.к. человек в этот момент останавливается)
  - Пробежать какую-то часть датасета и составить словарь с аннотацией pose2gloss
  - Построить полный пайплайн перевода куска видео в словарь
3) Сопоставить с аннотацией глоссов датасета и сделать инверсию в gloss2pose
4) Визуализировать полученные позы в качестве тестирования
5) Создать плавные переходы между изображениями -> mp4 (прим. Сглаживание Савицкого-Голея + конкатенация)

## <a name="Sources">Sources</a>
- [Mediapipe для выделения ключевых точек из изображений](https://developers.google.com/mediapipe)
- [Датастет РЯЖ](https://habr.com/ru/companies/sberdevices/articles/737018/)
