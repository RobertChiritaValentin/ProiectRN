import os
import shutil
import random
from pathlib import Path

# definim calea catre folderul cu imagini procesate
SOURCE_DIR = "data/processed/images"
# definim caile unde vom salva seturile impartite
DEST_DIR_TRAIN = "data/train"
DEST_DIR_VAL = "data/validation"
DEST_DIR_TEST = "data/test"

# procentele pentru fiecare set 70 antrenare 15 validare 15 testare
TRAIN_SPLIT = 0.70
VAL_SPLIT = 0.15
TEST_SPLIT = 0.15

# cream folderele daca nu exista deja
for d in [DEST_DIR_TRAIN, DEST_DIR_VAL, DEST_DIR_TEST]:
    Path(d).mkdir(parents=True, exist_ok=True)

# iteram prin fiecare clasa de defecte
for cls in os.listdir(SOURCE_DIR):
    cls_path = f"{SOURCE_DIR}/{cls}"
    if not os.path.isdir(cls_path):
        continue

    # obtinem lista de imagini si o amestecam aleatoriu
    images = os.listdir(cls_path)
    random.shuffle(images)

    # calculam indexii de taiere pentru impartire
    train_end = int(len(images) * TRAIN_SPLIT)
    val_end = train_end + int(len(images) * VAL_SPLIT)

    # impartim lista de fisiere
    train_files = images[:train_end]
    val_files = images[train_end:val_end]
    test_files = images[val_end:]

    # copiem fisierele in folderul de antrenament
    for file in train_files:
        dest = f"{DEST_DIR_TRAIN}/{cls}"
        Path(dest).mkdir(parents=True, exist_ok=True)
        shutil.copy(f"{cls_path}/{file}", f"{dest}/{file}")

    # copiem fisierele in folderul de validare
    for file in val_files:
        dest = f"{DEST_DIR_VAL}/{cls}"
        Path(dest).mkdir(parents=True, exist_ok=True)
        shutil.copy(f"{cls_path}/{file}", f"{dest}/{file}")

    # copiem fisierele in folderul de testare
    for file in test_files:
        dest = f"{DEST_DIR_TEST}/{cls}"
        Path(dest).mkdir(parents=True, exist_ok=True)
        shutil.copy(f"{cls_path}/{file}", f"{dest}/{file}")

print("done.")
