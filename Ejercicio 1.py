archivo = "LibroCuentas.txt"

def LeerDocumento():
    """funcion que lee la informacion de un fichero, y la 
    guarda en una lista
    
    - Parametros: 
        - La entrada es la ruta del fichero a leer
        
    - Salida:
        - devuelve una lista con los datos del fichero
        
    """
    with open(archivo, "r") as file:
        
        listaDatos = file.readlines()
        
        morosos = [line.strip() for line in listaDatos if "PAGADO" in line]

    return str(morosos)
x = LeerDocumento()

LeerDocumento()

def IdentificarPagado():
    
    f = open("PAGADO.txt")
    with open(f, "w") as file:
        
        z = file.write(x)

IdentificarPagado()
