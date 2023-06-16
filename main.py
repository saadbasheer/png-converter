import sys
import os
from PIL import Image

inputdir = r'C:\Users\saadbasheer\Desktop\Code\Python\Projects\jpgtopngconverter\input'
outputdir = r'C:\Users\saadbasheer\Desktop\Code\Python\Projects\jpgtopngconverter\output'

for index,images in enumerate(os.listdir(inputdir),start=1):
    imagedir = os.path.join(inputdir,images)
    outdir=os.path.join(outputdir,os.path.splitext(images)[0]+".png")
    img = Image.open(imagedir)
    img.save(outdir,'png')
    print(f"image {index} converted to png")

print("all images converted to png")

