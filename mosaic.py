from PIL import Image
import pathlib
import glob
import subprocess
import re
import os
import datetime

T = 512

r  = Image.new("RGB", (1920, 1080), "black")

j = "output/jpeg/1.jpg"
index = int(os.path.splitext(os.path.basename(j))[0])
im = Image.open(j)
for z in range(0,4):
  t = im.copy()
  p = pow(2,z)
  t2 = t.resize((T * p*2,T * p),Image.LANCZOS)
  for x in range(0,p*2):
    for y in range(0,p):
      print(z,x,y)
      tile = t2.crop((T*x,T*y,T*(x+1),T*(y+1)))
      LT = 64
      tx = tile.resize((LT,LT),Image.LANCZOS)
      foo = 0
      if z == 1:
        foo = 128
      if z == 2:
        foo = 256
      if z == 3:
        foo = 512
      r.paste(tx,(x * 66,y*66+foo,x * 66+LT,y*66+LT+foo))

r.save("mosaic.jpg","JPEG")
