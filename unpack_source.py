import hashlib,zipfile
from pathlib import Path
archive=Path('mediateka-ipad740-source.zip')
assert hashlib.sha256(archive.read_bytes()).hexdigest()=='ce58a3a2d8cf6be776be94a9e9d41513efc47c67ce74259626a5233f7a246264', 'Unexpected source archive'
root=Path.cwd().resolve()
with zipfile.ZipFile(archive) as z:
    for entry in z.infolist():
        target=(root/entry.filename).resolve()
        assert root in target.parents and entry.filename.startswith('MediatekaLite/'), 'Unsafe source path'
    z.extractall(root)
print('Native source archive verified and unpacked.')
