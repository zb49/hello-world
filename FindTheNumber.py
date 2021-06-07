from random import randint
salir = input('introduce la letra "e" para empezar ')
while salir !='y':
    n = int(input("¿Número entre 1 y 30? "))
    p = randint(1,30)
    if n > p: 
        print ("tu numero es mayor")
    else:
        if n==p:
            print ("*****Atinaste al número*****")
        else:
            print ("tu numero es menor")
        
    print (n,"es tu número")
    print (p,"es mi número")
    print (" ")
    salir = input('para salir presione "y", para continuar, cualquiera otra letra ')

  
    
    
    
