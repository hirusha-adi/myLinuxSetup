import re
import subprocess

class Base:
    @staticmethod
    def askExecute(prompt, command):
        answer = input(f"? -> {prompt} (yes/No): ")
        if re.match(r'^[Yy](es)?$', answer):
            subprocess.run(command, shell=True)
            
Base.askExecute("dsfsd", "echo 3ew45tr4e5ydfg")