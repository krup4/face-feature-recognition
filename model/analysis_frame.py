from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
from io import BytesIO
import numpy as np
import cv2
import os

import logging

import cv2
import torch
from humsis.predictor import Predictor
from timm.utils import setup_default_logging

import download_weights

_logger = logging.getLogger("inference")


class Config:
    detector_weights = 'models_weight/yolov8x_person_face.pt'
    checkpoint = 'models_weight/mivolo.pth.tar'
    resnet_weights = 'models_weight/resnet50.pt'
    device = 'cpu'
    with_persons = True
    disable_faces = False
    draw = False


app = Flask(__name__)


@app.route('/analysis-frame', methods=['POST'])
def upload_frame():
    data = request.get_data()
    bytes_io = BytesIO(data)

    byte_array = np.frombuffer(bytes_io.getvalue(), dtype=np.uint8)

    image = cv2.imdecode(byte_array, cv2.IMREAD_COLOR)
    height, width = image.shape[:2]

    # if torch.cuda.is_available():
    #     torch.backends.cuda.matmul.allow_tf32 = True
    #     torch.backends.cudnn.benchmark = True

    args = Config()
    predictor = Predictor(args, verbose=True)

    detected_objects, out_im = predictor.recognize(image)

    names = detected_objects.yolo_results.names
    pred_boxes = detected_objects.yolo_results.boxes

    annotator = []

    if pred_boxes:
        for bb_ind, (d, age, gender, gender_score, emotion) in enumerate(
            zip(pred_boxes, detected_objects.ages, detected_objects.genders,
                detected_objects.gender_scores, detected_objects.emotions)
        ):
            bbox = {}
            c, conf, guid = int(d.cls), float(
                d.conf), None if d.id is None else int(d.id.item())
            name = ("" if guid is None else f"id:{guid} ") + names[c]
            bbox['name'] = name
            bbox['conf'] = f"{conf:.2f}"
            if age is not None:
                bbox['age'] = f"{age:.1f}"
            if gender is not None:
                bbox['gender'] = 'Ж' if gender == 'female' else 'М'
            if gender_score is not None:
                bbox['gender_score'] = f"({gender_score:.1f})"
            if emotion is not None:
                emotion_names = ['сердитая', 'отвращение',
                                 'страх', 'счастливая', 'нейтральная', 'грустная', 'удивления']
                bbox['emotion'] = emotion_names[emotion]
            bbox['boxes'] = d.xyxy.squeeze().tolist()
            bbox['image_size'] = [height, width]
            annotator.append(bbox)

    if args.draw:
        cv2.imwrite('humsis/online.jpg', out_im)

    return jsonify(annotator), 200, {'ContentType': 'application/json', "Access-Control-Allow-Origin": "*"}


if __name__ == '__main__':
    app.run(host='model', port=5050, debug=True)
