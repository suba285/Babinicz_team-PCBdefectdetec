from ultralytics import YOLO
import os


def show_on_camera():
    model = YOLO('./my_model/my_model.pt')
    results = model(0, show=True)

    for result in results:
        boxes = result.boxes
        classes = result.names


