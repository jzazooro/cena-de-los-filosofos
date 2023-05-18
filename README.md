# cena-de-los-filosofos


El enlace al repositorio de GitHub de este proyecto es el siguiente: [GitHub](https://github.com/jzazooro/cena-de-los-filosofos.git)

He resuelto el ejercicio de los filosofos cenando

### main

```
from lanzador import main

if __name__ == '__main__':
    main()
```

### lanzador

```
from clases. filosofos import *
import tkinter
import sys

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
```

### clases (filosofos)

```
import threading
import time
import random

class Filosofo(threading.Thread):
    semaforo = threading.Lock()

    def __init__(self, nombre, tenedorIzq, tenedorDer):
        threading.Thread.__init__(self)
        self.name = nombre
        self.tenedorIzq = tenedorIzq
        self.tenedorDer = tenedorDer
        self.comidas=0
    
    def pensar(self):
        self.semaforo.acquire()
        print(self.name, 'ahora esta pensando')
        time.sleep(random.uniform(0.2,2))
        self.semaforo.release()

    def comer(self):
        self.semaforo.acquire()
        self.tenedorDer.acquire()
        print(self.name, 'tiene el tenedor derecho')
        self.tenedorIzq.acquire()
        print(self.name, 'tiene el tenedor izquierdo')
        self.comidas+=1
        print(self.name, 'tiene los dos tenedores y esta comiendo')
        time.sleep(random.uniform(0.1,3))
        print(self.name, 'termino de comer')
        self.tenedorDer.release()
        self.tenedorIzq.release()
        self.semaforo.release()

    def run(self):
        while self.comidas<3:
            self.pensar()
            self.comer()
        else:
            print(self.nombre, 'ya comio 3 veces y se va a dormir')
```

### clases(interfaz)

```
import tkinter
import sys
ventana=tkinter.Tk()
canvas=tkinter.Canvas(bg="black", width=800, height=600)
    
canvas.create_rectangle(100, 50, 200, 100, fill="black")
canvas.create_rectangle(25, 125, 125, 175, fill="green")
canvas.create_rectangle(50, 200, 150, 250, fill="blue")
canvas.create_rectangle(275, 175, 175, 225, fill="red")
canvas.create_rectangle(200, 160, 300, 110, fill="pink")
canvas.create_text(150, 75, text="Filosofo 1")
canvas.create_text(75, 150, text="Filosofo 2")
canvas.create_text(100, 225, text="Filosofo 3")
canvas.create_text(225, 200, text="Filosofo 4")
canvas.create_text(250, 135, text="Filosofo 5")
    
canvas.create_rectangle(60, 80, 80, 100, fill="black")
canvas.create_rectangle(20, 200, 40, 220, fill="green")
canvas.create_rectangle(220, 80, 240, 100, fill="blue")
canvas.create_rectangle(290, 180, 310, 200, fill="red")
canvas.create_rectangle(170, 240, 190, 260, fill="pink")
    
canvas.pack()
    
ejecutar=tkinter.Button(canvas, text="Ejecutar")
ejecutar.place(x=100, y=300)
    
salir=tkinter.Button(canvas, text="Salir", command=sys.exit)
salir.place(x=200, y=300)
    
ventana.mainloop
```
