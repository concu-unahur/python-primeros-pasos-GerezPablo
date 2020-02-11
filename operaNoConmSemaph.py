import threading
import time
import logging

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)

varIni = 10
sema = threading.Semaphore(1)


def setValorInicial(valor):
    global varIni
    varIni = valor



def sumarUno():
    global varIni
    global sema

    sema.acquire()
    try:
        varIni += 1
    finally:
        sema.release()


def multiplicarPorDos():
    global varIni
    global sema

    sema.acquire()
    try: 
        varIni *=2
    finally:
        
        sema.release()

def toString():
    print(f"El resultado es: {varIni}")


def main():
    threadParaSumar = threading.Thread(target=sumarUno)
    threadParaMultiplicar = threading.Thread(target=multiplicarPorDos)
    


    threadParaMultiplicar.start()
    threadParaSumar.start()        

    threadParaMultiplicar.join()

    toString()



if __name__ == '__main__':
    main()