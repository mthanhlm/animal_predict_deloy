import os
from flask import Flask, render_template, request, url_for
from tensorflow.keras.applications.vgg16 import VGG16, preprocess_input, decode_predictions
from keras_preprocessing.image import load_img, img_to_array

app = Flask(__name__)
model = VGG16()

# Đảm bảo thư mục static/uploads tồn tại
if not os.path.exists('./static/uploads'):
    os.makedirs('./static/uploads')

@app.route('/', methods=["GET","POST"])
def home():
    return render_template("index.html", prediction="Hãy chọn ảnh để chuẩn đoán")

@app.route('/predict', methods=["POST"])
def predict():
    imagefile = request.files.get("imagefile")
    if imagefile:
        # Lưu file vào thư mục static/uploads
        filename = imagefile.filename
        filepath = os.path.join('static', 'uploads', filename)
        imagefile.save(filepath)

        # Dự đoán
        image = load_img(filepath, target_size=(224, 224))
        image = img_to_array(image)
        image = image.reshape((1, image.shape[0], image.shape[1], image.shape[2]))
        image = preprocess_input(image)
        history = model.predict(image)
        label = decode_predictions(history)
        label = label[0][0]

        prediction = '%s (%.2f%%)' % (label[1], label[2] * 100)
        
        # Tạo URL cho hình ảnh đã tải lên
        image_url = url_for('static', filename=f'uploads/{filename}')
    else:
        prediction = "Không có hình ảnh nào được tải lên"
        image_url = None

    return render_template("index.html", prediction=prediction, image_url=image_url)

if __name__ == '__main__':
    app.run(port=3000, debug=True)