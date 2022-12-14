import requests


requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL,ETH-BRL")
requisicao_dic = requisicao.json()

cotacao_dolar = requisicao_dic['USDBRL']['bid']
cotacao_euro = requisicao_dic['EURBRL']['bid']
cotacao_btc = requisicao_dic['BTCBRL']['bid']
cotacao_eth = requisicao_dic['ETHBRL']['bid']

cotacoes = f'''
Dólar: {cotacao_dolar}
Euro: {cotacao_euro}
BTC: {cotacao_btc}
ETH: {cotacao_eth}'''

## training

def dolar_t() :
    return cotacao_dolar

def euro_t() :
    return cotacao_euro

def btc_t() :
    return cotacao_btc

def eth_t() :
    return cotacao_eth

## match

def txt_cotacoes() :
    return cotacoes

def dolar() :
    return round(float(cotacao_dolar), 2)

def euro() :
    return round(float(cotacao_euro), 2)

def btc() :
    return round(float(cotacao_btc), 2)

def eth() :
    return round(float(cotacao_eth), 2)


def money_dolar(self) :
    return round(self / dolar(), 2)


print(money_dolar(352))





