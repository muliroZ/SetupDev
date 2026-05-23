import sh
import os
from pathlib import Path
from typing import Optional
from setupdev.core.models import Service
from setupdev.core.ports import WorkspaceDriver

class TmuxAdapter(WorkspaceDriver):
    def __init__(self, session_name: str) -> None:
        self.session_name = session_name
        self.tmux = sh.tmux
    
    def session_exists(self) -> bool:
        try:
            self.tmux("has-session", "-t", self.session_name)
            return True
        except sh.ErrorReturnCode:
            return False

    def create_session(self, root_path: Path):
        if not self.session_exists():
            self.tmux("new-session", "-d", "-s", self.session_name, "-c", str(root_path))

    def create_window(self, service: Service, command: Optional[str] = None):
        args = ["new-window", "-t", f"{self.session_name}:", "-n", service.name, "-c", str(service.path)]

        if command:
            args.append(command)

        self.tmux(*args)

    def rename_initial_window(self, new_name: str) -> None:
        self.tmux("rename-window", new_name)

    def send_command(self, window_name, command) -> None:
        self.tmux("send-keys", "-t", window_name, command, "C-m")

    def attach(self):
        os.execvp("tmux", ["tmux", "attach-session", "-t", self.session_name])
