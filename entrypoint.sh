#!/bin/bash

# Download selected model
python startup.py
# Start web server
gunicorn --bind 0.0.0.0:8000 server:app