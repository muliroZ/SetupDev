from pathlib import Path
import pytest
from setupdev.core.detector import identify_project_in_dir
from setupdev.core.models import ProjectType

def test_identify_project_resolves_conflict(tmp_path: Path):
    """
    Testa se a resolução de conflitos de marker files é feita
    corretamente usando a estratégia de pesos
    """
    backend_dir = tmp_path / "my_backend"
    backend_dir.mkdir()

    (backend_dir / "pyproject.toml").touch()
    (backend_dir / "package.json").touch()

    project_type, marker_file = identify_project_in_dir(backend_dir)

    assert project_type == ProjectType.PYTHON
    assert marker_file == "pyproject.toml"

def test_identify_project_returns_unknown_for_empty_dir(tmp_path: Path):
    """
    Testa se a funcão identify_project_in_dir retorna UNKNOWN para
    diretórios vazios
    """
    empty_dir = tmp_path / "pasta_vazia"
    empty_dir.mkdir()

    project_type, marker_file = identify_project_in_dir(empty_dir)

    assert project_type == ProjectType.UNKNOWN
    assert marker_file is None
