from ultralytics import YOLO
from PIL import Image


class Predictor:
    def __init__(self, model):
        self.model = YOLO(f"./my_model/{model}")
        self.results = []

    def predict(self, path):
        im1 = Image.open(path)
        self.results = self.model.predict(source=im1, save=True)


