import pickle
import pandas as pd

# import the ml model
with open('model/model.pkl', 'rb') as f:
    model = pickle.load(f)


def predict_output(userInput: dict):
    input_df = pd.DataFrame([userInput])
    prediction = model.predict(input_df)[0]
    return prediction