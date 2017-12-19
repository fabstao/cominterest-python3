#!/usr/bin/env python3
# *********************
# Fabian Salamanca 2017
# Interés Compuesto
# Compund Interest
# *********************

import math

class Credito:

    def __init__(self, ci, n, intanual):
        self.ci = float(ci)
        self.intanual = float(intanual)
        self.n = int(n)
        self.cf = 0
        self.mens = 0
        print("Initial capital : ${0:.2f}".format(self.ci))
        print("Anual interest : %{0:.2f}".format(self.intanual))
        print("Period : {}".format(self.n))
        print("")
        
    def __calcular(self):
        # Calculate final capital
        self.cf = self.ci * math.pow(1+(self.intanual /(12*100)),self.n)
        self.mens = self.cf/self.n

    def printDetails(self):
    	
    	self.__calcular()
    	if(self.cf > 0):
            vcf = self.cf
            for i in range(self.n):
                vcf-=self.mens 
                print("Monthly = ${0:.2f} | Pending capital = ${1:.2f}".format(self.mens, vcf))
                
        
class Cliente:
	
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("__________")
        print(" CUSTOMER")
        print("----------")
        print("Name: "+self.name+", age: "+self.age)
        print("")

# Main

print("=========================")
print("COMPOUND INTEREST EXAMPLE")
print("=========================")
print("")

name = input("Please input full name: ")
age = input("Please input your age: ")

ci = input("Initial capital: ")
ci = ci.strip()
intanual = input("Annual interest (only numbers): ")
intanual = intanual.strip()
n = input("Period in months please: ")
n = n.strip()

cliente = Cliente(name,age)

cred = Credito(ci, n, intanual)
cred.printDetails()
