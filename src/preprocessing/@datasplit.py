import os
import shutil
import random
from pathlib import Path

SOURCE_DIR = "data/processed/images"
DEST_DIR_TRAIN = "data/train"
DEST_DIR_VAL = "data/validation"
DEST_DIR_TEST = "data/test"

TRAIN_SPLIT = 0.70
VAL_SPLIT = 0.15
TEST_SPLIT = 0.15

for d in [DEST_DIR_TRAIN, DEST_DIR_VAL, DEST_DIR_TEST]:
    Path(d).mkdir(parents=True, exist_ok=True)

for cls in os.listdir(SOURCE_DIR):
    cls_path = f"{SOURCE_DIR}/{cls}"
    if not os.path.isdir(cls_path):
        continue

    images = os.listdir(cls_path)
    random.shuffle(images)

    train_end = int(len(images) * TRAIN_SPLIT)
    val_end = train_end + int(len(images) * VAL_SPLIT)

    train_files = images[:train_end]
    val_files = images[train_end:val_end]
    test_files = images[val_end:]

    for file in train_files:
        dest = f"{DEST_DIR_TRAIN}/{cls}"
        Path(dest).mkdir(parents=True, exist_ok=True)
        shutil.copy(f"{cls_path}/{file}", f"{dest}/{file}")

    for file in val_files:
        dest = f"{DEST_DIR_VAL}/{cls}"
        Path(dest).mkdir(parents=True, exist_ok=True)
        shutil.copy(f"{cls_path}/{file}", f"{dest}/{file}")

    for file in test_files:
        dest = f"{DEST_DIR_TEST}/{cls}"
        Path(dest).mkdir(parents=True, exist_ok=True)
        shutil.copy(f"{cls_path}/{file}", f"{dest}/{file}")

print("Done.")