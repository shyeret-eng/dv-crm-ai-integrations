import importlib.util, json, sys, unittest, zipfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
import release
class ReleaseTests(unittest.TestCase):
    def test_reproducible_packages_and_contents(self):
        release.build()
        output=ROOT/'dist'/release.version()
        first=(output/'release-index.json').read_bytes()
        release.build()
        self.assertEqual(first,(output/'release-index.json').read_bytes())
        for archive in output.glob('*.zip'):
            with zipfile.ZipFile(archive) as z:
                self.assertIsNone(z.testzip())
                for name in z.namelist():
                    self.assertFalse(name.startswith('/') or '..' in Path(name).parts)
                    self.assertFalse(any(part in ['.env','.git','node_modules'] for part in Path(name).parts))
                self.assertTrue(any(x.endswith('/SKILL.md') for x in z.namelist()))
        portable=output/'portable/dv-crm'
        self.assertFalse((portable/'mcp.json').exists())
        self.assertFalse((portable/'.app.json').exists())
        self.assertNotIn('includeTools',json.loads((output/'gemini/dv-crm/gemini-extension.json').read_text())['mcpServers']['dv-crm'])
        unsupported = ['activate_quote','confirm_quote','send_quote','send_message','get_integration_guidance']
        for archive in output.glob('*.zip'):
            with zipfile.ZipFile(archive) as z:
                for name in z.namelist():
                    text=z.read(name).decode('utf-8')
                    for tool in unsupported:
                        self.assertNotIn(tool,text, (archive.name,name,tool))
                    if name.endswith('/gemini-extension.json'):
                        self.assertNotIn('includeTools',text)
                    if name.endswith('/SKILL.md'):
                        for safeguard in ['expectedStatus','expectedUpdatedAt','get_whats_new','explicit yes','10 minutes','seven days']:
                            self.assertIn(safeguard,text)
if __name__=='__main__': unittest.main()
