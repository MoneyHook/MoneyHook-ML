# from pathlib import Path

# import joblib

# MODEL_PATH = Path(__file__).resolve().parent.parent / "models" / "category_model.pkl"
# _model = joblib.load(MODEL_PATH)


def predict_category(text: str) -> str:
    # prediction = _model.predict([text])[0]
    prediction = text
    return prediction
