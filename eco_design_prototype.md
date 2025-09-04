# Prototype de Page Web Minimaliste pour l'Analyse

Ce prototype présente une page web simple et respectueuse des principes d'éco-conception pour afficher les résultats de l'analyse de régression logistique.

## Structure de la Page

### 1. **En-tête**
- Titre : "Analyse des Emails : SPAM ou Non"
- Sous-titre : "Résultats de la Régression Logistique"

### 2. **Section : Résumé des Résultats**
- Précision globale : `99.55%`
- Nombre total d'emails analysés : `X`

### 3. **Section : Visualisations**
- **Matrice de Confusion** :
  ![Placeholder Matrice de Confusion](#)
- **Courbe ROC** :
  ![Placeholder Courbe ROC](#)
- **Distribution des Probabilités** :
  ![Placeholder Distribution](#)

### 4. **Section : Interprétation**
- Explication des graphiques.
- Points clés à retenir.

### 5. **Pied de Page**
- Lien vers le code source.
- Contact.

## Principes d'Éco-Conception
- **Design minimaliste** : Utilisation de couleurs simples et d'éléments essentiels uniquement.
- **Images compressées** : Les graphiques sont optimisés pour réduire leur taille.
- **Code optimisé** : Scripts et styles minimisés.

## Prototype avec Streamlit
Voici un exemple de code Streamlit pour afficher les résultats :

```python
import streamlit as st
import matplotlib.pyplot as plt
from PIL import Image

st.title("Analyse des Emails : SPAM ou Non")
st.subheader("Résultats de la Régression Logistique")

st.write("### Résumé des Résultats")
st.metric(label="Précision Globale", value="99.55%")
st.metric(label="Nombre d'emails analysés", value="X")

st.write("### Visualisations")
st.image("confusion_matrix.png", caption="Matrice de Confusion")
st.image("roc_curve.png", caption="Courbe ROC")
st.image("probability_distribution.png", caption="Distribution des Probabilités")

st.write("### Interprétation")
st.write("- La matrice de confusion montre les performances du modèle.")
st.write("- La courbe ROC indique une excellente séparation entre les classes.")
st.write("- La distribution des probabilités montre la confiance des prédictions.")
```

---

Ce prototype peut être adapté selon vos besoins. Vous pouvez utiliser Streamlit pour une version interactive ou simplement un fichier HTML statique.
