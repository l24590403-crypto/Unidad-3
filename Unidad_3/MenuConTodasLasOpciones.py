#unidad 3 
# menuuuu con todas las opciones
# Victor Hugo perusquia cruz

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.prev = None
        self.next = None

class ListaDoble:
    def __init__(self):
        self.head = None
        self.tail = None

    def insertar_inicio(self, dato):
        nuevo = Nodo(dato)
        nuevo.next = self.head
        if self.head:
            self.head.prev = nuevo
        else:
            self.tail = nuevo
        self.head = nuevo

    def insertar_final(self, dato):
        nuevo = Nodo(dato)
        nuevo.prev = self.tail
        if self.tail:
            self.tail.next = nuevo
        else:
            self.head = nuevo
        self.tail = nuevo

    def mostrar_adelante(self):
        actual, salida = self.head, []
        while actual:
            salida.append(actual.dato)
            actual = actual.next
        return salida

    def mostrar_atras(self):
        actual, salida = self.tail, []
        while actual:
            salida.append(actual.dato)
            actual = actual.prev
        return salida

    def buscar(self, valor):
        actual = self.head
        while actual:
            if actual.dato == valor:
                return actual
            actual = actual.next
        return None

    def insertar_despues(self, valor_ref, dato):
        ref = self.buscar(valor_ref)
        if not ref:
            print("No se encontró el valor.")
            return False
        nuevo = Nodo(dato)
        nuevo.prev = ref
        nuevo.next = ref.next
        if ref.next:
            ref.next.prev = nuevo
        else:
            self.tail = nuevo
        ref.next = nuevo
        return True

    def eliminar_nodo(self, nodo):
        if not nodo:
            return
        if nodo.prev:
            nodo.prev.next = nodo.next
        else:
            self.head = nodo.next
        if nodo.next:
            nodo.next.prev = nodo.prev
        else:
            self.tail = nodo.prev

    def eliminar_valor(self, valor):
        nodo = self.buscar(valor)
        if not nodo:
            print("Valor no encontrado.")
            return
        self.eliminar_nodo(nodo)

    def eliminar_duplicados(self):
        vistos = set()
        actual = self.head
        while actual:
            if actual.dato in vistos:
                sig = actual.next
                self.eliminar_nodo(actual)
                actual = sig
            else:
                vistos.add(actual.dato)
                actual = actual.next

    def k_desde_final(self, k):
        if k <= 0:
            return None
        actual = self.tail
        i = 1
        while actual and i < k:
            actual = actual.prev
            i += 1
        return actual.dato if actual else None

    def __len__(self):
        c, actual = 0, self.head
        while actual:
            c += 1
            actual = actual.next
        return c

    def __str__(self):
        return str(self.mostrar_adelante())


def menu():
    print("\n=== LISTA DOBLE ===")
    print("1. Insertar al inicio")
    print("2. Insertar al final")
    print("3. Insertar después de un valor")
    print("4. Eliminar un valor")
    print("5. Eliminar duplicados")
    print("6. Mostrar adelante")
    print("7. Mostrar atrás")
    print("8. Longitud")
    print("9. Buscar k desde el final")
    print("10. Salir")

ld = ListaDoble()
ld.insertar_final(10)
ld.insertar_final(20)
ld.insertar_final(30)
ld.insertar_final(10)

while True:
    print(f"\nLista actual: {ld}")
    menu()
    op = input("Opción: ")

    try:
        if op == '1':
            d = int(input("Dato: "))
            ld.insertar_inicio(d)
        elif op == '2':
            d = int(input("Dato: "))
            ld.insertar_final(d)
        elif op == '3':
            ref = int(input("Después de qué valor: "))
            d = int(input("Dato nuevo: "))
            ld.insertar_despues(ref, d)
        elif op == '4':
            v = int(input("Valor a eliminar: "))
            ld.eliminar_valor(v)
        elif op == '5':
            ld.eliminar_duplicados()
            print("Duplicados eliminados.")
        elif op == '6':
            print(ld.mostrar_adelante())
        elif op == '7':
            print(ld.mostrar_atras())
        elif op == '8':
            print("Longitud:", len(ld))
        elif op == '9':
            k = int(input("Posición desde el final: "))
            r = ld.k_desde_final(k)
            print("Resultado:", r if r is not None else "No existe.")
        elif op == '10':
            print("Saliendo...")
            break
        else:
            print("Opción inválida.")
    except ValueError:
        print("Ingrese un número válido.")
