
class NS:
    def __init__(self, dato) -> None:
        """Inicializa un nodo simple con el dato y un enlace nulo"""
        self.dato = dato
        self.liga = None

    def asignaLiga(self, nodoALigar) -> None:
        """Asigna un enlace al siguiente nodo"""
        self.liga = nodoALigar

    def asignaDato(self, dato) -> None:
        """Modifica el dato del nodo"""
        self.dato = dato

    def retornaLiga(self):
        """Devuelve el enlace al siguiente nodo"""
        return self.liga
    
    def retornaDato(self):
        """Devuelve el dato almacenado en el nodo"""
        return self.dato


class Cola:
    def __init__(self, max_tamano=None):
        self.primero = None
        self.ultimo = None
        self.tamano = 0
        self.max_tamano = max_tamano  # Límite opcional

    def esVacia(self):
        return self.primero is None

    def encolar(self, dato):
        if self.max_tamano is not None and self.tamano >= self.max_tamano:
            print("Cola llena, no se puede encolar más elementos.")
            return
        
        nodo = NS(dato)
        if self.primero is not None:
            self.ultimo.asignaLiga(nodo)
        else:
            self.primero = nodo
        self.ultimo = nodo
        self.tamano += 1

    def pistear(self):
        return self.primero.retornaDato()

    def recorrer(self):
        if self.primero is not None:
            self.primero = self.primero.retornaLiga()
            self.tamano -= 1


class HashMap:
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.tamano = 0
        self.tabla = [None] * capacidad
    
    def funcion_hash(self, clave):
        return hash(clave) % self.capacidad

    def agregar(self, clave, valor):
        if self.tamano / self.capacidad > 0.7:
            self.redimensionar()
        
        indice = self.funcion_hash(clave)
        if self.tabla[indice] is None:
            self.tabla[indice] = [(clave, valor)]
            self.tamano += 1
        else:
            for par in self.tabla[indice]:
                if par[0] == clave:
                    par[1] = valor
                    return
            self.tabla[indice].append((clave, valor))
            self.tamano += 1
    
    def obtener(self, clave):
        indice = self.funcion_hash(clave)
        if self.tabla[indice] is not None:
            for par in self.tabla[indice]:
                if par[0] == clave:
                    return par[1]
        return None
    
    def eliminar(self, clave):
        indice = self.funcion_hash(clave)
        if self.tabla[indice] is not None:
            self.tabla[indice] = [par for par in self.tabla[indice] if par[0] != clave]
            self.tamano -= 1

    def redimensionar(self):
        nueva_capacidad = self.capacidad * 2
        nueva_tabla = [None] * nueva_capacidad
        for entrada in self.tabla:
            if entrada is not None:
                for clave, valor in entrada:
                    indice = hash(clave) % nueva_capacidad
                    if nueva_tabla[indice] is None:
                        nueva_tabla[indice] = [(clave, valor)]
                    else:
                        nueva_tabla[indice].append((clave, valor))
        self.capacidad = nueva_capacidad
        self.tabla = nueva_tabla


def test_hash_map_y_cola():
    # Crear el hash map con capacidad para 10 elementos
    hash_map_pinturas = HashMap(10)

    # Test 1: Agregar pinturas al hash map
    print("Test 1: Agregar pinturas")
    hash_map_pinturas.agregar('Pintura1', {'Color': 'Rojo', 'Cantidad': 10})
    hash_map_pinturas.agregar('Pintura2', {'Color': 'Azul', 'Cantidad': 15})
    print(hash_map_pinturas.obtener('Pintura1'))  # Debe devolver {'Color': 'Rojo', 'Cantidad': 10}
    print(hash_map_pinturas.obtener('Pintura2'))  # Debe devolver {'Color': 'Azul', 'Cantidad': 15}

    # Test 2: Eliminar una pintura
    print("\nTest 2: Eliminar Pintura2")
    hash_map_pinturas.eliminar('Pintura2')
    print(hash_map_pinturas.obtener('Pintura2'))  # Debe devolver None

    # Test 3: Cola de procesos
    print("\nTest 3: Gestión de procesos en la cola")
    cola_procesos = Cola()
    cola_procesos.encolar('Pintura1')
    cola_procesos.encolar('Pintura2')  # Pintura2 ya fue eliminada, debe manejarse

    # Procesar la cola
    while not cola_procesos.esVacia():
        referencia = cola_procesos.pistear()  # Tomar el primer elemento de la cola
        materiales = hash_map_pinturas.obtener(referencia)
        if materiales:
            print(f"Procesando envío de {materiales['Cantidad']} unidades de {materiales['Color']} para {referencia}")
        else:
            print(f"No se encontró información para la referencia {referencia}")
        cola_procesos.recorrer()  # Continuar con el siguiente proceso



test_hash_map_y_cola()
