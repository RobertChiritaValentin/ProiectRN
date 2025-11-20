from PIL import Image
import os

input_folder = "data/raw/images/scratches"   # folder imaginile originale
output_folder = "data/processed/images/scratches" # folder imaginile convertite

os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(input_folder):
    if filename.lower().endswith((".png", ".jpg", ".jpeg", ".bmp")):
        img_path = os.path.join(input_folder, filename)
        img = Image.open(img_path) #open

        img = img.convert("L") #greyscale

        img = img.resize((150, 150)) #150x150px

        save_path = os.path.join(output_folder, filename)
        img.save(save_path) #save

        print(f"Procesat: {filename}")

print("Gata!")

from PIL import Image
import os

input_folder = "data/raw/images/crazing"   # folder imaginile originale
output_folder = "data/processed/images/crazing" # folder imaginile convertite

os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(input_folder):
    if filename.lower().endswith((".png", ".jpg", ".jpeg", ".bmp")):
        img_path = os.path.join(input_folder, filename)
        img = Image.open(img_path) #open

        img = img.convert("L") #greyscale

        img = img.resize((150, 150)) #150x150px

        save_path = os.path.join(output_folder, filename)
        img.save(save_path) #save

        print(f"Procesat: {filename}")

print("Gata!")

from PIL import Image
import os

input_folder = "data/raw/images/inclusion"   # folder imaginile originale
output_folder = "data/processed/images/inclusion" # folder imaginile convertite

os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(input_folder):
    if filename.lower().endswith((".png", ".jpg", ".jpeg", ".bmp")):
        img_path = os.path.join(input_folder, filename)
        img = Image.open(img_path) #open

        img = img.convert("L") #greyscale

        img = img.resize((150, 150)) #150x150px

        save_path = os.path.join(output_folder, filename)
        img.save(save_path) #save

        print(f"Procesat: {filename}")

print("Gata!")

from PIL import Image
import os

input_folder = "data/raw/images/patches"   # folder imaginile originale
output_folder = "data/processed/images/patches" # folder imaginile convertite

os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(input_folder):
    if filename.lower().endswith((".png", ".jpg", ".jpeg", ".bmp")):
        img_path = os.path.join(input_folder, filename)
        img = Image.open(img_path) #open

        img = img.convert("L") #greyscale

        img = img.resize((150, 150)) #150x150px

        save_path = os.path.join(output_folder, filename)
        img.save(save_path) #save

        print(f"Procesat: {filename}")

print("Gata!")

from PIL import Image
import os

input_folder = "data/raw/images/pitted_surface"   # folder imaginile originale
output_folder = "data/processed/images/pitted_surface" # folder imaginile convertite

os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(input_folder):
    if filename.lower().endswith((".png", ".jpg", ".jpeg", ".bmp")):
        img_path = os.path.join(input_folder, filename)
        img = Image.open(img_path) #open

        img = img.convert("L") #greyscale

        img = img.resize((150, 150)) #150x150px

        save_path = os.path.join(output_folder, filename)
        img.save(save_path) #save

        print(f"Procesat: {filename}")

print("Gata!")

from PIL import Image
import os

input_folder = "data/raw/images/rolled-in_scale"   # folder imaginile originale
output_folder = "data/processed/images/rolled-in_scale" # folder imaginile convertite

os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(input_folder):
    if filename.lower().endswith((".png", ".jpg", ".jpeg", ".bmp")):
        img_path = os.path.join(input_folder, filename)
        img = Image.open(img_path) #open

        img = img.convert("L") #greyscale

        img = img.resize((150, 150)) #150x150px

        save_path = os.path.join(output_folder, filename)
        img.save(save_path) #save

        print(f"Procesat: {filename}")

print("Gata!")