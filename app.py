from flask import Flask, render_template_string, request, redirect, url_for
from dataclasses import dataclass
from typing import List

app = Flask(__name__)

@dataclass
class Donation:
    streamer: str
    nickname: str
    amount: float
    message: str

donations: List[Donation] = []

# Simple donation form template
FORM_TEMPLATE = """
<!doctype html>
<title>Donate to {{ streamer }}</title>
<h1>Donate to {{ streamer }}</h1>
<form method=post action="{{ url_for('donate', streamer=streamer) }}">
    <label>Nickname: <input type=text name=nickname required></label><br>
    <label>Amount (in crypto units): <input type=number step=any name=amount required></label><br>
    <label>Message: <input type=text name=message></label><br>
    <button type=submit>Donate</button>
</form>
<p><a href="{{ url_for('list_donations', streamer=streamer) }}">View donations</a></p>
"""

# Template to list donations
LIST_TEMPLATE = """
<!doctype html>
<title>Donations for {{ streamer }}</title>
<h1>Donations for {{ streamer }}</h1>
<ul>
{% for d in donations %}
  <li><strong>{{ d.nickname }}</strong> donated {{ d.amount }}: {{ d.message }}</li>
{% else %}
  <li>No donations yet.</li>
{% endfor %}
</ul>
<p><a href="{{ url_for('donation_form', streamer=streamer) }}">Back to form</a></p>
"""

@app.route('/<streamer>')
def donation_form(streamer: str):
    return render_template_string(FORM_TEMPLATE, streamer=streamer)

@app.route('/<streamer>/donate', methods=['POST'])
def donate(streamer: str):
    nickname = request.form['nickname']
    amount = float(request.form['amount'])
    message = request.form.get('message', '')
    donations.append(Donation(streamer, nickname, amount, message))
    # TODO: integrate actual cryptocurrency payment processing
    return redirect(url_for('list_donations', streamer=streamer))

@app.route('/<streamer>/donations')
def list_donations(streamer: str):
    streamer_donations = [d for d in donations if d.streamer == streamer]
    return render_template_string(LIST_TEMPLATE, streamer=streamer, donations=streamer_donations)

if __name__ == '__main__':
    app.run(debug=True)
