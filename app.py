from flask import Flask, render_template, jsonify
from signal_parser import parse_signal
from mt5_handler import connect_mt5, place_trade
from database import log_trade, Session, Trade

app = Flask(__name__)

@app.route("/")
def index():
    s = Session()
    return render_template("dashboard.html", trades=s.query(Trade).all())

@app.route("/run")
def run():
    signal = parse_signal()
    connect_mt5()
    place_trade(signal)
    log_trade(signal)
    return jsonify(signal)

app.run(debug=True)
