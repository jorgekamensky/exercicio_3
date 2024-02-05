# Vai apontar para o construtores
from .constructor.introduction_process import introduction_process
from .constructor.calculator_1_constructor import calculator_1_contructor
from .constructor.calculator_2_constructor import calculator_2_contructor
from .constructor.calculator_3_constructor import calculator_3_contructor


def start() -> None:
    while True:

        command = introduction_process()

        if command == '1':
            calculator_1_contructor()
        elif command == '2':
            calculator_2_contructor()
        elif command == '3':
            calculator_3_contructor()
        elif command == "S":
            exit()
        else:
            print("\n Comando nao encontrado \n\n")