import json
import requests
import request



print("Posted file: {}".format(request.file['file']))
file = request.files['file']
files = {'file': file.read()}

url = requests.get("https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token=98a71e34b1dd5c3fcf661b1ea738732c52eb72f2")
#meuToken = {'token': '98a71e34b1dd5c3fcf661b1ea738732c52eb72f2'}

response = requests.post(url, files=files)

print(response)

#arquivo = open("danswer.json", "w")
#json.dump(response.json(), arquivo)
#arquivo.close()