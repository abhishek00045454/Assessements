#!/bin/bash

echo "Setting up the environment..."

# Update and install required system dependencies
sudo apt update && sudo apt install -y python3 python3-pip python3-venv

# Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate

# Install required Python dependencies
pip install --upgrade pip
pip install -r requirements.txt

# Run the Flask app
echo "Starting the Flask server..."
python app.py
