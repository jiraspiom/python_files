#print (response.url)
#print (response.status_code) 
#print (response.content)
#print (response.json())
#https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token=SEU_TOKEN

import json
import requests

url = "https://api.codenation.dev/v1/challenge/dev-ps/generate-data"
parametro = {'token': '98a71e34b1dd5c3fcf661b1ea738732c52eb72f2'}

response = requests.get(url, params=parametro)
response_json = response.json()

casa = response_json["numero_casas"]
token = response_json["token"]
cifrado = response_json["cifrado"]
decifrado = response_json["decifrado"]
resumo = response_json["resumo_criptografico"]

descriptografado = ""

for v in cifrado:
    if v == " " or v == "!" or v == ",":
        descriptografado = descriptografado + v
    else:
        descriptografado = descriptografado +  (chr(ord(v) - casa))
    
print(descriptografado)


#----------------------------------
recebe = input("qual é seu nome? ")

print("Olá " + recebe)

wait = input("PRESS ENTER TO CONTINUE.")

