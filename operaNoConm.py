import threading
import time
import logging

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)

varIni = 10
lock = threading.Lock()
auxLock = threading.Lock()

def setValorInicial(valor):
    global varIni
    varIni = valor

def sumarUno():
    global varIni
    global lock
    try:
        varIni += 1
    finally:
        lock.release()


def multiplicarPorDos():
    global varIni
    global lock

    lock.acquire()
    
    try:
        varIni *=2
    finally:
        lock.release()






def dividirPorDos():
    global varIni
    global lock
    
    try:
        varIni /=2
    finally:
        lock.release()

def toString():
    print(f"El resultado es: {varIni}")





def main():
    threadParaSumar = threading.Thread(target=sumarUno)
    threadParaMultiplicar = threading.Thread(target=multiplicarPorDos)

    lock.acquire()

    
    threadParaSumar.start()    
    threadParaMultiplicar.start()
    threadParaMultiplicar.join()

    toString()



if __name__ == '__main__':
    main()