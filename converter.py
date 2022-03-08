# Convert images in a folder "new/" to a format that can easily be read by the website
# James Sprague 3-8-2022

from PIL import Image, ImageOps
import os

old_path = "new/"
new_path = "pics/"
old_dir = os.listdir(old_path)
num_pics = len(os.listdir(new_path)) - 1

for i in old_dir:
    im1 = Image.open(f'{old_path}{i}')
    im1 = im1.convert('RGB')
    im1 = ImageOps.exif_transpose(im1)
    num_pics = num_pics + 1
    im1.save(f'{new_path}{num_pics}.jpg')
    os.remove(f'{old_path}{i}')