#unidad 3 
# Contador nodo k-esimo
# Victor Hugo perusquia cruz

"""
Ejercicio 4 — Contar nodos y obtener k-ésimo desde el final 
Enunciado: (a) Implementa len() que recorra y cuente. (b) Implementa k_from_end(k) que devuelva 
el dato del k-ésimo desde el final (k=1 es el último). 
"""
def __len__(self): 
    cur, c = self.head, 0 
    while cur: c += 1; cur = cur.next 
    return c 
 
def k_from_end(self, k): 
    # usando tail y prev: 
    cur = self.tail 
    i = 1 
    while cur and i < k: 
        cur = cur.prev; i += 1 
    return cur.dato if cur else None 

#Complejidad: len O(n), k_from_end O(k). Sugerencia: mantener un contador size para O(1).