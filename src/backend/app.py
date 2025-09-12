from ultralytics import YOLO
import cv2
from .detect_food import predict_and_detect
from mistralai import Mistral
import os

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


def ask_mistral(name):
    api_key = os.environ["MISTRAL_API_KEY"]
    model = "mistral-large-latest"

    client = Mistral(api_key=api_key)

    chat_response = client.chat.complete(
        model=model,
        messages=[
            {
                "role": "user",
                "content": "what is the calorie content of "
                + name
                + "?"
                + "format your answer as a json object with a single key 'calories' and an integer value only. No text or sentences outside of the json object",
            },
        ],
    )
    print(chat_response.choices[0].message.content)


if __name__ == "__main__":
    ask_mistral("banana")
