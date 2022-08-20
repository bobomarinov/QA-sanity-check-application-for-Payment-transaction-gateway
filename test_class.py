import pytest
import configparser
from loadTestData import *
from functions import *

TransactionsArray, saleVoidTransactionsArray, saleVoidVoidTransactionsArray = LoadData() #load the test data from the .ini file

class TestClass: #class for testing the functions in the functions.py file
    def test_one(self): #testing sale transactions and void transactions that are stored in TransactionsArray
        for transaction in TransactionsArray:
            #testing sale transactions and void transactions that are stored in TransactionsArray
            print("\n\nTestID: " + str(getattr(transaction,"testId"))) #printing the test id
            response = ExecuteTransaction(transaction) #executing the transaction
            readStatus(response) #reading the status of the transaction
            assert int(response.status_code) == int(getattr(transaction,"expectedStatusCode")) #asserting the status code of the transaction is the expected status code
 
    def test_two(self): #testing sale transactions and void transactions that are stored in saleVoidTransactionsArray
        for transaction in saleVoidTransactionsArray:
            #testing sale transaction that is voided right after
            print("\n\nTestID: " + str(getattr(transaction,"testId"))) #printing the test id
            response = ExecuteTransaction(transaction)  #executing the transaction
            readStatus(response) #reading the status of the transaction
            assert int(response.status_code) == int(getattr(transaction,"expectedStatusCode")) #asserting the status code of the transaction is the expected status code

            immediateVoidTransaction = VoidTransactionData(response.json()["unique_id"], getattr(transaction,"auth"), getattr(transaction,"url"), getattr(transaction,"testId"), getattr(transaction,"expectedStatusCode")) #creating the object for the void transaction
            response = ExecuteTransaction(immediateVoidTransaction) #executing the void transaction
            readStatus(response) #reading the status of the transaction
            assert int(response.status_code) == int(getattr(transaction,"expectedStatusCode")) #here we check if the status is as expected

    def test_three(self):
        for transaction in saleVoidVoidTransactionsArray: #testing sale transaction that is voided right after and then voided again
            
            print("\n\nTestID: " + str(getattr(transaction,"testId"))) #printing the test id
            response = ExecuteTransaction(transaction) #executing the transaction
            readStatus(response) #reading the status of the transaction
            assert int(response.status_code) == 200 #asserting the status code of the transaction is the expected status code

            immediateVoidTransaction = VoidTransactionData(response.json()["unique_id"], getattr(transaction,"auth"), getattr(transaction,"url"), getattr(transaction,"testId"), getattr(transaction,"expectedStatusCode"))
            response = ExecuteTransaction(immediateVoidTransaction) #executing the void transaction
            readStatus(response) #reading the status of the transaction
            assert int(response.status_code) == 200 #asserting the status code of the transaction is the expected status code

            immediateVoidTransaction2 = VoidTransactionData(response.json()["unique_id"], getattr(transaction,"auth"), getattr(transaction,"url"), getattr(transaction,"testId"), getattr(transaction,"expectedStatusCode"))
            response = ExecuteTransaction(immediateVoidTransaction2) #executing the void transaction
            readStatus(response) #reading the status of the transaction
            assert int(response.status_code) == 422 #asserting the status code of the transaction is the expected status code





        


        

