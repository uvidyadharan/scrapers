import wget
import os
import hashlib

wget.download("https://www.firstinspires.org/sites/default/files/uploads/resource_library/ftc/game-manual-part-1-traditional-events.pdf", "gm1.pdf")

buffer = 100000
sha256 = hashlib.sha256()
oldHash = None

with open("gm1.pdf", 'rb') as file:
  while True:
    data = file.read(buffer)
    if not data:
      break
    sha256.update(data)

try:
  with open("gm1.pdf.sha256", "r") as hashFile:
    oldHash = hashFile.read()
except:
  oldHash = ""
  
if oldHash != sha256.hexdigest():
  os.environ["UPDATED"] = "1"
  with open("gm1.pdf.sha256", "w") as hashFile:
    hashFile.write(sha256.hexdigest())
else:
  os.environ["UPDATED"] = "0"
  
