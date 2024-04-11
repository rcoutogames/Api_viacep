import requests
import json

cep = int(input("Digite seu Cep"))

link = (f'https://viacep.com.br/ws/{cep}/json/') 

zip_code = requests.get(link)
 
print(zip_code)

print(zip_code.json())

# https://viacep.com.br/ws/{uf}/{cidade/{endereço}/json/

