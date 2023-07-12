import wget
import hashlib
import os
from pushbullet import PushBullet

filename = "gm2.pdf"

access_token = os.getenv('PUSHBULLET_ACCESS_TOKEN')
pb = PushBullet(access_token)

if os.path.exists(filename):
  os.remove(filename)
wget.download("https://www.firstinspires.org/sites/default/files/uploads/resource_library/ftc/game-manual-part-2-remote.pdf", filename)

buffer = 100000
sha256 = hashlib.sha256()
oldHash = None

with open(filename, 'rb') as file:
  while True:
    data = file.read(buffer)
    if not data:
      break
    sha256.update(data)
    
hashName = filename + ".sha256"

try:
  with open(hashName, "r") as hashFile:
    oldHash = hashFile.read()
except:
  oldHash = ""
  
if oldHash != sha256.hexdigest():
  with open(hashName, "w") as hashFile:
    hashFile.write(sha256.hexdigest())

  pb.push_note("Game Manual 1 Updated", "The Game Manual 1 has been updated. Please download the new version.")