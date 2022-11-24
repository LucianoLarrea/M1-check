class Nodo():
    def __init__(self, dato):
        self.__dato = dato
        self.__siguiente = None

    def getDato(self):
        return self.__dato

    def getSiguiente(self):
        return self.__siguiente

    def setDato(self, val):
        self.__dato = val

    def setSiguiente(self, val):
        self.__siguiente = val

class Lista():
    def __init__(self):
        self.__cabecera = None

    def agregarElemento(self,dato):
        if (self.__cabecera != None):
            puntero = self.__cabecera
            while(puntero != None):
                if(puntero.getSiguiente() == None):
                    puntero.setSiguiente(Nodo(dato))
                    break
                puntero = puntero.getSiguiente()
        else:
            self.__cabecera = Nodo(dato)

    def contarElementos(self):
        if (self.__cabecera == None):
            return 0
        else:
            contador = 1
            puntero = self.__cabecera
            while(puntero.getSiguiente() != None):
                contador += 1
                puntero = puntero.getSiguiente()
            return contador

    def getCabecera(self):
        return self.__cabecera