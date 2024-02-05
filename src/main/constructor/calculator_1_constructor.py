from src.views.calculator_1_view import Calculator1View
from src.controllers.calculator_1_controller import Calculator1Controller

def calculator_1_contructor():
   calculator_1_view = Calculator1View()
   calculator_1_controller = Calculator1Controller()

   input_number = calculator_1_view.input_numbers() # enviar para o controller
   calculation = calculator_1_controller.calculator_1(input_number)
   response = calculator_1_view.format_response(calculation)