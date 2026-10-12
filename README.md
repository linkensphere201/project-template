# Project Template

Reusable documentation and AI-collaboration skeleton. Requires Python 3.10+;
no third-party packages are needed.

## Usage

```sh
git clone git@github.com:linkensphere201/project-template.git
git -C project-template checkout v1.0.0
python project-template/scripts/create_project.py example-project --output-root ./projects --description "Describe the outcome" --owner "Your team" --no-index
```

Creates `projects/YYYY-MM-DD-example-project/`. Use `--date YYYY-MM-DD` for a
fixed date. Existing projects are never overwritten or automatically updated.

## Source Of Truth

- `AGENTS.md`: reusable project-level collaboration rules.
- `PROJECT.md`: rendered as the generated project's README.
- `context/`, `tasks/`, `prompts/`, `logs/`: project documents.
- `scripts/create_project.py`: generator; documents are not duplicated in code.
- `VERSION`: release version; `tests/`: generator regression tests.

Supported placeholders: `{{PROJECT_TITLE}}`, `{{PROJECT_DIRECTORY}}`,
`{{DESCRIPTION}}`, `{{ACTIVE_GOAL}}`, `{{OWNER}}`, `{{START_DATE}}`.
Unknown placeholders fail before creating files.

Generated projects contain twelve Markdown documents and
`.template-source.json` recording version, commit and dirty state.
ZIP exports have a null commit. Git metadata, maintenance scripts, tests and
this repository README are never copied. Global safety and workspace policies
remain owned by the host environment.

## Pinned Workspace Integration

```sh
git submodule add git@github.com:linkensphere201/project-template.git project-template
git submodule update --init --recursive
```

Clone the parent workspace with `git clone --recurse-submodules <workspace-url>`.
After pulling the parent, use `git submodule update --init --recursive`.
Do not use `--remote` for routine initialization: upgrading the pinned version
is a separate reviewed change.

The create-task skill delegates to this generator. Without `--no-index`,
existing workspace README and WORKSPACE-STRUCTURE files receive a project entry.
Use `--no-index` outside that workspace convention. `--project-root` aliases
`--output-root`; `--template-dir` selects another initialized template checkout.

## Validation And Releases

```sh
python -m unittest discover -s project-template/tests -v
```

Tests retain isolated temporary directories; no existing project is deleted.
Tag releases and update VERSION. Review generated documents before upgrading;
automatic migration of existing project documents is intentionally unsupported.

The initial commit preserves the original twelve-file project-manager snapshot.
Earlier history remains in that repository. Version 1.0.0 adds standalone
generation, explicit placeholders and Git-metadata isolation.
