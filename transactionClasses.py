#transaction classes 

class SaleTransactionData: #class for the sale transaction
    def __init__(self, card_number, cvv, expiration_date, amount, usage, transaction_type, card_holder, email, address, auth, url, testId, expectedStatusCode):
        self.card_number=card_number,
        self.cvv=cvv,
        self.expiration_date=expiration_date,
        self.amount=amount,
        self.usage=usage,
        self.transaction_type=transaction_type,
        self.card_holder=card_holder,
        self.email=email,
        self.address=address
        self.auth=auth
        self.url=url
        self.testId=testId
        self.expectedStatusCode=expectedStatusCode

class VoidTransactionData: #class for the void transaction
    def __init__(self, reference_id, auth, url, testId,expectedStatusCode, transaction_type="void"):
        self.reference_id=reference_id,
        self.transaction_type=transaction_type,
        self.auth=auth
        self.url=url
        self.testId=testId
        self.expectedStatusCode=expectedStatusCode
