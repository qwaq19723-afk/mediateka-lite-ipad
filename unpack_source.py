import hashlib,zipfile
from pathlib import Path
archive=Path('mediateka-ipad744-source.zip')
assert hashlib.sha256(archive.read_bytes()).hexdigest()=='7a7f5d8ce6ec6f8ba8aa81a4c101769c4e2dc81e5b7c317869c20b2b0811a9fd'
root=Path.cwd().resolve()
with zipfile.ZipFile(archive) as z:
    for entry in z.infolist():
        target=(root/entry.filename).resolve()
        assert root in target.parents and entry.filename.startswith('MediatekaLite/')
    z.extractall(root)
print('Native source archive verified and unpacked.')
