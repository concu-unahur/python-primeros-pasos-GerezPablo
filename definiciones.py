import threading
import time
import logging

class UnThread(threading.Thread):
    def __init__(self):
        super().__init__() 
        self.name = 'threadClase'

    def run(self):
        logging.info('Empezando')
        time.sleep(1)
        logging.info('Finalizado')
    
    def dormir(tiempo):
        logging.info('Empenzado')
        time.sleep(tiempo)
        logging.info('Finalizado')



