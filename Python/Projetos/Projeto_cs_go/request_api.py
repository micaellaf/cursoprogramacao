import requests

headers = {
    "x-rapidapi-key": "3be01a29a9msh1147fa36f6934f8p13aa60jsn802d2dd1cc9f",
    "x-rapidapi-host": "cs-skin-api.p.rapidapi.com",
}


def get_random_weapon(weapon):
    url = f"https://cs-skin-api.p.rapidapi.com/random/{weapon}"
    response = requests.get(url, headers=headers)
    return response.json()


def get_random_class(item_class):
    url = f"https://cs-skin-api.p.rapidapi.com/randomclass/{item_class}"
    response = requests.get(url, headers=headers)
    return response.json()

def get_random_skin():
    url = "https://cs-skin-api.p.rapidapi.com/random"
    response = requests.get(url, headers=headers)
    return response.json()

print(get_random_skin())

