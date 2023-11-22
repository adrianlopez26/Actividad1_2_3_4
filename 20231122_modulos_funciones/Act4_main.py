from Actividad_4 import Silla, Color

def crear_silla(color, precio):
    try:
        silla = Silla(color=color, precio=float(precio))
        return silla
    except ValueError as e:
        print(f"Error: {e}")
        return None

# Crear dos instancias de la clase Silla
silla_azul = crear_silla(color=Color.AZUL, precio=9.95)
silla_roja = crear_silla(color=Color.ROJA, precio=9.95)

# Imprimir información de las sillas
if silla_azul:
    print(f"Silla Azul - Color: {silla_azul.color.value}, Precio: {silla_azul.precio:.2f}")

if silla_roja:
    print(f"Silla Roja - Color: {silla_roja.color.value}, Precio: {silla_roja.precio:.2f}")