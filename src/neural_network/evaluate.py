import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from sklearn.metrics import classification_report, confusion_matrix
import numpy as np
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# --- CONFIGURARE CAI RELATIVE ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_TEST_DIR = os.path.abspath(os.path.join(BASE_DIR, '../../data/test'))
MODELS_DIR = os.path.abspath(os.path.join(BASE_DIR, '../../models'))
RESULTS_DIR = os.path.abspath(os.path.join(BASE_DIR, '../../results'))
DOCS_DIR = os.path.abspath(os.path.join(BASE_DIR, '../../docs'))

# Asiguram existenta folderelor pentru output
os.makedirs(RESULTS_DIR, exist_ok=True)
os.makedirs(DOCS_DIR, exist_ok=True)

# --- 1. PREGATIRE DATE TEST ---
test_datagen = ImageDataGenerator(rescale=1./255)
test_generator = test_datagen.flow_from_directory(
    DATA_TEST_DIR,
    target_size=(150, 150),
    batch_size=32,
    class_mode='categorical',
    shuffle=False
)

class_labels = list(test_generator.class_indices.keys())

# --- 2. LISTA MODELE DE EVALUAT ---
# Cheia este numele afisat, valoarea este numele fisierului din folderul models/
models_to_compare = {
    "Model_Initial": "trained_model.h5",
    "Model_Optimizat": "optimized_model.h5"
}

comparison_data = []

print("Incepere evaluare comparativa...")

for label, filename in models_to_compare.items():
    model_path = os.path.join(MODELS_DIR, filename)
    
    if not os.path.exists(model_path):
        print(f"⚠️ Atentie: Nu am gasit fisierul {filename} in {MODELS_DIR}. Sari peste.")
        continue

    print(f"\nEvaluare {label} ({filename})...")
    model = tf.keras.models.load_model(model_path)
    
    # Predictii
    predictions = model.predict(test_generator, verbose=0)
    y_pred = np.argmax(predictions, axis=1)
    y_true = test_generator.classes
    
    # Calcul metrici prin classification_report
    report = classification_report(y_true, y_pred, target_names=class_labels, output_dict=True)
    
    comparison_data.append({
        "Model": label,
        "Fisier": filename,
        "Acuratete": report['accuracy'],
        "F1_Score_Macro": report['macro avg']['f1-score']
    })

    # Generare Matrice de Confuzie individuala (doar pentru vizualizare)
    cm = confusion_matrix(y_true, y_pred)
    plt.figure(figsize=(8, 6))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=class_labels, yticklabels=class_labels)
    plt.title(f'Matrice Confuzie: {label}')
    plt.ylabel('Adevarat')
    plt.xlabel('Predictie')
    # Salvam matricea specifica (ex: confusion_matrix_trained.png)
    plt.savefig(os.path.join(DOCS_DIR, f'confusion_matrix_{label.lower()}.png'))
    plt.close()

# --- 3. SALVARE REZULTATE COMPARATIVE ---
df = pd.DataFrame(comparison_data)
csv_path = os.path.join(RESULTS_DIR, 'comparatie_finala_modele.csv')
df.to_csv(csv_path, index=False)

print("\n" + "="*40)
print("TABEL COMPARATIV FINAL")
print("="*40)
print(df)
print(f"\n✓ Rezultate CSV salvate in: {csv_path}")

# --- 4. GENERARE GRAFIC COMPARATIV (BAR CHART) ---
plt.figure(figsize=(10, 6))
x = np.arange(len(df['Model']))
plt.bar(x - 0.2, df['Acuratete'], 0.4, label='Acuratete', color='firebrick')
plt.bar(x + 0.2, df['F1_Score_Macro'], 0.4, label='F1-Score', color='forestgreen')

plt.xticks(x, df['Model'])
plt.ylim(0, 1.1)
plt.ylabel('Scor (0-1)')
plt.title('Comparatie Performanta: Model Initial vs Optimizat')
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Salvam poza ceruta pentru documentatie
plot_path = os.path.join(DOCS_DIR, 'comparatie_vizuala.png')
plt.savefig(plot_path)
print(f"✓ Grafic comparativ salvat in: {plot_path}")
plt.show()