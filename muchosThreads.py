import threading
import time
import logging
from tiempo import Contador
from definiciones import UnThread


logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)

# la función para usar para el thread
def dormir():
    time.sleep(1)

contador =  Contador()

contador.iniciar()
listonga = []
for i in range(10):
    i = UnThread()
    i.start()
    listonga.append(i)

for i in listonga:
    i.join()

contador.finalizar()
contador.imprimir()
    
