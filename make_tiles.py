from PIL import Image
import pathlib
import glob
import subprocess
import re

pathlib.Path("output").mkdir(parents=True, exist_ok=True)
for g in glob.glob("sources/*.tiff"):
  m = re.search("sources/B20_day(\d{2})_resx2.tiff",g)
  num = int(m.group(1))
  subprocess.check_call(['gdal_translate','-of','JPEG',g,"output/{0}.jpg".format(num)])




