#!/bin/bash

directory="./models_weight/"

filename1="mivolo.pth.tar"
filename2="resnet50.pt"
filename3="yolov8x_person_face.pt"

url="https://www.kaggle.com/models/krupn0ff/face-feature-recognition"


if [ -d "$directory" ]; then
    echo "Папка '$directory' существует"
else
    mkdir "$directory"

    if [ $? -eq 0 ]; then
        echo "Папка '$directory' успешно создана."
    else
        echo "Ошибка при создании папки."
        exit 1
    fi
fi

cd models_weight

if [ -f "./$filename1" ]; then
    echo "File '$filename1' is already exist'"
else
    curl https://www.kaggle.com/models/krupn0ff/face-feature-recognition -o ./mivolo.pth.tar
    
    if [ $? -eq 0 ]; then
        echo "Файл '$filename1' успешно скачан."
    else
        echo "Ошибка при скачивании файла."
        exit 1
    fi
fi


if [ -f "./$filename2" ]; then
    echo "File '$filename2' is already exist'"
else
    curl "$url" -o "./$filename2"
    if [ $? -eq 0 ]; then
        echo "Файл '$filename2' успешно скачан."
    else
        echo "Ошибка при скачивании файла."
        exit 1
    fi
fi


if [ -f "./$filename3" ]; then
    echo "File '$filename3' is already exist'"
else
    curl "$url" -o "./$filename3"
    if [ $? -eq 0 ]; then
        echo "Файл '$filename3' успешно скачан."
    else
        echo "Ошибка при скачивании файла."
        exit 1
    fi
fi
