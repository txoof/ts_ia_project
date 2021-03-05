#!/bin/bash 
pipenv run pyinstaller --add-binary './geckodriver:.' --onefile --clean --noconfirm IA_Project.py
