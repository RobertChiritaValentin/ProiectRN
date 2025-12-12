import cv2
import numpy as np
import os

# config
base_dir = os.path.dirname(os.path.abspath(__file__))
input_folder = os.path.join(base_dir, '../../data/raw/images/scratches') # good images
output_folder = os.path.join(base_dir, '../../data/generated/defects') # save

os.makedirs(output_folder, exist_ok=True)

def add_scratch(image):
    # simuleaza o zgarietura
    h, w, _ = image.shape
    x1, y1 = np.random.randint(0, w), np.random.randint(0, h)
    x2, y2 = np.random.randint(0, w), np.random.randint(0, h)
    # deseneaza 
    cv2.line(image, (x1, y1), (x2, y2), (255, 255, 255), thickness=2)
    return image

print("Generare date sintetice...")
# incarca img reale cu zgomot
for i in range(100):
    img = np.zeros((224, 224, 3), dtype=np.uint8) # imagine neagra
    img = add_scratch(img)
    # Salvam folosind calea completa
    cv2.imwrite(os.path.join(output_folder, f"syn_defect_{i}.jpg"), img)

print(f"Au fost generate 100 imagini in {output_folder}")