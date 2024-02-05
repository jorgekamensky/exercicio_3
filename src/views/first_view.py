def initial_screen():
    message = """
                Calculadora

                1 - Calculadora 1
                2 - Calculadora 2
                3 - Calculadora 3
                S - Sair

                """
    print(message)
    command = input("Digite o comando desejada: ")

    return command
