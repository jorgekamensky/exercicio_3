from .interface.Icalculator import ICalculator
from src.drivers import calculator_manager
from typing import Dict
from src.main.http_types.http_response import HttpResponse
from src.main.http_types.http_request import HttpRequest

class Calculator3Controller(ICalculator):

    def execute(self, req: HttpRequest) -> HttpResponse:
        body = req.body
        input_number = body["numbers"]
        result_dict = self.__calculator_3(input_number)
        return HttpResponse(203, result_dict)
    
    def __calculator_3(self, input_numbers: list) -> Dict:

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
