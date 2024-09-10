nome_frase = str(input("Digite uma frase ou nome: \n")).strip().upper()

frase_separada = nome_frase.split()

caracteres = ''.join(frase_separada)

frase_invertida = ''

for i in range(len(caracteres) - 1, -1, -1):
    frase_invertida += caracteres[i]

print(caracteres, frase_invertida)
if (frase_invertida == caracteres):
    print("Esta frase/nome é um palíndromo!!")

else:
    print("Esta frase nao é um palindromo")
