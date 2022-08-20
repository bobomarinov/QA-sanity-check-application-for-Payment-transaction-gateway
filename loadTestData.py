import configparser
from transactionClasses import *

def LoadData():
    #this function is used to load test transaction data from .ini file. Data is stored in 3 different arrays of objects.
    config = configparser.ConfigParser()
    config.sections()
    config.read('test.ini')
    TransactionsArray = [] #sale and void transaction data
    saleVoidTransactionsArray = [] #sale transactions that are voided instantly
    saleVoidVoidTransactionsArray = [] #sale transactions that are voided instantly and the trying to be voided again


    for section in config.sections(): #loop through the sections in the .ini file
        if (config[section]['transaction_type'] == 'sale'):
            TransactionsArray.append(SaleTransactionData( 
            config[section]['card_number'],
            config[section]['cvv'],
            config[section]['expiration_date'],
            config[section]['amount'],
            config[section]['usage'], 
            config[section]['transaction_type'], 
            config[section]['card_holder'], 
            config[section]['email'], 
            config[section]['address'], 
            config[section]['auth'],
            config[section]['url'],
            config[section]['testId'],
            config[section]['expectedStatusCode']
            ))
        elif (config[section]['transaction_type'] == 'void'): #if the transaction type is void then add the data to the void transaction array
            TransactionsArray.append(VoidTransactionData( 
            config[section]['reference_id'],
            config[section]['auth'],
            config[section]['url'],
            config[section]['testId'], 
            config[section]['expectedStatusCode'],
            config[section]['transaction_type'],
            ))
        elif(config[section]['transaction_type'] == 'saleVoid'): #if the transaction type is saleVoid then add the data to the saleVoid transaction array
            saleVoidTransactionsArray.append(SaleTransactionData( 
            config[section]['card_number'],
            config[section]['cvv'],
            config[section]['expiration_date'],
            config[section]['amount'],
            config[section]['usage'], 
            'sale', 
            config[section]['card_holder'], 
            config[section]['email'], 
            config[section]['address'], 
            config[section]['auth'],
            config[section]['url'],
            config[section]['testId'],
            config[section]['expectedStatusCode']
            ))
        elif(config[section]['transaction_type'] == 'saleVoidVoid'): #if the transaction type is saleVoidVoid then add the data to the saleVoidVoid transaction array
            saleVoidVoidTransactionsArray.append(SaleTransactionData( 
            config[section]['card_number'],
            config[section]['cvv'],
            config[section]['expiration_date'],
            config[section]['amount'],
            config[section]['usage'], 
            'sale', 
            config[section]['card_holder'], 
            config[section]['email'], 
            config[section]['address'], 
            config[section]['auth'],
            config[section]['url'],
            config[section]['testId'],
            config[section]['expectedStatusCode']
            ))
    return TransactionsArray , saleVoidTransactionsArray, saleVoidVoidTransactionsArray #return the arrays of objects