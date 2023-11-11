import random
import time

class Nodo:
    def __init__(self, valor, izq=None, der=None):
        self.valor = valor
        self.izq = izq
        self.der = der

class Arbol:

    def __init__(self, raiz=None):
        self.raiz = raiz

    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._insertar(valor, self.raiz)

    def _insertar(self, valor, nodo):
        if valor < nodo.valor:
            if nodo.izq is None:
                nodo.izq = Nodo(valor)
            else:
                self._insertar(valor, nodo.izq)
        else:
            if nodo.der is None:
                nodo.der = Nodo(valor)
            else:
                self._insertar(valor, nodo.der)

    def buscar(self, valor):
        if self.raiz is None:
            return False
        else:
            return self._buscar(valor, self.raiz)

    def _buscar(self, valor, nodo):
        if valor == nodo.valor:
            return True
        elif valor < nodo.valor and nodo.izq is not None:
            return self._buscar(valor, nodo.izq)
        elif valor > nodo.valor and nodo.der is not None:
            return self._buscar(valor, nodo.der)
        return False

    def eliminar(self, valor):
        if self.raiz is None:
            return False
        else:
            return self._eliminar(valor, self.raiz)

    def _eliminar(self, valor, nodo):
        if valor == nodo.valor:
            if nodo.izq is None and nodo.der is None:
                nodo = None
            elif nodo.izq is None:
                nodo = nodo.der
            elif nodo.der is None:
                nodo = nodo.izq
            else:
                nodo.valor = self._buscarMin(nodo.der)
                nodo.der = self._eliminar(nodo.valor, nodo.der)
        elif valor < nodo.valor and nodo.izq is not None:
            nodo.izq = self._eliminar(valor, nodo.izq)
        elif valor > nodo.valor and nodo.der is not None:
            nodo.der = self._eliminar(valor, nodo.der)
        return nodo

    def _buscarMin(self, nodo):
        if nodo.izq is None:
            return nodo.valor
        else:
            return self._buscarMin(nodo.izq)

    def preorden(self):
        
        if self.raiz is not None:
            self._preorden(self.raiz)

    def _preorden(self, nodo):
        print(nodo.valor)
        if nodo.izq is not None:
            self._preorden(nodo.izq)
        if nodo.der is not None:
            self._preorden(nodo.der)

    def inorden(self):
        if self.raiz is not None:
            self._inorden(self.raiz)

    def _inorden(self, nodo):
        if nodo.izq is not None:
            self._inorden(nodo.izq)
        print(nodo.valor)
        if nodo.der is not None:
            self._inorden(nodo.der)

    def postorden(self):
        if self.raiz is not None:
            self._postorden(self.raiz)

    def _postorden(self, nodo):
        if nodo.izq is not None:
            self._postorden(nodo.izq)
        if nodo.der is not None:
            self._postorden(nodo.der)
        print(nodo.valor)

    def imprimir(self):
        if self.raiz is not None:
            self._imprimir(self.raiz, 0)

    def _imprimir(self, nodo, nivel):
        if nodo is not None:
            self._imprimir(nodo.der, nivel+1)
            print('   '*nivel, nodo.valor)
            self._imprimir(nodo.izq, nivel+1)

arbol = Arbol()

inicio = time.time()
random.seed(10)
for i in range(5000):
    arbol.insertar(random.randint(1, 10000))

arbol.inorden()
fin = time.time()
print("Tiempo de ejecucion: ", fin-inicio)

print("Si su dato esta va a salir True, si no esta va a salir False")
dato_b = int(input("Indique el dato a buscar: "))
inicio_b = time.time()
print(arbol.buscar(dato_b))
fin_b = time.time()
print("Tiempo de ejecucion: ", fin_b-inicio_b)