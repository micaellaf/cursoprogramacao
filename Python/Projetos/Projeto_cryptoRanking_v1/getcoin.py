import requests
import pandas as pd


inicio = True
while inicio == True:
    id_coin = input("insira o id de uma moeda: ")
    name_coin = input("insira o nome da moeda: ")

    url = f"https://coinranking1.p.rapidapi.com/coin/{id_coin}"

    querystring = {"referenceCurrencyUuid":"yhjMzLPhuIDl","timePeriod":"24h"}

    headers = {
	"X-RapidAPI-Key": "4d8bf38d7cmshb12a12581bb09ccp12709ejsnb9a3507d9ab0",
	"X-RapidAPI-Host": "coinranking1.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    data = response.json()
    coin = {
            "ïd": data["data"]["coin"]["uuid"],
            "coin": data["data"]["coin"]["name"],
            "preço": data["data"]["coin"]["price"],
            "24h Volume":data["data"]["coin"]["24hVolume"],
            "ranking": data["data"]["coin"]["rank"]
        }
    coin_tabela = pd.DataFrame([coin])
    coin_tabela.to_excel(f"{name_coin}.xlsx",index=False)
    inicio = False