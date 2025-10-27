import os
import sys
import datetime

def log(msg: str):
    timestamp = datetime.datetime.now().strftime("%H:%M:%S")
    print(f"[{timestamp}] {msg}")

def detect_luci_env():
    """Detects if running inside a LUCI build context."""
    return any(key.startswith("LUCI_") for key in os.environ.keys())

def ensure_python_version():
    """Ensures Python 3.10+."""
    if sys.version_info < (3, 10):
        sys.exit("❌ Python 3.10 or higher required for infra_virtualenv.")
