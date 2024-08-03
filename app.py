from flask import *
# from flask import render_template
import numpy as np
# from io import BytesIO
from PIL import Image
import tensorflow as tf

app = Flask(__name__)

MODEL_PATATO = tf.keras.models.load_model(r"C:\Users\utkarsh.alpuria\Desktop\My Work\Python\Python ML\Potato_Disease_1-main\Models\2.keras")
CLASS_NAMES_PATATO = ['Early Blight', 'Late Blight', 'Healthy']

MODEL_TOMATO = tf.keras.models.load_model(r"C:\Users\utkarsh.alpuria\Desktop\My Work\Python\Python ML\Potato_Disease_1-main\Models\tomato_model_1.keras")
CLASS_NAMES_TOMATO = ['Bacterial Spot', 'Early Blight', 'Late Blight', 'Leaf Mold', 'Septoria Leaf Spot', 'Spider Mites', 'YellowLeaf Curl Virus', 'Target Spot', 'Healthy', 'Mosaic Virus']

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/potato", methods=["GET", "POST"])
def potato_select():
    return render_template("potato_classify.html")

@app.route("/tomato", methods=["GET", "POST"])
def tomato_select():
    return render_template("tomato_classify.html")

    
def read_file_as_image(image_file) -> np.ndarray:
    image = np.array((Image.open(image_file)).convert("RGB").resize((256,256)))
    return image

@app.route("/potato_disease_classification", methods=["POST"])
def potato_disease_classification():
    if request.method == "POST":

        image = read_file_as_image(request.files["potato_leaf_image"])
        
        image_batch = np.expand_dims(image, 0) # since the predict function takes batch of images and not a single image
        predictions = MODEL_PATATO.predict(image_batch)
        prediction_index = np.argmax(predictions[0])
        predicted_class = CLASS_NAMES_PATATO[prediction_index]
        confidence = round((np.max(predictions[0]))*100, 2)
        return render_template("potato_classify.html", prediction = predicted_class, score = confidence)
    
@app.route("/tomato_disease_classification", methods=["POST"])
def tomato_disease_classification():
    if request.method == "POST":

        image = read_file_as_image(request.files["tomato_leaf_image"])

        image_batch = np.expand_dims(image, 0) # since the predict function takes batch of images and not a single image
        predictions = MODEL_TOMATO.predict(image_batch)
        prediction_index = np.argmax(predictions[0])
        predicted_class = CLASS_NAMES_TOMATO[prediction_index]
        confidence = round((np.max(predictions[0]))*100, 2)
        return render_template("tomato_classify.html", prediction = predicted_class, score = confidence)

if __name__ == '__main__':
    app.run(port=5000, debug=True)