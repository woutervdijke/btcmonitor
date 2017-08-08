# -*- coding: utf-8 -*-

from flask import Flask
app = Flask(__name__)

import requests
def getbtc():
	r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
	bitcoinprice = r.json()['bpi']['EUR']['rate_float']
	myval = 0.04362136 * bitcoinprice
	return "€"+str("%.2f" % round(myval,2))


@app.route("/")
def hello():
	html = "<div style=\"width: auto; margin:auto; margin-top: 50px; text-align: center;\"><h2>De waarde van mijn bitcoin is</h2><h1>"+getbtc()+"</h1></div>"
	return html

@app.route("/raw")
def rawbtc():
	return getbtc()+"\r\n"
