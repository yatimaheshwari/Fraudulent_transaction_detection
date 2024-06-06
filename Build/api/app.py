
from flask import Flask, request, redirect,render_template
from flask_restful import Resource, Api
from flask_cors import CORS
import os
import model

app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "*"}})
api = Api(app)

class Test(Resource):
    # def get():
        # return render_template('index.html')
    def get(self):
        return 'Welcome to, Test App API!'

    def post(self):
        try:
            value = request.get_json()
            if(value):
                return {'Post Values': value}, 201

            return {"error":"Invalid format."}

        except Exception as error:
            return {'error': error}

class GetPredictionOutput(Resource):
    def get(self):
        return {"error":"Invalid Method."}

    def post(self):
        try:
            data = request.get_json()
            predict = model.predict_mpg(data)
            predictOutput = predict
            return {'predict':predictOutput}

        except Exception as error:
            return {'error': error}
@app.route('/')
def home():
    return render_template('index.html')



@app.route('/predict', methods=['POST'])
def predict():
    try:
        form_data = request.form.to_dict()
        for key in form_data:
            form_data[key] = [float(form_data[key])] if key != 'type_TRANSFER' else [int(form_data[key])]  # Converting to list and handling types
        print(form_data)
        prediction = model.predict_mpg(form_data)
        return render_template('result.html', prediction=prediction)
    except Exception as e:
        return str(e)
api.add_resource(Test,'/api')
api.add_resource(GetPredictionOutput,'/api/getPredictionOutput')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
