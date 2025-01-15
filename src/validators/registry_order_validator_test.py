from .registry_order_validator import registry_order_validator
import pytest


def test_registry_order_validator():
    body = {
        "data": {
            "name": "Joaozinho",
            "address": "rua do limao",
            "cupom": False,
            "items": [
                {"item": "refrigerante", "quantidade": 2},
                {"item": "pizza", "quantidade": 2},
            ],
        }
    }
    registry_order_validator(body)


def test_registry_order_validator_with_errors():
    body_with_error = {
        "data": {
            "name": "Joaozinho",
            "address": "rua do limao",
            "cupom": True,
            "items": [
                {"item": "refrigerante", "quantidade": 2},
                {"item": "pizza", "quantidade": 2},
            ],
        }
    }

    with pytest.raises(Exception):
        registry_order_validator_with_errors(body_with_error)
