def bubble_sort(ventana, v, mostrar_intercambio):
    n = len(v)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if v[j] > v[j + 1]:
                v[j], v[j + 1] = v[j + 1], v[j]
                mostrar_intercambio(ventana, v)


def insertion_sort(ventana, v, mostrar_intercambio):
    n = len(v)
    for j in range(1, n):
        y = v[j]
        k = j - 1
        while k >= 0 and y < v[k]:
            v[k + 1] = v[k]
            mostrar_intercambio(ventana, v)
            k -= 1
        v[k + 1] = y


def shell_sort(ventana, v, mostrar_intercambio):
    n = len(v)
    h = 1
    while h <= n // 9:
        h = 3 * h + 1

    while h > 0:
        for j in range(h, n):
            y = v[j]
            k = j - h
            while k >= 0 and y < v[k]:
                v[k + h] = v[k]
                k -= h
            v[k + h] = y
            mostrar_intercambio(ventana, v)
        h //= 3


def heap_sort(ventana, v, mostrar_intercambio):
    n = len(v)

    for i in range(n):
        e = v[i]
        s = i
        f = (s - 1) // 2
        while s > 0 and v[f] < e:
            v[s] = v[f]
            s = f
            f = (s - 1) // 2
        v[s] = e
        mostrar_intercambio(ventana, v)

    for i in range(n - 1, 0, -1):
        valori = v[i]
        v[i] = v[0]
        f = 0
        if i == 1:
            s = -1
        else:
            s = 1
        if i > 2 and v[2] > v[1]:
            s = 2
        while s >= 0 and valori < v[s]:
            v[f] = v[s]
            f = s
            s = 2 * f + 1
            if s + 1 <= i - 1 and v[s] < v[s + 1]:
                s += 1
            if s > i - 1:
                s = -1
        v[f] = valori
        mostrar_intercambio(ventana, v)


def quick(ventana, v, izq, der, mostrar_intercambio):
    pivot = v[(izq + der) // 2]

    i, j = izq, der
    while i <= j:

        while v[i] < pivot and i < der:
            i += 1

        while v[j] > pivot and j > izq:
            j -= 1

        if i <= j:
            v[i], v[j] = v[j], v[i]
            mostrar_intercambio(ventana, v)
            i += 1
            j -= 1

    if izq < j:
        quick(ventana, v, izq, j, mostrar_intercambio)

    if i < der:
        quick(ventana, v, i, der, mostrar_intercambio)


def quick_sort(ventana, v,  mostrar_intercambio):
    quick(ventana, v, 0, len(v) - 1, mostrar_intercambio)
