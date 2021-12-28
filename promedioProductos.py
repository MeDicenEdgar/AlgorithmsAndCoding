def promedio(*productos):
    prom=0
    for producto in productos:
        prom+=producto
    prom=prom/len(productos)
    print(prom)
promedio(10, 30, 40, 10, 30)

