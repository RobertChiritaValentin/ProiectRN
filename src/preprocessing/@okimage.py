from PIL import Image

# cream o imagine simpla de culoare gri
img = Image.new('RGB', (300, 300), color = (128, 128, 128))
# o salvam ca piesa ok pentru teste
img.save('piesa_ok.jpg')
print("imaginea piesa_ok.jpg a fost generata!")
