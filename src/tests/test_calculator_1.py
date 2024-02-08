from src.controllers.calculator_1_controller import Calculator1Controller

def test_check_calculator_1():

    input_values = {"body":{"number": 6}}
    calculator = Calculator1Controller()
    result = calculator.execute(input_values)
    assert result == {'calculadora': 'CALCULADORA 1', 'Parte 1': 0.7038234863941385, 'Parte 2': 1.8699907126839064, 'Parte 3': 2.0, 'Média dos Resultados': 1.524604733026015}