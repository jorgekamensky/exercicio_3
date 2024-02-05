from src.views.calculator_2_view import Calculator2View
from src.controllers.calculator_2_controller import Calculator2Controller

def calculator_2_contructor():
   calculator_2_view = Calculator2View()
   calculator_2_controller = Calculator2Controller()

   input_numbers = calculator_2_view.input_numbers() # enviar para o controller
   calculation = calculator_2_controller.calculator_2(input_numbers)
   response = calculator_2_view.format_response(calculation)