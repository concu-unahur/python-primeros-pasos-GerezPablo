import threading
import time
import logging

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)

varIni = 10
lock = threading.Lock()
def sumarUno():
    global varIni
    global lock
    #time.sleep(0)
    try:
        lock.acquire()
        varIni +=1
    finally:
        lock.release()

def multiplicarPorDos():
    global varIni
    global lock
    #time.sleep(0)
    try:
        lock.acquire()
        varIni *=2
    finally:
        lock.release()



def varIni():
    print(f"El resultado es: {varIni}")

threadParaSumar = threading.Thread(target=sumarUno)
threadParaMultiplicar = threading.Thread(target=multiplicarPorDos)

threadParaSumar.start()

threadParaMultiplicar.start()

varIni()


