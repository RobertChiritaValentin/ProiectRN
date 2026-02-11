import cv2
import numpy as np
import os

# configuram caile catre folderele de intrare si iesire
base_dir = os.path.dirname(os.path.abspath(__file__))
input_folder = os.path.join(base_dir, '../../data/raw/images/scratches') # imagini bune de referinta
output_folder = os.path.join(base_dir, '../../data/generated/defects') # unde salvam datele generate

# ne asiguram ca folderul de iesire exista
os.makedirs(output_folder, exist_ok=True)

# functia care adauga o zgarietura artificiala pe o imagine
def add_scratch(image):
    # obtinem dimensiunile imaginii
    h, w, _ = image.shape
    # alegem coordonate aleatorii pentru capetele liniei
    x1, y1 = np.random.randint(0, w), np.random.randint(0, h)
    x2, y2 = np.random.randint(0, w), np.random.randint(0, h)
    
    # desenam o linie alba care simuleaza zgarietura
    cv2.line(image, (x1, y1), (x2, y2), (255, 255, 255), thickness=2)
    return image

print("generare date sintetice...")

# generam 100 de imagini cu defecte simulate
for i in range(100):
    # cream o imagine neagra de baza 224x224
    img = np.zeros((224, 224, 3), dtype=np.uint8) 
    
    # aplicam efectul de zgarietura
    img = add_scratch(img)
    
    # salvam imaginea generata pe disc
    cv2.imwrite(os.path.join(output_folder, f"syn_defect_{i}.jpg"), img)

print(f"au fost generate 100 imagini in {output_folder}")
