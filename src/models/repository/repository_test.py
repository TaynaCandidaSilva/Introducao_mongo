import pytest
from src.models.connection.connection_handler import DBConnectionHandler
from .orders_repository import OrdersRepository

db_connection_handler = DBConnectionHandler()
db_connection_handler.connect_to_db()
conn = db_connection_handler.get_db_connection()


@pytest.mark.skip(reason="Interacao com o banco")
def test_insert_document():
    orders_repository = OrdersRepository(conn)
    my_doc = {"Ola": "Mundo"}
    orders_repository.insert_document(my_doc)


@pytest.mark.skip(reason="Interacao com o banco")
def test_insert_list_of_documents():
    orders_repository = OrdersRepository(conn)
    my_doc = [{"elem1": "aqui1"}, {"elem2": "aqui2"}, {"elem3": "aqui3"}]
    orders_repository.insert_list_of_documents(my_doc)


def test_select_many():
    orders_repository = OrdersRepository(conn)
    doc_filter = {"cupom": True}
    response = orders_repository.select_many(doc_filter)
    print()
    print(response)
    for doc in response:
        print(doc)
        print(doc["itens"])
        print()


def test_select_one():
    orders_repository = OrdersRepository(conn)
    doc_filter = {"cupom": True}
    response = orders_repository.select_one(doc_filter)
    print()
    print(response)


def test_select_many_with_properties():
    orders_repository = OrdersRepository(conn)
    doc_filter = {"cupom": True}
    response = orders_repository.select_many_with_properties(doc_filter)
    print()
    for doc in response:
        print(doc)
        print()


def test_select_if_properties_exists():
    orders_repository = OrdersRepository(conn)
    response = orders_repository.select_if_properties_exists()
    print()
    for doc in response:
        print(doc)
        print()
