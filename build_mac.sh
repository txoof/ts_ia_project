#!/bin/bash 
pipenv run pyinstaller --add-binary '/usr/local/bin/geckodriver:.' --onefile --clean --noconfirm IA_Project.py
