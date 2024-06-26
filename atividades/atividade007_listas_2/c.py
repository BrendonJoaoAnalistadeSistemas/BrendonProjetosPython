# Curso de Desenvolvimento de Sistemas.
# Turma: 0152.
# Autor: Brendon João Campos Neves.
# Data: 17/06/2024.
# C) Faça um programa que preencha uma lista com 50 números aleatórios.
# Depois fatie essa lista em 5 listas de 10 elementos.

# Importando as bibliotecas do sistema:
import os
import random


# Limpando o terminal:
os.system('cls')

# Declarações de variáveis:
numeros = []
numero = 0
de0a10 = []
de11a20 = []
de21a30 = []
de31a40 = []
de41a50 = []

# Gerando 50 números aleatórios:
for numero in range(0, 50):
    numero = random.randint(0, 100)
    numeros.append(numero)

# Processamento de dados:
de0a10 = numeros[0:10]
de11a20 = numeros[10:20]
de21a30 = numeros[20:30]
de31a40 = numeros[30:40]
de41a50 = numeros[40:50]

# Saída de dados:
print('='*79)
print(f'Lista completa de números aleatórios: {numeros}')
print(f'Dividindo a lista: ')
print(f'Índice 0 a 10: {de0a10}')
print(f'Índice 11 a 20: {de11a20}')
print(f'Índice 21 a 30: {de21a30}')
print(f'Índice 31 a 40: {de31a40}')
print(f'Índice 41 a 50: {de41a50}')
print('='*79)

# Exibindo título de fim:
print('.'*79)
print('Fim do programa! Obrigado!')
print('.'*79)