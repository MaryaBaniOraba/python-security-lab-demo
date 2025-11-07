import shlex
import subprocess
import yaml

def safe_command(input_str: str) -> None:
    # Avoid shell=True; split args safely
    args = shlex.split(input_str)
    subprocess.run(args, check=True)

with open('config.yaml', 'r', encoding='utf-8') as f:
    # Use safe loader
    config = yaml.safe_load(f)

# Example: limit to allowlist command
cmd = config.get('user_input', 'echo Hello')
if cmd.split()[0] in {'echo'}:
    safe_command(cmd)
else:
    raise ValueError('Command not allowed')
