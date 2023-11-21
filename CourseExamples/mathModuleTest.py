# -*- coding: utf-8 -*-

import mathModule

mathModule.multiply(2, 3)
mathModule.total(5, 3) 
print(mathModule.customer["firstName"])

#renaming
import mathModule as mm

mm.multiply(2, 3)
mm.total(5, 3) 
print(mm.customer["lastName"])

from mathModule import multiply
multiply(2, 12)

from mathModule import customer
print(customer["firstName"])