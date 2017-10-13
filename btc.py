#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding: utf-8

from flask import Flask, render_template
app = Flask(__name__)

from setup import *

import requests

mybtcprice = ""
myetherprice = ""

def getcrypto():
	r = requests.get('https://min-api.cryptocompare.com/data/pricemulti?fsyms=BTC,ETH&tsyms=EUR')
	getbtc(r)
	geteth(r)

def getbtc(r):
	bitcoinprice = r.json()['BTC']['EUR']
	mybtc = btcsetup * bitcoinprice
	global mybtcprice
	global btcchange
	global btcdir
	btcchange = "€" + str("%.2f" % round(mybtc - 100, 2))
	mybtcprice = "€"+str("%.2f" % round(mybtc,2))
	if mybtc > 100:
		btcdir = "positive"
	else:
		btcdir = "negative"

def geteth(r):
	etherprice = r.json()['ETH']['EUR']
	myether = ethsetup * etherprice
	global myetherprice
	global ethchange
	global ethdir
	ethchange = "€" + str("%.2f" % round(myether - 100, 2))
	myetherprice = "€" + str("%.2f" % round(myether, 2))
	if myether > 100:
		ethdir = "positive"
	else:
		ethdir = "negative"

@app.route("/btc")
def hello():
	getcrypto()
	return render_template('btc.html', btcprice=mybtcprice, ethprice=myetherprice, btcchange=btcchange, ethchange=ethchange, btcdir=btcdir, ethdir=ethdir)

@app.route("/raw")
def rawbtc():
	getcrypto()
	return "BTC: "+mybtcprice+" ETH: "+myetherprice+"\r\n"
