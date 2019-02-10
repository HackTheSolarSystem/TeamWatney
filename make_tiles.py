from PIL import Image
import pathlib
import glob
import subprocess
import re
import os
import datetime

T = 512

start_date = datetime.datetime.strptime("2019-01-01","%Y-%m-%d")
print(start_date)

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
  print(im)
  t = im.copy()
  p = pow(2,0)
  t2 = t.resize((T * p,T * p),Image.LANCZOS)
  dirname = "output/tiles/{0}/{1}/{2}".format(date.strftime("%Y-%m-%d"),0,0)
  pathlib.Path(dirname).mkdir(parents=True, exist_ok=True)
  t2.save(dirname + "/0.jpg", "JPEG")




