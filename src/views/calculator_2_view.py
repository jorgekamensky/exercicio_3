from typing import Dict, List
import os

class Calculator2View:
    def input_numbers(self) -> List:
        os.system("cls||clear")

        print("Calculadora 2 \n\n")

        user_input = input("Digite os numeros para o calculo: ")
        user_input_str_list = user_input.split(",")
        user_input_int_list = [int(num) for num in user_input_str_list]
        return user_input_int_list
    
    def format_response(self, response: Dict) -> Dict:
        return print(response)