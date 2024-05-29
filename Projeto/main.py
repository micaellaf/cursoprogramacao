import requests 
import pandas as pd

url = "https://coinranking1.p.rapidapi.com/coins"

querystring = {"referenceCurrencyUuid": "yhjMzLPhuIDl", "timePeriod": "24h", "tiers[0]": "1", "orderBy": "marketCap", "orderDirection": "desc", "limit": "50", "offset": "0"}


headers = {
	"X-RapidAPI-Key": "3be01a29a9msh1147fa36f6934f8p13aa60jsn802d2dd1cc9f",
	"X-RapidAPI-Host": "coinranking1.p.rapidapi.com"
}

req = requests.get(url, headers=headers, params=querystring)
res = req.json()

coins = res["data"]["coins"]
lista_coins = []
for element in coins:
    lista_coins.append(
        {
            "ïd": element["uuid"],
            "coin": element["name"],
            "preço": element["price"],
            "24h Volume": element["24hVolume"],
            "ranking": element["rank"]
        }
    )
tabela_coins = pd.DataFrame(lista_coins) 
tabela_coins.to_excel("tabela_moedas.xlsx",index=False)

