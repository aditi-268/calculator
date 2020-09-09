# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 18:55:13 2020

@author: ADITI
"""

class calculator:
    def sum(self,x,y):
       print("add",(x+y))
       return(x+y)
        
    def sub(self,x,y):
         print("sub",(x-y))
         return(x-y)
       
    def mul(self,x,y):
        print("mul",(x*y))
        return(x*y)
    
    def div(self,x,y):
         print("div",(x/y))
         return(x/y)
       
cal=calculator()
print(cal.sum(10,2))
print(cal.sub(10,2))
print(cal.mul(10,2))
print(cal.div(10,2))
    
        
    