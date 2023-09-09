from ast import If
from time import sleep
import mysql.connector

def save_expense(details):
    sql="insert into details(expensename,amount,name) values(%s,%s,%s)"
    data=(details["expense_name"],details["amount"],details["date"])
    mydb.commit()

print("1.Add new expense")
print("2.View all expenses")
print("3.delete expense")
print("4.modify expense")

selected_option=int(input("select option : "))

if selected_option==1: 
    # reading the inputs
    expensename=input("Expense name : " )
    amount=input("Amount : ")
    amount=float(amount)

    #creating the expense object
    new_expense={}
    new_expense["expense_name"]=expensename
    new_expense["amount"]=amount

    # connect to database
    mydb=mysql.connector.connect(
        host="localhost",
        user="root",
        password="Gshock@123",
        database="expense_tracker"

    )
    mycursor=mydb.cursor()  

    #save new expense to database
    insert_query="insert into expenses(name,amount) values(%s,%s)"

    data=(new_expense["expense_name"],new_expense["amount"])
    mycursor.execute(insert_query,data)
    mydb.commit()





     