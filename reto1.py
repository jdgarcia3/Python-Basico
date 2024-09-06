import math

# Solicitar datos al usuario
consumo_anual = float(input("Introduce el consumo anual de electricidad en kWh: "))
area_panel = float(input("Introduce el área del panel en metros cuadrados (m²): "))
radiacion_solar = float(input("Introduce la radiación solar promedio por metro cuadrado en kWh/m²/día: "))
eficiencia_panel = float(input("Introduce la eficiencia del panel (como decimal, por ejemplo 0.15 para 15%): "))

# Calcular la potencia diaria generada por un panel solar
potencia_diaria = area_panel * radiacion_solar * eficiencia_panel
print(f"Potencia diaria generada por un panel solar: {potencia_diaria:.2f} kWh")

# Calcular la potencia anual generada por un panel solar
potencia_anual_panel = potencia_diaria * 365
print(f"Potencia anual generada por un panel solar: {potencia_anual_panel:.2f} kWh")

# Calcular el número de paneles solares necesarios
paneles_necesarios = math.ceil(consumo_anual / potencia_anual_panel)
print(f"Número de paneles necesarios: {paneles_necesarios}")

# Calcular el área total necesaria para instalar los paneles solares
area_total = paneles_necesarios * area_panel
print(f"Área total necesaria para instalar los paneles: {area_total:.2f} metros cuadrados")

# Mostrar sugerencias si el número de paneles es mayor a 50
if paneles_necesarios > 50:
    print("\nEl número de paneles excede los 50. Considera mejorar la eficiencia de los paneles o reducir el consumo energético.")
