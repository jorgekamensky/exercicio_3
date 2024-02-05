from src.drivers import calculator_manager
from typing import Dict

class Calculator1Controller:
 
    # def calculator_1(self, input_numbers: list) -> Dict:
    #     calculation = calculator_manager.CalculationManager()
    #     result = calculation.avg_calculation(input_numbers)
    #     return_dict = {
    #         "calculadora": "CALCULADORA 1",
    #         "input": input_numbers,
    #         "resultado do calculo": result
    #     }
    #     return return_dict
    
    CONST = 0.257

    def calculator_1(self, input_number: int) -> Dict:

        part_1 = input_number/3
        part_2 = input_number/3
        part_3 = input_number/3

        result_part_1 = (part_1/4+7)**0.5*self.CONST
        result_part_2 = (part_2**2.121 / 5) + 1
        result_part_3 = part_3

        list_return = [result_part_1, result_part_2, result_part_3]

        calculation = calculator_manager.CalculationManager()

        avg_result = calculation.avg_calculation(list_return)

        return {
            "calculadora": "CALCULADORA 1",
            "Parte 1": result_part_1,
            "Parte 2": result_part_2,
            "Parte 3": result_part_3,
            "Média dos Resultados": avg_result
        }
