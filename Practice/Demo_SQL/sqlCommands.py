# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 15:26:37 2023

@author: Admin
"""

import sqlite3

def selectCustomer():
    
    connection = sqlite3.connect("chinook.db")
    # cursor = connection.execute("""
    #                             SELECT firstname,lastname
    #                             FROM customers
    #                             ORDER BY firstname, lastname asc
    #                             """)
    # for data in cursor:
    #     print("Name: "+data[0] + " "+data[1])
    
    
    
    
    # cursor = connection.execute("""
    #                             SELECT city, count(*)
    #                             FROM customers
    #                             GROUP BY city
    #                             ORDER BY count(*) asc
    #                             """)
    # for data in cursor:
    #     print("Name: "+data[0] + " "+str(data[1]))
    
    
    
    
    cursor = connection.execute("""
                                SELECT firstname,lastname
                                FROM customers
                                WHERE firstname LIKE 'e%'
                                ORDER BY firstname, lastname asc
                                """)
    for data in cursor:
        print("Name: "+data[0] + " "+data[1])
    connection.close()

selectCustomer()


def insertCustomer():
    connection = sqlite3.connect("chinook.db")
    connection.execute("""
                       INSERT INTO customers (firstName,lastName,email,city)
                       values ('Utku','Cifci','utku.cifci@gmail.com','Ankara')
                       """)
    connection.commit()
    connection.close()

# insertCustomer()


def updateCustomer():
    connection = sqlite3.connect("chinook.db")
    connection.execute("""
                       UPDATE customers
                       SET city='İstanbul'
                       WHERE city='Ankara'
                       """)
    connection.commit()
    connection.close()

# updateCustomer()


def deleteCustomer():
    connection = sqlite3.connect("chinook.db")
    connection.execute("""
                       DELETE FROM customers
                       WHERE city='İstanbul'
                       """)
    connection.commit()
    connection.close()

# deleteCustomer()



def joinCustomer():
    
    connection = sqlite3.connect("chinook.db")
    cursor = connection.execute("""
                       SELECT artists.Name,albums.Title
                       FROM artists 
                       INNER JOIN albums on artists.ArtistId = albums.ArtistId
                       ORDER BY artists.Name asc
                       """)
                       
    for data in cursor:
        print("Name: "+data[0] + " Title: "+data[1])
    connection.commit()
    connection.close()
    
joinCustomer()







