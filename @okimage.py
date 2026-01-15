from PIL import Image

img = Image.new('RGB', (300, 300), color = (128, 128, 128))
img.save('piesa_ok.jpg')
print("Imaginea piesa_ok.jpg a fost generata!")