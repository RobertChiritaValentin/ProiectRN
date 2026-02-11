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

# verificam daca exista arhiva cu date si o extragem daca e cazul
if os.path.exists('data.zip'):
    print("dezarhivare data.zip...")
    with zipfile.ZipFile('data.zip', 'r') as zip_ref:
        zip_ref.extractall('.')
    print("gata!")
else:
    print("atentie: nu gasesc data.zip.")

# configuram parametrii de baza pentru antrenare
IMG_SIZE = (150, 150)
BATCH_SIZE = 32
EPOCHS = 15

# pregatim generatorii de date cu normalizare
# impartim valoarea pixelilor la 255 pentru a fi intre 0 si 1
train_datagen = ImageDataGenerator(rescale=1./255)
val_datagen = ImageDataGenerator(rescale=1./255)
test_datagen = ImageDataGenerator(rescale=1./255)

print("incarcare imagini...")
# incarcam imaginile de antrenament direct din folder
train_generator = train_datagen.flow_from_directory(
    'data/train', 
    target_size=IMG_SIZE, 
    batch_size=BATCH_SIZE, 
    class_mode='categorical'  # folosim categorical pentru mai multe clase
)

# incarcam imaginile pentru validare
validation_generator = val_datagen.flow_from_directory(
    'data/validation', 
    target_size=IMG_SIZE, 
    batch_size=BATCH_SIZE, 
    class_mode='categorical'
)

# numaram cate clase a detectat automat generatorul
NUM_CLASSES = len(train_generator.class_indices)
print(f"s-au detectat {NUM_CLASSES} clase: {list(train_generator.class_indices.keys())}")

# functia care construieste arhitectura retelei neuronale
def build_model():
    model = models.Sequential([
        # definim forma datelor de intrare 150x150 px color
        layers.Input(shape=(150, 150, 3)),
        
        # primul bloc convolutional pentru extragerea trasaturilor de baza
        layers.Conv2D(32, (3, 3), activation='relu'),
        layers.MaxPooling2D((2, 2)),
        
        # al doilea bloc convolutional
        layers.Conv2D(64, (3, 3), activation='relu'),
        layers.MaxPooling2D((2, 2)),
        
        # al treilea bloc pentru complexitate sporita
        layers.Conv2D(128, (3, 3), activation='relu'), 
        layers.MaxPooling2D((2, 2)),
        
        # transformam matricea 3d intr-un vector 1d
        layers.Flatten(),
        
        # strat dens complet conectat
        layers.Dense(128, activation='relu'),
        
        # stratul de iesire cu activare softmax pentru clasificare
        layers.Dense(NUM_CLASSES, activation='softmax') 
    ])
    
    # configuram procesul de invatare
    model.compile(optimizer='adam', 
                  loss='categorical_crossentropy', 
                  metrics=['accuracy'])
    return model

# instantiem modelul
model = build_model()

# incepem procesul de antrenare
print("start antrenare...")
# oprim antrenarea daca nu mai invata pentru a evita overfitting
early_stopping = callbacks.EarlyStopping(monitor='val_loss', patience=5, restore_best_weights=True)

history = model.fit(
    train_generator,
    epochs=EPOCHS,
    validation_data=validation_generator,
    callbacks=[early_stopping]
)

# salvam modelul antrenat si istoricul
model.save('trained_model.h5')
pd.DataFrame(history.history).to_csv('training_history.csv', index=False)

# generam graficele pentru loss
plt.figure(figsize=(12, 4))
plt.subplot(1, 2, 1)
plt.plot(history.history['loss'], label='train loss')
plt.plot(history.history['val_loss'], label='val loss')
plt.title('loss curve')
plt.legend()
plt.savefig('loss_curve.png')

# evaluam modelul pe setul de testare
test_generator = test_datagen.flow_from_directory(
    'data/test', 
    target_size=IMG_SIZE, 
    batch_size=BATCH_SIZE, 
    class_mode='categorical', 
    shuffle=False
)

# facem predictii
predictions = model.predict(test_generator)
y_pred = np.argmax(predictions, axis=1) # luam clasa cu probabilitatea cea mai mare
y_true = test_generator.classes

# generam si salvam matricea de confuzie
cm = confusion_matrix(y_true, y_pred)
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', 
            xticklabels=list(test_generator.class_indices.keys()),
            yticklabels=list(test_generator.class_indices.keys()))
plt.title('confusion matrix')
plt.ylabel('real')
plt.xlabel('predis')
plt.savefig('confusion_matrix.png')

print("gata! descarca fisierele generate.")
