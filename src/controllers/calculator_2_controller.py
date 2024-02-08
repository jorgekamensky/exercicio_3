from .interface.Icalculator import ICalculator
from src.drivers import calculator_manager
from typing import Dict
from src.main.http_types.http_response import HttpResponse
from src.main.http_types.http_request import HttpRequest

class Calculator2Controller(ICalculator):

    def execute(self, req: HttpRequest) -> HttpResponse:
        body = req.body
        input_number = body["numbers"]
        result_dict = self.__calculator_2(input_number)
        return HttpResponse(203, result_dict)

    def __calculator_2(self, input_numbers: list) -> Dict:

        result = [(input_number * 11) ** 0.95 for input_number in input_numbers]
        calculation = calculator_manager.CalculationManager()
        std_result = calculation.std_dev_calculation(result)
        final_std_result = 1 / std_result

        return {
            "calculadora": "CALCULADORA 2",
            "Entrada": input_numbers,
            "Desvio Padrao do Resultado": final_std_result
        }
