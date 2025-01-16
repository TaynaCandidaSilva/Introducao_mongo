from src.models.repository.orders_repository import OrdersRepository
from src.main.http_types.http_request import HttpRequest
from src.main.http_types.http_response import HttpResponse
from src.errors.types.http_not_found import HttpNotFoundError
from src.validators.registry_updater_validator import registry_updater_validator
from src.errors.error_handler import error_handle


class RegistryUpdater:
    def __init__(self, orders_repository: OrdersRepository) -> None:
        self.__orders_repository = orders_repository

    def updater(self, http_request: HttpRequest) -> HttpResponse:
        try:
            order_id = http_request.path_params["order_id"]
            body = http_request.body
            self.__validate_body(body)

            self.__update_order(order_id, body)
            return self.__format_response(order_id)
        except Exception as exception:
            return error_handle(exception)

    def __validate_body(self, body: dict) -> None:
        registry_updater_validator(body)

    def __update_order(self, order_id: str, body: dict) -> None:
        update_fields = body["data"]
        self.__orders_repository.edit_registry(order_id, update_fields)

    def __format_response(self, order_id: str) -> HttpResponse:
        return HttpResponse(
            body={
                "data": {
                    "order_id": order_id,
                    "Type": "Order",
                    "count": 1,
                }
            },
            status_code=200,
        )
