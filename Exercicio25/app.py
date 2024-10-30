
#Fibonnaci: 0, 1, 1, 2, 3, 5, 8, 13

def fibonnaci(n):

    if (n <= 1 and n >= 0):

        return n
    
    else:
        return fibonnaci(n - 1) + fibonnaci(n - 2)
    


numero = int(input("Digite um Numero para encontrar seu Fibonnaci: "))
resultado = fibonnaci(numero - 1)
print(resultado)





