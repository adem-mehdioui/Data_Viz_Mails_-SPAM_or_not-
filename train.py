import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import CountVectorizer
import joblib


# 1. Charger les données
df = pd.read_csv("emails.csv")  # CSV avec colonnes: category, message
print("Columns in the dataset:", df.columns)
print("First few rows:\n", df.head())

# Ensure the column name matches the CSV file
if 'Message' not in df.columns:
    raise ValueError("The column 'Message' does not exist in the dataset. Available columns: " + ", ".join(df.columns))

X = df["Message"]
y = df["Category"]

# 2. Vectoriser le texte
vectorizer = CountVectorizer()
X_vec = vectorizer.fit_transform(X)

# 3. Séparer train/test
X_train, X_test, y_train, y_test = train_test_split(
    X_vec, y, test_size=0.2, random_state=42
)

# 4. Entraîner un modèle baseline
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# 5. Sauvegarder le modèle + le vectorizer
joblib.dump(model, "model.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")

print("Modèle entraîné et sauvegardé : model.pkl + vectorizer.pkl")



