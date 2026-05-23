from pathlib import Path
from setupdev.core.models import ProjectType
from setupdev.core.models import MARKERS
from setupdev.core.detector import identify_project_in_directory, scan_workspace

def test_identify_project_resolves_conflict(tmp_path: Path):
    backend_dir = tmp_path / "meu_backend"
    backend_dir.mkdir()
    
    (backend_dir / "pyproject.toml").touch()
    (backend_dir / "package.json").touch()

    project_type, marker_file = identify_project_in_directory(backend_dir)

    assert project_type == ProjectType.PYTHON
    assert marker_file == "pyproject.toml"

def test_identify_project_returns_unknown_for_empty_dir(tmp_path: Path):
    empty_dir = tmp_path / "pasta_vazia"
    empty_dir.mkdir()
    
    project_type, marker_file = identify_project_in_directory(empty_dir)
    
    assert project_type == ProjectType.UNKNOWN
    assert marker_file is None

def test_scan_workspace_ignores_glob_patterns(tmp_path: Path):
    monorepo_dir = tmp_path
    egg_dir = monorepo_dir / "projeto.egg-info"
    egg_dir.mkdir()
    
    (egg_dir / "package.json").touch() 

    workspace = scan_workspace(monorepo_dir)
    
    assert len(workspace.services) == 0
