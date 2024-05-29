"""
    Esse é o arquivo que vai ficar as funções de requisições
    na api.
"""
import requests


id_coin = "Qwsogvtv82FCd"
url_coins = "https://coinranking1.p.rapidapi.com/coins"
url_coin = f"https://coinranking1.p.rapidapi.com/coin/{id_coin}"

querystring = {
    "referenceCurrencyUuid": "yhjMzLPhuIDl",
    "timePeriod": "24h",
    "tiers[0]": "1",
    "orderBy": "marketCap",
    "orderDirection": "desc",
    "limit": "50",
    "offset": "0",
}


headers = {
    "X-RapidAPI-Key": "3be01a29a9msh1147fa36f6934f8p13aa60jsn802d2dd1cc9f",
    "X-RapidAPI-Host": "coinranking1.p.rapidapi.com",
}


def busca_todas_moedas():
    req = requests.get(url_coins, headers=headers, params=querystring)
    res = req.json()
    return res
