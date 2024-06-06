import pandas as pd
import numpy as np
from tensorflow.keras.models import load_model
def predict_mpg(config):
    try:
        print("creating model")
        #loading the model from the saved file  
        model = load_model(r'Build\api\model.h5')
    except Exception as e:
        print(e)
    if type(config) == dict:
        df = pd.DataFrame(config)
    else:
        df = config
    y_thre = model.predict(df)
    y_pred = np.where(y_thre > .5,1,0)
    if y_pred == 0:
        return 'Not a Fraud'
    elif y_pred == 1:
        return 'absolutely Fraud'