
from time import sleep

def cotação():
    import requests
    import json
    cotacoes = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
    cotacoes = cotacoes.json()
    cotacao_dolar = cotacoes['USDBRL']['bid']
    cotacao_euro = cotacoes['EURBRL']['bid']
    cotacao_btc = cotacoes['BTCBRL']['bid']
    cotacao_dolar = float(cotacao_dolar)
    cotacao_euro = float(cotacao_euro)
    cotacao_btc = float(cotacao_btc)
    return cotacao_dolar, cotacao_euro, cotacao_btc

def exibir_cotacoes(cotacao_dolar, cotacao_euro, cotacao_btc):
    print('Cotação do Dólar:',f'R$ {cotacao_dolar:.2f}')
    print('Cotação do Euro:',f'R$ {cotacao_euro:.2f}')
    print('Cotação do Bitcoin:',f'R$ {cotacao_btc}')

