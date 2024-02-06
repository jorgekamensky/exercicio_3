from flask import request as FlaskRequest
from src.main.http_types.http_request import HttpRequest

def request_adapter(request: FlaskRequest) -> HttpRequest:
    http_request = HttpRequest(
        header=request.headers,
        body=request.json,
        query_params=dict(request.args),
        path_params=request.view_args,
        url=request.full_path,
        ipv4=request.remote_addr,
    )

    return http_request
