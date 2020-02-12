from PIL import Image
import os

#WORK IN PROGRESS
#Author: Ricardus Hasbani
#Version 1


#IMPORTANT a and b need to be coprime (plan to make random coprime generator or give a user the option to input coprimes)
a = 13
b = 3

def encrypt(val): #simple affine cipher for the time being
    e = (a * val + b) % 255
    return e

im = Image.open(r"INSERT PATH HERE")
im = im.convert("RGB")
px = im.load()
width, height = im.size
pv = list(im.getdata())
pv_flat = [x for sets in pv for x in sets] #cleans list from [(10, 10, 10), (20, 20, 20)] to [10, 10, 10, 20, 20, 20]

m = 0
for i in range(width):
    print(i)
    for j in range(height):
        px[i,j] = (encrypt(pv_flat[m]), encrypt(pv_flat[m + 1]), encrypt(pv_flat[m + 2])) #alters the RGB colour values
        m = m + 1

im = im.save("EncryptedImage.jpg")