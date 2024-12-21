
def fact(n):
    f = 1
    for i in range(1, n +1 ):
        f = f*i

    return f


#způsob jak zjistit faktorial, proměnná x = číslo
x = 5

# funkce je přirazena k proměnná result a ta je pak vytištěna
result = fact(x)
print(result)

#druhá možnost je udělat print funkce s parametrem
print(fact(5))