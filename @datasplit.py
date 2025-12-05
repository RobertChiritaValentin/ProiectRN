import os
import shutil
import random
from pathlib import Path

SOURCE_DIR = "data/processed/images" 
DEST_DIR   = "data/test"              

SPLIT = {
    "train": 0.70,
    "val":   0.15,
    "test":  0.15
}


for subset in SPLIT.keys():
    Path(f"{DEST_DIR}/{subset}").mkdir(parents=True, exist_ok=True)

for cls in os.listdir(SOURCE_DIR):
    cls_path = f"{SOURCE_DIR}/{cls}"
    if not os.path.isdir(cls_path):
        continue

    images = os.listdir(cls_path)
    random.shuffle(images)

    train_end = int(len(images) * SPLIT["train"])
    val_end   = train_end + int(len(images) * SPLIT["val"])

    subsets = {
        "train": images[:train_end],
        "val":   images[train_end:val_end],
        "test":  images[val_end:]
    }

    for subset, files in subsets.items():
        dest_folder = f"{DEST_DIR}/{subset}/{cls}"
        Path(dest_folder).mkdir(parents=True, exist_ok=True)
        for img in files:
            shutil.copy(f"{cls_path}/{img}", f"{dest_folder}/{img}")

print("\nDataset impartit cu succes in 70/15/15!")
print("Rezultat final in: data/test/\n")