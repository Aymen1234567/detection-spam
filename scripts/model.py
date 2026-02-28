import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.metrics import (accuracy_score, precision_score, recall_score, 
                           f1_score, roc_auc_score)
from sklearn.feature_extraction.text import TfidfVectorizer
import time
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
import os
import joblib


n = pd.read_csv("../notebook/numero.csv")
data = pd.read_csv("../notebook/data_for_use.csv")

data['processed_text'] = data['processed_text'].fillna("")  # remplace NaN par ""
X = data[['processed_text'] + list(n.columns)]
y = data['label']
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

print(f"\nTrain : {X_train.shape[0]} samples")
print(f"Test : {X_test.shape[0]} samples")
print(f"distribution Train class : {np.bincount(y_train)}")
print(f"distribution Test class : {np.bincount(y_test)}")

text_features = ['processed_text']
numerical_features = list(n.columns)

tfidf_vectorizer = TfidfVectorizer(
    max_features=5000,  
    min_df=2,          
    max_df=0.95,       
    ngram_range=(1, 3), 
    stop_words='english',
    sublinear_tf=True,  
    smooth_idf=True
)

preprocessor = ColumnTransformer(
    transformers=[
        ('text', tfidf_vectorizer, 'processed_text'),
        ('num', StandardScaler(), numerical_features)
    ]
)

print("Ajustement et transformation des données avec TF-IDF...")
start_time = time.time()
X_train_transformed = preprocessor.fit_transform(X_train)
X_test_transformed = preprocessor.transform(X_test)
transform_time = time.time() - start_time

print(f"Transformation TF-IDF terminée en {transform_time:.2f} seconds")
print(f"Dimensions des données d’entraînement transformées: {X_train_transformed.shape}")
print(f"Dimensions des données de test transformées: {X_test_transformed.shape}")
print(f"Nombre total de caractéristiques: {X_train_transformed.shape[1]}")


models = {
    'Logistic Regression': LogisticRegression(random_state=42, max_iter=1000, class_weight='balanced'),
    'Support Vector Machine': SVC(random_state=42, probability=True, class_weight='balanced'),
    'Random Forest': RandomForestClassifier(random_state=42, class_weight='balanced', n_jobs=-1),
}

results = []
model_predictions = {}


# Train and evaluate each model
for name, model in models.items():
    print(f"\n{'='*50}")
    print(f"entrainement {name}...")
    print('='*50)
    
  
    
    # Train model
    model.fit(X_train_transformed, y_train)
 
    
    # Make predictions
    y_pred = model.predict(X_test_transformed)
    y_pred_proba = model.predict_proba(X_test_transformed)[:, 1] if hasattr(model, 'predict_proba') else None
   
    
    # Calculate metrics
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred, zero_division=0)
    recall = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    
    # Calculate ROC-AUC if probabilities are available
    roc_auc = roc_auc_score(y_test, y_pred_proba) if y_pred_proba is not None else 0
    
    # Store results
    results.append({
        'Model': name,
        'Accuracy': accuracy,
        'Precision': precision,
        'Recall': recall,
        'F1-Score': f1,
        'ROC-AUC': roc_auc,
    })
    
    model_predictions[name] = {'y_pred': y_pred, 'y_pred_proba': y_pred_proba}
    
    print(f"Accuracy: {accuracy:.4f}")
    print(f"Precision: {precision:.4f}")
    print(f"Recall: {recall:.4f}")
    print(f"F1-Score: {f1:.4f}")
    print(f"ROC-AUC: {roc_auc:.4f}")

model_dir = "../model"
os.makedirs(model_dir, exist_ok=True)  # crée le dossier si nécessaire

results_df = pd.DataFrame(results)

# Choisir le meilleur modèle selon F1-Score
best_index = results_df['F1-Score'].idxmax()
best_model_name = results_df.loc[best_index, 'Model']
best_model = models[best_model_name]

print(f"Meilleur modèle: {best_model_name} avec F1 = {results_df.loc[best_index, 'F1-Score']:.4f}")

model_path = os.path.join(model_dir, f"{best_model_name}.joblib")
joblib.dump(best_model, model_path)

print(f"Modèle sauvegardé dans : {model_path}")
