import threading
from operaNoConm import *
import primerCuenta

start = threading.Thread(target=setValorInicial, arg= [primerCuenta])

dividePerTwo= threading.Thread(target=dividirPorDos)

dividePerTwo.start()
toString()