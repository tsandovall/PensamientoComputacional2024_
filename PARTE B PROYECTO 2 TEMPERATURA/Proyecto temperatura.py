from datetime import datetime
import threading
import time

class Horario:
    def __init__(self, inicio, fin, temperatura):
        self.inicio = inicio
        self.fin = fin
        self.temperatura = temperatura

class ZonaTemperatura:
    def __init__(self, nombre, temperatura_deseada):
        self.nombre = nombre
        self.temperatura_deseada = temperatura_deseada
        self.temperatura_actual = temperatura_deseada  
        self.horarios = []

    def agregar_horario(self, inicio, fin, temperatura):
        self.horarios.append(Horario(inicio, fin, temperatura))

    def ajustar_temperatura(self, temperatura):
        self.temperatura_actual = temperatura

    def verificar_horarios(self):
        ahora = datetime.now().strftime("%H:%M")
        for horario in self.horarios:
            if horario.inicio <= ahora <= horario.fin:
                self.ajustar_temperatura(horario.temperatura)
                return
        self.ajustar_temperatura(self.temperatura_deseada)  
    def restablecer_temperatura(self):
        self.temperatura_deseada = 22
        self.temperatura_actual = 22

    def __str__(self):
        info = f"{self.nombre}: Temp. Deseada {self.temperatura_deseada}°C, Temp. Actual {self.temperatura_actual}°C\n"
        if self.horarios:
            info += "Horarios programados:\n"
            for horario in self.horarios:
                info += f"- {horario.inicio} a {horario.fin}: {horario.temperatura}°C\n"
        return info

class Sistema:
    def __init__(self):
        self.zonas_temperatura = {}

    def agregar_zona(self, nombre, temperatura_deseada):
        if nombre not in self.zonas_temperatura:
            self.zonas_temperatura[nombre] = ZonaTemperatura(nombre, temperatura_deseada)
        else:
            print("¡La zona ya existe!")

    def mostrar_zonas(self):
        for zona in self.zonas_temperatura.values():
            print(zona)

    def mostrar_horarios(self):
        for zona in self.zonas_temperatura.values():
            print(f"Horarios programados para {zona.nombre}:")
            if zona.horarios:
                for horario in zona.horarios:
                    print(f"- {horario.inicio} a {horario.fin}: {horario.temperatura}°C")
            else:
                print("No hay horarios programados.")

    def configurar_zonas(self):
        print("Configuración de Zonas de Temperatura:")
        while True:
            nombre = input("Ingrese el nombre de la zona (o 'fin' para terminar): ")
            if nombre == 'fin':
                break
            temperatura = float(input("Ingrese la temperatura deseada para la zona (en °C): "))
            self.agregar_zona(nombre, temperatura)
            print("Zona configurada correctamente.")

    def verificar_horarios(self):
        for zona in self.zonas_temperatura.values():
            zona.verificar_horarios()

    def restablecer_zonas(self):
        for zona in self.zonas_temperatura.values():
            zona.restablecer_temperatura()
        print("Todas las zonas han sido restablecidas a la temperatura predeterminada de 22°C.")

def menu_control_temperatura(sistema):
    while True:
        print("\nControl de Temperatura por Zonas:")
        print("1. Mostrar Zonas de Temperatura")
        print("2. Ajustar Temperatura de una Zona")
        print("3. Programar Horario para una Zona")
        print("4. Mostrar Horarios Programados")
        print("5. Restablecer Zonas a Temperatura Predeterminada")
        print("6. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            sistema.mostrar_zonas()
        elif opcion == '2':
            nombre_zona = input("Ingrese el nombre de la zona a ajustar: ")
            if nombre_zona in sistema.zonas_temperatura:
                nueva_temperatura = float(input("Ingrese la nueva temperatura para la zona (en °C): "))
                sistema.zonas_temperatura[nombre_zona].temperatura_deseada = nueva_temperatura
                sistema.zonas_temperatura[nombre_zona].ajustar_temperatura(nueva_temperatura)
                print("Temperatura ajustada correctamente.")
            else:
                print("¡Zona no encontrada!")
        elif opcion == '3':
            nombre_zona = input("Ingrese el nombre de la zona a programar: ")
            if nombre_zona in sistema.zonas_temperatura:
                inicio = input("Ingrese el inicio del horario (HH:MM): ")
                fin = input("Ingrese el fin del horario (HH:MM): ")
                temperatura = float(input("Ingrese la temperatura para el horario (en °C): "))
                sistema.zonas_temperatura[nombre_zona].agregar_horario(inicio, fin, temperatura)
                print("Horario programado correctamente.")
            else:
                print("¡Zona no encontrada!")
        elif opcion == '4':
            sistema.mostrar_horarios()
        elif opcion == '5':
            sistema.restablecer_zonas()
        elif opcion == '6':
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Inténtelo de nuevo.")

def loop_verificacion_horarios(sistema):
    while True:
        sistema.verificar_horarios()
        time.sleep(60)  

sistema = Sistema()
sistema.configurar_zonas()

verificacion_thread = threading.Thread(target=loop_verificacion_horarios, args=(sistema,))
verificacion_thread.daemon = True
verificacion_thread.start()

menu_control_temperatura(sistema)




