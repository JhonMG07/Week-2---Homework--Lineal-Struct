from queue import Queue

# El ordenamiento por mezcla (también conocido como Merge Sort en inglés) es un algoritmo de ordenamiento
# eficiente que divide una lista desordenada en dos sublistas de igual tamaño (o aproximadamente iguales),
# las ordena recursivamente y luego las mezcla para obtener una lista ordenada completa.

# La idea principal detrás del algoritmo es dividir repetidamente la lista en mitades hasta que queden
# sublistas de tamaño 1 o 0, que ya se consideran ordenadas.


def merge_sort_queue(arr):
    # caso que solo sea un elemento
    if len(arr) <= 1:
        return arr

    # caso que tenga mas de un elemento
    # dividimos el arreglo y obtenemos la mitad del tamaño ya que (//) devulve el numero entero

    # Los dos puntos (:) antes de mid indican que se debe tomar una porción de la lista arr,
    # desde el inicio hasta el índice mid-1 para left, y desde el índice mid hasta el final
    # para right. Esto se conoce como "slicing" o "rebanado" en Python, y se utiliza para
    # obtener una sección de una lista, tupla o cadena.

    mid: int = len(arr) // 2
    left: int = arr[:mid]
    right: int = arr[mid:]

    # Ordenar recursivamente cada sub-lista
    left = merge_sort_queue(left)
    right = merge_sort_queue(right)

    # Mezclar las dos colas resultantes en una sola cola ordenada
    result: Queue = Queue()
    while len(left) > 0 and len(right) > 0:
        if left[0] < right[0]:
            result.put(left.pop(0))
        else:
            result.put(right.pop(0))

    # Agregar cualquier elemento restante a la cola resultante
    while len(left) > 0:
        result.put(left.pop(0))
    while len(right) > 0:
        result.put(right.pop(0))

    # Devolver la cola resultante como una lista
    return list(result.queue)


numeros: list = [9, 3, 1, 7, 2, 8, 5, 4, 6]
print("Lista original:", numeros)

ordenados = merge_sort_queue(numeros)
print("Lista ordenada:", ordenados)
