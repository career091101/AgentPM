#!/bin/bash

# Load environment variables from .env
export $(cat .env | grep -v '^#' | sed 's/\r$//' | xargs)

# Activate virtual environment
source .venv/bin/activate

# Start backend
uvicorn backend.app.api:app --reload --port 8000
