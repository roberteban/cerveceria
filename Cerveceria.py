# Programa: Cerveceria
# Descripción: Combina dos palabras para crear un nombre de cerveza.

def crear_nombre_cerveza():
    print("\u2615 Bienvenido a la Cervecería \u2615")
    print("Vamos a crear un nombre único para tu cerveza.")

    # Preguntas al usuario
    palabra1 = input("Ingresa una palabra que describa el sabor o estilo de la cerveza: ")
    palabra2 = input("Ingresa una palabra que describa la esencia o identidad de la cerveza: ")

    # Generar nombre combinando las palabras
    nombre_cerveza = palabra1.capitalize() + " " + palabra2.capitalize()

    # Mostrar el nombre sugerido
    print("\nEl nombre sugerido para tu cerveza es: \ud83c\udf7b " + nombre_cerveza + " \ud83c\udf7b")

# Llamar a la función
crear_nombre_cerveza()
