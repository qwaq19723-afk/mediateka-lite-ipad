import hashlib,zipfile
from pathlib import Path
archive=Path('mediateka-ipad744-source.zip')
assert hashlib.sha256(archive.read_bytes()).hexdigest()=='7425ca74ae1afa319df81539853a7190bc63ff54b4b0547af5ea5040d5cd7f36'
root=Path.cwd().resolve()
with zipfile.ZipFile(archive) as z:
    for entry in z.infolist():
        target=(root/entry.filename).resolve()
        assert root in target.parents and entry.filename.startswith('MediatekaLite/')
    z.extractall(root)
print('Native source archive verified and unpacked.')
