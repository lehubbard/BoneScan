from pathlib import Path

path = str(Path.home()) + '/.ssh/beagleKey.pub'
pKey = open(path, 'rb')
pKeyBytes = pKey.read()
print(pKeyBytes)
