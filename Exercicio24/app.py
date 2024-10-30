#*args (Parametros com variáveis)

def justaposicao(*args):

    resultado = 0
    for i in args:
        resultado+= 1
    return resultado



resultado_justaposicao = justaposicao(1, 2, 3, 4, 5, 10, 11, 20, 40)
print(resultado_justaposicao)

#*kwargs (Parametros nomeados)


def parametros_nomeados(**kwargs):
    print(kwargs)



parametros_nomeados(nome = "Luiz", idade = 18, estado_civil = "Solteiro")











