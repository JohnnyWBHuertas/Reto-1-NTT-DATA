#Johnny
from datetime import datetime
import random, folium

result = []

#Johnny
# Solucion Ejercicio 1.A
def simulacion_read():
    # Los siguientes datos se esctructura así para simular la lectura de un
    # archivo csv
    list_data =[
            ['Estado', 'Alabama', 'Florida', 'Georgia', 'South Carolina'], 
            ['Poblacion 2000', '4447100', '15982378', '8186453', '4012012'], 
            ['Poblacion 2001', '4451493', '17054000', '8229823', '4023438'], 
            ['Residentes < 65 anios 2000', '3870598', '13237167', '7440877', '3535770'], 
            ['Residentes < 65 anios 2001', '3880476', '13548077', '7582146', '3567172'], 
            ['Muertes 2000', '10622', '38103', '14804', '8581'], 
            ['Muertes 2001', '15912', '166069', '15000', '9500'], 
            ['Latitud', '33.258882', '27.756767', '32.329381', '33.687439'], 
            ['Longitud', '-86.829534', '-81.463983', '-83.113737', '-80.436374'], 
            ['Fecha fundacion', '14-12-1819', '03-03-1845', '12-02-1733', '26-03-1776']
        ]
    return list_data

#Johnny
# Solucion Ejercicio 1.A
def create_diccionario(lista): 
    # El range(len(list_data[0])) me permite obtener el total de las columnas de la tabla
    for index in range(len(lista[0])):
        diccionario = {}
        for row in lista:
            # Este if me garantiza que no se consulte los nombres de la primer columna, es decir:
            # Estado, Población 2000, Población 2001, Residentes < 65 años 2000, ........
            if row[0] != row[index]:
                diccionario[row[0].lower()] = row[index].lower()
        if diccionario != {} :
            result.append(diccionario)
    
#Johnny
# Solucion Ejercicio 1.C
def update_diccionario(key_estado: str, value_estado: str, key: str, value: str):
    # Aseguramos que la las llaves y los valorres esten en minusculas
    key_estado = key_estado.lower(); value_estado = value_estado.lower()
    key = key.lower(); value = value.lower()

    # realizamos la busqueda del dato en especifico y actulizamos el valor de la llave
    # de un diccionario
    for diccionario in result:
        if diccionario[key_estado] == value_estado:
            diccionario[key] = value

