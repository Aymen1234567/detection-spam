🛡️ Détection d'Emails de Phishing (Phishing Email Detection)
Ce projet utilise des techniques d'Apprentissage Automatique (Machine Learning) et de Traitement du Langage Naturel (NLP) pour classer les courriels en deux catégories : emails légitimes (Safe Email) ou tentatives d'hameçonnage (Phishing Email).

📂 Structure du Projet
data_exploration.ipynb : 🔍 Carnet Jupyter dédié à l'analyse exploratoire (EDA), au nettoyage et à la visualisation des données.

model.py : ⚙️ Script Python pour l'entraînement, l'évaluation et l'exportation des modèles de classification.

../notebook/ : Contient les fichiers CSV de données (data_for_use.csv, numero.csv).

../model/ : Dossier de destination pour les modèles entraînés (fichiers .joblib).

📊 Analyse des Données (EDA)
Le projet s'appuie sur un jeu de données d'environ 18 650 emails.

🧹 Prétraitement
Nettoyage : Gestion des valeurs manquantes et suppression des doublons.

NLP : Mise en minuscule, suppression des stop-words et ponctuation.

Ingénierie de caractéristiques : Extraction de données numériques (longueur du texte, présence de caractères spéciaux, etc.).

📈 Distribution des Classes
Safe Email : ~60,7%

Phishing Email : ~39,3%

[Image d'un graphique à barres montrant la distribution entre les classes "Safe Email" et "Phishing Email"]

🤖 Modélisation & Pipeline
Le script model.py implémente un pipeline robuste :

Vectorisation : Utilisation de TfidfVectorizer pour convertir le texte en vecteurs numériques.

Algorithmes testés :

LogisticRegression (Régression Logistique)

SVC (Machines à Vecteurs de Support)

RandomForestClassifier (Forêt Aléatoire)

Métriques d'évaluation :

✅ Accuracy

🎯 Précision & Rappel (Recall)

⚖️ F1-Score

📊 ROC-AUC

🛠️ Installation et Utilisation
1️⃣ Prérequis
Installez les dépendances nécessaires via pip :

Bash
pip install pandas numpy scikit-learn matplotlib seaborn joblib
2️⃣ Exploration des données
Pour visualiser l'analyse et les graphiques :

Bash
jupyter notebook data_exploration.ipynb
3️⃣ Entraînement du modèle
Pour lancer l'entraînement des modèles et sauvegarder le meilleur résultat :

Bash
python model.py
📈 Résultats et Export
Une fois l'exécution de model.py terminée :

Un tableau comparatif des performances s'affiche dans la console.

Le meilleur modèle est automatiquement sauvegardé dans le dossier ../model au format .joblib pour une utilisation ultérieure en production.
