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

    def desencolar(self):
        """Desencola un elemento de la cola"""
        if self.esVacia():
            raise IndexError("Desencolar desde una cola vacía")
        
        dato = self.primero.retornaDato()
        self.primero = self.primero.retornaLiga()
        self.tamano -= 1
        if self.esVacia():
            self.ultimo = None
        return dato

    def peek(self):
        """Retorna el primer elemento de la cola sin desencolarlo"""
        if self.esVacia():
            raise IndexError("Peek en una cola vacía")
        return self.primero.retornaDato()

    def __iter__(self):
        """Permite que la cola sea iterable"""
        actual = self.primero
        while actual is not None:
            yield actual.retornaDato()
            actual = actual.retornaLiga()
    
    def tamano_actual(self):
        """Devuelve el tamaño actual de la cola"""
        return self.tamano


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
            for i, par in enumerate(self.tabla[indice]):
                if par[0] == clave:
                    self.tabla[indice][i] = (clave, valor)  # Reemplazar la tupla completa
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

    def __contains__(self, clave):
        return self.obtener(clave) is not None

    def __str__(self):
        """Devuelve una representación visual del HashMap"""
        result = []
        for i, entrada in enumerate(self.tabla):
            if entrada is not None:
                for clave, valor in entrada:
                    result.append(f"Índice {i}: ({clave}: {valor})")
        return "\n".join(result)


def test_hash_map_y_cola():
    """Función para probar la implementación de HashMap y Cola"""
    # Crear el HashMap con capacidad para 10 elementos
    hash_map_pinturas = HashMap(10)

    # Test 1: Agregar pinturas al HashMap
    print("Test 1: Agregar pinturas")
    hash_map_pinturas.agregar('Pintura1', {'Color': 'Rojo', 'Cantidad': 10})
    hash_map_pinturas.agregar('Pintura2', {'Color': 'Azul', 'Cantidad': 15})
    hash_map_pinturas.agregar('Pintura3', {'Color': 'Verde', 'Cantidad': 20})
    hash_map_pinturas.agregar('Pintura4', {'Color': 'Amarillo', 'Cantidad': 5})
    hash_map_pinturas.agregar('Pintura5', {'Color': 'Negro', 'Cantidad': 8})
    hash_map_pinturas.agregar('Pintura6', {'Color': 'Blanco', 'Cantidad': 12})
    print("Estado del HashMap después de agregar pinturas:")
    print(hash_map_pinturas)  # Ver el estado completo del HashMap

    # Test 2: Obtener pinturas
    print("\nTest 2: Obtener pinturas")
    print("Pintura1:", hash_map_pinturas.obtener('Pintura1'))  # {'Color': 'Rojo', 'Cantidad': 10}
    print("Pintura3:", hash_map_pinturas.obtener('Pintura3'))  # {'Color': 'Verde', 'Cantidad': 20}
    print("Pintura4:", hash_map_pinturas.obtener('Pintura4'))  # {'Color': 'Amarillo', 'Cantidad': 5}
    
    # Test 3: Eliminar una pintura
    print("\nTest 3: Eliminar Pintura2")
    hash_map_pinturas.eliminar('Pintura2')
    print("Pintura2 después de eliminar:", hash_map_pinturas.obtener('Pintura2'))  # Debe devolver None

   # Test 4: Actualizar información de una pintura
    
    print("\nTest 4: Actualizar Pintura1")
    hash_map_pinturas.agregar('Pintura1', {'Color': 'Rojo', 'Cantidad': 25}) # Actualizar cantidad
    print("Pintura1 después de actualizar:", hash_map_pinturas.obtener('Pintura1'))
     # {'Color': 'Rojo', 'Cantidad': 25}

     
    # Test 5: Verificar si una pintura está en el HashMap
    print("\nTest 5: Verificar existencia de pinturas")
    print("Pintura3 existe:", 'Pintura3' in hash_map_pinturas)  # True
    print("Pintura2 existe:", 'Pintura2' in hash_map_pinturas)  # False

    # Test 6: Gestión de procesos en la cola
    print("\nTest 6: Gestión de procesos en la cola")
    cola_procesos = Cola(max_tamano=5)

    # Agregar referencias de pinturas a la cola
    cola_procesos.encolar('Pintura1')
    cola_procesos.encolar('Pintura2')  # Pintura2 fue eliminada, debe manejarse
    cola_procesos.encolar('Pintura3')
    cola_procesos.encolar('Pintura4')
    cola_procesos.encolar('Pintura5')

    print("\nEstado de la Cola antes de procesar:")
    print([item for item in cola_procesos])  # Mostrar la cola como lista

    # Procesar la cola
    while not cola_procesos.esVacia():
        referencia = cola_procesos.peek()  # Tomar el primer elemento de la cola
        materiales = hash_map_pinturas.obtener(referencia)
        if materiales:
            print(f"Procesando envío de {materiales['Cantidad']} unidades de {materiales['Color']} para {referencia}")
        else:
            print(f"Referencia {referencia} eliminada o no encontrada.")
        cola_procesos.desencolar()  # Continuar con el siguiente proceso

    # Test 7: Intentar encolar más elementos de los permitidos
    print("\nTest 7: Intentar encolar más elementos de los permitidos")
    cola_procesos.encolar('Pintura6')  # Debería agregarse sin problema
    cola_procesos.encolar('Pintura7')  # Debería dar un mensaje de error
    print("Estado de la cola después de intentar encolar más elementos:", [item for item in cola_procesos])

    # Test 8: Ver el estado final del HashMap después de las operaciones
    print("\nTest 8: Estado final del HashMap")
    print(hash_map_pinturas)  # Ver el estado del HashMap después de todas las operaciones

# Ejecutamos la prueba de HashMap y Cola
test_hash_map_y_cola()

