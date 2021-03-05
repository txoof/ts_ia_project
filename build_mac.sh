#!/bin/bash 
pipenv run pyinstaller --add-binary './gecodriver:.' --onefile --clean --noconfirm IA_Project.py
