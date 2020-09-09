# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 15:53:56 2020

@author: ADITI
"""



#program to make simple calculator


#this function add two numbers
def add(x,y):
    return x+y
#this function subtact two numbers
def subtract (x,y):
    return x-y
#this function two numbers
def multiply (x,y):
    return x*y
#this function  two numbers
def divide(x,y):
    return x/y
print("select operation")
print("1.Add")
print("2.Subtaction")
print("3.Multiply")
print("4.Divide")
while True:
    #take unput from the user
    choice=input("enter choice(1/2/3/4)")
    
#check if choice is in one of the  four options
    if choice in ('1','2','3','4'):
        num1=float(input("enter the first number"))
        num2=float(input("enter the second number"))
  
        if  choice=='1':
             print(num1,"+",num2,"=",add(num1,num2))
          
        elif choice=='2':
             print(num1,"-",num2,"=",subtract(num1,num2))
 
        elif choice=='3':
             print(num1,"*",num2,"=",multiply(num1,num2))               
      
        elif choice=='4':
             print(num1,"/",num2,"=",divide(num1,num2))
        break  
      
      
    else:
      print("invalid input")
     
