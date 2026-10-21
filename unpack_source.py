import hashlib,zipfile
from pathlib import Path
archive=Path('mediateka-ipad757-source.zip')
assert hashlib.sha256(archive.read_bytes()).hexdigest()=='95b67484d2b7cea570254ab209605b5067bf9e4a79eaf956316d4c5a406f4906'
root=Path.cwd().resolve()
with zipfile.ZipFile(archive) as z:
    for entry in z.infolist():
        target=(root/entry.filename).resolve()
        assert root in target.parents and entry.filename.startswith('MediatekaLite/')
    z.extractall(root)
print('Native source archive verified and unpacked.')
