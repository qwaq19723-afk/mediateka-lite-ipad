import hashlib,zipfile
from pathlib import Path
archive=Path('mediateka-ipad740-source.zip')
assert hashlib.sha256(archive.read_bytes()).hexdigest()=='36c6bca33821a48839c7710ddb783ef40bc7c331475b8946ea83762f138fa37b', 'Unexpected source archive'
root=Path.cwd().resolve()
with zipfile.ZipFile(archive) as z:
    for entry in z.infolist():
        target=(root/entry.filename).resolve()
        assert root in target.parents and entry.filename.startswith('MediatekaLite/'), 'Unsafe source path'
    z.extractall(root)
print('Native source archive verified and unpacked.')
