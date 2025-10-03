productos = ["lapiz", "cuaderno", "borrador"]
precios = [50, 70, 40]

def calcular_total(cantidades, precios):
    total = 0
    for i in range(len(cantidades)):
        total += cantidades[i] * precios[i]
    return total

print("MENU DE PAPELERIA - BIENVENIDO")
print("=" * 35)

cantidades = [] 

for i in range(len(productos)):
    print(f"{i+1}. {productos[i]} - ${precios[i]}")
    cantidad_input = int(input("Ingresa la cantidad de este producto: "))
    cantidades.append(cantidad_input) 

total = calcular_total(cantidades, precios)

print("\n--- TICKET DE COMPRA ---")
print("Papelería ")
print("-----------------------")
print("Producto\tCant.\tPrecio\tSubtotal")
print("-----------------------")

for i in range(len(productos)):
    subtotal = cantidades[i] * precios[i]  
    print(f"{productos[i].capitalize()}\t\t{cantidades[i]}\t${precios[i]}\t${subtotal}")

print("-----------------------")
print(f"TOTAL:\t\t\t\t${total}")
print("-----------------------")
print("¡Gracias por su compra!")