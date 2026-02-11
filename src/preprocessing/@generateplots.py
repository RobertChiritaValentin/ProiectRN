import pandas as pd
import matplotlib.pyplot as plt
import os

# determinam calea catre radacina proiectului
# scriptul este in src preprocessing deci mergem 2 nivele mai sus
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, '..', '..'))

# definim caile catre fisierele de rezultate
history_path = os.path.join(project_root, 'results', 'training_history.csv')
experiments_path = os.path.join(project_root, 'results', 'optimization_experiments.csv')
output_dir = os.path.join(project_root, 'reports', 'figures')

# cream folderul de output daca nu exista
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# 1 generare grafice din istoric antrenare
if os.path.exists(history_path):
    print("se genereaza graficele de antrenare...")
    try:
        # citim datele din csv
        df = pd.read_csv(history_path)
        
        # construim graficul pentru acuratete
        plt.figure(figsize=(10, 6))
        plt.plot(df['accuracy'], label='train accuracy')
        plt.plot(df['val_accuracy'], label='validation accuracy')
        plt.title('model accuracy')
        plt.xlabel('epoch')
        plt.ylabel('accuracy')
        plt.legend()
        plt.grid(True)
        # salvam graficul ca imagine
        plt.savefig(os.path.join(output_dir, 'accuracy_plot.png'))
        plt.close()
        
        # construim graficul pentru pierdere loss
        plt.figure(figsize=(10, 6))
        plt.plot(df['loss'], label='train loss')
        plt.plot(df['val_loss'], label='validation loss')
        plt.title('model loss')
        plt.xlabel('epoch')
        plt.ylabel('loss')
        plt.legend()
        plt.grid(True)
        # salvam imaginea
        plt.savefig(os.path.join(output_dir, 'loss_plot.png'))
        plt.close()
        
        print("graficele de antrenare au fost salvate in reports figures.")
        
    except Exception as e:
        print("eroare la generarea graficelor de istoric: " + str(e))
else:
    print("nu s-a gasit fisierul training_history.csv in results.")

# 2 generare grafic comparatie experimente
if os.path.exists(experiments_path):
    print("se genereaza comparatia experimentelor...")
    try:
        # citim datele despre experimente
        exp_df = pd.read_csv(experiments_path)
        
        plt.figure(figsize=(10, 6))
        # presupunem ca prima coloana e numele si a doua e rezultatul
        nume = exp_df.iloc[:, 0]
        valori = exp_df.iloc[:, 1]
        
        # desenam un grafic de tip bare
        plt.bar(nume, valori)
        plt.title('rezultate experimente optimizare')
        plt.ylabel('acuratete')
        # rotim etichetele de pe axa x pentru claritate
        plt.xticks(rotation=45)
        plt.tight_layout()
        
        plt.savefig(os.path.join(output_dir, 'experiments_comparison.png'))
        plt.close()
        
        print("graficul comparativ a fost salvat.")
        
    except Exception as e:
        print("eroare la generarea comparatiei: " + str(e))
else:
    print("nu s-a gasit fisierul optimization_experiments.csv in results.")
