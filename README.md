# 🛡️ Détection d'Emails de Phishing
### *Phishing Email Detection avec Machine Learning & NLP*

> Classifiez automatiquement les emails en **légitimes** ou **tentatives de phishing** grâce à des modèles de Machine Learning entraînés sur plus de 18 000 exemples réels.

---

## 📂 Structure du Projet

```text
projet-phishing/
├── 📓 data_exploration.ipynb     # Analyse exploratoire, nettoyage et visualisations
├── ⚙️  model.py                   # Entraînement, évaluation et export des modèles
├── notebook/
│   ├── data_for_use.csv          # Dataset principal
│   └── numero.csv                # Dataset secondaire
└── model/
    └── *.joblib                  # Modèles entraînés (générés après exécution)
```

---

## 📊 Analyse Exploratoire des Données (EDA)

Le projet s'appuie sur un jeu de données de **~18 650 emails** étiquetés.

### 🧹 Prétraitement

| Étape | Description |
|---|---|
| 🗑️ **Nettoyage** | Suppression des valeurs manquantes et des doublons |
| 🔤 **NLP** | Mise en minuscules, suppression des stop-words et de la ponctuation |
| 🔢 **Feature Engineering** | Extraction de variables numériques : longueur du texte, présence de caractères spéciaux, URLs, etc. |

### 📈 Distribution des Classes

```
✅ Safe Email      ██████████████████░░░░░░░░   60,7 %
🎣 Phishing Email  ████████████░░░░░░░░░░░░░░   39,3 %
```

> Le déséquilibre des classes (~60/40) est modéré — les métriques de **Précision**, **Rappel** et **F1-Score** sont donc privilégiées à la simple Accuracy.

---

## 🤖 Modélisation & Pipeline

Le script `model.py` implémente un pipeline de classification complet :

### 🔁 Pipeline

```
Texte brut
    │
    ▼
┌─────────────────────┐
│  TF-IDF Vectorizer  │  ← Conversion texte → vecteurs numériques
└─────────────────────┘
    │
    ▼
┌─────────────────────────────────────────────────────┐
│               Algorithmes testés                    │
│                                                     │
│  📐 LogisticRegression   (Régression Logistique)    │
│  🔷 SVC                  (Support Vector Machine)   │
│  🌲 RandomForestClassifier (Forêt Aléatoire)        │
└─────────────────────────────────────────────────────┘
    │
    ▼
  Meilleur modèle → sauvegardé dans ../model/*.joblib
```

### 🎯 Métriques d'Évaluation

| Métrique | Description |
|---|---|
| ✅ **Accuracy** | Taux global de bonne classification |
| 🎯 **Précision** | Fiabilité des alertes phishing déclenchées |
| 🔁 **Rappel (Recall)** | Capacité à détecter tous les phishings |
| ⚖️ **F1-Score** | Équilibre précision / rappel |
| 📊 **ROC-AUC** | Performance globale du classifieur |

---

## 🛠️ Installation et Utilisation

### 1️⃣ Installer les dépendances

```bash
pip install pandas numpy scikit-learn matplotlib seaborn joblib
```

### 2️⃣ Explorer les données

Lancez le notebook pour visualiser l'analyse et les graphiques :

```bash
jupyter notebook data_exploration.ipynb
```

### 3️⃣ Entraîner les modèles

```bash
python model.py
```

---

## 📈 Résultats et Export

Une fois `model.py` exécuté :

- 📋 Un **tableau comparatif** des performances s'affiche dans la console
- 💾 Le **meilleur modèle** est automatiquement sauvegardé au format `.joblib` dans `../model/`
- 🚀 Le fichier `.joblib` est prêt à être intégré dans un pipeline de **production**

---

## 📦 Dépendances

| Package | Rôle |
|---|---|
| `pandas` / `numpy` | Manipulation et traitement des données |
| `scikit-learn` | Modélisation, vectorisation et évaluation |
| `matplotlib` / `seaborn` | Visualisations et graphiques |
| `joblib` | Sauvegarde et chargement des modèles |
