import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
import torchvision.models as models
from torchvision import transforms

data_transforms = transforms.Compose([
    transforms.Resize(224),
    transforms.CenterCrop(224),
    transforms.Normalize((0.5, ), (0.5, ))
])


class ResNet:
    def __init__(self, resnet_weights, device='cuda', num_classes=7):
        self.device = device

        self.model = models.resnet50()
        num_ftrs = self.model.fc.in_features
        self.model.fc = nn.Linear(num_ftrs, num_classes)
        self.model.load_state_dict(torch.load(
            resnet_weights, map_location=torch.device(device)))
        self.model = self.model.to(device)
        self.model.eval()

    def crops_face(self, image: np.ndarray, bbox: torch.Tensor):
        crop_coords = bbox.cpu().numpy()
        cropped_image = image[crop_coords[1]
            :crop_coords[3], crop_coords[0]:crop_coords[2]]
        cropped_image = torch.from_numpy(
            cropped_image.transpose(2, 0, 1)).float() / 255.0

        return data_transforms(cropped_image)

    def predict(self, image, detected_objects):
        with torch.no_grad():
            faces = []
            use_inds = []
            for ind in detected_objects.get_bboxes_inds('face'):
                bbox = detected_objects.get_bbox_by_ind(ind)
                faces.append(self.crops_face(image, bbox))
                use_inds.append(ind)
            if faces != []:
                data = torch.stack(faces, dim=0)
                data = data.to(self.device)
                pred = self.model(data)
                emotions = torch.argmax(F.softmax(pred, dim=1), dim=1)
                for i, ind in enumerate(use_inds):
                    detected_objects.set_emotion(ind, emotions[i].int())
