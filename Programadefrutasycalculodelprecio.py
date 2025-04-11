# Diccionario con frutas y sus precios por kilo
frutas = {
    "manzana": 2.5,
    "pera": 3.0,
    "naranja": 2.0,
    "plátano": 1.8,
    "fresa": 4.5
}

# Lista para guardar las compras
carrito = []

print("=== Bienvenido a la Frutería ===")

while True:
    print("\nFrutas disponibles:")
    for fruta, precio in frutas.items():
        print(f"- {fruta.capitalize()} (${precio} por kilo)")

    fruta = input("\nIngrese el nombre de la fruta que desea comprar: ").lower().strip()

    if fruta in frutas:
        try:
            cantidad = float(input(f"¿Cuántos kilos de {fruta} desea?: "))
            subtotal = frutas[fruta] * cantidad
            carrito.append((fruta, cantidad, subtotal))
            print(f"✅ Añadido al carrito: {cantidad} kg de {fruta} - Subtotal: ${subtotal:.2f}")
        except ValueError:
            print("❌ Por favor, ingrese una cantidad válida.")
    else:
        print("❌ Lo sentimos, esa fruta no está disponible.")

    repetir = input("\n¿Desea hacer otra consulta? (sí/no): ").strip().lower()
    if repetir not in ["sí", "si", "s"]:
        break

# Mostrar resumen de compras
print("\n🧾 Resumen de su compra:")
total_general = 0
for i, (fruta, cantidad, subtotal) in enumerate(carrito, 1):
    print(f"{i}. {cantidad} kg de {fruta} - Subtotal: ${subtotal:.2f}")
    total_general += subtotal

print(f"\n💵 Total a pagar: ${total_general:.2f}")
print("¡Gracias por su compra! 🛒")