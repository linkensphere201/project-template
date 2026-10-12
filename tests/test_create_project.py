import json
from pathlib import Path
import runpy
import shutil
import tempfile
import unittest

TEMPLATE = Path(__file__).resolve().parents[1]
module = runpy.run_path(str(TEMPLATE / 'scripts/create_project.py'))
create = module['create_project']


class GeneratorTests(unittest.TestCase):
    def setUp(self):
        self.root = Path(tempfile.mkdtemp(prefix='project-template-test-'))

    def generate(self, template=TEMPLATE, **kwargs):
        options = dict(template=template, root=self.root, name='demo-ai',
                       description='A test project', goal='Validate scope',
                       owner='Test owner', day='2026-10-12', update_indexes=False)
        options.update(kwargs)
        return create(**options)

    def test_renders_without_repository_metadata(self):
        target = self.generate()
        self.assertEqual(len(list(target.rglob('*.md'))), 12)
        self.assertIn('# Demo AI', (target / 'README.md').read_text())
        self.assertIn('Test owner', (target / 'tasks/active.md').read_text())
        self.assertIn('Validate scope', (target / 'tasks/active.md').read_text())
        self.assertIn('Planning gate: Pending', (target / 'tasks/milestones.md').read_text())
        for name in ('.git', 'scripts', 'tests', 'PROJECT.md', 'VERSION'):
            self.assertFalse((target / name).exists())
        self.assertEqual(json.loads((target / '.template-source.json').read_text())['version'],
                         (TEMPLATE / 'VERSION').read_text().strip())
        self.assertEqual((target / 'AGENTS.md').read_text(encoding='utf-8'),
                         (TEMPLATE / 'AGENTS.md').read_text(encoding='utf-8-sig').rstrip() + '\n')

    def test_refuses_overwrite(self):
        target = self.generate()
        before = (target / 'README.md').read_bytes()
        with self.assertRaises(ValueError):
            self.generate(description='Overwrite')
        self.assertEqual((target / 'README.md').read_bytes(), before)

    def test_invalid_input_creates_nothing(self):
        for options in [dict(day='../../outside'), dict(day='2026-02-30'), dict(name='!!!')]:
            with self.assertRaises(ValueError):
                self.generate(**options)
        self.assertEqual(list(self.root.iterdir()), [])

    def test_local_template(self):
        local = self.root / 'source'
        shutil.copytree(TEMPLATE, local, ignore=shutil.ignore_patterns('.git', '__pycache__'))
        (local / '.git').write_text('gitdir: nonexistent-test-metadata\n')
        (local / 'context/glossary.md').write_text('# Custom glossary\n')
        target = self.generate(template=local)
        self.assertEqual((target / 'context/glossary.md').read_text(), '# Custom glossary\n')
        self.assertFalse((target / '.git').exists())

    def test_unknown_placeholder_fails_before_creation(self):
        local = self.root / 'source'
        shutil.copytree(TEMPLATE, local, ignore=shutil.ignore_patterns('.git', '__pycache__'))
        (local / 'PROJECT.md').write_text('{{UNKNOWN_TOKEN}}')
        with self.assertRaises(ValueError):
            self.generate(template=local)
        self.assertFalse((self.root / '2026-10-12-demo-ai').exists())

    def test_user_text_not_recursively_expanded(self):
        target = self.generate(description='Literal {{OWNER}} remains literal')
        self.assertIn('Literal {{OWNER}} remains literal', (target / 'README.md').read_text())

    def test_indexes(self):
        readme = self.root / 'README.md'
        readme.write_text('# Workspace\n- `project-template/`: Template\n')
        structure = self.root / 'WORKSPACE-STRUCTURE.md'
        structure.write_text('| `project-template/` | Template |\n')
        self.generate(update_indexes=True)
        self.assertIn('# Workspace', readme.read_text())
        self.assertEqual(readme.read_text().count('2026-10-12-demo-ai'), 1)
        self.assertIn('2026-10-12-demo-ai', structure.read_text())

    def test_no_index(self):
        readme = self.root / 'README.md'
        readme.write_text('# Workspace\n')
        self.generate()
        self.assertEqual(readme.read_text(), '# Workspace\n')

    def test_output_outside_template(self):
        with self.assertRaises(ValueError):
            self.generate(root=TEMPLATE / 'output')

    def test_uninitialized_template(self):
        with self.assertRaises(ValueError):
            self.generate(template=self.root / 'uninitialized')
        self.assertEqual(list(self.root.iterdir()), [])


if __name__ == '__main__':
    unittest.main()
