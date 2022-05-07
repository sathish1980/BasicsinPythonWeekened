class loopsclass:

    def __init__(self): #constructor with out parameter
        print("Beasant Technologies")

    def __init__(self,i,j):  #constructor with parameter
        print("Beasant Technologies with parameters")
    def forloopconcept(i=10):
        name=["sathish","kumar","R","B.tech"]
        rank=[2,4,5,3,6,7]
        """for x in name:
            print(x)"""

        for num in range(6):
            print(rank[num])
            for x in name:
                print(x)

objname=loopsclass(2,3)
objname.forloopconcept()  # function call