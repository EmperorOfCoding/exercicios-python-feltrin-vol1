from time import sleep


sistema = {
    'Pergunta 01': {
        'Pergunta': 'Quanto é 5 x 5?',
        'Alternativas': {'a': '10', 'b': '15', 'c': '20', 'd': '25'},
        'Resposta_certa': 'd'
    },

    'Pergunta 02': {
        'Pergunta': 'Qual é a Capital da Italia?',
        'Alternativas': {'a': 'Madri', 'b': 'Barcelona', 'c': 'Veneza', 'd': 'Roma'},
        'Resposta_certa': 'd' 
    },
}

respostas_certas = 0

for pkeys, pvalues in sistema.items():
    print(f'{pkeys}: {pvalues['Pergunta']}')

    for rkeys, rvalues in pvalues['Alternativas'].items():
        print(f'[{rkeys}: {rvalues}]')

    resposta = input("Digite a Resposta: [a], [b], [c], [d] \n")

    if (resposta == pvalues['Resposta_certa']):
        print("Resposta Correta!!!")
        respostas_certas += 1

    else:
        print("Resposta Incorreta!!!")

        sleep(2)


if (respostas_certas == 0):
    print("Voce nao acertou nenhuma questao :(")

elif (respostas_certas == 1):
    print("Voce acertou apenas uma questao :/")

else:
    print("Voce acertou todas as questoes!!! Parabéns!!!")





