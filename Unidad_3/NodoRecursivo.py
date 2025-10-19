#unidad 3 
# Nodo recursivo
# Victor Hugo perusquia cruz

class Nodo():
    dato = None
    siguiente = None

    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

def agregar_al_final(nodo_actual, dato):
    if nodo_actual is None:
        return Nodo(dato)
    
    if nodo_actual.siguiente is None:
        nodo_actual.siguiente = Nodo(dato)
    else:
        agregar_al_final(nodo_actual.siguiente, dato)
    
    return nodo_actual

def agregar_al_inicio(nodo_inicial, dato):
    nuevo_nodo = Nodo(dato)
    nuevo_nodo.siguiente = nodo_inicial
    return nuevo_nodo

def imprimir_lista(nodo):
    if nodo is None:
        return
    
    print(f"Tenemos {nodo.dato}")
    
    imprimir_lista(nodo.siguiente)

def obtener_cabeza(nodo_inicial):
    return nodo_inicial

def obtener_cola(nodo):
    if nodo is None or nodo.siguiente is None:
        return nodo
    
    return obtener_cola(nodo.siguiente)

def existe(nodo, busqueda):
    if nodo is None:
        return False
        
    if nodo.dato == busqueda:
        return True
    
    return existe(nodo.siguiente, busqueda)

def eliminar(nodo, busqueda):
    if nodo is None:
        return None
    
    if nodo.dato == busqueda:
        return nodo.siguiente
    
    nodo.siguiente = eliminar(nodo.siguiente, busqueda)
    
    return nodo

def main():
    lista = None
    lista = agregar_al_final(lista, "Luis")
    lista = agregar_al_final(lista, "Leon")
    lista = agregar_al_inicio(lista, "Link")
    
    print("Antes de eliminar: ")
    imprimir_lista(lista)  # Link, Luis, Leon
    
    lista = eliminar(lista, "Link")
    
    print("Después de eliminar: ")
    imprimir_lista(lista)  # Luis, Leon
    
    print(existe(lista, "Link"))  # False
    print(existe(lista, "Luis"))  # True
    
    print(obtener_cabeza(lista).dato)  # type: ignore # Luis
    print(obtener_cola(lista).dato) # type: ignore # Leon

main()