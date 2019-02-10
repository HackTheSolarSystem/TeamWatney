from PIL import Image
import pathlib
import glob
import subprocess
import re
import os
import datetime

T = 512

start_date = datetime.datetime.strptime("2019-01-01","%Y-%m-%d")

pathlib.Path("output/jpeg/").mkdir(parents=True, exist_ok=True)
for g in glob.glob("sources/*.tiff"):
  m = re.search("sources/B20_day(\d{2})_resx2.tiff",g)
  num = int(m.group(1))
  fpath = "output/jpeg/{0}.jpg".format(num)
  if not os.path.isfile(fpath):
    subprocess.check_call(['gdal_translate','-of','JPEG',g,fpath])

for j in glob.glob("output/jpeg/*.jpg"):
  index = int(os.path.splitext(os.path.basename(j))[0])
  im = Image.open(j)
  date = start_date + datetime.timedelta(days=index)
  for z in range(0,4):
    t = im.copy()
    p = pow(2,z)
    t2 = t.resize((T * p*2,T * p),Image.LANCZOS)
    for x in range(0,p*2):
      for y in range(0,p):
        print(z,x,y)
        tile = t2.crop((T*x,T*y,T*(x+1),T*(y+1)))
        dirname = "output/tiles/{0}/{1}/{2}".format(date.strftime("%Y-%m-%d"),z,y)
        pathlib.Path(dirname).mkdir(parents=True, exist_ok=True)
        tile.save(dirname + "/{0}.jpg".format(x), "JPEG")
