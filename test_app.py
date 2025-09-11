import app
import cv2


def test_inference_img_1():
    example_img = cv2.imread("./test_img/example_food.png")
    assert len(app.inference_img(example_img)) == 5


def test_inference_img_2():
    assert app.inference_img() == 1
    assert app.inference_img("Haha je suis méchant") == 1
