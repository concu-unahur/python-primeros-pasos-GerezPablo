import threading
from operaNoConm import *

lock = threading.Lock()
plusOne = threading.Thread(target=sumarUno)
divideByTwo = threading.Thread(target=dividirPorDos)

starting = threading.Thread(target=setValorInicial, args=[3])
starting.start()

divideByTwo.start()
plusOne.start()

toString()