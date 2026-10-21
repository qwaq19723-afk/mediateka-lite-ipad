import hashlib,zipfile
from pathlib import Path
archive=Path('mediateka-ipad747-source.zip')
assert hashlib.sha256(archive.read_bytes()).hexdigest()=='3c5eafbd77b521306218b1e98acb6dcc001f7b498b8e1182d958d584b1323882'
root=Path.cwd().resolve()
with zipfile.ZipFile(archive) as z:
    for entry in z.infolist():
        target=(root/entry.filename).resolve()
        assert root in target.parents and entry.filename.startswith('MediatekaLite/')
    z.extractall(root)
print('Native source archive verified and unpacked.')
