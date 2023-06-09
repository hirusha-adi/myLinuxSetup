import re
import subprocess
import os
import typing as t
from pyfiglet import print_figlet

class Base:
    @staticmethod
    def askExecute(prompt, command: t.Union[str, t.Iterable]):
        answer = input(f"? -> {prompt} (yes/No): ")
        if re.match(r'^[Yy](es)?$', answer):
            if isinstance(command, str):
                subprocess.run(command, shell=True)
            else:
                for cmnd in command:
                    subprocess.run(cmnd, shell=True)
    
    @staticmethod
    def banner(text):
        print_figlet(text, font='rounded') # or 'epic'

    @staticmethod
    def archInstallYay():
        os.system("sudo pacman -Sy base-devel --no-confirm")
        os.system("git clone https://aur.archlinux.org/yay.git")
        os.chdir(os.path.join(os.getcwd(), "yay"))
        os.system("makepkg -si")
        os.chdir("..")
        os.remove(os.path.join(os.getcwd(), "yay"))
    
    
    