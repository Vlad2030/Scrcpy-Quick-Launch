import command_line
import install
import time


if __name__ == "__main__":
    while True:
        try:
            adb: str = command_line.send(
                command="adb devices",
                stdout=True,
            )
        except Exception: 
            install.packages()

        if "unauthorized" in adb:
            print("Accept debugging")

        elif "device\n" in adb:
            command_line.send(
                command="scrcpy",
                stdout=False,
            )
            break

        else:
            print("Connect an android")

        time.sleep(1)