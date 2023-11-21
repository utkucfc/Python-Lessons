# -*- coding: utf-8 -*-

import json

data = '{"firstName":"utku","lastName":"CIFCI"}'

y = json.loads(data)

print(y["firstName"])
print(y["lastName"])

customer = {
    "firstName":"utku",
    "email":"utku.cifci@gmail.com"
    }

customerJson = json.dumps(customer)
print(customer)
print(json.dumps("utku"))