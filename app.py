import os
from flask import Flask, render_template, request
from dataclasses import dataclass
from typing import List, Dict
from tronpy import Tron
from tronpy.keys import PrivateKey

app = Flask(__name__)

# derive donation address from TRON_PRIVATE_KEY if provided
_priv_key_hex = os.getenv("TRON_PRIVATE_KEY", "")
tron_address = None
if _priv_key_hex:
    try:
        priv = PrivateKey(bytes.fromhex(_priv_key_hex))
        tron_address = priv.public_key.to_base58check_address()
    except ValueError:
        tron_address = None

eth_address = os.getenv("ETHEREUM_ADDRESS", "")

donation_addresses: Dict[str, str] = {
    "tron": tron_address,
    "ethereum": eth_address,
}

tron = Tron()

@dataclass
class Donation:
    streamer: str
    nickname: str
    amount: float
    currency: str
    network: str
    message: str
    tx_id: str = ""
    status: str = "pending"

donations: List[Donation] = []


@app.route('/<streamer>')
def donation_form(streamer: str):
    return render_template("donation_form.html", streamer=streamer, addresses=donation_addresses)

@app.route('/<streamer>/donate', methods=['POST'])
def donate(streamer: str):
    nickname = request.form['nickname']
    amount = float(request.form['amount'])
    currency = request.form['currency']
    network = request.form['network']
    message = request.form.get('message', '')
    donation = Donation(streamer, nickname, amount, currency, network, message)
    donations.append(donation)
    address = donation_addresses.get(network)
    return render_template(
        "payment_instructions.html",
        streamer=streamer,
        donation=donation,
        address=address,
    )

@app.route('/<streamer>/donations')
def list_donations(streamer: str):
    streamer_donations = [d for d in donations if d.streamer == streamer]
    return render_template("donations_list.html", streamer=streamer, donations=streamer_donations)

if __name__ == '__main__':
    app.run(debug=True)
