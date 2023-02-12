import distro
import platform
import command_line

def packages() -> any:
    system: str = platform.system()
    distr: str = distro.like()
    try:
        if "Linux" in system:
            if "debian" or "ubuntu" in distr:
                return command_line.send(command="sh linux_deb_install.sh")
            elif "arch" in distr:
                return command_line.send(command="sh linux_arch_install.sh")
        elif "Darwin" in system:
            return command_line.send(command="sh mac_os_install.sh")
    except Exception as excp:
        return print(excp)
