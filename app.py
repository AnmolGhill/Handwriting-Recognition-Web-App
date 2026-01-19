from flask import Flask, render_template, request
import tensorflow as tf
import numpy as np
import cv2
from PIL import Image
import os

app = Flask(__name__)

# Load trained model
model = tf.keras.models.load_model("handwriting_model.h5")

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None

    if request.method == "POST":
        file = request.files["image"]

        if file:
            # Read image
            image = Image.open(file).convert("L")
            image = np.array(image)

            # Resize to MNIST size
            image = cv2.resize(image, (28, 28))

            # Invert colors
            image = cv2.bitwise_not(image)

            # Normalize
            image = image / 255.0

            # Reshape for model
            image = image.reshape(1, 28, 28, 1)

            # Predict
            pred = model.predict(image)
            prediction = np.argmax(pred)

    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)
