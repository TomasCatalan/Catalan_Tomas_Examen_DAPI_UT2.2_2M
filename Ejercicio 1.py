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
        
        morosos = [line.strip() for line in 
                   listaDatos if "PAGADO" in line]

    return (morosos)
x = LeerDocumento()

LeerDocumento()

def IdentificarPagado():
    """funcion que crea un fichero en el que se escriben 
    todas las lineas en las que aparezca la palabra pagado
    
    - Parametros:
        - Recibe una lista
        
    - Salida:
        - La funcion no devuelve nada"""
    
    f = ("PAGADO.txt")

    y = str(x)
    with open(f, "w") as file:
        
        z = file.write(y)

IdentificarPagado()
