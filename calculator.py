class Calculator():
    def add(self , x , y):
        return(x+y)
    def substruct(self , x , y):
        return(x-y)
    def multyply(self , x , y):
        return(x*y)
    def divid(self , x , y):
        return(x/y)
cal = Calculator()
adding = cal.add(40,30)
minus = cal.substruct(70,20)
multi = cal.multyply(5,7)
division = cal.divid(80,20)
print("Sum is:" ,adding)
print("substructed value:" , minus)
print("multiplication numer is:" , multi)
print("result:" , division)