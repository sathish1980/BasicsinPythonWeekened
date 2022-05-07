from Baiscs.Exceptionhandling import excp
from Baiscs.inheritance import inheritance


class multilevel(inheritance,excp):
    def multi(self):
        print("This is multilievel example")

mul=multilevel()
mul.multi()
mul.allmethod(2,3)
mul.multiplication(3,9)
