import hashlib,zipfile
from pathlib import Path
archive=Path('mediateka-ipad758-source.zip')
assert hashlib.sha256(archive.read_bytes()).hexdigest()=='4c2c9a0f3d844a4a01e68ff9188b18d8ce8954b7d9c55ee15564f59353c57cb6'
root=Path.cwd().resolve()
with zipfile.ZipFile(archive) as z:
    for entry in z.infolist():
        target=(root/entry.filename).resolve()
        assert root in target.parents and entry.filename.startswith('MediatekaLite/')
    z.extractall(root)
print('Native source archive verified and unpacked.')
