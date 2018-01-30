import sys
from cx_Freeze import setup, Executable

setup(
    name = "happy_alien",
    version = "1.0",
    description = "happy_alien",
    executables = [Executable("happy_alien.py", base = "Win32GUI")])