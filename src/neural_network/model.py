import tensorflow as tf
from tensorflow.keras import layers, models
import os

# 1. definire arhitectura cnn
def build_model(input_shape=(150, 150, 3)):
    model = models.Sequential([
        layers.Input(shape=input_shape),
        # layer1
        layers.Conv2D(32, (3, 3), activation='relu'),
        layers.MaxPooling2D((2, 2)),
        # layer2
        layers.Conv2D(64, (3, 3), activation='relu'),
        layers.MaxPooling2D((2, 2)),
        # clasificare
        layers.Flatten(),
        layers.Dense(64, activation='relu'),
        layers.Dense(1, activation='sigmoid') # 0 = ok, 1 = defect
    ])
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return model

# 2. cale salvare
base_dir = os.path.dirname(os.path.abspath(__file__))
models_dir = os.path.join(base_dir, '../../models')
os.makedirs(models_dir, exist_ok=True)
save_path = os.path.join(models_dir, 'visinspai_model.h5')

# 3. compile and save
if __name__ == "__main__":
    model = build_model()
    model.summary()
    model.save(save_path)
    print(f"Modelul a fost compilat si salvat in: {save_path}")