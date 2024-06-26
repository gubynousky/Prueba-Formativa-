import os
import csv
clean="cls"
menu_principal=1
trabajadores=[["Trabajador","Cargo","Sueldo Bruto","Desc. Salud","Descuento AFP","Liquido a Pagar"]]
os.system(clean)
def menu():
    print("1. Registar trabajador\n2. Listar los trabajadores\n3. Imprimir planilla de sueldos\n4. Guargar\n5. Salir del programa")

def registro():
    user=input("Ingrese el nombre del trabajador: ")
    user1=user.title()
    cargo=input("Ingrese el cargo del trabajadador: ")
    cargo1=cargo.upper()
    sueldo_bruto=input("Ingrse el sueldo bruto del trabajador: ")
    desc_salud=input("Ingrese el descuento de salud: ")
    afp=input("Ingrese el descuento de AFP: ")
    liquido=input("Ingrese el sueldo liquido a pagar: ")
    trabajadores.append([user1,cargo1,sueldo_bruto,desc_salud,afp,liquido])

def listar_trabajadores():
    for elemento in trabajadores:
        print(elemento)

def cargar_planilla():
    try:
        with open('archivo.trabajadores.csv', mode='r', newline='') as archivo_trabajador:
            leer=csv.reader(archivo_trabajador)
            for elemento in leer:
                for dato in elemento:
                    print(dato)
    except FileNotFoundError:
        print("Archivo no encontrado")

def guardar_datos():
    with open('archivo.trabajadores.csv', mode='w', newline='') as archivo_trabajador:
        guardar=csv.writer(archivo_trabajador)
        guardar.writerow(trabajadores)
        print("Archivo guardado correctamente")

while menu_principal==1:
    menu()
    try:
        opcion=int(input("Seleccione una opcion del menu: "))
        if opcion==1:
            registro()
        elif opcion==2:
            listar_trabajadores()
        elif opcion==3:
            cargar_planilla()
        elif opcion==4:
            guardar_datos()
        elif opcion==5:
            print("Saliendo del programa")
            menu_principal=0
        else:
            print("Seleccione una opcion del menu")
    except ValueError:
        print("Ingrese una opcion valida")
        continue
