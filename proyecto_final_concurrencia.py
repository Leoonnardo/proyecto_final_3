from os import name
import time
from threading import *
from collections import deque
import threading
import random
from PyQt5 import uic
from PyQt5.QtWidgets import QAbstractItemView, QMainWindow, QApplication, QTableWidgetItem, QDialog
import sys
from PyQt5.QtGui import QPixmap
quiet = Lock()


marcaLanzadores = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
distanciaFinal = [0,0,0,0]

vueltas = 0

class index(QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi("main.ui", self)
        
        self.botonIniciar.clicked.connect(lambda:self.arranque())

    def arranque(self):
        lanzador1 = Thread(name='1',target=self.accion, args=())
        lanzador1.start()

        lanzador2 = Thread(name='2',target=self.accion, args=())
        lanzador2.start()

        lanzador3 = Thread(name='3',target=self.accion, args=())
        lanzador3.start()

        lanzador4 = Thread(name='4',target=self.accion, args=())
        lanzador4.start()
    
    def accion(self):
        vueltas = 0
        fork = deque()
        forks = fork.copy()
        for i in range(0, 3): 
            forks.append(i)
        current = threading.current_thread().getName()
        numeroLanzador = int(current)
        for i in range(0,3):
            while True:
                # print('Lanzador #', current, 'Listo.')
                time.sleep(2)
                quiet.acquire()
                if len(forks) != 0:
                    vueltas = vueltas+1
                    print(vueltas)
                    if int(current) == 1:
                        self.lanza1.setText(str('Lanzador '+current+' preparandoce'))
                    elif int(current) == 2:
                        self.lanza2.setText(str('Lanzador '+current+' preparandoce'))
                    elif int(current) == 3:
                        self.lanza3.setText(str('Lanzador '+current+' preparandoce'))
                    elif int(current) == 4:
                        self.lanza4.setText(str('Lanzador '+current+' preparandoce'))    
                    print('\nLanzador #', current, 'Preparandoce')
                    time.sleep(1)
                    fork.append(forks.pop())
                    fork.append(forks.pop())
                try:
                    if len(fork)==2:
                        if int(current) == 1:
                            self.lanza1.setText(str('Lanzador '+current+' ejecuta lanzamiento'))
                        elif int(current) == 2:
                            self.lanza2.setText(str('Lanzador '+current+' ejecuta lanzamiento'))
                        elif int(current) == 3:
                            self.lanza3.setText(str('Lanzador '+current+' ejecuta lanzamiento'))
                        elif int(current) == 4:
                            self.lanza4.setText(str('Lanzador '+current+' ejecuta lanzamiento'))
                        print('Lanzador #', current, 'Ejecuta lanzamiento')   
                        time.sleep(1) 
                        forks.append(fork.pop())
                        forks.append(fork.pop())
                finally:
                    numero = self.distancia()
                    marcaLanzadores[numeroLanzador-1][i] = numero
                    if int(current) == 1:
                        self.lanza1.setText(str('Lanzador '+current+' esperando'))
                    elif int(current) == 2:
                        self.lanza2.setText(str('Lanzador '+current+' esperando'))
                    elif int(current) == 3:
                        self.lanza3.setText(str('Lanzador '+current+' esperando'))
                    elif int(current) == 4:
                        self.lanza4.setText(str('Lanzador '+current+' esperando'))
                    print('Lanzador #', current, 'Su distancia fue: ', numero)
                    mejorDistancia = self.mejorMarca(numeroLanzador-1)
                    print('Mejor marca del lanzador #', current, 'Es: ', mejorDistancia)       
                    time.sleep(1)
                    quiet.release()
                    if vueltas == 1:
                        if int(current) == 1:
                            self.ls11.setText(str(numero))
                            self.ls14.setText(str(mejorDistancia))
                            distanciaFinal[0] = mejorDistancia
                        elif int(current) == 2:
                            self.ls21.setText(str(numero))
                            self.ls24.setText(str(mejorDistancia))
                            distanciaFinal[1] = mejorDistancia
                        elif int(current) == 3:
                            self.ls31.setText(str(numero))
                            self.ls34.setText(str(mejorDistancia))
                            distanciaFinal[2] = mejorDistancia
                        elif int(current) == 4:
                            self.ls41.setText(str(numero))
                            self.ls44.setText(str(mejorDistancia))
                            distanciaFinal[3] = mejorDistancia
                    if vueltas == 2:
                        if int(current) == 1:
                            self.ls12.setText(str(numero))
                            self.ls14.setText(str(mejorDistancia))
                            distanciaFinal[0] = mejorDistancia
                        elif int(current) == 2:
                            self.ls22.setText(str(numero))
                            self.ls24.setText(str(mejorDistancia))
                            distanciaFinal[1] = mejorDistancia
                        elif int(current) == 3:
                            self.ls32.setText(str(numero))
                            self.ls34.setText(str(mejorDistancia))
                            distanciaFinal[2] = mejorDistancia
                        elif int(current) == 4:
                            self.ls42.setText(str(numero))
                            self.ls44.setText(str(mejorDistancia))
                            distanciaFinal[3] = mejorDistancia
                    if vueltas == 3:
                        if int(current) == 1:
                            self.ls13.setText(str(numero))
                            self.ls14.setText(str(mejorDistancia))
                            distanciaFinal[0] = mejorDistancia
                        elif int(current) == 2:
                            self.ls23.setText(str(numero))
                            self.ls24.setText(str(mejorDistancia))
                            distanciaFinal[1] = mejorDistancia
                        elif int(current) == 3:
                            self.ls33.setText(str(numero))
                            self.ls34.setText(str(mejorDistancia))
                            distanciaFinal[2] = mejorDistancia
                        elif int(current) == 4:
                            self.ls43.setText(str(numero))
                            self.ls44.setText(str(mejorDistancia))
                            distanciaFinal[3] = mejorDistancia
                    break
        if vueltas == 3:
            print("Mejor :",mejorDistancia)

    def distancia(self):
        numero = random.randint(1, 25)
        return numero

    def mejorMarca(self, posicion):
        comparar = marcaLanzadores[posicion][0]
    
        for i in range(0, 3):
            if marcaLanzadores[posicion][i] >= comparar:
                comparar = marcaLanzadores[posicion][i]
        return comparar

    def mejorMarcaFinal(self):
        comparar = [distanciaFinal[0], ""]
        for i in range(0, 3):
            if distanciaFinal[i] >= comparar[0]:
                comparar[0] = distanciaFinal[i]
                comparar[1] = "Lanzador i"
        return comparar


def vista():
    app = QApplication(sys.argv)
    GUI = index()
    GUI.show()
    
    sys.exit(app.exec_())
    
    

if __name__ == '__main__':

    vista()
