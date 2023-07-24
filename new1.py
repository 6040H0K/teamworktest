from math import sqrt
def quadratic_equation(a,b,c):
    x1 = None
    x2 = None
    no_rezult = ''
    def calc_rezult(a,b,c):
        return b**2-4*a*c
    d = calc_rezult(a,b,c)    
    if d >= 0:
        x1 = -b - (sqrt(d))/2*a
        x2 = -b + (sqrt(d))/2*a        
    else:
        no_rezult = ("Розв'язків немає")  
    return (x1,x2,no_rezult)  
a = float(input("Введіть a"))
b = float(input("Введіть b"))
c = float(input("Введіть c"))
print(quadratic_equation(a,b,c))