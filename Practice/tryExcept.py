# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 16:42:42 2023

@author: Admin
"""
import sys
list1 = [5,"AAA",0,10,"6"]

for data in list1:
    try:
        print("Number: " + str(data))
        res = 1/int(data)
        print("Result = "+ str(res))
    except ValueError:
        print(str(data) + " is not a number.")
    # except ZeroDivisionError:
    #     print(str(data) + " can not divide by zero.")
    except:
        print(str(data) + " can not calculated.")
        print("Exception is: " + str(sys.exc_info()[0]))
    finally:
        print("Calculation is finished.")