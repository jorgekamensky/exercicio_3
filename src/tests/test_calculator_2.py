from src.controllers.calculator_2_controller import Calculator2Controller

def test_check_2():

    input_values = [2, 4, 6, 8, 10]
    calculator = Calculator2Controller()
    result = calculator.calculator_2(input_values)
    assert result == {'calculadora': 'CALCULADORA 2', 'Entrada': [2, 4, 6, 8, 10], 'Desvio Padrao do Resultado': 0.04155377411672721}