
def welcome(nome, nacionalidade = "Americano") -> None:
    print(f"Olá {nome}, Voce é {nacionalidade}")


nome = input("Digite o seu nome: \n")
exemplo1 = welcome(nome)

nacionalidade = input("Digite a sua nacionalidade: \n")
exemplo2 = welcome(nome, nacionalidade)



