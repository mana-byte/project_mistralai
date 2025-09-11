import cv2
from ultralytics import YOLO

MODEL = YOLO("./yolo11n.pt").to("cuda")
# MODEL = YOLO("./vrheadset/vrheadset/weights/best.pt").to("cuda")


def predict(chosen_model, img, classes=[], conf=0.5):
    if classes != []:
        results = chosen_model.predict(img, classes=classes, conf=conf, device=0)
    else:
        results = chosen_model.predict(img, conf=conf, device=0)

    return results


def predict_and_detect(
    chosen_model, img, classes=[], conf=0.5, rectangle_thickness=2, text_thickness=1
):
    results = predict(chosen_model, img, classes, conf=conf)
    items_name = []
    for result in results:
        for box in result.boxes:
            cv2.rectangle(
                img,
                (int(box.xyxy[0][0]), int(box.xyxy[0][1])),
                (int(box.xyxy[0][2]), int(box.xyxy[0][3])),
                (0, 0, 255),
                rectangle_thickness,
            )
            item_name = f"{result.names[int(box.cls[0])]}"
            items_name.append(item_name)
            cv2.putText(
                img,
                f"{result.names[int(box.cls[0])]}",
                (int(box.xyxy[0][0]), int(box.xyxy[0][1]) - 10),
                cv2.FONT_HERSHEY_PLAIN,
                1,
                (255, 0, 0),
                text_thickness,
            )
    return img, items_name
