import tensorflow as tf
from tensorflow.keras import layers, models
import os

# functia pentru construirea arhitecturii retelei neuronale
# definim dimensiunea implicita a imaginii de intrare
def build_model(input_shape=(150, 150, 3)):
    model = models.Sequential([
        # specificam forma input-ului
        layers.Input(shape=input_shape),
        
        # primul strat convolutional pentru extragere trasaturi
        layers.Conv2D(32, (3, 3), activation='relu'),
        # reducem dimensiunea hartii de trasaturi
        layers.MaxPooling2D((2, 2)),
        
        # al doilea strat convolutional
        layers.Conv2D(64, (3, 3), activation='relu'),
        layers.MaxPooling2D((2, 2)),
        
        # transformam datele pentru stratul dens
        layers.Flatten(),
        layers.Dense(64, activation='relu'),
        
        # stratul de iesire pentru clasificare binara ok sau defect
        layers.Dense(1, activation='sigmoid') 
    ])
    
    # configuram optimizatorul si functia de pierdere
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return model

# pregatim calea unde se va salva modelul
base_dir = os.path.dirname(os.path.abspath(__file__))
models_dir = os.path.join(base_dir, '../../models')
# cream directorul daca nu exista
os.makedirs(models_dir, exist_ok=True)
save_path = os.path.join(models_dir, 'visinspai_model.h5')

# daca rulam acest script direct construim si salvam modelul
if __name__ == "__main__":
    model = build_model()
    # afisam sumarul arhitecturii in consola
    model.summary()
    # salvam modelul pe disc
    model.save(save_path)
    print(f"modelul a fost compilat si salvat in: {save_path}")
