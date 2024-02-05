import numpy as np

class CalculationManager:
    def __init__(self) -> None:
        self.__np = np
    
    def avg_calculation(self, input_numbers: list) -> int:
        result = self.__np.average(input_numbers)
        return result
    
    def std_dev_calculation(self, input_numbers: list) -> float:
        result = self.__np.std(input_numbers)
        return result
    
    def var_calculation(self, input_numbers: list) -> float:
        result = self.__np.var(input_numbers)
        return result