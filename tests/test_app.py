import backend.app as app
import cv2


def test_inference_img_1():
    test1 = cv2.imread("tests/test_img/test1.png")
    test2 = cv2.imread("tests/test_img/test2.png")
    test3 = cv2.imread("tests/test_img/test3.png")
    test4 = cv2.imread("tests/test_img/test4.png")
    assert app.inference_img(test1) == ["Banana"]
    assert app.inference_img(test2) == ["Orange"]
    assert app.inference_img(test3) == ["Beef Steak"]
    assert app.inference_img(test4) == ["Bread"]


def test_inference_img_2():
    assert app.inference_img() == 1
    assert app.inference_img("Haha je suis méchant") == 1
