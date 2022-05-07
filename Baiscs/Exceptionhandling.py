class excp():
    listvalue=[1,2,3]
    def divide(self,a,b):
        try:
           # val=self.listvalue[2]
            #print(val)
            div = a / b
            print(div)
            if div>5.0:
                print("Valid value")
            else:
                raise Exception()
        except ZeroDivisionError:
            print("This is divided by zero error")
        except IndexError:
            print("You are it profession")
        except :
            print("An error occurred")
        finally:
            print("this is finally block")
    def addition(self,a,b):
        try:
            add=a+b
            print("The addition of 2 number is : "+str(add))
        except:
            pass
    def subtraction(self,a,b):
        try:
            sub=a-b
            print("The sub of 2 number is : " + str(sub))
        except:
            pass
    def allmethod(self,a,b):
        self.addition(a,b)
        self.divide(a,b)
        self.subtraction(a,b)

obj2=excp()
obj2.divide(2,3)
obj2.subtraction(4,5)