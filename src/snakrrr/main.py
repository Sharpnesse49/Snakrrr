import os
import platform

def main():
    os_name = platform.freedesktop_os_release()["PRETTY_NAME"]
    kernel = platform.release()

    with open("/proc/meminfo") as f:
        mem_inf = f.readlines()

    mem_all = int(mem_inf[0].split(":")[1].split()[0])
    mem_ava = int(mem_inf[2].split(":")[1].split()[0])
    disk = os.statvfs("/")
    disk_all = int(disk.f_blocks)
    disk_ava = int(disk.f_bavail)

    info = [
        f"hello, {os.getlogin()}",
        f"",
        f"\033[93mOs :\033[0m {os_name}",
        f"\033[92mKernel :\033[0m {kernel}",
        f"\033[94mMemo :\033[0m {round(100 - (mem_ava/mem_all)*100)}%",
        f"\033[95mDisk :\033[0m {round(100 - (disk_ava/disk_all)*100)}%",
        f""
    ]

    logo = [
        r"          __________     ",
        r"         (__  ______)    ",
        r"            \/           ",
        r"       _______    /*_>-< ",
        r"  ___/ _____ \__/ /      ",
        r" <____/     \____/       ",
        r"                         ",
    ]

    for logo_line, info_line in zip(logo, info):
        print(logo_line, info_line)


if __name__ == "__main__":
    main()
