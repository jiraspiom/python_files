#print (response.url)
#print (response.status_code) 
#print (response.content)
#print (response.json())
#https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token=SEU_TOKEN

import json
import requests
import hashlib

url = "https://api.codenation.dev/v1/challenge/dev-ps/generate-data"
meuToken = {'token': '98a71e34b1dd5c3fcf661b1ea738732c52eb72f2'}

response = requests.get(url, params=meuToken)
response_json = response.json()

casa = response_json["numero_casas"]
#token = response_json["token"]
cifrado = response_json["cifrado"]
#decifrado = response_json["decifrado"]
#resumo = response_json["resumo_criptografico"]

descriptografado = ""

for v in cifrado:
    if v == " " or v == "!" or v == ",":
        descriptografado = descriptografado + v
    else:
        descriptografado = descriptografado +  (chr(ord(v) - casa))

#mostro o valor descriptografado    
print("mensaguem:>>> " + descriptografado)

#adicionando valores no json
response_json["decifrado"] = descriptografado
response_json["resumo_criptografico"] = hashlib.sha1(descriptografado.encode()).hexdigest()

#conferindo se foi adiconado certo
print(response_json)

