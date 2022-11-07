with open('bovespa.csv', 'r') as arq:
    lendo = arq.readlines()
    lista = lendo.split()

tam = len(lista)
d_inicial = lista[0]
d_final = lista[tam-1]