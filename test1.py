lista=[]

for numero in range(1,101):
    lista.append(numero)
#while len(lista)!=100:

listaInversa= sorted(lista,reverse=True)

print(listaInversa)