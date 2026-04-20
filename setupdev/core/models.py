from dataclasses import dataclass
from enum import Enum
from pathlib import Path

class ProjectType(Enum):
    PYTHON = "python"
    JAVA = "java"
    NODE = "node"
    UNKNOWN = "unknown"

@dataclass
class Marker:
    filename: str
    project_type: ProjectType
    weight: int

MARKERS = [
    Marker("pyproject.toml", ProjectType.PYTHON, weight=100),
    Marker("pom.xml", ProjectType.JAVA, weight=100),
    Marker("bun.lockb", ProjectType.NODE, weight=90),
    Marker("package.json", ProjectType.NODE, weight=50),
]

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
