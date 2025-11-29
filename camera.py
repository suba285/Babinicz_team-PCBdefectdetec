from ultralytics import YOLO


def show_on_camera():
    model = YOLO('./my_model/bestofthebest.pt')
    results = model(0, show=True)

    for result in results:
        boxes = result.boxes
        classes = result.names


