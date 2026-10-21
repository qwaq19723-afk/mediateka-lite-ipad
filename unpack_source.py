import hashlib,zipfile
from pathlib import Path
archive=Path('mediateka-ipad757-source.zip')
assert hashlib.sha256(archive.read_bytes()).hexdigest()=='8c1d8f092a45405355fcdc793a3568f833b0ee42b86367cf44f1887396895118'
root=Path.cwd().resolve()
with zipfile.ZipFile(archive) as z:
    for entry in z.infolist():
        target=(root/entry.filename).resolve()
        assert root in target.parents and entry.filename.startswith('MediatekaLite/')
    z.extractall(root)
print('Native source archive verified and unpacked.')
