import joblib
import pandas as pd

print("Le script commence à s'exécuter...")

def test_model_accuracy():
    print("Chargement du dataset...")
    df = pd.read_csv("emails.csv")
    print("Dataset chargé avec succès !")

    print("Extraction des features et des labels...")
    X, y = df["Message"], df["Category"]
    print("Features et labels extraits !")

    print("Chargement du vectoriseur...")
    vectorizer = joblib.load("vectorizer.pkl")  # Assurez-vous que le vectoriseur a été sauvegardé lors de l'entraînement
    X_vec = vectorizer.transform(X)
    print("Données vectorisées !")

    print("Chargement du modèle...")
    model = joblib.load("model.pkl")
    print("Modèle chargé avec succès !")

    print("Calcul de la précision...")
    score = model.score(X_vec, y)
    print(f"Précision calculée : {score}")

    try:
        assert score >= 0.8, f"Accuracy trop faible : {score}"
    except AssertionError as e:
        print(e)
        return

    print(f"Test réussi ! Précision du modèle : {score}")

# Appel de la fonction
test_model_accuracy()