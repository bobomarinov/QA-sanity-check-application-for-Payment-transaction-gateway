
# Purpose

  

This is sanity checks application for https://github.com/eMerchantPay/codemonsters_api_full

## Setting up test data

  

Test data/transaction data should be added in test.ini file:

  

4 types of transactions can be added:

  

 - sale transaction
 - void trsanaction:
 - saleVoid transaction
 - saleVoidVoid transaction


Example of sale transaction:
```ini

[t1]

transaction_type = sale

card_number = 4200000000000000

cvv = 321

expiration_date = 06/2025

amount = 300

usage = Ship

card_holder = George Lucas

email = george@lucas.com

address = Desert Street 12, Tatooine

auth = Basic Y29kZW1vbnN0ZXI6bXk1ZWNyZXQta2V5Mm8ybw==

url = http://localhost:3001/payment_transactions

testId = 1

expectedStatusCode = 200

```
When creating test data **sale**,**saleVoid** and **saleVoidVoid** transactions require the same paramteres mentioned above. The **void** stransaction requiers the following parameters:
```ini
[t2]

transaction_type = void

reference_id = 1234

auth = Basic Y29kZW1vbnN0ZXI6bXk1ZWNyZXQta2V5Mm8ybw==

url = http://localhost:3001/payment_transactions

testId = 2

expectedStatusCode = 422
```
## Executing tests

  

To execute the test just type the following

  

```bash

pytest

```