import os
import zipfile

path = '.'

def zipdir(path, zf):
  for root, dirs, files in os.walk(path):
    for f in files:
      zf.write(os.path.join(root, f))

if __name__ == '__main__':
  for folder in os.listdir(path):
    if not os.path.isdir(os.path.join(path, folder)):
      continue
    zipf = zipfile.ZipFile('{}.zip'.format(os.path.join(path, folder)), 'w', zipfile.ZIP_DEFLATED)
    zipdir(os.path.join(path, folder), zipf)
    zipf.close()