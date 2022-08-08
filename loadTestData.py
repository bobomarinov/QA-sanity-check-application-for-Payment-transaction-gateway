import configparser
from transactionClasses import *

def LoadData():
    config = configparser.ConfigParser()
    config.sections()
    config.read('test.ini')
    TransactionsArray = []
    saleVoidTransactionsArray = []
    saleVoidVoidTransactionsArray = []


    for section in config.sections():
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
        elif (config[section]['transaction_type'] == 'void'):
            TransactionsArray.append(VoidTransactionData( 
            config[section]['reference_id'],
            config[section]['auth'],
            config[section]['url'],
            config[section]['testId'], 
            config[section]['expectedStatusCode'],
            config[section]['transaction_type'],
            ))
        elif(config[section]['transaction_type'] == 'saleVoid'):
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
        elif(config[section]['transaction_type'] == 'saleVoidVoid'):
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
    return TransactionsArray , saleVoidTransactionsArray, saleVoidVoidTransactionsArray