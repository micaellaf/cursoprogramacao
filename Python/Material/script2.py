"""
    Função é uma forma de reaproveitar um trecho de código
    
    Imaigna que todo mês, pelo menos algumas vezes você soma suas dispesas
    para você ter o balanço dos seus gastos no final do mês.
    
    Todo mês é gasto com:
    - Aluguel
    - luz + agua + energia
    - Comida
    - Gasto Pessoal
"""


def somar_dispesas(valor1, valor2, valor3, valor4):
    return valor1 + valor2 + valor3 + valor4


janeiro = somar_dispesas(1200, 400, 1400, 1000)
fevereiro = somar_dispesas(500, 300, 1200, 3200)

print(fevereiro)