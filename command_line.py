import subprocess
import os


def send(command: str) -> None:
    return os.system(
        command=command,
    )


def stdout(command: str) -> str:
    return subprocess.run(
        args=command.split(" "),
        stdout=subprocess.PIPE,
    ).stdout.decode("utf-8")
