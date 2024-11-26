class Envio:
    def __init__(self, numero_guia, destinatario, direccion, fecha_envio, estado):
        self.numero_guia = numero_guia
        self.destinatario = destinatario
        self.direccion = direccion
        self.fecha_envio = fecha_envio
        self.estado = estado
        self.siguiente = None  # Apunta al siguiente nodo en la lista

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def insertar_al_final(self, envio):
        if not self.cabeza:
            self.cabeza = envio
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = envio

    def insertar_al_inicio(self, envio):
        envio.siguiente = self.cabeza
        self.cabeza = envio

    def eliminar_por_numero_guia(self, numero_guia):
        actual = self.cabeza
        previo = None
        while actual:
            if actual.numero_guia == numero_guia:
                if previo:
                    previo.siguiente = actual.siguiente
                else:
                    self.cabeza = actual.siguiente
                return f"Envío con número de guía {numero_guia} eliminado."
            previo = actual
            actual = actual.siguiente
        return f"Envío con número de guía {numero_guia} no encontrado."

    def buscar_por_numero_guia(self, numero_guia):
        actual = self.cabeza
        while actual:
            if actual.numero_guia == numero_guia:
                return vars(actual)
            actual = actual.siguiente
        return f"Envío con número de guía {numero_guia} no encontrado."

    def buscar_por_destinatario(self, destinatario):
        actual = self.cabeza
        resultados = []
        while actual:
            if actual.destinatario == destinatario:
                resultados.append(vars(actual))
            actual = actual.siguiente
        return resultados if resultados else f"No se encontraron envíos para {destinatario}."

    def mostrar_todos(self):
        envios = []
        actual = self.cabeza
        while actual:
            envios.append(vars(actual))
            actual = actual.siguiente
        return envios if envios else "No hay envíos registrados."

# Menú principal
def menu():
    lista_envios = ListaEnlazada()

    while True:
        print("\n--- Sistema de Registro de Envíos ---")
        print("1. Agregar envío al final")
        print("2. Agregar envío al inicio")
        print("3. Eliminar envío por número de guía")
        print("4. Buscar envío por número de guía")
        print("5. Buscar envío por destinatario")
        print("6. Mostrar todos los envíos")
        print("7. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            numero_guia = input("Número de guía: ")
            destinatario = input("Destinatario: ")
            direccion = input("Dirección: ")
            fecha_envio = input("Fecha de envío: ")
            estado = input("Estado: ")
            envio = Envio(numero_guia, destinatario, direccion, fecha_envio, estado)
            lista_envios.insertar_al_final(envio)
            print("Envío agregado al final.")

        elif opcion == "2":
            numero_guia = input("Número de guía: ")
            destinatario = input("Destinatario: ")
            direccion = input("Dirección: ")
            fecha_envio = input("Fecha de envío: ")
            estado = input("Estado: ")
            envio = Envio(numero_guia, destinatario, direccion, fecha_envio, estado)
            lista_envios.insertar_al_inicio(envio)
            print("Envío agregado al inicio.")

        elif opcion == "3":
            numero_guia = input("Número de guía del envío a eliminar: ")
            print(lista_envios.eliminar_por_numero_guia(numero_guia))

        elif opcion == "4":
            numero_guia = input("Número de guía a buscar: ")
            print(lista_envios.buscar_por_numero_guia(numero_guia))

        elif opcion == "5":
            destinatario = input("Nombre del destinatario: ")
            resultados = lista_envios.buscar_por_destinatario(destinatario)
            print(resultados)

        elif opcion == "6":
            print(lista_envios.mostrar_todos())

        elif opcion == "7":
            print("Saliendo del sistema. ¡Hasta luego!")
            break

        else:
            print("Opción no válida. Intente nuevamente.")

# Ejecutar el menú
if __name__ == "__main__":
    menu()