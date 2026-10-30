from fastapi import FastAPI
from fastapi.responses import JSONResponse
from schema.userInput import UserInput
from schema.ApiOutput import apiOutput
from model.predict import predict_output

app = FastAPI()

@app.get('/')
def home():
    return JSONResponse(status_code=200, content={'message': 'Welcome to the Insurance Premium Prediction API!'})


@app.get('/health')
def health_check():
    return JSONResponse(status_code=200, content={'status': 'ok'})


@app.post('/predict', response_model=apiOutput)
def predict_premium(data: UserInput):

    input = {
        'bmi': data.bmi,
        'age_group': data.age_group,
        'lifestyle_risk': data.lifestyle_risk,
        'city_tier': data.city_tier,
        'income_lpa': data.income_lpa,
        'occupation': data.occupation
    }

    try:
        prediction = predict_output(input)
        return JSONResponse(status_code=200, content={'predicted_category': prediction})
    except Exception as e:
        return JSONResponse(status_code=500, content={'error': str(e)})




