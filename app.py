from flask import Flask, request, jsonify, render_template
import os
from flask_cors import CORS, cross_origin
from cnnClassifier.utils.common import decodeImage
from cnnClassifier.pipeline.s5_prediction import PredictionPipeline



app = Flask(__name__)
CORS(app)


class MyApp:
    def __init__(self):
        self.filename = "Image.jpg"
        self.classifier = PredictionPipeline(self.filename)


@app.route("/", methods=['GET'])
@cross_origin()
def home():
    return render_template('index.html')



@app.route("/predict", methods=['POST'])
@cross_origin()
def predictRoute():
    image = request.json['image']
    decodeImage(image, myapp.filename)
    result= myapp.classifier.predict()
    return jsonify(result)


if __name__ == "__main__":
    myapp = MyApp()

    app.run(host='0.0.0.0', port=8080)