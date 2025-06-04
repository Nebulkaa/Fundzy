import os
from flask import Flask, render_template, request, redirect, url_for
from dataclasses import dataclass
from typing import List
from coinbase_commerce.client import Client

app = Flask(__name__)
client = Client(api_key=os.getenv("COINBASE_COMMERCE_API_KEY", ""))

@dataclass
class Donation:
    streamer: str
    nickname: str
    amount: float
    message: str
    charge_id: str = ""
    status: str = "pending"

donations: List[Donation] = []


@app.route('/<streamer>')
def donation_form(streamer: str):
    return render_template("donation_form.html", streamer=streamer)

@app.route('/<streamer>/donate', methods=['POST'])
def donate(streamer: str):
    nickname = request.form['nickname']
    amount = float(request.form['amount'])
    message = request.form.get('message', '')
    if client.api_key:
        charge = client.charge.create(
            name=f"Donation to {streamer}",
            description=message or f"Donation from {nickname}",
            local_price={"amount": amount, "currency": "USD"},
            pricing_type="fixed_price",
            metadata={"streamer": streamer, "nickname": nickname},
            redirect_url=url_for('list_donations', streamer=streamer, _external=True),
            cancel_url=url_for('donation_form', streamer=streamer, _external=True)
        )
        donations.append(Donation(streamer, nickname, amount, message, charge.id))
        return redirect(charge.hosted_url)
    else:
        donations.append(Donation(streamer, nickname, amount, message))
        return redirect(url_for('list_donations', streamer=streamer))

@app.route('/<streamer>/donations')
def list_donations(streamer: str):
    streamer_donations = [d for d in donations if d.streamer == streamer]
    return render_template("donations_list.html", streamer=streamer, donations=streamer_donations)

if __name__ == '__main__':
    app.run(debug=True)
