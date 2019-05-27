from flask import Flask, request
import werkzeug
import cv2
from keras.preprocessing.image import img_to_array
from keras.models import load_model
import tensorflow as tf
import numpy as np


labels = ["daisy", "dandelion", "roses", "sunflower", "tulips"]
print("[INFO] Loading Model")

model = load_model("flowers.model")
graph = tf.get_default_graph()

def detectImg(img):
    global graph
    print("[INFO] Processing Image")
    img = cv2.resize(img, (150, 150))
    img = img.astype("float") / 255.0
    img = img_to_array(img)
    img = np.expand_dims(img, axis=0)
    with graph.as_default():
        res = model.predict(img)
    resClass = np.argmax(res[0])
    return labels[resClass]



app = Flask(__name__)

@app.route("/")
def index():
    return "App is working"


@app.route("/process", methods=["POST"])
def processImg():
    filedata = request.files["img"]
    filename = werkzeug.utils.secure_filename(filedata.filename)
    filedata.save(filename)
    img = cv2.imread(filename)
    className = detectImg(img)
    return className

if __name__ == "__main__":
    app.run(debug=True)