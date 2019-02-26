
# Exercício para converter número de base 10 para base 16
# Requisitos: não usar looping, três dígitos apenas

numero = int(input("Insira um número em decimal: "))
base = 16

lista = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', "A", "B", "C", "D", "E", "F"]

resultado = ''

resultado = lista[int(numero % base)] + resultado
resultado = lista[int(int(numero)/base) % base] + resultado
resultado = lista[int(int(numero)/base/base) % base] + resultado

print('Hexadecimal: ' + resultado)
