import cv2
import numpy as np

from api import settings


def pre_processing(image: np.ndarray) -> np.ndarray:
    image = cv2.resize(image, settings.preprocessing.IMAGE_SHAPE_WITHOUT_SHAPE)
    image = image[:, :, np.newaxis]
    image = image / 255.
    return image


def get_image_bounding_box(image: np.ndarray) -> list[np.ndarray]:
    _, threshold = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY_INV)
    contours, _ = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    bbs = []
    for contour in sorted(contours, key=lambda ctr: cv2.boundingRect(ctr)[0]):
        x, y, w, h = cv2.boundingRect(contour)
        bbs.append(image[y:y + h, x:x + w])
    return bbs


def padding(image: np.ndarray) -> np.ndarray:
    pad_image = np.pad(image, settings.preprocessing.IMAGE_SHAPE_WITHOUT_SHAPE, constant_values=255)
    x_shape, y_shape = pad_image.shape

    x = (x_shape // 2) - 46 // 2
    w = x + 45

    y = (y_shape // 2) - 46 // 2
    h = y + 45

    return pad_image[y:h, x:w]
