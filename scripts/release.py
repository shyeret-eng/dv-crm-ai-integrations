"""Deterministic local packaging. No installs, publishing, or network calls."""
import hashlib, json, shutil, tempfile, zipfile
from pathlib import Path
from check import ROOT, check, version

def write_json(path, data):
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(data,indent=2)+'\n')

def archive(source,path):
    with zipfile.ZipFile(path,'w',zipfile.ZIP_DEFLATED) as out:
        for p in sorted(source.rglob('*')):
            if p.is_file():
                info=zipfile.ZipInfo(str(Path(source.name)/p.relative_to(source)),(2026,1,1,0,0,0))
                info.compress_type=zipfile.ZIP_DEFLATED
                info.external_attr=0o100644<<16
                out.writestr(info,p.read_bytes())

def build():
    check(generated=False)
    ver=version(); cfg=json.loads((ROOT/'config/integration.json').read_text())
    dist=ROOT/'dist'; dist.mkdir(exist_ok=True)
    target=dist/ver
    if target.is_symlink(): raise ValueError('Refusing symlink release directory')
    with tempfile.TemporaryDirectory(prefix='.build-',dir=dist) as tmp:
        base=Path(tmp)
        metadata={'name':'dv-crm','version':ver,'description':'Use Dynamic Vision CRM for lookups and requested event, task and inactive draft quote work within caller permissions.','author':{'name':'Dynamic Vision'}}
        for platform in ['portable','claude','gemini']:
            package=base/platform/'dv-crm'
            shutil.copytree(ROOT/'skills',package/'skills')
            (package/'README.md').write_text('Dynamic Vision CRM workflow, version '+ver+'.\nReview canonical platform guides before installation. OAuth and runtime paths remain untested.\n')
            if platform=='portable':
                write_json(package/'plugin.json',dict({'$schema':'https://agent-plugins.org/schemas/1.0.0/plugin.schema.json'},**metadata))
            elif platform=='claude':
                write_json(package/'.claude-plugin/plugin.json',metadata)
                write_json(package/'.mcp.json',{'mcpServers':{'dv-crm':{'type':'http','url':cfg['endpoint']}}})
            else:
                write_json(package/'gemini-extension.json',{'name':'dv-crm','version':ver,'description':metadata['description'],'contextFileName':'GEMINI.md','mcpServers':{'dv-crm':{'httpUrl':cfg['endpoint']}}})
                (package/'GEMINI.md').write_text('For Dynamic Vision CRM requests, use the bundled dv-crm skill. Discover caller-permitted schemas; use requested deployed writes with optimistic concurrency. Never send messages or activate/confirm quotes.\n')
            archive(package,base/(platform+'-'+ver+'.zip'))
        archive(ROOT/'skills/dv-crm',base/('skill-'+ver+'.zip'))
        write_json(base/'release-index.json',{'version':ver,'status':'local-review-candidate','schemaSha256':hashlib.sha256((ROOT/'config/plugin.schema.json').read_bytes()).hexdigest(),'sha256':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(base.glob('*.zip'))}})
        (base/'UPDATE-ACTIONS.md').write_text('# Client actions for '+ver+'\n\n- ChatGPT: retain existing hosted connection; skill import needs version/review/refresh as appropriate. No cloud binding is created by this skills-only artifact.\n- Codex: review companion and enable existing CRM connection; installation untested.\n- Claude Code: version changed; update/reload through host. Marketplace auto-update requires opt-in. Approve only needed role-eligible scopes; use DV Edit permissions then client refresh for new capabilities.\n- Gemini CLI: update extension and restart; auto-update requires opt-in. OAuth is untested.\n- Gemini consumer: separate custom app consent/account restrictions; no extension auto-update claim.\n\nNo messages, installs, or publication were performed. See canonical CHANGELOG.md and docs/platforms.md.\n')
        if target.exists(): shutil.rmtree(target)
        shutil.copytree(base,target)
    check()
    print('Generated:',target)
if __name__=='__main__': build()
