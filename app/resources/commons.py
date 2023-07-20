from datetime import datetime, timedelta
import random
import string


def data_atual():
    data_atual = datetime.today()
    data_atual_formatada = data_atual.strftime('%d/%m/%Y')
    return data_atual_formatada

# string 6 caracteres
def cria_sequencial_alfanumerico(): 
    num = str(random.randint(100, 900))
    size = 3
    chars = string.ascii_uppercase
    caracter = ''.join(random.choice(chars) for _ in range(size))
    
    return num + caracter

# string 2 caracteres
def cria_sequencial_caracter():
    size = 2
    chars = string.ascii_uppercase
    caracter = ''.join(random.choice(chars) for _ in range(size))
    
    return caracter



