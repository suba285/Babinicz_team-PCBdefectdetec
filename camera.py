from ultralytics import YOLO
import os


def show_on_camera():
    model = YOLO('./my_model/best.pt')
    results = model(0, show=True)

    counter = 100

    for result in results:
        counter -= 1
        print(counter)
        boxes = result.boxes
        classes = result.names
        if counter < 0:
            exit()

