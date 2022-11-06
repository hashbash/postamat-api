#!bin/bash
cd /root/postamat-api/app
source /root/postamat-api-venv/bin/activate
/root/postamat-api-venv/bin/uvicorn app:app --port 8098
