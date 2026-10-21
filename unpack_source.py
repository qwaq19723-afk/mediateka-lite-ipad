import hashlib,zipfile
from pathlib import Path
archive=Path('mediateka-ipad758-source.zip')
assert hashlib.sha256(archive.read_bytes()).hexdigest()=='0a0827775ca3ea2da6917c183679b0acfc740564e43a00f4a294090e43ae71ed'
root=Path.cwd().resolve()
with zipfile.ZipFile(archive) as z:
    for entry in z.infolist():
        target=(root/entry.filename).resolve()
        assert root in target.parents and entry.filename.startswith('MediatekaLite/')
    z.extractall(root)
print('Native source archive verified and unpacked.')
