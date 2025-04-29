# Codigo Listas Enlazdas
# Clase Nodo
class Nodo:
    def __init__(self, ubicacion):
        self.ubicacion = ubicacion
        self.conexiones = []
        self.siguiente = None
# Clase ListaSE
class ListaSE:
    def __init__(self):
        self.cabeza = None

    def estaVacia(self):
        return self.cabeza == None
    
    def contadorElementos(self):
        contador = 0
        temp = self.cabeza
        while temp:
            contador = contador + 1
            temp = temp.siguiente
        return contador
    
    def imprimirLista(self):
        temp = self.cabeza
        while temp:
            print(f"Ubicación : {temp.ubicacion}, Conexiones : {[temp.ubicacion for i in temp.conexiones]}")
            temp = temp.siguiente

    def agregarAlInicio(self, ubicacion):
        nuevo_nodo = Nodo(ubicacion)
        if self.estaVacia():
            self.cabeza = nuevo_nodo
            return
        else: 
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza = nuevo_nodo

    def buscar_elemento(self, ubicacion):
        actual = self.cabeza
        while actual:
            if actual.ubicacion == ubicacion:
                return actual
            actual = actual.siguiente
        return None

    def agregar_ruta(self, ubicacion1, ubicacion2):
        nodo1 = self.buscar_elemento(ubicacion1)
        nodo2 = self.buscar_elemento(ubicacion2)
        if nodo1 and nodo2:
            nodo1.conexiones.append(nodo2)
            nodo2.conexiones.append(nodo1)

    
    def encontrar_ruta(self, inicio, destino):
        def dfs(nodo_actual, destino, visitados=None, ruta_actual=None):
            if visitados is None:
                visitados = set()
            if ruta_actual is None:
                ruta_actual = []

            visitados.add(nodo_actual)
            ruta_actual.append(nodo_actual.ubicacion)

            if nodo_actual.ubicacion == destino:
                return ruta_actual

            for vecino in nodo_actual.conexiones:
                if vecino not in visitados:
                    resultado = dfs(vecino, destino, visitados, ruta_actual.copy())
                    if resultado:
                        return resultado

            return None

        nodo_inicio = self.buscar_elemento(inicio)
        if nodo_inicio:
            return dfs(nodo_inicio, destino)
        return None