"""Offline structural/link checks; --schema adds the vendored official schema."""
import argparse, hashlib, json, re
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
def version():
    value = (ROOT / 'VERSION').read_text().strip()
    if not re.fullmatch(r'(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)', value):
        raise ValueError('VERSION must use strict x.y.z')
    return value

def check(schema=False, generated=True):
    ver = version()
    cfg = json.loads((ROOT / 'config/integration.json').read_text())
    assert len(cfg['scopes']) == 16 and len(cfg['tools']) == 42
    assert set(cfg['tools'].values()) == set(cfg['scopes'])
    assert cfg['tools']['get_whats_new'] == 'events.read'
    assert cfg['tools']['remove_quote_line'] == 'quotes.write'
    assert cfg['roleEligibleScopes']['user'] == ['events.read','tasks.read','tasks.write','attention.read']
    assert all('activity.read' not in scopes for role, scopes in cfg['roleEligibleScopes'].items() if role != 'admin')
    assert 'quotes.read' in cfg['roleEligibleScopes']['warehouse_manager']
    assert 'quotes.write' not in cfg['roleEligibleScopes']['warehouse_manager']
    assert 'equipment.read' in cfg['roleEligibleScopes']['warehouse_manager']
    assert all(not {'equipment.write','labor.finance','schedule.write'} & set(cfg['roleEligibleScopes'][r]) for r in ['warehouse_manager','user'])
    assert cfg['roleEligibleScopes']['admin'].count('events.create') == 1 and all('events.create' not in s for r,s in cfg['roleEligibleScopes'].items() if r != 'admin')
    assert cfg['endpoint'].startswith('https://')
    skill = ROOT / 'skills/dv-crm/SKILL.md'
    content = skill.read_text()
    assert content.startswith('---\nname: dv-crm\ndescription: ')
    description = content.split('\ndescription: ',1)[1].split('\n',1)[0]
    assert 0 < len(description) <= 1024
    for p in ROOT.rglob('*'):
        if any(x in p.parts for x in ['.git','.venv','__pycache__','dist']): continue
        assert not p.is_symlink(), f'Symlink: {p}'
        if p.suffix == '.json': json.loads(p.read_text())
        if p.suffix == '.md':
            for target in re.findall(r'\]\(([^)]+)\)',p.read_text()):
                if '://' in target or target.startswith('#'): continue
                target = target.split('#',1)[0]
                dest = (p.parent / target).resolve()
                assert ROOT in dest.parents, f'Escaping link in {p}: {target}'
                if generated or 'dist' not in dest.relative_to(ROOT).parts:
                    assert dest.exists(), f'Broken link in {p}: {target}'
    if generated:
        release = ROOT / 'dist' / ver
        if release.exists():
            index = json.loads((release/'release-index.json').read_text())
            for name, expected in index['sha256'].items():
                assert hashlib.sha256((release/name).read_bytes()).hexdigest() == expected, f'Hash mismatch: {name}'
            for platform in ['portable','claude','gemini']:
                package = release/platform/'dv-crm'
                assert (package/'skills/dv-crm/SKILL.md').read_bytes() == skill.read_bytes()
                for ref in (skill.parent/'references').iterdir():
                    assert (package/'skills/dv-crm/references'/ref.name).read_bytes() == ref.read_bytes()
            portable = release/'portable/dv-crm'
            assert not (portable/'mcp.json').exists() and not (portable/'.app.json').exists()
            manifest = json.loads((portable/'plugin.json').read_text())
            assert manifest['version'] == ver
            if schema:
                from jsonschema import Draft202012Validator
                spec=json.loads((ROOT/'config/plugin.schema.json').read_text())
                Draft202012Validator.check_schema(spec)
                Draft202012Validator(spec).validate(manifest)
            for platform,filename,key in [('claude','.mcp.json','url'),('gemini','gemini-extension.json','httpUrl')]:
                data=json.loads((release/platform/'dv-crm'/filename).read_text())
                assert data['mcpServers']['dv-crm'][key] == cfg['endpoint']
                assert 'headers' not in data['mcpServers']['dv-crm']
                assert 'includeTools' not in data['mcpServers']['dv-crm']
                assert 'excludeTools' not in data['mcpServers']['dv-crm']
        elif schema:
            raise ValueError('Generate packages before schema checking')
    print('PASS: version, production scope metadata, canonical skill, JSON, local links, package parity and hashes' + ('; official manifest schema' if schema else ''))
if __name__ == '__main__':
    parser=argparse.ArgumentParser(); parser.add_argument('--schema',action='store_true')
    check(schema=parser.parse_args().schema)
