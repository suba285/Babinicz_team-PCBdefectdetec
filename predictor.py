from ultralytics import YOLO
from PIL import Image


class Predictor:
    def __init__(self):
        self.model = YOLO("./my_model/best.pt")
        self.results = []

    def predict(self, path):
        im1 = Image.open(path)
        self.results = self.model.predict(source=im1, save=True)

