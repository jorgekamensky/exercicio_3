from abc import ABC, abstractmethod
from src.main.http_types.http_response import HttpResponse
from src.main.http_types.http_request import HttpRequest

class ICalculator(ABC):

    @abstractmethod
    def execute(self, req: HttpRequest) -> HttpResponse:
        pass