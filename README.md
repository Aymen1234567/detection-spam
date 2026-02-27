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


Gemini a dit
Voici une proposition de fichier README.md basée sur le contenu de vos fichiers data_exploration.ipynb et model.py. Ce document présente une vue d'ensemble de votre projet de détection de phishing.

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
Prérequis
Assurez-vous d'avoir installé les bibliothèques suivantes :

Bash
pip install pandas numpy scikit-learn matplotlib seaborn joblib
Exécution
Exploration : Ouvrez data_exploration.ipynb dans un environnement Jupyter pour visualiser les données.

Entraînement : Lancez le script de modélisation pour entraîner les classifieurs et sauvegarder le meilleur modèle :

Bash
python model.py
📈 Résultats
Les résultats de l'entraînement sont sauvegardés dans un DataFrame et affichés dans la console, permettant de choisir le modèle le plus performant pour le déploiement. Le modèle final est exporté dans le dossier ../model à l'aide de joblib.
