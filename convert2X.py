n= int(input("numero entero? "))
q=n
r=n%2
print(r)
while n > 1:
    n = n//2
    r = n%2
    print (r)
print ("el número binario se lee de abajo hacia arriba")

r=q%16
if r < 10: 
    print (r)
elif r == 10:
    print ("A")
elif r == 11:
    print ("B")
elif r == 12:
    print ("C")
elif r == 13:
    print ("D")
elif r == 14:
    print ("E")
elif r == 15:
    print ("F")
while q>1:
    q=q//16
    r=q%16
    if r < 10: 
        print (r)
    elif r == 10:
        print ("A")
    elif r == 11:
        print ("B")
    elif r == 12:
        print ("C")
    elif r == 13:
        print ("D")
    elif r == 14:
        print ("E")
    elif r == 15:
        print ("F")
print ("el numero Hexadecimal se lee de abajo hacia arriba")
    
        

    




    
