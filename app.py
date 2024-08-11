from flask import Flask, render_template, request
import os 
import numpy as np
from src.mlProject.pipeline.prediction import PredictionPipeline

app = Flask(__name__)

@app.route('/', methods=['GET'])  # route to display the home page
def homePage():
    return render_template("index.html")

@app.route('/train', methods=['GET'])  # route to train the pipeline
def training():
    try:
        os.system("python main.py")
        return "Training Successful!"
    except Exception as e:
        print(f'Training failed: {e}')
        return f"Training failed: {e}"

@app.route('/predict', methods=['POST', 'GET'])  # route to show the predictions in a web UI
def index():
    if request.method == 'POST':
        try:
            # Reading the inputs given by the user
            features = [
                float(request.form['fixed_acidity']),
                float(request.form['volatile_acidity']),
                float(request.form['citric_acid']),
                float(request.form['residual_sugar']),
                float(request.form['chlorides']),
                float(request.form['free_sulfur_dioxide']),
                float(request.form['total_sulfur_dioxide']),
                float(request.form['density']),
                float(request.form['pH']),
                float(request.form['sulphates']),
                float(request.form['alcohol'])
            ]
            data = np.array(features).reshape(1, -1)
            
            # Prediction pipeline
            obj = PredictionPipeline()
            predict = obj.predict(data)

            return render_template('results.html', prediction=str(predict))

        except Exception as e:
            print(f'The Exception message is: {e}')
            return f'Something went wrong: {e}'

    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)