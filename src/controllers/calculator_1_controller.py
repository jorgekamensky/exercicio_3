from .interface.Icalculator import ICalculator
from src.drivers import calculator_manager
from typing import Dict
from src.main.http_types.http_response import HttpResponse
from src.main.http_types.http_request import HttpRequest

class Calculator1Controller(ICalculator):

    def execute(self, req: HttpRequest) -> HttpResponse:
        body = req.body
        input_number = body["number"]
        result_dict = self.__calculator_1(input_number)
        return HttpResponse(203, result_dict)


    def __calculator_1(self, input_number: int) -> Dict:

        part_1 = input_number/3
        part_2 = input_number/3
        part_3 = input_number/3

        __CONST = 0.257

        result_part_1 = (part_1/4+7)**0.5*__CONST
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
