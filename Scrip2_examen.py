print("Validar Rangos de VLAN")

try:
    vlan = int(input("Ingrese el numero de VLAN para consultar: "))

    if 1 <= vlan <= 1005:
        print(f"El numero {vlan} corresponde al rango VLAN ESTANDAR")
    elif 1006 <= vlan <= 4094:
        print(f"El numero {vlan} corresponde al rango VLAN EXTENDIDO")
    else:
        print(f"Error: {vlan} no es un numero de VLAN valido (debe estar entre 1 y 4094).")
except ValueError:
    print("Error: Por favor, ingrese solo números enteros.")
