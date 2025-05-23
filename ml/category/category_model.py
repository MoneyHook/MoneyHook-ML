import os
from datetime import datetime

import joblib
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

CSV_PATH = "/workspace/ml/category/"
TRAIN_CSV = "category_training_data.csv"
CATEGORY_MASTER_CSV = "category_master.csv"
CLASSIFICATION_MASTER_CSV = "category_classification_master.csv"

ML_MODELS = "random_forest"
# ML_MODELS = "multinomial"
# ML_MODELS = "logistic_regression"

LOGS_DIR = "/workspace/ml/category/logs"

MODEL_DIR = "/workspace/app/models"


def load_data() -> pd.DataFrame:
    """データを読み込む関数"""
    df = pd.read_csv(f"{CSV_PATH}{TRAIN_CSV}")

    category_class_master = pd.read_csv(f"{CSV_PATH}{CLASSIFICATION_MASTER_CSV}")
    category_map = dict(
        zip(
            category_class_master["classification"],
            category_class_master["id"],
        )
    )
    df["classification"] = df["classification"].map(category_map)

    # 件数を絞り込み
    df_limited = (
        df.groupby("classification")
        .apply(lambda g: g.sample(n=min(len(g), 300), random_state=42))
        .reset_index(drop=True)
    )

    return df_limited


def multinomial_model() -> Pipeline:
    """Multinomial Naive Bayesモデルを定義する関数"""
    pipeline = Pipeline([("vect", CountVectorizer()), ("clf", MultinomialNB())])
    return pipeline


def logistic_regression_model() -> Pipeline:
    """ロジスティック回帰モデルを定義する関数"""
    pipeline = Pipeline(
        [
            ("tfidf", TfidfVectorizer()),
            (
                "clf",
                LogisticRegression(
                    max_iter=1000, random_state=42, class_weight="balanced"
                ),
            ),
        ]
    )
    return pipeline


def random_forest_model() -> Pipeline:
    """Random Forestモデルを定義する関数"""
    pipeline = Pipeline(
        [
            ("tfidf", TfidfVectorizer()),
            ("clf", RandomForestClassifier(random_state=42, class_weight="balanced")),
        ]
    )
    return pipeline


def save_logs(report) -> None:
    """ログを保存する関数"""
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    os.makedirs(LOGS_DIR, exist_ok=True)

    report_path = os.path.join(
        LOGS_DIR, f"{ML_MODELS.lower()}-category_classification_report-{timestamp}.txt"
    )

    with open(report_path, "w", encoding="utf-8") as f:
        f.write(report)


def main():
    df = load_data()

    # データ分割
    X_train, X_test, y_train, y_test = train_test_split(
        df["title"],
        df["classification"],
        test_size=0.1,
        random_state=42,
        stratify=df["classification"],
    )

    # パイプライン定義
    match ML_MODELS:
        case "multinomial":
            pipeline = multinomial_model()
        case "random_forest":
            pipeline = random_forest_model()
        case "logistic_regression":
            pipeline = logistic_regression_model()
        case _:
            pipeline = multinomial_model()

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

    # ログの保存
    save_logs(report)

    print(report)
