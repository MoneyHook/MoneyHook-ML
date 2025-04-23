import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import joblib
import os

# サンプルデータの作成（実際はCSVを読み込むことを想定）
data = {
    "title": [
        "コンビニでパン購入",
        "スーパーで野菜と肉を購入",
        "電車の定期券を購入",
        "ガソリンスタンドで給油",
        "Amazonでシャンプー購入",
        "ユニクロで服を購入",
        "市役所で住民票を取得",
        "映画館で映画鑑賞",
        "スタバでコーヒー",
        "iPhoneのアプリ課金",
    ],
    "category": [
        "食費",
        "食費",
        "交通費",
        "交通費",
        "日用品",
        "衣服",
        "行政",
        "娯楽",
        "食費",
        "娯楽",
    ],
}
df = pd.DataFrame(data)

# データ分割
X_train, X_test, y_train, y_test = train_test_split(
    df["title"], df["category"], test_size=0.2, random_state=42
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
model_path = "/mnt/data/category_model.pkl"
joblib.dump(pipeline, model_path)

report, model_path
