import requests 
import pandas as pd

url = "https://coinranking1.p.rapidapi.com/coins"

querystring = {"referenceCurrencyUuid": "yhjMzLPhuIDl", "timePeriod": "24h", "tiers[0]": "1", "orderBy": "marketCap", "orderDirection": "desc", "limit": "50", "offset": "0"}


headers = {
	"X-RapidAPI-Key": "4d8bf38d7cmshb12a12581bb09ccp12709ejsnb9a3507d9ab0",
	"X-RapidAPI-Host": "coinranking1.p.rapidapi.com"
}


req = requests.get(url, headers=headers, params=querystring)
res = req.json()

#podemos pegar o symbol, name, marketCap, price, rank, 24Volume
bitcoin = res["data"]["coins"][0]
tabela_bitcoin={
    "símbolo":bitcoin["symbol"],
    "moeda":bitcoin["name"],
    "marketCap":bitcoin["marketCap"],
    "preço":bitcoin["price"],
    "ranking":bitcoin["rank"],
    "24hVolume":bitcoin["24hVolume"]
}
df = pd.DataFrame([tabela_bitcoin])

df.to_excel("bitcoin.xlsx",index=False)