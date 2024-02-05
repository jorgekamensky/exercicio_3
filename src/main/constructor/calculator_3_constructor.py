from src.views.calculator_3_view import Calculator3View
from src.controllers.calculator_3_controller import Calculator3Controller

def calculator_3_contructor():
   calculator_3_view = Calculator3View()
   calculator_3_controller = Calculator3Controller()

   input_numbers = calculator_3_view.input_numbers() # enviar para o controller
   calculation = calculator_3_controller.calculator_3(input_numbers)
   response = calculator_3_view.format_response(calculation)