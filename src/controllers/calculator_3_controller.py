from src.drivers import calculator_manager
from typing import Dict

class Calculator3Controller:

    def calculator_3(self, input_numbers: list) -> Dict:

        calculation_manager = calculator_manager.CalculationManager()
        var_result = calculation_manager.var_calculation(input_numbers)
        std_result = calculation_manager.std_dev_calculation(input_numbers)

        if var_result > std_result:
            return {
                    "calculadora": "CALCULADORA 3",
                    "Entrada": input_numbers,
                    "Variancia": var_result,
                    "Desvio Padrao": std_result,
                    "Resultado": "Sucesso: A variância é maior que o desvio padrão."
                    }
        else:
            return {
                    "calculadora": "CALCULADORA 3",
                    "Entrada": input_numbers,
                    "Variancia": var_result,
                    "Desvio Padrao": std_result,
                    "Resultado": "Falha: A variância não é maior que o desvio padrão."
                    }            
