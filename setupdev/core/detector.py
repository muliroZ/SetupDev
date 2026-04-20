from pathlib import Path

from setupdev.core.models import MARKERS, Marker, ProjectType

def identify_project_in_dir(dir: Path) -> tuple[ProjectType, str | None]:
    winner: Marker | None = None

    for marker in MARKERS:
        file_path = dir / marker.filename

        if file_path.exists() and file_path.is_file():
            if winner is None or marker.weight > winner.weight:
                winner = marker

    if winner:
        return winner.project_type, winner.filename

    return ProjectType.UNKNOWN, None
