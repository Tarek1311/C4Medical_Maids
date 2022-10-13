import base64
from io import BytesIO

import requests


def encode_image(image_url):
    buffered = BytesIO(requests.get(image_url).content)
    image_base64 = base64.b64encode(buffered.getvalue())
    return (b"data:image/png;base64," + image_base64).decode()


IMG_BED_DICT = {
    "LMS": encode_image("https://www.altivie.fr/api/media/w_433/CvvaQZ_8Y.jpg"),
    "LMXXL": encode_image("https://www.altivie.fr/api/media//MwqGVQ4hK.jpg"),
    "LMPLE": encode_image(
        "https://i.pinimg.com/originals/66/6a/a8/666aa81ff3a685bb4f8ee1decab26989.jpg"
    ),
}

IMG_WHEELCHAIR_DICT = {
    "FMS": encode_image("https://www.altivie.fr/api/media/w_433/CvvaQZ_8Y.jpg"),
    "FMXXL": encode_image("https://www.altivie.fr/api/media//MwqGVQ4hK.jpg"),
    "FMPLE": encode_image(
        "https://i.pinimg.com/originals/66/6a/a8/666aa81ff3a685bb4f8ee1decab26989.jpg"
    ),
}

IMG_LIFTER_DICT = {
    "LMS": encode_image("https://www.altivie.fr/api/media/w_433/CvvaQZ_8Y.jpg"),
    "LMXXL": encode_image("https://www.altivie.fr/api/media//MwqGVQ4hK.jpg"),
    "LMPLE": encode_image(
        "https://i.pinimg.com/originals/66/6a/a8/666aa81ff3a685bb4f8ee1decab26989.jpg"
    ),
}
