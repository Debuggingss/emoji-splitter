from PIL import Image
from sys import argv
import math
import requests


if len(argv) < 4:
    print("usage: python splitter.py <image_url> <emoji_size> <emoji_name>")
    exit(1)

URL = argv[1]
ENDSIZE = int(argv[2])
EMOJINAME = argv[3]


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
        im1 = im.crop((w * ENDSIZE, h * ENDSIZE, w * ENDSIZE +
                      ENDSIZE, h * ENDSIZE + ENDSIZE))
        im1.save(f"{EMOJINAME}_{counter}.png")
        counter += 1

emojis = []

for i in range(widthratio*heightratio):
    emojis.append(f":{EMOJINAME}_{i}:")

print("".join(emojis))
