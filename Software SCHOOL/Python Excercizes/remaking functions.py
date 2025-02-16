def lenght(val):
    n=0
    for char in val:
        n+= 1
    return n
def insert(list,val,index):
    lista = list[:index]
    listb = list[index:]
    lista.append(val)
    return lista + listb
