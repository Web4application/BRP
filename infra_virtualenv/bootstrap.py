import os
import sys
import subprocess
from pathlib import Path

VENV_DIR = Path(__file__).resolve().parent / ".venv"

def create_virtualenv():
    if not VENV_DIR.exists():
        print("[+] Creating virtual environment...")
        subprocess.run([sys.executable, "-m", "venv", str(VENV_DIR)], check=True)
    else:
        print("[=] Virtual environment already exists.")

def install_requirements():
    pip = VENV_DIR / "bin" / "pip"
    print("[+] Installing dependencies...")
    subprocess.run([str(pip), "install", "--upgrade", "pip", "setuptools", "wheel"], check=True)
    subprocess.run([str(pip), "install", "-r", "requirements.txt"], check=True)

def activate_and_run():
    python_bin = VENV_DIR / "bin" / "python"
    subprocess.run([str(python_bin), "runner.py"], check=True)

if __name__ == "__main__":
    create_virtualenv()
    install_requirements()
    activate_and_run()
