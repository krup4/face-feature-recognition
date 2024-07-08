import os
import urllib.request

import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
)

directory = os.path.join(os.getcwd(), 'models_weight/')

url = 'https://www.kaggle.com/api/v1/models/krupn0ff/face-feature-recognition/pyTorch/weights/1/download/'

filename1 = "mivolo.pth.tar"
filename2 = "resnet50.pt"
filename3 = "yolov8x_person_face.pt"

if os.path.isdir(directory):
    logging.info("Папка уже существует")
else:
    os.makedirs(directory)
    logging.info("Папка создана")

if os.path.exists(os.path.join(directory, filename1)) and os.path.exists(os.path.join(directory, filename2)) and os.path.exists(os.path.join(directory, filename3)):
    logging.info("Файлы существует!")
else:
    logging.info("Установка весов!")

    if not os.path.exists(os.path.join(directory, filename1)):
        urllib.request.urlretrieve(
            url + filename1, os.path.join(directory, filename1))

    if not os.path.exists(os.path.join(directory, filename2)):
        urllib.request.urlretrieve(
            url + filename2, os.path.join(directory, filename2))

    if not os.path.exists(os.path.join(directory, filename3)):
        urllib.request.urlretrieve(
            url + filename3, os.path.join(directory, filename3))

    logging.info("Файлы скачаны!")
