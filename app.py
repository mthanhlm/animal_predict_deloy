from flask import Flask, render_template, request
from tensorflow import keras
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.applications.vgg16 import preprocess_input
from keras.applications.vgg16 import decode_predictions
from keras.applications.vgg16 import VGG16

app = Flask(__name__)
model = VGG16()
@app.route('/', methods=["GET"])
def home():
    return render_template("index.html")

@app.route('/', methods=["POST"])
def predict():
    imagefile = request.files.get("imagefile")
    image_data = request.form.get("image_data")
    if imagefile:
        imagepath = "./img/" + imagefile.filename
        imagefile.save(imagepath)
        
        #Predict
        image = load_img(imagepath, target_size = (224,224))
        image = img_to_array(image)
        image = image.reshape((1,image.shape[0], image.shape[1], image.shape[2]))
        image = preprocess_input(image)
        history = model.predict(image)
        label = decode_predictions(history)
        label = label[0][0]
        
        prediction = '%s (%.2f%%)' % (label[1], label[2]*100)
    else:
        prediction = "Không có hình ảnh nào được tải lên"

    return render_template("index.html", prediction=prediction, image_data=image_data)

if __name__ == '__main__':
    app.run(port=3000, debug=True)
