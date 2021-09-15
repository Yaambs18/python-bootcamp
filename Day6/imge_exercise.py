from PIL import Image

words = Image.open('word_matrix.jpg')
hider = Image.open('mask.jpg')
# hider.resize((1015,559))
hider.putalpha(128)

words.paste(im=hider.resize((1015,559)), box=(0,0), mask=hider.resize((1015,559)))
words.save('message.png')

msg = Image.open('message.png')
msg.show()