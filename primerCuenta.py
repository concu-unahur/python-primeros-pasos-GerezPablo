import threading
from operaNoConm import *

lock = threading.Lock()
plusOne = threading.Thread(target=sumarUno)
divideByTwo = threading.Thread(target=dividirPorDos)

starting = threading.Thread(target=setValorInicial, args=[0])
starting.start()

plusOne.start()
divideByTwo.start()
for i in range(3):
    i = threading.Thread(target=sumarUno)
    i.start()

toString()



    

    
