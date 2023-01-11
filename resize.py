'''
author: masumori.toshiaki@sysmex.co.jp
resize and convert png to jpg
'''

from PIL import Image
import os

directory = 'org'   # input directory
distination = 'output'  # output directory

target_w = 800  # direct risized width with pixel

dirList = os.listdir(directory)
print(dirList)

for file in dirList:
    # filter for image file's extension
    if '.png' not in file:
        continue

    path = os.path.join(directory, file)

    # change filename xxx.png -> xxx.jpg
    sp = file.split('.')
    sp[-1] = 'jpg'
    dist = os.path.join(distination, '.'.join(sp))

    img = Image.open(path)
    img = img.convert('RGB')    # png to jpeg (drop alpha value)

    img_w = img.width
    img_h = img.height

    ratio = float(img_h) / img_w    # aspect ratio

    # height is automatically calcurated by target width.
    print(img_w, img_h, ratio)
    target_h = int(target_w * ratio)

    img_resize_lanczos = img.resize((target_w, target_h), Image.LANCZOS)
    img_resize_lanczos.save(dist)
