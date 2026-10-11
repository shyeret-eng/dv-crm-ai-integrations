"""Publication gate: scan files, nested ZIP members, and all local Git blobs/metadata.
Patterns supplement manual review; they cannot prove absence of every possible secret.
Only public-safe sources/current release belong in this repository.
"""
import io, re, subprocess, zipfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
PATTERNS={
 'local user path':r'/(?:Users|home)/[A-Za-z0-9_. -]+/',
 'private hosted app identifier':r'plugin_asdk_app_[a-f0-9]{20,}',
 'private session identifier':r'\b(?:019fd85c|6abd337e|01a0f39b)[-a-f0-9]{15,}\b',
 'private backend identity':r'dynamic-vision-erp-BU4|mcp/work|b8c66fe|fe97347|3c7d548',
 'private key':r'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----',
 'GitHub token':r'\b(?:gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{30,})\b',
 'CRM token':r'\bdvcrm_[A-Za-z0-9_-]{20,}\b',
 'JWT':r'\beyJ[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}\b',
 'literal bearer':r'Bearer\s+[A-Za-z0-9._-]{15,}',
 'email address':r'(?<![A-Za-z0-9._-])[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}',
}
# The denylist literals in this gate are checks, not private records. Do not
# exempt any other source, artifact, or Git object from the gate.
def scan(name,data,depth=0):
 if depth>3:raise ValueError('Archive nesting too deep: '+name)
 if name.endswith('.zip'):
  with zipfile.ZipFile(io.BytesIO(data)) as z:
   for member in z.infolist():
    assert not member.filename.startswith('/') and '..' not in Path(member.filename).parts
    assert member.file_size < 5_000_000
    scan(name+'!'+member.filename,z.read(member),depth+1)
  return
 text=data.decode('utf-8')
 if name.endswith('scripts/audit_public.py'):return
 for label,pattern in PATTERNS.items():
  for match in re.finditer(pattern,text):
   if label=='email address' and (match.group(0).endswith('@users.noreply.github.com') or match.group(0)=='noreply@anthropic.com'):continue
   raise ValueError(label+' found in '+name+' (value suppressed)')

def git(*args):
 return subprocess.check_output(['git','-C',str(ROOT),*args],stderr=subprocess.DEVNULL)

def run():
 files=0
 for p in ROOT.rglob('*'):
  rel=p.relative_to(ROOT)
  if any(x in rel.parts for x in ['.git','.venv','__pycache__']):continue
  if not p.is_file():continue
  assert not p.is_symlink(),str(rel)
  assert p.suffix not in ['.db','.sqlite','.pem','.key'],str(rel)
  assert not p.name.startswith('.env'),str(rel)
  scan(str(rel),p.read_bytes());files+=1
 blobs=0
 if (ROOT/'.git').exists():
  # Includes unreachable objects: old private blobs must not enter publication.
  entries=git('cat-file','--batch-all-objects','--batch-check=%(objectname) %(objecttype)').decode().splitlines()
  audit_bytes=(ROOT/'scripts/audit_public.py').read_bytes()
  # Earlier versions of this file list the forbidden patterns too; skip only those exact blobs.
  audit_history={line.split()[0] for line in git('rev-list','--all','--objects','--','scripts/audit_public.py').decode().splitlines() if line.endswith(' scripts/audit_public.py')}
  for entry in entries:
   oid,kind=entry.split()
   if kind not in ['blob','commit','tag']:continue
   data=git('cat-file',kind,oid)
   if kind=='blob' and (data==audit_bytes or oid in audit_history):continue
   name='git-object:'+oid
   if data.startswith(b'PK\x03\x04'):name+='.zip'
   scan(name,data);blobs+=1
 print(f'PASS: {files} files including ZIP members; {blobs} Git blobs/commit/tag objects audited. No flagged sensitive content. Manual semantic review is also required.')
if __name__=='__main__':run()
