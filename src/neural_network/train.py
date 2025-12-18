import os
import zipfile
import tensorflow as tf
from tensorflow.keras import layers, models, callbacks
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.metrics import classification_report, confusion_matrix
import seaborn as sns

# 1. DEZARHIVARE
if os.path.exists('data.zip'):
    print("Dezarhivare data.zip...")
    with zipfile.ZipFile('data.zip', 'r') as zip_ref:
        zip_ref.extractall('.')
    print("Gata!")
else:
    print("Atentie: Nu gasesc data.zip.")

# 2. CONFIGURARE
IMG_SIZE = (150, 150)
BATCH_SIZE = 32
EPOCHS = 15

# 3. GENERATORI DE DATE 
train_datagen = ImageDataGenerator(rescale=1./255)
val_datagen = ImageDataGenerator(rescale=1./255)
test_datagen = ImageDataGenerator(rescale=1./255)

print("Incarcare imagini...")
train_generator = train_datagen.flow_from_directory(
    'data/train', 
    target_size=IMG_SIZE, 
    batch_size=BATCH_SIZE, 
    class_mode='categorical'  # SCHIMBAT DIN BINARY
)

validation_generator = val_datagen.flow_from_directory(
    'data/validation', 
    target_size=IMG_SIZE, 
    batch_size=BATCH_SIZE, 
    class_mode='categorical' # SCHIMBAT DIN BINARY
)

# Numaram cate clase a gasit automat
NUM_CLASSES = len(train_generator.class_indices)
print(f"S-au detectat {NUM_CLASSES} clase: {list(train_generator.class_indices.keys())}")

# 4. CONSTRUIRE MODEL (Adaptat pentru 6 Clase)
def build_model():
    model = models.Sequential([
        layers.Input(shape=(150, 150, 3)),
        
        layers.Conv2D(32, (3, 3), activation='relu'),
        layers.MaxPooling2D((2, 2)),
        
        layers.Conv2D(64, (3, 3), activation='relu'),
        layers.MaxPooling2D((2, 2)),
        
        layers.Conv2D(128, (3, 3), activation='relu'), # Am mai adaugat un strat pt complexitate
        layers.MaxPooling2D((2, 2)),
        
        layers.Flatten(),
        layers.Dense(128, activation='relu'),
        
        # STRATUL FINAL ESTE CRITIC:
        # Trebuie sa aiba 'NUM_CLASSES' neuroni si activare 'softmax'
        layers.Dense(NUM_CLASSES, activation='softmax') 
    ])
    
    # Loss function schimbat in categorical_crossentropy
    model.compile(optimizer='adam', 
                  loss='categorical_crossentropy', 
                  metrics=['accuracy'])
    return model

model = build_model()

# 5. ANTRENARE
print("Start Antrenare...")
early_stopping = callbacks.EarlyStopping(monitor='val_loss', patience=5, restore_best_weights=True)

history = model.fit(
    train_generator,
    epochs=EPOCHS,
    validation_data=validation_generator,
    callbacks=[early_stopping]
)

# 6. SALVARE
model.save('trained_model.h5')
pd.DataFrame(history.history).to_csv('training_history.csv', index=False)

# 7. GRAFICE
plt.figure(figsize=(12, 4))
plt.subplot(1, 2, 1)
plt.plot(history.history['loss'], label='Train Loss')
plt.plot(history.history['val_loss'], label='Val Loss')
plt.title('Loss Curve')
plt.legend()
plt.savefig('loss_curve.png')

# 8. EVALUARE (Confusion Matrix Multi-Class)
test_generator = test_datagen.flow_from_directory(
    'data/test', 
    target_size=IMG_SIZE, 
    batch_size=BATCH_SIZE, 
    class_mode='categorical', 
    shuffle=False
)

predictions = model.predict(test_generator)
y_pred = np.argmax(predictions, axis=1) # Luam indexul clasei cu probabilitatea maxima
y_true = test_generator.classes

cm = confusion_matrix(y_true, y_pred)
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', 
            xticklabels=list(test_generator.class_indices.keys()),
            yticklabels=list(test_generator.class_indices.keys()))
plt.title('Confusion Matrix')
plt.ylabel('Real')
plt.xlabel('Predis')
plt.savefig('confusion_matrix.png')

print("Gata! Descarca fisierele generate.")