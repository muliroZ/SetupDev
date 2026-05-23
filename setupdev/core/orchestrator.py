from pathlib import Path
from setupdev.core.models import ProjectType
from setupdev.core.ports import WorkspaceDriver
from setupdev.core.detector import Detector

DEFAULT_COMMANDS = {
    ProjectType.NODE: "bun run dev",
    ProjectType.PYTHON: "uv run uvicorn main:app --reload",
    ProjectType.JAVA: "./mvnw spring-boot:run",
    ProjectType.GO: "go run .",
}

def orchestrate(root_path: Path, driver: WorkspaceDriver, with_editor: bool = True):
    detector = Detector()
    workspace = detector.scan_workspace(root_path)

    driver.create_session(root_path)

    if with_editor:
        driver.rename_initial_window("editor")
        driver.send_command("editor", "nvim .")

        for service in workspace.services:
            command = DEFAULT_COMMANDS.get(service.project_type)
            driver.create_window(service, command)

    else:
        is_first = True

        for service in workspace.services:
            command = DEFAULT_COMMANDS.get(service.project_type)
            if is_first:
                driver.rename_initial_window(service.name)
                driver.send_command(service.name, command)
                is_first = False
            else:
                driver.create_window(service, command)

    driver.attach()
