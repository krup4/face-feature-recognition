#!/bin/bash

cd

folder_name="face_feature_recognition"

# Проверка существования папки
if [ -d "./$folder_name" ]; then
    echo "Папка '$folder_name' уже существует"
else
    source_dir="~/face-feature-recognition"
    target_dir="~/"
    find "$source_dir" -maxdepth 1 -type f -exec mv {} "$target_dir" \;
fi

