# -*- coding: utf-8 -*-

from flask import Flask
app = Flask(__name__)

import requests

mybtcprice = ""
myetherprice = ""

def getcrypto():
	r = requests.get('https://min-api.cryptocompare.com/data/pricemulti?fsyms=BTC,ETH&tsyms=EUR')
	getbtc(r)
	geteth(r)

def getbtc(r):
	bitcoinprice = r.json()['BTC']['EUR']
	mybtc = 0.04362136 * bitcoinprice
	global mybtcprice
	mybtcprice = "€"+str("%.2f" % round(mybtc,2))

def geteth(r):
	etherprice = r.json()['ETH']['EUR']
	myether = 0.31298156 * etherprice
	global myetherprice
	myetherprice = "€" + str("%.2f" % round(myether, 2))

@app.route("/")
def hello():
	getcrypto()
	html = "<div style=\"width: auto; margin:auto; margin-top: 50px; text-align: center;\"><h2>De waarde van mijn bitcoin is</h2><h1>"+mybtcprice+"</h1><h2>De waarde van mijn ethereum is</h2><h1>"+myetherprice+"</h1> (v=cryptocompare3)</div>"
	return html

@app.route("/raw")
def rawbtc():
	getcrypto()
	return "BTC: "+mybtcprice+" ETH: "+myetherprice+"\r\n"
