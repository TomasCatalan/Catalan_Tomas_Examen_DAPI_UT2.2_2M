import csv
import cProfile

def letraDNI(dni):
    secuencia = "TRWAGMYFPDXBNJZSQVHLCKE"
    return secuencia[int(dni) % 23]

def leer_fichero(fichero):
    with open(fichero, 'r') as csvfile:

        leer = csv.DictReader(csvfile)
        for i in leer:
            y = str(i)
            x = y.split("\t")
            nombre = x[0].capitalize()
        
            dni = x[1]
            letra = letraDNI(dni)
            print(letra)


leer_fichero("50.csv")

            