import os
from sinesp_client import SinespClient

sc = SinespClient()
placa = input("Digite sua placa: ")

resultado = sc.search(placa)

clear = lambda: os.system('cls')
clear()

print("  _______________________________________________________")
print("/|                                                       |")
print("||_______________________________________________________|")
print("|/______________________________________________________/")

print ("restricao : " + resultado.get('status_message'))
print ("placa     : " + resultado.get('plate'))
print ("chassis   : " + resultado.get('chassis'))
print ("modelo    : " + resultado.get('model'))
print ("marca     : " + resultado.get('brand'))
print ("cor       : " + resultado.get('color'))
print ("ano/modelo: " + resultado.get('year') + "/" + resultado.get('model_year'))
print ("cidade    : " + resultado.get('city') + " - " + resultado.get('state'))
print ("data da consulta: " + resultado.get('date'))

print("=========================================================")
print ("codigo: " + resultado.get('return_code') + " resultado: " + resultado.get('return_message') + " status: " + resultado.get('status_code'))
print("=========================================================")
      

input("Consulta finalizada...")



"""
201 ╔  ═205═   ╗187
186 ║          ║
200 ╚══════════╝ 188

      203╦

204╠  206╬     ╣ 185

      202╩


179 │
180 ┤
191 ┐
192└
193┴
194┬
195├
196─
197┼
217┘
218┌

219█
220▄
223▀
"""