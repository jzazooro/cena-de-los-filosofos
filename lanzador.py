from clases. filosofos import *

def main():
    tenedores = []
    for i in range(5):
        tenedores.append(threading.Lock())
    filosofos = []

    filosofo1=Filosofo('Socrates', tenedores[0], tenedores[4])
    filosofo2=Filosofo('Platon', tenedores[1], tenedores[2])
    filosofo3=Filosofo('Aristoteles', tenedores[2], tenedores[3])
    filosofo4=Filosofo('Descartes', tenedores[3], tenedores[4])
    filosofo5=Filosofo('Kant', tenedores[4], tenedores[0])

    filosofos.append(filosofo1)
    filosofos.append(filosofo2)
    filosofos.append(filosofo3)
    filosofos.append(filosofo4)
    filosofos.append(filosofo5)

    for filosofo in filosofos:
        filosofo.start()