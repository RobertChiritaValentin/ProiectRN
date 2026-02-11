import pandas as pd
import matplotlib.pyplot as plt
import os

# Determinam calea catre radacina proiectului
# Scriptul este in src/preprocessing, deci mergem 2 nivele mai sus
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, '..', '..'))

# Definim caile catre fisiere
history_path = os.path.join(project_root, 'results', 'training_history.csv')
experiments_path = os.path.join(project_root, 'results', 'optimization_experiments.csv')
output_dir = os.path.join(project_root, 'reports', 'figures')

# Cream folderul de output daca nu exista
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# 1. Generare grafice din istoric antrenare
if os.path.exists(history_path):
    print("Se genereaza graficele de antrenare...")
    try:
        df = pd.read_csv(history_path)
        
        # Grafic Acuratete
        plt.figure(figsize=(10, 6))
        plt.plot(df['accuracy'], label='Train Accuracy')
        plt.plot(df['val_accuracy'], label='Validation Accuracy')
        plt.title('Model Accuracy')
        plt.xlabel('Epoch')
        plt.ylabel('Accuracy')
        plt.legend()
        plt.grid(True)
        plt.savefig(os.path.join(output_dir, 'accuracy_plot.png'))
        plt.close()
        
        # Grafic Loss
        plt.figure(figsize=(10, 6))
        plt.plot(df['loss'], label='Train Loss')
        plt.plot(df['val_loss'], label='Validation Loss')
        plt.title('Model Loss')
        plt.xlabel('Epoch')
        plt.ylabel('Loss')
        plt.legend()
        plt.grid(True)
        plt.savefig(os.path.join(output_dir, 'loss_plot.png'))
        plt.close()
        
        print("Graficele de antrenare au fost salvate in reports/figures.")
        
    except Exception as e:
        print("Eroare la generarea graficelor de istoric: " + str(e))
else:
    print("Nu s-a gasit fisierul training_history.csv in results.")

# 2. Generare grafic comparatie experimente
if os.path.exists(experiments_path):
    print("Se genereaza comparatia experimentelor...")
    try:
        exp_df = pd.read_csv(experiments_path)
        
        plt.figure(figsize=(10, 6))
        # Presupunem ca prima coloana e numele si a doua e rezultatul
        nume = exp_df.iloc[:, 0]
        valori = exp_df.iloc[:, 1]
        
        plt.bar(nume, valori)
        plt.title('Rezultate Experimente Optimizare')
        plt.ylabel('Acuratete')
        plt.xticks(rotation=45)
        plt.tight_layout()
        
        plt.savefig(os.path.join(output_dir, 'experiments_comparison.png'))
        plt.close()
        
        print("Graficul comparativ a fost salvat.")
        
    except Exception as e:
        print("Eroare la generarea comparatiei: " + str(e))
else:
    print("Nu s-a gasit fisierul optimization_experiments.csv in results.")