from src.controllers.calculator_3_controller import Calculator3Controller

def test_check_var_success():

    input_values = [2, 4, 6, 8, 10]
    calculator = Calculator3Controller()
    result = calculator.calculator_3(input_values)
    assert result == {
                    "calculadora": "CALCULADORA 3",
                    "Entrada": input_values,
                    "Variancia": 8.0,
                    "Desvio Padrao": 2.8284271247461903,
                    "Resultado": "Sucesso: A variância é maior que o desvio padrão."
                    }

def test_check_var_fail():

    input_values = [2, 2, 2, 2, 2]
    calculator = Calculator3Controller()
    result = calculator.calculator_3(input_values)
    assert result == {
                    "calculadora": "CALCULADORA 3",
                    "Entrada": input_values,
                    "Variancia": 0.0,
                    "Desvio Padrao": 0.0,
                    "Resultado": "Falha: A variância não é maior que o desvio padrão."
                    }