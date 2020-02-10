import threading
import logging
import time

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)
sema = threading.Lock()
posActual = 0

def agregarPares(lista):
    global posActual

    for posActual in range(10):
        try:
            sema.acquire()
            lista.append(2 * posActual)
            time.sleep(0.1)
        finally:
            sema.release()
    
def agregarImpares(lista):
    global posActual
    
    for posActual in range(10):
        try:
            sema.acquire()
            lista.append(2 * posActual + 1)
        finally:
            sema.release()

lista = []

t1 = threading.Thread(target=agregarPares, args=[lista])
t2 = threading.Thread(target=agregarImpares, args=[lista])

t1.start()
t1.join()
t2.start()
t2.join()

print(lista)


#Pone primero los pares y despues los impares.(valores reducidos para que quede mas explicito)
#Una posible solucion seria hacer un append asincronico de ambas listas a la lista final que se quiere -
# imprimir para poder tener los valores intercalados. Creo que se podria lograr con una variable compartida 