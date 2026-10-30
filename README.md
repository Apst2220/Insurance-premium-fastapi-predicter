# Insurance Premium Prediction API

A machine learning-based REST API built using **FastAPI** to predict insurance premium categories based on user input.

### Tech Stack
- Python
- FastAPI
- Pydantic
- Pandas
- Scikit-learn
- Docker

### Features
- Insurance premium category prediction.
- Input validation using Pydantic.
- Interactive API documentation using Swagger UI.
- Docker containerization.

### Setup

```bash
git clone https://github.com/YOUR_USERNAME/Insurance-Premium-FastAPI.git
cd Insurance-Premium-FastAPI

python3 -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt
uvicorn app:app --reload
```

### API Documentation

Visit: `http://localhost:8000/docs`

### Docker

```bash
docker build -t insurance-premium-api .
docker run -p 8999:8000 insurance-premium-api
```

API available at: `http://localhost:8999/docs`

### Docker Hub

[Insurance Premium Prediction API](https://hub.docker.com/r/amanpreet2002/insurance-premium-api)

### Author
Amanpreet Singh