#!/bin/bash

source ./venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt -r requirements_dev.txt
python3 app.py