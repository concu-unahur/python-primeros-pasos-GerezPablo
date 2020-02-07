import threading
import time
import logging

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)

def dormir():
    time.sleep()

t1 = threading.Thread(target=dormir, name= "Thread desde funcion")
t1.start()

class UnThread(threading.Thread):
    def __init__(self):
        super().__init__()
        self.name = "Thread Clase"

    def run(self):
        logging.info("Empezando desde clase")
        time.sleep()
        logging.info("Finalizando desde clase")