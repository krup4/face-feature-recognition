import logging

import cv2
import torch
from humsis.predictor import Predictor
from timm.utils import setup_default_logging

_logger = logging.getLogger("inference")


class Config:
    detector_weights = 'models_weight/yolov8x_person_face.pt'
    checkpoint = 'models_weight/model_imdb_cross_person_4.22_99.46.pth.tar'
    device = 'cuda:0'
    with_persons = True
    disable_faces = False
    draw = True


def main():
    # setup_default_logging()

    if torch.cuda.is_available():
        torch.backends.cuda.matmul.allow_tf32 = True
        torch.backends.cudnn.benchmark = True

    args = Config()
    predictor = Predictor(args, verbose=True)

    # detected_objects, out_im = predictor.recognize(
    #     cv2.imread('photo_2024-07-02_12-32-12.jpg'))

    camera = cv2.VideoCapture(0)

    ret, _ = camera.read()
    while not ret:
        ret, _ = camera.read()

    while True:
        _, img = camera.read()
        detected_objects, out_im = predictor.recognize(img)

        if args.draw:
            cv2.imshow('Online', out_im)

        if cv2.waitKey(1) == ord('q'):
            break

    camera.release()

    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
