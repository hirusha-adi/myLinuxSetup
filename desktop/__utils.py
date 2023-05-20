import re
import subprocess
import os

class Base:
    @staticmethod
    def askExecute(prompt, command):
        answer = input(f"? -> {prompt} (yes/No): ")
        if re.match(r'^[Yy](es)?$', answer):
            subprocess.run(command, shell=True)