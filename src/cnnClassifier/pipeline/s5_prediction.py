import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import os



class PredictionPipeline:
    def __init__(self,filename):
        self.filename =filename


    
    def predict(self):
        
        model = load_model(os.path.join("model", "model.h5"))

        imagename = self.filename
        test_image = image.load_img(imagename, target_size = (224,224))
        img_array = image.img_to_array(test_image)
        img_array = np.expand_dims(img_array, axis = 0)
        img_array = img_array / 255.0
        ac_res = model.predict(img_array)
        result = np.argmax(ac_res, axis=1)
        print(result)

        if result[0] == 1:
            prediction = 'Tumor'
            return [prediction]
        else:
            prediction = 'Normal'
            return [prediction]