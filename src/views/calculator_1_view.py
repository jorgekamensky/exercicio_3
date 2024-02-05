from typing import Dict
import os

class Calculator1View:
    def input_numbers(self) -> int:
        os.system("cls||clear")

        print("Calculadora 1 \n\n")

        user_input = input("Digite os numeros para o calculo: ")
        user_input_int = int(user_input)
        return user_input_int
    
    def format_response(self, response: Dict) -> Dict:
        return print(response)