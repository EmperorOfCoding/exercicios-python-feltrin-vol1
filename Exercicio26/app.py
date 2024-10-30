from time import sleep
import medicos

print("Bem vindo a Clinica Médica Victor Martins, por favor, aguarde...")
sleep(5)
print("Iniciando Consulta...")
sleep(2)

menu = str(input("Deseja agendar uma consulta? (S ou N)")).upper()

if (menu == 'S'):
    paciente = input("Por favor, digite o seu nome completo: ")
    print(f"{paciente}, escolha com qual médico deseja consultar: ")
    print('1 - Dr. Joao')
    print('2 - Dr. Wallace')
    print('3 - Dr. Bruno Austregelio')
    print('4 - Dr. Rafael Silva')

    medico = int(input('Com qual médico deseja agendar consulta?'))

    if (medico == 1):
        print(f'Sua consulta com o Dr. {medicos.medicos[0]} será agendada')

    elif (medico == 2):
        print(f'Sua consulta com o Dr. {medicos.medicos[1]} será agendada.')

    elif (medico == 3):
        print(f'Sua consulta com o Dr. {medicos.medicos[2]} será agendada.')

    elif (medico == 4):
        print(f'Sua consulta com o Dr. {medicos.medicos[3]} será agendada.')

    else:
        print("Agradecemos o seu contato!!!")