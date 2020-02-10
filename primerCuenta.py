import threading
import time
from operaNoConm import *

resultado = 0
varIni = 3
lock = threading.Lock()
firstPart = threading.Thread(target=sumarUno)
secondPar = threading.Thread()


def laCuenta():
    global varIni
    global lock
    #time.sleep(0)
    try:
        lock.acquire()
        firstPart()    
    finally:
        lock.release()
    

    
