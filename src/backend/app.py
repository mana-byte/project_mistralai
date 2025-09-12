from ultralytics import YOLO
import cv2
from backend.detect_food import predict_and_detect
import mistralai

MODEL = YOLO("yolo11n.pt").to("cuda")


def inference_img(img=None):
    if img is None:
        print("[WARNING]: No image")
        return 1
    try:
        result_img, items = predict_and_detect(MODEL, img, classes=[], conf=0.5)
    except Exception as e:
        print("[WARNING]: something went wrong in predict_and_detect : " + str(e))
        return 1
    return items
