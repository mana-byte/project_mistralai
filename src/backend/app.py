from ultralytics import YOLO
import cv2
from .detect_food import predict_and_detect
from mistralai import Mistral
import os

# NOTE: This weight is experimental (Trained quickly to finish the project as fast as possible) and may not work well on every food item + may have some false positives.
# The end goal is to have a model that can detect food items and then use mistral to get the calorie content of the detected food items.
# The final model should be able to detect even small food items such as ingredients in a dish.
# WARNING: The current model is just a proof of concept.
MODEL = YOLO("models/foodWeight.pt").to("cuda")  # Experimental food detection model

# Class names for the food detection model
""" {0: 'Apple', 1: 'Apricot', 2: 'Aubergine', 3: 'Avocado', 4: 'Banana', 5: 'Beef Curry', 6: 'Beef Steak', 7: 'Bread', 8: 'Cabbage', 9: 'Carrot', 10: 'Cauliflower', 11: 'Cheese', 12: 'Cherry', 13: 'Chicken', 14: 'Chili', 15: 'Corn', 16: 'Croissant', 17: 'Cucumber', 18: 'Dates', 19: 'Egg', 20: 'Fig', 21: 'Finger', 22: 'French Fries', 23: 'Garlic', 24: 'Ginger', 25: 'Grapes', 26: 'Green Onions', 27: 'Green Salad', 28: 'Hamburger', 29: 'Hot Dog', 30: 'Kiwi', 31: 'Lemon', 32: 'Lettuce', 33: 'Melon', 34: 'Olives', 35: 'Omelet', 36: 'Orange', 37: 'Pasta', 38: 'Peach', 39: 'Pear', 40: 'Pineapple', 41: 'Pizza', 42: 'Pomegranate', 43: 'Potato', 44: 'Rice', 45: 'Sauce', 46: 'Sausage', 47: 'Strawberry', 48: 'Sushi', 49: 'Tomato', 50: 'Watermelon'}"""


def inference_img(img=None):
    if img is None:
        print("[WARNING]: No image")
        return 1
    try:
        result_img, items = predict_and_detect(
            MODEL, img, classes=[], conf=0.501
        )  # cf models/boxF1_curve
    except Exception as e:
        print("[WARNING]: something went wrong in predict_and_detect : " + str(e))
        return 1
    cv2.imwrite("tests/test_img/test4_output.png", result_img)
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
    # ask_mistral("banana")
    test_img = cv2.imread("tests/test_img/test4.png")
    print(inference_img(test_img))
