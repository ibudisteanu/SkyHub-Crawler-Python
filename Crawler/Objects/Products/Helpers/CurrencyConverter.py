# source code from GitHub https://github.com/wathika/CurrencyConverter/blob/master/currencyconverter.py

#!/usr/bin/python
# -*- coding: utf-8 -*-
import json
import urllib3
import re

currencies = [
    ["USD", "US", "$"],
    ["EUR", "EURO", "EU", "€"],
    ['GBP', '£'],
    ['CAD', 'Can$', 'C$'],
    ['CNY', 'yuan'],
    ['JPY', 'yen'],
]

class CurrencyConverter():

    def __init__(self):
        pass

    @staticmethod
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


    # it will return ['USD','US','$', 'EUR', 'EURO', 'EU', '€', ....

    @staticmethod
    def getAllCurrencyList():

        allCurrencyList = []

        for currency in currencies:
            for symbol in currency:
                allCurrencyList.append(symbol)

        return allCurrencyList

    @staticmethod
    def get_number(s):
        try:
            nr = float(s)
            return nr
        except ValueError:
            return None

    @staticmethod
    def is_number(s):
        if CurrencyConverter.get_number(s) is None: return False
        else: return True

    @staticmethod
    def get_currency_symbol(s):
        for currency in currencies:
            for symbol in currency:
                if symbol == s:
                    return currency[0]

        return None

    @staticmethod
    def is_currency_symbol(s):
        if CurrencyConverter.get_currency_symbol(s) is None: return False
        else: return True

    @staticmethod
    def parseStringCurrency(string):

        results = []

        allCurrencyList = CurrencyConverter.getAllCurrencyList()
        for currency in allCurrencyList:
            string.replace(currency, currency+" ")

        words = string.split()
        wordsCurrencies = []
        wordsIsCurrencies = []
        wordsNumbers = []
        wordsIsNumbers = []

        for word in words:
            wordsCurrencies.append(CurrencyConverter.get_currency_symbol(word))
            wordsIsCurrencies.append(CurrencyConverter.is_currency_symbol(word))

        for word in words:
            wordsNumbers.append(CurrencyConverter.get_number(word))
            wordsIsNumbers.append(CurrencyConverter.is_number(word))

        i = 0
        while i < len(words):

            # USD 5533.2
            if i+1 < len(words) and wordsIsCurrencies[i] and wordsIsNumbers[i+1]:
                results.append([wordsCurrencies[i], wordsNumbers[i+1]])
            # USD $333
            elif i+2 < len(words) and wordsIsCurrencies[i] and wordsIsCurrencies[i+1] and wordsIsNumbers[i+2]:
                results.append([wordsCurrencies[i], wordsNumbers[i+1]])
            # 333.2 EUR
            elif i+1 < len(words) and wordsIsNumbers[i] and wordsIsCurrencies[i+1]:
                results.append([wordsCurrencies[i+1], wordsNumbers[i]])

        return results

    @staticmethod
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

    @staticmethod
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

    @staticmethod
    # check ordinal value of character to get type of currency
    def __getType(char):
        if ord(char) == 36:
            return "USD"
        if ord(char) == 172:
            return "EUR"
        if ord(char) == 163:
            return "GBP"
