corredor = {}
q = 1   

while q == 1:
    try:
        hora = input("A que hora ha pasado")
        km = int(input("Por que km va, introducir fin si acabo la carrera"))
        corredor[hora] = km

    except ValueError:
        for i in corredor:
            x = corredor[i]
            print("A las", i, "estaba en el km", x)  
        q = q + 1  


    
