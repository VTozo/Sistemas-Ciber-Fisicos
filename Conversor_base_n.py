
letras = {
  'a': 10,
  'b': 11,
  'c': 12,
  'd': 13,
  'e': 14,
  'f': 15,
  'g': 16,
  'h': 17,
  'i': 18,
  'j': 19,
  'k': 20,
  'l': 21,
  'm': 22,
  'n': 23,
  'o': 24,
  'p': 25,
  'q': 26,
  'r': 27,
  's': 28,
  't': 29,
  'u': 30,
  'v': 31,
  'w': 32,
  'x': 33,
  'y': 34,
  'z': 35
}


def conversor_base_n(valor, base):
    posicao = 0
    resultado = 0
    for digito in reversed(valor):
        if not digito.isdigit():
            digito = letras[digito.lower()]

        resultado += int(digito)*base**posicao
        posicao += 1

    return 'Valor na base decimal: '+str(resultado)


base_digitada = int(input('Digite a base de origem: '))
valor_digitado = input('Digite o valor a ser convertido: ')

print(conversor_base_n(valor_digitado, base_digitada))