#Johnny
# Solucion Ejercicio 1.D
def add_diccionario(key: str, new_key: str):
    # Se asegura que la llave esté en minusculas
    key = key.lower(); new_key = new_key.lower()
    for diccionario in result:
        fecha_conv = convertir_fecha(diccionario[key])
        fecha_actual = datetime.now()
        diferencia = fecha_actual - fecha_conv
        anios_transcurridos = int(diferencia.days // 30.4375)
        diccionario[new_key] = anios_transcurridos

#Johnny
# Solucion Ejercicio 1.D
def convertir_fecha(fecha_str):
    # convertimos la fecha del formato dia-mes-anio
    return datetime.strptime(fecha_str, '%d-%m-%Y')

#Johnny
# Solucion Ejercicio 1.E
def add_porcentaje(key_pob_1: str, key_pob_2: str, key_res_1: str, key_res_2: str):
    key_pob_1 = key_pob_1.lower(); key_pob_2 = key_pob_2.lower()
    key_res_1 = key_res_1.lower(); key_res_2 = key_res_2.lower()
    for diccionario in result:
        po_to_2000 = int(diccionario[key_pob_1])
        po_to_2001 = int(diccionario[key_pob_2])
        re_me_65_2000 = int(diccionario[key_res_1])
        re_me_65_2001 = int(diccionario[key_res_2])
        porc_2000 = (po_to_2000 - re_me_65_2000) / po_to_2000 * 100
        porc_2001 = (po_to_2001 - re_me_65_2001) / po_to_2001 * 100
        diccionario['porcentaje mayores 65 años 2000'] = f'{porc_2000:.2f}'
        diccionario['porcentaje mayores 65 años 2001'] = f'{porc_2001:.2f}'

#Johnny
# Solucion Ejercicio 1.F
def antiguedad(key_estado: str, key: str):
    anios_de_antiguo = 0
    anios_de_moderno = float('inf')
    estado_antiguo = ''
    estado_moderno = ''
    key_estado = key_estado.lower() ;key = key.lower()
    for diccionario in result:
        anios = int(diccionario[key]/12)
        if anios > anios_de_antiguo:
            anios_de_antiguo = anios
            estado_antiguo = diccionario[key_estado]
        if anios < anios_de_moderno:
            anios_de_moderno = anios
            estado_moderno = diccionario[key_estado]
    return  estado_antiguo, anios_de_antiguo, estado_moderno, anios_de_moderno

#Johnny
# Solucion Ejercicio 2
def tasa_poblacion():
    # Generar números aleatorios entre 0 y 0.1 para las tasas de crecimiento
    tasa_crec_alabama = random.uniform(0, 0.1)
    tasa_crec_south_carolina = random.uniform(0, 0.1)

    # Asignar la tasa de crecimiento menor a Alabama y la mayor a South Carolina
    if tasa_crec_alabama < tasa_crec_south_carolina:
        tasa_crec_alabama = tasa_crec_alabama
        tasa_crec_south_carolina = tasa_crec_south_carolina
    else:
        tasa_crec_alabama = tasa_crec_south_carolina
        tasa_crec_south_carolina = tasa_crec_alabama


    for diccionario in result:
        if diccionario['estado'] == 'alabama':
            poblacion_2001 = float(diccionario['poblacion 2001'])
            poblacion_2002 = poblacion_2001 * (1 + tasa_crec_alabama)
            diccionario['poblacion 2002'] = str(int(poblacion_2002))

        elif diccionario['estado'] == 'south carolina':
            poblacion_2001 = float(diccionario['poblacion 2001'])
            poblacion_2002 = poblacion_2001 * (1 + tasa_crec_south_carolina)
            diccionario['poblacion 2002'] = str(int(poblacion_2002))

#Johnny
# Solucion Ejercicio 2.A y 2.B
def anios_crecimiento():
    print('SOLUCION EJERCICIO 2.A y 2.B: ')
    p_2001_ala = 0; p_2002_ala = 0
    p_2001_car = 0; p_2002_car = 0

    # Se consulta la poblacion del 2001 y 2002 de Alabama y Carolina del Sur
    for diccionario in result:
        if diccionario['estado'] == 'alabama':
            p_2001_ala = int(diccionario['poblacion 2001'])
            p_2002_ala = int(diccionario['poblacion 2002'])
        elif diccionario['estado'] == 'south carolina':
            p_2001_car = int(diccionario['poblacion 2001'])
            p_2002_car = int(diccionario['poblacion 2002'])
    
    # Se calcula la tasa de crecimiento de Alabama y Carolina del Sur
    ta_cre_ala = (p_2002_ala - p_2001_ala) / p_2001_ala
    ta_cre_car = (p_2002_car - p_2001_car ) / p_2001_car

    print(f'La tasa de cremiento de Alabama es {ta_cre_ala} y de South Carolina es {ta_cre_car}')

    # año incial para la muestra o conteo
    anio = 2002
    counter = 0
    tiempo_inf = False

    # hasta que momento la poblacion de Carolina del Sur es mayor
    while p_2002_car <= p_2002_ala:
        # Calcular la población del próximo año
        p_2002_ala = p_2002_ala * (1 + ta_cre_ala)
        p_2002_car = p_2002_car * (1 + ta_cre_car)

        if counter == 23300:
            tiempo_inf = True
            break
    
        # Incrementar el año
        counter += 1
    
    if tiempo_inf :
        print(f'South Carolina tardará mas de {counter} año(s) en que alcance a Alabama\n')
    else:
        print(f'South Carolina tardará {counter} año(s) en que alcance a Alabama')
        print(f'Esto ocurrirá en el año {anio + counter}\n')

#Johnny
# Solucion Ejercicio 2.C
def anios_crecimiento_menos_fallecidos():
    print('SOLUCION EJERCICIO 2.C: ')
    p_2001_ala = 0; p_2002_ala = 0; p_fell_2001_ala = 0
    p_2001_car = 0; p_2002_car = 0; p_fell_2001_car = 0

    # Se consulta la poblacion del 2001 y 2002 de Alabama y Carolina del Sur
    for diccionario in result:
        if diccionario['estado'] == 'alabama':
            p_2001_ala = int(diccionario['poblacion 2001'])
            p_fell_2001_ala = int(diccionario['muertes 2001'])
            p_2002_ala = int(diccionario['poblacion 2002'])
        elif diccionario['estado'] == 'south carolina':
            p_2001_car = int(diccionario['poblacion 2001'])
            p_fell_2001_car = int(diccionario['muertes 2001'])
            p_2002_car = int(diccionario['poblacion 2002'])
    
    # Se calcula la tasa de crecimiento de Alabama y Carolina del Sur
    ta_cre_ala = (p_2002_ala - p_2001_ala) / p_2001_ala
    ta_cre_car = (p_2002_car - p_2001_car ) / p_2001_car

    ta_mor_ala = p_fell_2001_ala / p_2001_ala
    ta_mor_car = p_fell_2001_car / p_2001_car

    print(f'La tasa de cremiento de Alabama es {ta_cre_ala:} y de South Carolina es {ta_cre_car}')
    print(f'La tasa de moratandad de Alabama es {ta_mor_ala} y de South Carolina es {ta_mor_car}')

    counter = 0
    tiempo_i = False

    # Validar hasta que momento la poblacion de Carolina del Sur es mayor
    while  p_2001_car <= p_2001_ala:
        # Calcular la población del próximo año
        p_2001_ala = p_2001_ala * (1 + ta_cre_ala) * (1 - ta_mor_ala)
        p_2001_car = p_2001_car * (1 + ta_cre_car) * (1 - ta_mor_car)

        if counter == 23300:
            tiempo_i = True
            break
    
        # Incrementar el año
        counter += 1
    
    if tiempo_i :
        print(f'South Carolina tardará mas de {counter} año(s) en que alcance a Alabama\n')
    else:
        print(f"South Carolina tardará {counter} años en alcanzar la población de Alabama.\n")

#Johnny
# Solucion Ejercicio 3
def proyeccion_poblacion():
    for item in result:
        poblacion_2000 = float(item['poblacion 2000'])
        poblacion_2001 = float(item['poblacion 2001'])
        fecha = item['fecha fundacion']
        
        # Calcular la proyección de población para 2002
        poblacion_2002 = poblacion_2001 / poblacion_2000 * poblacion_2001

        # Ajustar variable del tiempo
        conv_fecha = datetime.strptime(fecha, '%d-%m-%Y')
        anio = conv_fecha.year
        t = 1900 - anio
        
        # Agregar la población y estudio demografico proyectada al diccionario
        item['poblacion 2002'] = str(int(poblacion_2002))
        item['estudio demografico'] = int(14500 * t + 7000 / (2 * t) + 1)
    return result

#Johnny
# Solucion Ejercicio 4
def folium_map():
    m = folium.Map([30.101271, -82.370146], zoom_start = 6)

    for diccionario in result:
        radius = int(diccionario['poblacion 2002']) / 100000
        folium.CircleMarker(
            location=[float(diccionario['latitud']), float(diccionario['longitud'])],
            radius=radius,
            icon=folium.Icon(color="blue"),
            tooltip=f"El estado de {diccionario['estado']} tiene un registro de la <br>" + 
                    f"población del año 2002 de {diccionario['poblacion 2002']} habitantes <br>" +
                    f"y su estudio demográfico es de {diccionario['estudio demografico']} <br>",
            popup=diccionario['poblacion 2002'],
            color="blue",
            fill=True, 
            fill_color="blue",
            fill_opacity=0.0,
        ).add_to(m)
    
    m.save("index.html")

#Johnny
# General
def organizarPlot(data):
    print('[')
    for diccionario in data:
        print('  {')
        for items in diccionario.items():
            print(f"    '{items[0]}' : '{items[1]}' ")
        print('  },')
    print(']\n')
    
data_lista = simulacion_read()
create_diccionario(data_lista)
print('SOLUCION EJERCICIO 1.A: ')
organizarPlot(result)

# Solucion Ejercicio 1.C
update_diccionario('Estado','Florida', 'Poblacion 2001', '16054328')
print('SOLUCION EJERCICIO 1.C: ')
organizarPlot(result)

# Solucion Ejercicio 1.D
add_diccionario('Fecha fundacion', 'Dias desde fundacion')
print('SOLUCION EJERCICIO 1.D: ')
organizarPlot(result)

# Solucion Ejercicio 1.E
add_porcentaje('Poblacion 2000', 'poblacion 2001', 'rEsidentes < 65 anios 2000', 'resIdentes < 65 anios 2001')
print('SOLUCION EJERCICIO 1.E: ')
organizarPlot(result)

# Solucion Ejercicio 1.F
a, b, c, d = antiguedad('Estado','Dias desde fundacion')

print('\nSOLUCION EJERCICIO 1.F: ')
print(f'El estado mas antiguo es {a} y tienen {b} años')
print(f'El estado mas moderno es {c} y tienen {d} años')
print(f'La diferencia de entre estos es de {b - d} años\n')

# Solucion Ejercicio 2
tasa_poblacion()
print('SOLUCION EJERCICIO 2: ')
organizarPlot(result)

# Solucion Ejercicio 2.A y 2.B
print('SOLUCION EJERCICIO 2.A y 2.B: ')
anios_crecimiento()

# Solucion Ejercicio 2.C
print('SOLUCION EJERCICIO 2.C: ')
anios_crecimiento_menos_fallecidos()

# Solucion Ejercicio 3
data = proyeccion_poblacion()
print('SOLUCION EJERCICIO 3: ')
organizarPlot(data)

#Solucion Ejercicio 4
folium_map()