import os
import yaml

def unsafe_command(input_str: str) -> None:
    # Bandit: B605/B607 (shell injection)
    os.system(input_str)  # nosec

with open('config.yaml', 'r', encoding='utf-8') as f:
    # Old PyYAML + full_load → unsafe in vulnerable versions
    config = yaml.full_load(f)  # nosec

unsafe_command(config.get('user_input', 'echo Hello'))
