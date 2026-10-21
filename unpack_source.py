import hashlib,zipfile
from pathlib import Path
archive=Path('mediateka-ipad746-source.zip')
assert hashlib.sha256(archive.read_bytes()).hexdigest()=='93c1583a6f5a983fbd08c09644d34d75fd8e543bb1707f46f84d0e8d47667b59'
root=Path.cwd().resolve()
with zipfile.ZipFile(archive) as z:
    for entry in z.infolist():
        target=(root/entry.filename).resolve()
        assert root in target.parents and entry.filename.startswith('MediatekaLite/')
    z.extractall(root)
print('Native source archive verified and unpacked.')
