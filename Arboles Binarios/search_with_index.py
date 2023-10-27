import random
import time

def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


inicio = time.time()
random.seed(10)
datos = [random.randint(0, 10000) for _ in range(5000)]
ordenado = bubble_sort(datos)
print(ordenado)
fin = time.time()
print("Tiempo de ejecucion: ", fin-inicio)

search = int(input("Ingrese un Numero :"))
inicio_b = time.time()
print("Si se encuentra en la lista en la posicion: ", datos.index(search))
fin_b = time.time()
time_b = (fin_b-inicio_b)
print(time_b)

inicio_c = time.time()
print("El valor Minimo es: ", ordenado[0])
fin_c = time.time()
print("El tiempo de busqueda del valor minimo fue:" , fin_c-inicio_c)
