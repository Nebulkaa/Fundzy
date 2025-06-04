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

Set the `TRON_PRIVATE_KEY` environment variable to the hex-encoded private key of the wallet that will receive donations. The application displays the derived TRON address for donors to send TRX or USDT (TRC20) directly.

This prototype stores donations in memory, so payments are not persisted across restarts.

