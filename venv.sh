#!/bin/bash 
cd backend && sh mongodb.sh && cd ..
apt install -y python3.12-venv 
python3 -m venv venv 
source ./venv/bin/activate 
pip install -r ./backend/requirements.txt
# 8000 port open and /docs for swagger
cd backend && uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
