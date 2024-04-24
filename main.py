from insert import *
from delete import *
from update import *
from select_1 import *
from aggregate import *
from sort import *
from join import *
from group import *
from sub import *
from transaction import *


#print statement for interface and then if statements for the input

print("Welcome to the Database CLI Interface\n")
print("Please Select an Option:")
print("1.Insert Data")
print("2.Delete Data")
print("3.Update Data")
print("4.Search Data")
print("5.Aggregate Functions")
print("6.Sorting")
print("7.Joins")
print("8.Grouping")
print("9.Subqueries")
print("10.Transactions")
print("11.Exit")
i = input("Enter your choice (1-11): ")

#insert
if i == "1":
   insertpg()

#delete
if i == "2":            
    deletepg()  

#update           
if i == "3":            
    updatepg()

#search            
if i == "4":            
    selectpg()
    
#aggregate
if i == "5":            
    aggregatepg()

#sort
if i == "6":            
    sortpg()

#join
if i == "7":  
    joinpg()

#grouping
if i == "8":            
    grouppg()

#subqueries
if i == "9":            
    subpg()

#transaction
if i == "10":
    transactionpg()
    
#exit
if i == "11":
    exit(1)

