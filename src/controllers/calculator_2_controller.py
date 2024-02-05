from src.drivers import calculator_manager
from typing import Dict

class Calculator2Controller:

    def calculator_2(self, input_numbers: list) -> Dict:

        result = [(input_number * 11) ** 0.95 for input_number in input_numbers]
        calculation = calculator_manager.CalculationManager()
        std_result = calculation.std_dev_calculation(result)
        final_std_result = 1 / std_result

        return {
            "calculadora": "CALCULADORA 2",
            "Entrada": input_numbers,
            "Desvio Padrao do Resultado": final_std_result
        }
