import logging
import os

import joblib
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline

CSV_PATH = "/workspace/ml/category/category_training_data.csv"
MODEL_DIR = "/workspace/app/models"


def main():
    df = pd.read_csv(CSV_PATH)

    # データ分割
    X_train, X_test, y_train, y_test = train_test_split(
        df["title"], df["category"], test_size=0.1, random_state=42
    )

    # パイプライン定義
    pipeline = Pipeline(
        [("vect", TfidfVectorizer()), ("clf", RandomForestClassifier(random_state=42))]
    )

    # モデル学習
    pipeline.fit(X_train, y_train)

    # 推論と評価
    y_pred = pipeline.predict(X_test)
    report = classification_report(y_test, y_pred, output_dict=False)

    # モデル保存
    model_dir = MODEL_DIR
    os.makedirs(model_dir, exist_ok=True)

    model_path = os.path.join(model_dir, "category_model.pkl")
    joblib.dump(pipeline, model_path)

    print(report)
