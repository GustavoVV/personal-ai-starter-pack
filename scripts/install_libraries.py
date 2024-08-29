import os
import subprocess
from typing import List

def install_libraries(libraries: List[str]):
    for library in libraries:
        try:
            __import__(library)
        except ImportError:
            subprocess.check_call([os.sys.executable, '-m', 'pip', 'install', library])

# List of libraries to ensure are installed
required_libraries = ['pydantic', 'sounddevice', 'PIL', 'pyperclip', 'keyboard', 'speech_recognition']

install_libraries(required_libraries)