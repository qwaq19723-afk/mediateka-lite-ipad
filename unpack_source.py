import hashlib,zipfile
from pathlib import Path
archive=Path('mediateka-ipad757-source.zip')
assert hashlib.sha256(archive.read_bytes()).hexdigest()=='9bd757ac57f7ca226dfe3b747f16c7d845a4b58ba30216be24087530b01410a1'
root=Path.cwd().resolve()
with zipfile.ZipFile(archive) as z:
    for entry in z.infolist():
        target=(root/entry.filename).resolve()
        assert root in target.parents and entry.filename.startswith('MediatekaLite/')
    z.extractall(root)
print('Native source archive verified and unpacked.')
