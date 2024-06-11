from request_api import (
    get_random_weapon,
    get_random_class
)

import pandas as pd


# get_random_class("Rifle")
# get_random_weapon("AK-47")



def create_csv_weapons():
    # Para criar uma tabela
    # Precisamos de ter um tipo de dado
    # Que corresponde a 
    # Uma lista de Dicionario
    weapon = get_random_weapon("AK-47")
    df_weapon = pd.DataFrame([weapon])
    df_weapon.to_excel('weapons.xlsx', index=False)
    
    
create_csv_weapons()
