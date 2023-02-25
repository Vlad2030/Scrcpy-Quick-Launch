import subprocess
import os


def send(command: str, stdout: bool) -> None:
    if command:
        if stdout:
            return subprocess.run(
                args=command.split(" "),
                stdout=subprocess.PIPE,
            ).stdout.decode("utf-8")
        else:
            return os.system(command=command)
    else:
        print(f"Empty command argument")