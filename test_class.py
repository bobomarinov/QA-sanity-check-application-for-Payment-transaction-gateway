import pytest
import configparser
from loadTestData import *
from functions import *

TransactionsArray, saleVoidTransactionsArray, saleVoidVoidTransactionsArray = LoadData()

class TestClass:
    def test_one(self):
        for transaction in TransactionsArray:
            print("\n\nTestID: " + str(getattr(transaction,"testId")))
            response = ExecuteTransaction(transaction)
            readStatus(response)
            assert int(response.status_code) == int(getattr(transaction,"expectedStatusCode"))

    def test_two(self):
        for transaction in saleVoidTransactionsArray:
            print("\n\nTestID: " + str(getattr(transaction,"testId")))
            response = ExecuteTransaction(transaction)
            readStatus(response)
            assert int(response.status_code) == int(getattr(transaction,"expectedStatusCode"))

            immediateVoidTransaction = VoidTransactionData(response.json()["unique_id"], getattr(transaction,"auth"), getattr(transaction,"url"), getattr(transaction,"testId"), getattr(transaction,"expectedStatusCode"))
            response = ExecuteTransaction(immediateVoidTransaction)
            readStatus(response)
            assert int(response.status_code) == int(getattr(transaction,"expectedStatusCode"))

    def test_three(self):
        for transaction in saleVoidVoidTransactionsArray:
            print("\n\nTestID: " + str(getattr(transaction,"testId")))
            response = ExecuteTransaction(transaction)
            readStatus(response)
            assert int(response.status_code) == 200

            immediateVoidTransaction = VoidTransactionData(response.json()["unique_id"], getattr(transaction,"auth"), getattr(transaction,"url"), getattr(transaction,"testId"), getattr(transaction,"expectedStatusCode"))
            response = ExecuteTransaction(immediateVoidTransaction)
            readStatus(response)
            assert int(response.status_code) == 200

            immediateVoidTransaction2 = VoidTransactionData(response.json()["unique_id"], getattr(transaction,"auth"), getattr(transaction,"url"), getattr(transaction,"testId"), getattr(transaction,"expectedStatusCode"))
            response = ExecuteTransaction(immediateVoidTransaction2)
            readStatus(response)
            assert int(response.status_code) == 422





        


        

