#http://buffml.com/

from keras.models import load_model
from keras.utils import load_img ,img_to_array
from PIL import Image
import cv2
import numpy as np
from flask import Flask, render_template, request

app = Flask(__name__)

dic = {0: 'Normal', 1: 'Doubtful', 2: 'Mild', 3: 'Moderate', 4: 'Severe'}

# Image Size
img_size = 256
model = load_model('model.h5')

def predict_label(img_path):
    img = Image.open(img_path).convert('L')
    resized = img.resize((img_size, img_size))
    i = np.array(resized) / 255.0
    i = i.reshape(1, img_size, img_size, 1)
    p = model.predict(i)
    predicted_class = np.argmax(p, axis=1)
    return dic[predicted_class[0]]

# Routes
@app.route("/", methods=['GET', 'POST'])
def main():
    return render_template("index.html") 

@app.route("/predict", methods=['POST'])
def upload():
    if request.method == 'POST':
        img = request.files['file']
        img_path = "uploads/" + img.filename
        img.save(img_path)
        p = predict_label(img_path)
        print(p)
        return str(p).lower()

if __name__ == '__main__':
    app.run(debug=True)



