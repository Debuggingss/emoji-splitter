from PIL import Image
import math
import requests

ENDSIZE = 128

EMOJINAME = "zany"

URL = "https://images.emojiterra.com/twitter/v13.0/512px/1f92a.png"

print("Downloading Image...")
r = requests.get(URL)

with open("toconvert.png", 'wb') as f:
    f.write(r.content)
    print("Image Downloaded")

im = Image.open(r".\toconvert.png").convert("RGBA")

width, height = im.size

widthratio = math.ceil(width/ENDSIZE)
heightratio = math.ceil(height/ENDSIZE)

print(f"Emoji Name: {EMOJINAME}\n"
      f"Split Size: {ENDSIZE}\n"
      f"Width: {width}\n"
      f"Height: {height}\n"
      f"Width Ratio: {widthratio}\n"
      f"Height Ratio: {heightratio}\n"
      f"Number of Images: {widthratio * heightratio}")

counter = 0

for h in range(heightratio):
    for w in range(widthratio):
        im1 = im.crop((w * ENDSIZE, h * ENDSIZE, w * ENDSIZE + ENDSIZE, h * ENDSIZE + ENDSIZE))
        im1.save(f"{EMOJINAME}_{counter}.png")
        counter += 1

emojis = []

for i in range(widthratio*heightratio):
    emojis.append(f":{EMOJINAME}_{i}:")

print("".join(emojis))
