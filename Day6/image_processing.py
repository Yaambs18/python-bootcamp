from PIL import Image

img = Image.open('python_logo.jpg')

print(img.size)
print(img.filename)
# img.show()

# ------------- cropping image---------
x = 0
y = 0

w = 250/5
h = 74/4
# img.crop((x,y,w,h)).show()

# img.resize((50,20)).show()

# img.rotate(180).show()

#---------------- mixing/transparency------------------

red = Image.open('red_color.jpg')
blue = Image.open('blue_color.jpg')
blue.show()

red.putalpha(128)
blue.putalpha(128)

blue.paste(im=red, box=(0,0), mask=red).convert('RGB')
blue.save("purple.jpg")

purple = Image.open("puprle.jpg")
purple.show()
