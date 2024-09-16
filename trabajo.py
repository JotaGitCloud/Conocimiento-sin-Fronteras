#Este seria el metodo que utilizaremos para tener una lista de espera a la hora de enmarcar los procesos de pintura, para así poder enviar varios pedidos simultaneamente

class NS:
    def __init__(self, dato) -> None:
        self.dato = dato
        self.liga = None

    def asignaLiga(self, nodoALigar) -> None:
        self.liga = nodoALigar

    def asignaDato(self, dato) -> None:
        self.dato = dato

    def retornaLiga(self):
        return self.liga
    
    def retornaDato(self):
        return self.dato


class Cola:
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def esVacia(self):
        return self.primero is None
    
    def esLlena(): # Puede ser implementada de manera diferente
        return False
    
    def encolar(self, dato):
        nodo = NS(dato)
        if self.primero is not None:
            self.ultimo.asignaLiga(nodo)
        else:
            self.primero = nodo
        self.ultimo = nodo

    def pistear(self):
        return self.primero.retornaDato()
    
    def recorrer(self):
        iterador = self.primero
        while iterador != None:
            print(iterador.dato)
            iterador = iterador.retornaLiga()
