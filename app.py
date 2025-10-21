from flask import Flask, render_template, request
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from werkzeug.utils import secure_filename
import numpy as np
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads/'

# Ensure upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Load trained model
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, 'model', 'waste_model.keras')
model = load_model(MODEL_PATH)

# Class mapping (update according to your dataset)
class_dict = {0: 'Organic', 1: 'Recyclable'}

# Confidence threshold (if model is not confident, classify as Unknown)
CONFIDENCE_THRESHOLD = 0.6  # 60%

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return "No file uploaded"

    file = request.files['file']
    if file.filename == '':
        return "No selected file"

    # Secure the filename to remove spaces & special chars
    filename = secure_filename(file.filename)
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(filepath)

    # Preprocess the image
    img = image.load_img(filepath, target_size=(128, 128))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0) / 255.0

    # Prediction
    pred = model.predict(img_array)[0]
    class_idx = np.argmax(pred)
    probability = pred[class_idx]

    # Check confidence threshold
    if probability < CONFIDENCE_THRESHOLD:
        result = "Unknown"
        probability_percent = probability * 100
    else:
        result = class_dict[class_idx]
        probability_percent = probability * 100

    return render_template('index.html', prediction=result, probability=probability_percent, img_path=filepath)

if __name__ == "__main__":
    app.run(debug=True)
