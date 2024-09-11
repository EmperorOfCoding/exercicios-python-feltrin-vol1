
dados_aluno = [{'Nome': 'Victor Martins Ferreira Brandao Ameno',
                'Notas': [6, 9, 6]}]

def calcular_media_aluno(dados_aluno):

    notas = []

    for index in dados_aluno:

        if len(index['Notas']) > 0:

            temp = round(sum(index['Notas']) / len(index['Notas']))

        else:
            temp = 0

        notas.append({'Nome': index['Nome'],
                      'Media': temp})
        
    print(notas)


novo_dict = calcular_media_aluno(dados_aluno)
