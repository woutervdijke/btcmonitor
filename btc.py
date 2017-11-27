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
	r = requests.get('https://min-api.cryptocompare.com/data/pricemulti?fsyms=BTC,ETH,BCH&tsyms=EUR')
	getbtc(r)
	geteth(r)
	getbch(r)

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
		
def getbch(r):
	bchprice = r.json()['BCH']['EUR']
	mycash = bchsetup * bchprice
	global mybchprice
	global bchchange
	global bchdir
	bchchange = "€" + str("%.2f" % round(mycash - 0, 2))
	mybchprice = "€" + str("%.2f" % round(mycash, 2))
	if mycash > 0:
		bchdir = "positive"
	else:
		bchdir = "negative"

@app.route("/btc")
def hello():
	getcrypto()
	return render_template('btc.html', btcprice=mybtcprice, ethprice=myetherprice, bchprice=mybchprice, btcchange=btcchange, ethchange=ethchange, bchchange=bchchange, btcdir=btcdir, ethdir=ethdir, bchdir=bchdir)

@app.route("/raw")
def rawbtc():
	getcrypto()
	return "BTC: "+mybtcprice+" ETH: "+myetherprice+" BCH: "+mybchprice+"\r\n"
