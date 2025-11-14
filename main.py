from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import pickle
import os

app = Flask(__name__)
app.secret_key = "Teams"

# Update the MODEL_PATH to point to your saved model
MODEL_PATH = os.path.join(os.path.dirname(__file__), 'ExtraTreesClassifier.pkl')

@app.route("/")
def home():
    return render_template("index.html", cont="User")

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Fetching input values from the form
        N = float(request.form['Nitrogen'])
        P = float(request.form['Phosphorous'])
        K = float(request.form['Potassium'])
        Temperature = float(request.form['Temperature'])
        Humidity = float(request.form['Humidity'])
        PH = float(request.form['PH'])
        Rainfall = float(request.form['Rainfall'])

        # Load the trained model from the file
        with open(MODEL_PATH, 'rb') as model_file:
            model = pickle.load(model_file)

        # Model prediction
        prediction = model.predict(np.array([N, P, K, Temperature, Humidity, PH, Rainfall]).reshape(1, -1))

        # Mapping prediction to crop names
        crop_names = {
            0: 'Apple', 1: 'Banana', 2: 'Blackgram', 3: 'Chickpea',
            4: 'Coconut', 5: 'Coffee', 6: 'Cotton', 7: 'Grapes',
            8: 'Jute', 9: 'Kidneybeans', 10: 'Lentil', 11: 'Maize',
            12: 'Mango', 13: 'Mothbeans', 14: 'Mungbeans', 15: 'Muskmelon',
            16: 'Orange', 17: 'Papaya', 18: 'Pigeonpeas', 19: 'Pomegranate',
            20: 'Rice', 21: 'Watermelon'
        }
        crop_name = crop_names.get(prediction[0], "Unknown")

        # Determining levels
        humidity_level = determine_level(Humidity, [(1, 33, 'Low Humid'), (34, 66, 'Medium Humid'), (67, 100, 'High Humid')])
        temperature_level = determine_level(Temperature, [(0, 6, 'Cool'), (7, 14, 'Warm'), (15, 65, 'Hot')])
        rainfall_level = determine_level(Rainfall, [(1, 100, 'Less'), (101, 200, 'Moderate'), (201, 1000, 'Heavy Rain')])
        N_level = determine_level(N, [(1, 50, 'Less'), (51, 100, 'Not too less and Not too High'), (101, 200, 'High')])
        P_level = determine_level(P, [(1, 50, 'Less'), (51, 100, 'Not too less and Not too High'), (101, 200, 'High')])
        K_level = determine_level(K, [(1, 50, 'Less'), (51, 100, 'Not too less and Not too High'), (101, 200, 'High')])
        ph_level = determine_level(PH, [(0, 5, 'Acidic'), (6, 8, 'Neutral'), (9, 14, 'Alkaline')])

        # Render the results on Display.html
        return render_template("Display.html", cont=[N_level, P_level, K_level, humidity_level, temperature_level, rainfall_level, ph_level],
                            values=[N, P, K, Humidity, Temperature, Rainfall, PH], cropName=crop_name)
    return render_template("index.html")

def determine_level(value, levels):
    for min_val, max_val, level_name in levels:
        if min_val <= value <= max_val:
            return level_name
    return "Unknown"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
