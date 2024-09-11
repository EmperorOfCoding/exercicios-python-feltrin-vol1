
def indentificacao(*args, **kwargs):

    for n in args:
        nome = n
        print(f"Nome: {nome}")


    for key, value in kwargs.items():

        idade = key
        sexo = value

        print(f"{idade}:")
        print(f"{sexo}:")


indentificacao('Victor', idade = 19, sexo = 'Masculino')