import command_line
import install


if __name__ == "__main__":
    try:
        while True:
            adb: str = command_line.stdout(
                command="adb devices",
            )
            if "unauthorized" in adb:
                pass
            elif "device" in adb:
                break

        command_line.send(
            command="scrcpy",
        )

    except Exception:
        install.packages()