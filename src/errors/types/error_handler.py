from src.main.http_types.http_response import HttpResponse
from src.errors.types.http_unprocessable_entity import HttpUnprocessableEntityError
from src.errors.types.http_not_found import HttpNotFoundError


def error_handle(error: Exception) -> HttpResponse:
    if isinstance(error, (HttpUnprocessableEntityError, HttpNotFoundError)):

        return HttpResponse(
            status_code=error.status_code,
            body={"errors": [{"title": error.name, "detail": error.message}]},
        )

    return HttpResponse(
        status_code=500,
        body={"errors": [{"title": "Server Error", "detail": str(error)}]},
    )
