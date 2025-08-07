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

Set `TRON_PRIVATE_KEY` to the hex-encoded private key of the wallet that will receive donations on the Tron network.  
Set `ETHEREUM_ADDRESS` to the address that should receive ERC-20 tokens on Ethereum or compatible L2 networks.  
The donation form lets viewers choose which network to use and shows the appropriate address.

This prototype stores donations in memory, so payments are not persisted across restarts.

