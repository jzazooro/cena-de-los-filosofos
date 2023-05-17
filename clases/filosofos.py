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