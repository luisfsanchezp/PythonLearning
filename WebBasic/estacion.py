def mostrar_menu():
    print("\n--- Gestión de Estación de Combustible ---")
    print("1. Registrar servicio.")
    print("2. Mostrar reporte del día.")
    print("3. Salir.")

def pedir_servicio():
    while True:
        try:
            clase = int(input("Ingresar la clase de servicio (1–4): "))
            if 1 <= clase <= 4:
                break
            print("Clase inválida, ingresa un valor entre 1 y 4.")
        except ValueError:
            print("Debe ser un número entero (1-4).")
    while True:
        jornada = input("Ingresar la jornada ('mañana' o 'tarde'): ").strip().lower()
        if jornada in ("mañana", "tarde"):
            break
        print("Jornada inválida. Escribe 'mañana' o 'tarde'.")
    while True:
        try:
            valor = float(input("Ingresa valor del servicio: "))
            if valor >= 0:
                break
            print("El valor debe ser no negativo.")
        except ValueError:
            print("Debe ser un número (puede incluir decimales).")
    return clase, jornada, valor

def generar_reporte(servicios_reg):
    print("\n📊 REPORTE DEL DÍA 📊")
    total_general = 0
    # calculamos totales por clase
    for clase in range(1, 5):
        datos = servicios_reg[clase]
        cantidad = datos['count']
        valor = datos['total']
        total_general += valor
        print(f"• Servicio {clase}: prestado {cantidad} veces — total recaudado: ${valor:.2f}")
    # identificamos servicio más prestado
    max_count = max(servicios_reg[c]['count'] for c in servicios_reg)
    servicios_top = [c for c, d in servicios_reg.items() if d['count'] == max_count]
    if max_count == 0:
        print("\nNo se prestó ningún servicio hoy.")
    else:
        if len(servicios_top) == 1:
            print(f"\n🔝 El servicio más prestado fue el {servicios_top[0]}, con {max_count} veces.")
        else:
            lista = ', '.join(map(str, servicios_top))
            print(f"\n🔝 Los servicios más prestados fueron {lista}, con {max_count} veces cada uno.")
    print(f"\nTotal general recaudado hoy: ${total_general:.2f}")

def main():
    servicios_reg = {
        i: {'count': 0, 'total': 0.0}
        for i in range(1, 5)
    }

    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ").strip()
        if opcion == "1":
            clase, jornada, valor = pedir_servicio()
            servicios_reg[clase]['count'] += 1
            servicios_reg[clase]['total'] += valor
            print(f"✅ Registrado servicio clase {clase}, jornada {jornada}, valor ${valor:.2f}.")
        elif opcion == "2":
            generar_reporte(servicios_reg)
        elif opcion == "3":
            print("\nSaliendo... ¡Hasta luego!")
            break
        else:
            print("Opción inválida, intenta de nuevo.")

if __name__ == "__main__":
    main()
