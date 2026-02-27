Détection d'Emails de Phishing (Phishing Email Detection)
Ce projet vise à analyser et à classer des courriers électroniques pour identifier s'il s'agit d'emails légitimes (Safe Email) ou de tentatives d'hameçonnage (Phishing Email) en utilisant des techniques d'apprentissage automatique (Machine Learning) et de traitement du langage naturel (NLP).

📂 Structure du Projet
data_exploration.ipynb : Carnet Jupyter dédié à l'analyse exploratoire des données (EDA), au nettoyage et à la visualisation du jeu de données initial.

model.py : Script Python pour l'entraînement, l'évaluation et la sauvegarde des modèles de classification.

📊 Analyse des Données (Exploration)
Le projet utilise un jeu de données contenant environ 18 650 emails.

Distribution des classes : Environ 60,7% d'emails sains et 39,3% d'emails de phishing.

Prétraitement : * Gestion des valeurs manquantes et des doublons.

Nettoyage du texte (suppression des stop-words, mise en minuscule, etc.).

Extraction de caractéristiques numériques à partir du texte.

[Image d'un graphique à barres montrant la distribution entre les classes "Safe Email" et "Phishing Email"]

🤖 Modélisation
Le script model.py met en place un pipeline de traitement complet :

Vectorisation : Utilisation de TfidfVectorizer pour transformer le texte traité en vecteurs numériques.

Modèles testés : Le script compare plusieurs algorithmes de classification, notamment :

Régression Logistique (LogisticRegression).

Machines à Vecteurs de Support (SVC).

Forêt Aléatoire (RandomForestClassifier).

Évaluation : Les modèles sont évalués selon plusieurs métriques : Accuracy, Précision, Rappel (Recall), F1-Score et ROC-AUC.

🛠️ Installation et Utilisation
