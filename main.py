from recetas import receta_pasta
# Aquí se irán importando más recetas a medida que se agreguen

def mostrar_menu():
    print("Recetario disponible:")
    print("1. Pasta al ajo")
    # Agrega aquí tu receta con un número nuevo
    print("2. Arroz con leche")
    opcion = input("Elige una receta (número): ")

    if opcion == "1":
        receta_pasta()
    if opcion == "2":
        receta_arroz_c_leche()
    else:
        print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    mostrar_menu()
