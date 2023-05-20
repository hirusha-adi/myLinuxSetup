import re
import subprocess
import os
import typing as t

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
                    