# Codigo Arboles BST
class NodoArbol:
    def __init__(self, ubicacion):
        self.ubicacion = ubicacion
        self.conexiones = []
        self.izquierda = None
        self.derecha = None

class ArbolBST:
    def __init__(self):
        self.raiz = None
    
    def insertar(self, ubicacion, nodo=None):
        if nodo is None: 
            if self.raiz is None:
                self.raiz = NodoArbol(ubicacion)
                return
            nodo = self.raiz
        
        if ubicacion < nodo.ubicacion:
            if nodo.izquierda is None:
                nodo.izquierda = NodoArbol(ubicacion)
            else:
                self.insertar(ubicacion, nodo.izquierda)
        elif ubicacion > nodo.ubicacion:
            if nodo.derecha is None:
                nodo.derecha = NodoArbol(ubicacion)
            else:
                self.insertar(ubicacion, nodo.derecha)
    
    def buscar(self, ubicacion, nodo=None):
        if nodo is None:
            nodo = self.raiz
        if nodo is None or nodo.ubicacion == ubicacion:
            return nodo
        if ubicacion < nodo.ubicacion:
            return self.buscar(ubicacion, nodo.izquierda)
        return self.buscar(ubicacion, nodo.derecha)
    
    def agregar_ruta(self, ubicacion1, ubicacion2):
        nodo1 = self.buscar(ubicacion1)
        nodo2 = self.buscar(ubicacion2)
        if nodo1 and nodo2:
            nodo1.conexiones.append(nodo2)
            nodo2.conexiones.append(nodo1)
    
    def encontrar_ruta(self, inicio, destino):
        nodo_inicio = self.buscar(inicio)
        if not nodo_inicio:
            return None
        cola = [(nodo_inicio, [nodo_inicio.ubicacion])]
        visitados = set()
        while cola:
            nodo_actual, ruta_actual = cola.pop(0)
            if nodo_actual.ubicacion == destino:
                return ruta_actual
            visitados.add(nodo_actual)
            for vecino in nodo_actual.conexiones:
                if vecino not in visitados:
                    cola.append((vecino, ruta_actual + [vecino.ubicacion]))
        return None

    
    def imprimir_arbol(self, nodo=None, nivel=0):
        if nodo is None:
            nodo = self.raiz
        if nodo is not None:
            self.imprimir_arbol(nodo.derecha, nivel + 1)
            print(' ' * 4 * nivel + '->', nodo.ubicacion)
            self.imprimir_arbol(nodo.izquierda, nivel + 1)
    
    def buscar_por_rango(self, minimo, maximo, nodo=None, resultados=None):
        if resultados is None:
            resultados = []
        if nodo is None:
            nodo = self.raiz
        if nodo is None:
            return resultados
        
        if minimo < nodo.ubicacion:
            self.buscar_por_rango(minimo, maximo, nodo.izquierda, resultados)
        if minimo <= nodo.ubicacion <= maximo:
            resultados.append(nodo.ubicacion)
        if maximo > nodo.ubicacion:
            self.buscar_por_rango(minimo, maximo, nodo.derecha, resultados)
