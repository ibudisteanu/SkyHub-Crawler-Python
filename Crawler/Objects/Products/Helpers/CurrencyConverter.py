# source code from GitHub https://github.com/wathika/CurrencyConverter/blob/master/currencyconverter.py

#!/usr/bin/python
# -*- coding: utf-8 -*-
import json
import urllib3
import re


def convert(base, val):
    val = float(val)
    # Make API call to fixer.io, load JSON data for exchange rates

    http = urllib3.PoolManager()
    r = http.request('GET', 'http://api.fixer.io/latest?symbols=USD,GBP')

    data = r.data

    USD_rate = data['rates']['USD']
    GBP_rate = data['rates']['GBP']
    EUR_rate = base_rate = 1.00

    convert_between = [
        ["GBP", GBP_rate],
        ["USD", USD_rate],
        ["EUR", EUR_rate]
    ]

    for type in convert_between:
        if type[0] == base:
            base_rate = type[1]

    output = base + "{:,}".format(val)

    for type in convert_between:
        if type[1] == base_rate:
            continue
        else:
            converted_amount = round(type[1] / base_rate * val, 2)
            converted_amount = "{:,}".format(converted_amount)
        output += " => " + type[0] + str(converted_amount)

    return output

currencies = [
    ["USD", "US","$"],
    ["EUR","EURO", "EU","€"],
    ['GBP', '£'],
    ['CAD','Can$','C$'],
    ['CNY','yuan'],
    ['JPY','yen'],
]

# it will return ['USD','US','$', 'EUR', 'EURO', 'EU', '€',
def getAllCurrencyList:
    allCurrencyList = []

    for currency in currencies:
        for symbol in currency:
            allCurrencyList.append(symbol)

    return allCurrencyList

def parseStringCurrency(string):

    allCurrencyList = getAllCurrencyList()
    for currency in allCurrencyList:
        string.replace(currency, currency+" ")

    words = string.split()

def parseString(string):
    # REGEX PARAMETERS
    type = r'([\$£€])'
    number = r'([\d+.,]+)'
    amounts = r'((million|m|billion|b|k|thousand)?(\s|\.|\,|$))?'
    matcher = re.compile(type + number + r"[\s]*" + amounts, re.UNICODE | re.IGNORECASE)
    matches = re.findall(matcher, string)

    detected_currency = []

    for match in matches:
        type = __getType(match[0])
        value = match[1]
        magnitude = match[3]

        if __checkValid(value):
            value = __checkMagnitude(value, magnitude)
            detected_currency.append([type, value])

    return detected_currency


def __checkValid(val):
    val = val.replace(",", "")
    try:
        val = float(val)
        return True
    except:
        return False


def __checkMagnitude(val, string):
    val = val.replace(",", "")
    val = float(val)

    if string == "billion" or string == "b":
        val *= 1000000000
    if string == "million" or string == "m":
        val *= 1000000
    if string == "thousand" or string == "k":
        val *= 1000
    return val


# check ordinal value of character to get type of currency
def __getType(char):
    if ord(char) == 36:
        return "USD"
    if ord(char) == 172:
        return "EUR"
    if ord(char) == 163:
        return "GBP"
