from PIL import Image

img = Image.open("bird.jpg")

mirror = img.transpose(Image.FLIP_LEFT_RIGHT)

mirror.save("mirror.jpg")

print("Mirror image saved as mirror.jpg")