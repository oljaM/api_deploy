import tensorflow as tf
from PIL import Image
from io import BytesIO
import numpy as np
from keras.applications.imagenet_utils import decode_predictions

model = None

# loading a sample model which will be replaced with our own model
def load_model():
    model = tf.keras.applications.MobileNetV2(weights='imagenet')
    print('model is loaded')
    return model

# this will be replaced by the preprocessing which is
# needed for our own model when it is ready
def predict(image: Image.Image):
    global model
    if model is None:
        model = load_model()

    image = np.asarray(image.resize((224,224)))[..., :3]
    image = np.expand_dims(image, 0)
    image = image / 127.5 - 1.0

    result = decode_predictions(model.predict(image), 2)[0]

#response separated into a dictionary with values
# class of prediction and probability %
    response = []
    for i, res in enumerate(result):
        resp = {}
        resp["class"] = res[1]
        resp['confidence'] = f"{res[2]*100:0.2f} %"
        response.append(resp)

    return response

#function to read the image uploaded by the user
def read_imagefile(file) -> Image.Image:
    image = Image.open(BytesIO(file))
    return image
