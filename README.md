# Fundzy

A simple prototype for a crypto-based donation platform for streamers.

## Setup

1. Create a virtual environment and install dependencies:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```
2. Run the development server:
   ```bash
   python app.py
   ```
3. Open `http://localhost:5000/<streamer>` in your browser to donate to a streamer.

This prototype stores donations in memory and does not handle real cryptocurrency payments yet.

