from datetime import datetime
# Datos de entrada
propiedades = [
    {'año': 2000, 'metros': 100, 'habitaciones': 3, 'garaje': True, 'zona': 'A'},
    {'año': 2012, 'metros': 60, 'habitaciones': 2, 'garaje': True, 'zona': 'B'},
    {'año': 1980, 'metros': 120, 'habitaciones': 4, 'garaje': False, 'zona': 'A'},
    {'año': 2005, 'metros': 75, 'habitaciones': 3, 'garaje': True, 'zona': 'B'},
    {'año': 2015, 'metros': 90, 'habitaciones': 2, 'garaje': False, 'zona': 'A'}
]

año_actual = datetime.now().year


for propiedad in propiedades:
    antigüedad = año_actual - propiedad['año']
    
    precio_base = propiedad['metros'] * 1000 + propiedad['habitaciones'] * 5000 + (15000 if propiedad['garaje'] else 0)
    
    # Calculo de  precio dependiendo de la zona
    if propiedad['zona'] == 'A':
        precio = precio_base * (1 - antigüedad / 100)
    elif propiedad['zona'] == 'B':
        precio = precio_base * (1 - antigüedad / 100) * 1.5

  
    print(f"Zona {propiedad['zona']}: Precio = {precio:.2f}")