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

Set the `COINBASE_COMMERCE_API_KEY` environment variable with your Coinbase Commerce API key before running the server. The app will create a charge for each donation request and redirect the donor to Coinbase's hosted payment page.

This prototype stores donations in memory, so payments are not persisted across restarts.

