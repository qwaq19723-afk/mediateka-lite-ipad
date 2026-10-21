import hashlib,zipfile
from pathlib import Path
archive=Path('mediateka-ipad749-source.zip')
assert hashlib.sha256(archive.read_bytes()).hexdigest()=='3d0860024652f25f701441905acf6a29fa632b63c62cbe7a7d748b8388624d92'
root=Path.cwd().resolve()
with zipfile.ZipFile(archive) as z:
    for entry in z.infolist():
        target=(root/entry.filename).resolve()
        assert root in target.parents and entry.filename.startswith('MediatekaLite/')
    z.extractall(root)
print('Native source archive verified and unpacked.')
