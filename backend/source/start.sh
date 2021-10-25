#!/bin/bash
set -eu

# FastAPI server start
echo ".: Starting server :."
# uvicorn main:app --reload
uvicorn main:app --host 0.0.0.0 --port 8000 --reload