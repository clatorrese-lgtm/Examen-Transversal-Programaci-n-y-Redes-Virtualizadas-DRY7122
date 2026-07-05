import requests

API_KEY = "1551b676-32c1-43c0-92bd-240aad689f99" 

print("--- Calculadora Avanzada de Rutas ---")
print("Sugerencia: Para mayor precisión, incluye el país (ej. 'Ciudad de Mendoza, Argentina')")
print("Escribe 's' en cualquier momento para salir del programa.\n")

# Iniciamos un bucle para que el programa siga corriendo hasta que decidas salir
while True:
    print("-" * 50)
    
    # 1. Solicitamos Origen
    origen = input("Ingrese la Ciudad de Origen (o 's' para salir): ").strip()
    if origen.lower() == 's':
        print("¡Gracias por usar la calculadora! Hasta luego.")
        break # Esto rompe el bucle y cierra el programa

    # 2. Solicitamos Destino
    destino = input("Ingrese la Ciudad de Destino (o 's' para salir): ").strip()
    if destino.lower() == 's':
        print("¡Gracias por usar la calculadora! Hasta luego.")
        break

    # 3. Menú para elegir el medio de transporte
    print("\nSeleccione el medio de transporte:")
    print("1. Auto")
    print("2. Bicicleta")
    print("3. A pie")
    opcion = input("Ingrese el número de su elección (1, 2 o 3): ").strip()

    if opcion == "2":
        perfil = "bike"
        transporte_texto = "en Bicicleta"
    elif opcion == "3":
        perfil = "foot"
        transporte_texto = "a Pie"
    else:
        perfil = "car" 
        transporte_texto = "en Auto"

    print(f"\nCalculando ruta {transporte_texto}...")

    # 4. Buscando coordenadas del origen
    url_origen = f"https://graphhopper.com/api/1/geocode?q={origen}&key={API_KEY}"
    respuesta_origen = requests.get(url_origen).json()

    if not respuesta_origen.get('hits'):
        print(f"Error: No se encontraron coordenadas para '{origen}'. Intenta de nuevo.")
        continue # Vuelve al inicio del bucle instead of cerrarse

    lat1 = respuesta_origen['hits'][0]['point']['lat']
    lon1 = respuesta_origen['hits'][0]['point']['lng']

    # 5. Buscando coordenadas del destino
    url_destino = f"https://graphhopper.com/api/1/geocode?q={destino}&key={API_KEY}"
    respuesta_destino = requests.get(url_destino).json()

    if not respuesta_destino.get('hits'):
        print(f"Error: No se encontraron coordenadas para '{destino}'. Intenta de nuevo.")
        continue

    lat2 = respuesta_destino['hits'][0]['point']['lat']
    lon2 = respuesta_destino['hits'][0]['point']['lng']

    # 6. Calculando ruta con el perfil seleccionado
    url_ruta = f"https://graphhopper.com/api/1/route?point={lat1},{lon1}&point={lat2},{lon2}&profile={perfil}&locale=es&key={API_KEY}"
    respuesta_ruta = requests.get(url_ruta).json()

    # 7. Extraer y mostrar los resultados
    if 'paths' in respuesta_ruta:
        ruta = respuesta_ruta['paths'][0]
        
        distancia_metros = ruta['distance']
        distancia_km = distancia_metros / 1000
        distancia_millas = distancia_km * 0.621371
        
        tiempo_ms = ruta['time']
        tiempo_segundos = tiempo_ms / 1000
        horas = int(tiempo_segundos // 3600)
        minutos = int((tiempo_segundos % 3600) // 60)
        
        print("\n--- Resumen del Viaje ---")
        print(f"Origen:     {origen}")
        print(f"Destino:    {destino}")
        print(f"Transporte: {transporte_texto}")
        print(f"Distancia:  {distancia_km:.2f} km / {distancia_millas:.2f} mi")
        print(f"Duración:   {horas} horas y {minutos} minutos")
        
        if 'instructions' in ruta:
            print("\n--- Narrativa del Viaje (Paso a Paso) ---")
            for paso in ruta['instructions']:
                texto_instruccion = paso.get('text', 'Sin instrucción detallada')
                distancia_tramo = paso.get('distance', 0) / 1000
                
                if distancia_tramo > 0:
                    print(f"* {texto_instruccion} ({distancia_tramo:.2f} km)")
                else:
                    print(f"* {texto_instruccion}")
                
    else:
        print(f"\n¡Oops! GraphHopper no pudo calcular la ruta {transporte_texto}.")
        print("Nota: Algunos trayectos largos o cruces fronterizos no son posibles a pie o en bicicleta.")
        print("Motivo de la API:", respuesta_ruta.get('message', 'Error desconocido'))
    
    print("\n") # Espacio extra antes de volver a preguntar