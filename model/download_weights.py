import os
import kagglehub
import shutil

directory = '/opt/model/models_weight'
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
    path = kagglehub.model_download("krupn0ff/face-feature-recognition/pyTorch/weights", filename1)
    print("Path to model file 1:", path)
    
    end = os.path.join(directory, filename1)

    if os.path.isfile(path):
        shutil.move(path, end)

    path = kagglehub.model_download("krupn0ff/face-feature-recognition/pyTorch/weights", filename2)
    print("Path to model file 2:", path)
    
    end = os.path.join(directory, filename2)

    if os.path.isfile(path):
        shutil.move(path, end)

    path = kagglehub.model_download("krupn0ff/face-feature-recognition/pyTorch/weights", filename3)
    print("Path to model file 3:", path)
    
    end = os.path.join(directory, filename3)

    if os.path.isfile(path):
        shutil.move(path, end)