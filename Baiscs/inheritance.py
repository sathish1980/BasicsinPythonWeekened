from Baiscs.Exceptionhandling import excp


class inheritance(excp):
    def multiplication(self,a,b):
        mul=a*b
        print("This is multiply of 2 number: "+str(mul))

obj=inheritance()
obj.allmethod(6,2)
obj.multiplication(3,5)
