import distro
import os
import platform


def packages() -> any:
    system: str = platform.system()
    distr: str = distro.like()
    try:
        if "Linux" in system:
            if "debian" or "ubuntu" in distr:
                return os.system("sh linux_deb_install.sh")
            elif "arch" in distr:
                return os.system("sh linux_arch_install.sh")
        elif "Darwin" in system:
            return os.system("sh mac_os_install.sh")
    except Exception as excp:
        return print(excp)