#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  loteria.py
#  
#  Copyright 2019 rafae <rafae@DESKTOP-JJ4ET6O>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

import time

def imprime():
	
	print("Parabéns, jovem campeão! Você chegou até aqui.")
	time.sleep(3)
	print("Após passar por tantas fases chegou a hora de ganhar uma recompensa, não acha?")
	time.sleep(4)
	print("O que você acha de jogar na loteria? Vamos lá, eu vou explicar como funciona...")
	time.sleep(4)
	print("A loteria é um jogo em que as pessoas fazem apostas com o objetivo de ganhar um valor estabelecido.")
	time.sleep(4)
	print("Você deve apostar entre 6 a 15 números, dentre os 60 número disponíveis")
	
def cria_lista(lista, tam):
	
	quant = 1
	while (quant<=tam):
		lista.append(quant)
		quant+1
		
def loteria():
	
	lista60 = []
	
	imprime()
	cria_lista(lista60, 60)
	
	n = input("Você deve apostar entre 6 e 15 números dentre os 60 números. Quantos números você quer apostar?")
	while (n<6 or n>15):
		n = input("Você deve apostar entre 6 e 15 números dentre os 60 números. Quantos números você quer apostar?")
		
	
	#teste
	for x in range (len(lista60)):
		print(lista60[x])
	
def main(args):
	
	loteria()
	
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
