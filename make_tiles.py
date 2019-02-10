from PIL import Image
import pathlib
import glob
import subprocess
import re
import os

pathlib.Path("output/jpeg/").mkdir(parents=True, exist_ok=True)
for g in glob.glob("sources/*.tiff"):
  m = re.search("sources/B20_day(\d{2})_resx2.tiff",g)
  num = int(m.group(1))
  fpath = "output/jpeg/{0}.jpg".format(num)
  if not os.path.isfile(fpath):
    subprocess.check_call(['gdal_translate','-of','JPEG',g,fpath])




