print("sathish kumar")
"""print("sathish R")
print("BTECH")
print("BTECH")
print("BTECH")
print("BTECH")"""
#local variable
age1,age2,age3="45","35","90"
max=min=medium=50
Age="50"
age1=34
name="s"
print(type(name))
fristname=7
lastname="kumar"
print(str(fristname)+lastname)
"""totalage=int(age)+age1
print(type(age))
print(type(age1))
print(totalage)"""

print("sathish \n kumar")
print("sathish \t kumar")
#function
#1.function with out parameter /arguments
#2.function with  parameter /arguments
#3.function with out return type
#4.function with  returntype

"""def add():
    a=10 #local variable
    b=20
    c=a+b
    print(c)"""
#2.function with  parameter /arguments
"""def add(a,b):
    c=a+b
    print(c)"""
global a
a=60

def add(a,b):
    c=a+b
    return c

d=add(10,25)
print("sum of the valus is:"+str(d))

def sub():
    a=30.3456
    b=20.4567
    c=b-a
    print(round(c, 2))
    print(c)

    print("The global variable is: "+str(a))
    print("sub of 2 numbr is: "+str(c))

def mul():
    #a=50
    b=20
    b+=2
    c=b*a
    print(type(c<100))
    print("The global variable is: " + str(a))
    print("Mul of 2 value is: "+str(c))

def voterid(age):
    if (age>18):
        print("You are eligible")
        if(age==60) and (age>60):
            print("You are eligible for senior citizen")
            if (age > 80):
                print("You are eligible for super senior citizen")
            else:
                print("You are not eligible for senior citizen")
    elif(age>15):
        print("you are greater than 15")
    elif (age > 12):
        print("you are greater than 12")
    elif (age > 10):
        print("you are greater than 10")
    else:
        print("you are not eligible")
    print("NO")

global temp
temp=0.00
def addproduct(product,quantity,price):
    global temp
    result=quantity*price
    print(product+" "+str(quantity)+" "+str(result))
    temp+=result

def whileloop(i):
    while(i<10):
        print(i)

"""addproduct("iphone",2,5.5)
addproduct("samsung",2,5.5)
print(temp)"""
whileloop(3)
#sub()
#mul()
#voterid(55)
