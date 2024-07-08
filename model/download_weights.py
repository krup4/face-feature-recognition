import os
import kagglehub
import shutil

directory = '/opt/model/models_weight/'

filename1 = "mivolo.pth.tar"
filename2 = "resnet50.pt"
filename3 = "yolov8x_person_face.pt"

if os.path.isdir(directory):
    print("Папка уже существует")
else:
    os.makedirs(directory)
    print("Папка создана")

if os.path.exists(directory + filename1):
    print(f"Файл {filename1} существует!")
else:
    path = kagglehub.model_download("krupn0ff/face-feature-recognition/pyTorch/weights")
    print("Path to model files:", path)
    
    start = os.path.join(path, filename1)
    end = os.path.join(directory, filename1)

    if os.path.isfile(start):
        shutil.move(start, end)

    start = os.path.join(path, filename2)
    end = os.path.join(directory, filename2)

    if os.path.isfile(start):
        shutil.move(start, end)

    start = os.path.join(path, filename3)
    end = os.path.join(directory, filename3)

    if os.path.isfile(start):
        shutil.move(start, end)
