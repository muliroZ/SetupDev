from pathlib import Path
from enum import Enum
from dataclasses import dataclass

class ProjectType(Enum):
    NODE = "node"
    PYTHON = "python"
    JAVA = "java"
    GO = "go"
    UNKNOWN = "unknown"

@dataclass
class Service:
    name: str
    path: Path
    project_type: ProjectType
    marker_file: str

@dataclass
class Workspace:
    root_path: Path
    services: list[Service]

@dataclass
class Marker:
    filename: str
    project_type: ProjectType
    weight: int

MARKERS = [
    Marker("bun.lockb", ProjectType.NODE, weight=90),
    Marker("package.json", ProjectType.NODE, weight=50),
    Marker("pyproject.toml", ProjectType.PYTHON, weight=100),
    Marker("pom.xml", ProjectType.JAVA, weight=100),
    Marker("go.mod", ProjectType.GO, weight=100),
]

IGNORED_DIRS = [
    ".git",
    ".github",
    ".venv",
    "venv",
    "__pycache__",
    "dist*",
    "target",
    "node_modules",
    "*.egg-info",
    "assets"
]