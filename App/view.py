"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
from DISClib.ADT import map
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("0- Cargar información en el catálogo")
    print("1- Listar las n obras más antiguas de un medio")
    print("2- Listar cronológicamente los artistas para un rango de años")
    print("3- Listar cronológicamente las adquisiciones")
    print("4- Clasificar las obras de un artista por técnica")
    print("5- Clasificar las obras por la nacionalidad de sus creadores")
    print("6- Transportar obras de un departamento")
    print("7- Realizar prueba de rendimiento")
    print("8- Encontrar el número total de obras para una nacionalidad")
    print("9- Salir")

def printPerfMenu():
    print("1- Listar cronológicamente los artistas para un rango de años")
    print("2- Listar cronológicamente las adquisiciones")
    print("3- Clasificar las obras de un artista por técnica")
    print("4- Clasificar las obras por la nacionalidad de sus creadores")
    print("5- Transportar obras de un departamento")
    print("6- Volver al menú principal")

def printLastArtists(Artists):
    LastArtists = lt.subList(Artists,lt.size(Artists)-4,3)
    i = 1
    for Artist in lt.iterator(LastArtists):
        print(str(i) + '. Name: ' + Artist['DisplayName'] +',', 'Biography:', Artist['ArtistBio'] + '.')
        i += 1

def printLastArtworks(Artworks):
    LastArtworks = lt.subList(Artworks,lt.size(Artworks)-4,3)
    i = 1
    for Artwork in lt.iterator(LastArtworks):
        print(str(i) + '. Title: ' + Artwork['Title'] +',', 'Date:', Artwork['Date'] +',',
        'Medium:', Artwork['Medium'] +',', 'Classification:', Artwork['Classification'] + '.')
        i+=1

#Requirement 0
def printReq0Answer(sorted_artworks,artists,n):
    print('Las',str(n),'obras más antiguas son:\n')
    if lt.size(sorted_artworks) > n:
        sorted_artworks = lt.subList(sorted_artworks,1,n)
    
    i = 1
    for artwork in lt.iterator(sorted_artworks):
            artist_IDs = artwork['ConstituentID']
            artists_artworks = controller.findArtist(artists,artist_IDs)
            artists_artworks = ', '.join(artists_artworks)
            print(str(i) + '. Título: ' + artwork['Title'] +',',  'Artista(s): ' + artists_artworks +',',
            'Año:', artwork['Date'] + ',', 'Medio:', artwork['Medium'] + ',', 'Dimensiones:', artwork['Dimensions'] + '.')
            i += 1
    input('Presione "Enter" para continuar.\n')


#Requirement 1
def printReq1Answer(SortedArtists,StartYear,EndYear):
    if lt.size(SortedArtists) > 0:
        print('Se encontró(aron)', str(lt.size(SortedArtists)), 'artista(s) entre el año',
        str(StartYear), 'y', str(EndYear) + '.')
        input('Presione "Enter" para continuar.')
        
        if lt.size(SortedArtists) > 6:
            print('Los primeros 3 y 3 últimos artistas encontrados fueron:\n')
            i = 1
            while i <= 3:
                Artist = lt.getElement(SortedArtists,i)
                print(str(i) + '. Nombre: ' + Artist['DisplayName'] +',', 'Año de nacimiento:', str(Artist['BeginDate']) + ',',
                'Nacionalidad:', Artist['Nationality'] + ',', 'Género:', Artist['Gender'] + '.')
                i += 1
            print('...')
            i = lt.size(SortedArtists)-2
            while i <= lt.size(SortedArtists):
                Artist = lt.getElement(SortedArtists,i)
                print(str(i) + '. Nombre: ' + Artist['DisplayName'] +',', 'Año de nacimiento:', str(Artist['BeginDate']) + ',',
                'Nacionalidad:', Artist['Nationality'] + ',', 'Género:', Artist['Gender'] + '.')
                i += 1
        else:
            print('El(los) artista(s) encontrado(s) fue(ron):\n')
            i = 1
            while i <= lt.size(SortedArtists):
                Artist = lt.getElement(SortedArtists,i)
                print(str(i) + '. Nombre: ' + Artist['DisplayName'] +',', 'Año de nacimiento:', str(Artist['BeginDate']) + ',',
                'Nacionalidad:', Artist['Nationality'] + ',', 'Género:', Artist['Gender'] + '.')
                i += 1
    else:
        print('No se encontró ningún artista para el rango de años dado.')
    input('Presione "Enter" para continuar.\n')

#Requirement 2
def printReq2Answer(SortedArtworks,StartYear,EndYear,artists):
    if lt.size(SortedArtworks) > 0:
        print('Se encontró(aron)', str(lt.size(SortedArtworks)), 'obra(s) entre la fecha',
        str(StartYear), 'y', str(EndYear) + '.')
        input('Presione "Enter" para continuar.')
        
        if lt.size(SortedArtworks) > 6:
            print('Las primeras 3 y 3 últimas obras encontradas fueron:\n')
            i = 1
            while i <= 3:
                artwork = lt.getElement(SortedArtworks,i)
                artist_IDs = artwork['ConstituentID']
                artists_artworks = controller.findArtist(artists,artist_IDs)
                artists_artworks = ', '.join(artists_artworks)
                print(str(i) + '. Título: ' + artwork['Title'] +',', 'Artista(s): ' + artists_artworks +',',
                'Fecha:', artwork['DateAcquired'] + ',', 'Medio:', artwork['Medium'] + ',', 'Dimensiones:', artwork['Dimensions'] + '.')
                i += 1
            print('...')
            i = lt.size(SortedArtworks)-2
            while i <= lt.size(SortedArtworks):
                artwork = lt.getElement(SortedArtworks,i)
                artist_IDs = artwork['ConstituentID']
                artists_artworks = controller.findArtist(artists,artist_IDs)
                artists_artworks = ', '.join(artists_artworks)
                print(str(i) + '. Título: ' + artwork['Title'] +',', 'Artista(s): ' + artists_artworks +',',
                'Fecha:', artwork['DateAcquired'] + ',', 'Medio:', artwork['Medium'] + ',', 'Dimensiones:', artwork['Dimensions'] + '.')
                i += 1
        else:
            print('La(s) obra(s) encontrada(s) fue(ron):\n')
            i = 1
            while i <= lt.size(SortedArtworks):
                artwork = lt.getElement(SortedArtworks,i)
                artist_IDs = artwork['ConstituentID']
                artists_artworks = controller.findArtist(artists,artist_IDs)
                artists_artworks = ', '.join(artists_artworks)
                print(str(i) + '. Título: ' + artwork['Title'] +',', 'Artista(s): ' + artists_artworks +',',
                'Fecha:', artwork['DateAcquired'] + ',', 'Medio:', artwork['Medium'] + ',', 'Dimensiones:', artwork['Dimensions'] + '.')
                i += 1
    else:
        print('No se encontró ninguna obra para el rango de fechas dado.')
    input('Presione "Enter" para continuar.\n')

#Requirement 3
def printReq3Answer(artist, artist_info):
    artist_artworks,artist_mediums,mostUsedMedium,mediumArtworks = artist_info

    print('\nEl número de obras creadas por ' + artist + ' es ' + str(artist_artworks) + '.')
    print('\nEl número de medios usados por ' + artist + ' en sus obras es ' + str(artist_mediums) + '.')
    print('\nEl medio más usado por ' + artist + ' en sus obras es ' + str(mostUsedMedium) + '.')
    input('Presione "Enter" para continuar.')
    print('\nLas obras creadas con el medio más usado son: ')
    if lt.size(mediumArtworks) > 6:
        print('Las primeras 3 y 3 últimas obras encontradas fueron:\n')
        i = 1
        while i <= 3:
            artwork = lt.getElement(mediumArtworks,i)
            print(str(i) + '. Título: ' + artwork['Title'] +',', 'Fecha:', artwork['DateAcquired'] + ',', 
            'Medio:', artwork['Medium'] + ',', 'Dimensiones:', artwork['Dimensions'] + '.')
            i += 1
        print('...')
        i = lt.size(mediumArtworks)-2
        while i <= lt.size(mediumArtworks):
            artwork = lt.getElement(mediumArtworks,i)
            print(str(i) + '. Título: ' + artwork['Title'] +',', 'Fecha:', artwork['DateAcquired'] + ',', 
            'Medio:', artwork['Medium'] + ',', 'Dimensiones:', artwork['Dimensions'] + '.')
            i += 1
    else:
        print('La(s) obra(s) encontrada(s) fue(ron):\n')
        i = 1
        while i <= lt.size(mediumArtworks):
            artwork = lt.getElement(mediumArtworks,i)
            print(str(i) + '. Título: ' + artwork['Title'] +',', 'Fecha:', artwork['DateAcquired'] + ',', 
            'Medio:', artwork['Medium'] + ',', 'Dimensiones:', artwork['Dimensions'] + '.')
            i += 1

#Requirement 4
def printReq4Answer(art_nation,artworks_nation,sorted_nations,artists):
    top10 = lt.subList(sorted_nations,1,10)
    print('Nación',' '*10, 'Número de Obras')
    for nation in lt.iterator(top10):
        print(nation['Nation'],' '*(16-len(nation['Nation'])), nation['NumbArtworks'])
    
    input('Presione "Enter" para continuar.')

    print('\nLa información de las 3 primeras y últimas obras de',art_nation,'es la siguiente:\n')
    i = 1
    first_nation = lt.subList(artworks_nation,1,3)
    for artwork in lt.iterator(first_nation):
        artist_IDs = artwork['ConstituentID']
        artists_artworks = controller.findArtist(artists,artist_IDs)
        artists_artworks = ', '.join(artists_artworks)
        print(str(i) + '. Título: ' + artwork['Title'] +',', 'Artista(s): ' + artists_artworks +',','Fecha:', artwork['DateAcquired'] + ',', 
        'Medio:', artwork['Medium'] + ',', 'Dimensiones:', artwork['Dimensions'] + '.')
        i += 1
    
    print('...')
    
    i = lt.size(artworks_nation)-2
    last_nation = lt.subList(artworks_nation,lt.size(artworks_nation)-2,3)
    for artwork in lt.iterator(last_nation):
        artist_IDs = artwork['ConstituentID']
        artists_artworks = controller.findArtist(artists,artist_IDs)
        artists_artworks = ', '.join(artists_artworks)
        print(str(i) + '. Título: ' + artwork['Title'] +',', 'Artista(s): ' + artists_artworks +',','Fecha:', artwork['DateAcquired'] + ',', 
        'Medio:', artwork['Medium'] + ',', 'Dimensiones:', artwork['Dimensions'] + '.')
        i += 1

#Requirement 5
def printReq5Answer(moveDepartmentAns, department, sort_type, artists,list_type):
    est_price, art2trans, est_weight, price_map, date_map = moveDepartmentAns
    print('\nSe realizó la estimación del cálculo de costos para mover las obras del departamento ' + department + '.')

    print('\nEl total de obras a trasnportar es de ' + str(art2trans) + '.')
    print('\nEl peso estimado de las obras transportadas es ' + str(round(est_weight,2)) + ' kg.')
    print('\nEl precio estimado del servicio es de USD $' + str(round(est_price,2)) + '.')
    input('Presione "Enter" para continuar.')

    print('\nLas 5 obras más antiguas encontradas son: ')
    artworks_date = controller.SortArtworksByDate(date_map,sort_type,list_type)
    i = 1
    while i <= 5:
        artwork = lt.getElement(artworks_date,i)
        artist_IDs = artwork['ConstituentID']
        artists_artworks = controller.findArtist(artists,artist_IDs)
        artist_name = ', '.join(artists_artworks )
        print(str(i) + '. Título: ' + artwork['Title'] +',', 'Artista(s): ' + artist_name  +',','Fecha:', artwork['DateAcquired'] + ',', 
        'Medio:', artwork['Medium'] + ',', 'Dimensiones:', artwork['Dimensions'] + ',', 'Costo:', str(round(artwork['EstPrice'],2)) + '.')
        i += 1
    input('Presione "Enter" para continuar.')

    print('\nLas 5 obras más costosas encontradas son: ')
    artworks_price = controller.SortArtworksByPrice(price_map,sort_type,list_type)
    i = 1
    while i <= 5:
        artwork = lt.getElement(artworks_price,i)
        artist_IDs = artwork['ConstituentID']
        artists_artworks = controller.findArtist(artists,artist_IDs)
        artists_artworks = ', '.join(artists_artworks)
        print(str(i) + '. Título: ' + artwork['Title'] +',', 'Artista(s): ' + artists_artworks +',','Fecha:', artwork['DateAcquired'] + ',', 
        'Medio:', artwork['Medium'] + ',', 'Dimensiones:', artwork['Dimensions'] + ',', 'Costo:', str(round(artwork['EstPrice'],2)) + '.')
        i += 1

#Requirement 7
def printReq7Answer(n_artworks,nationality):
    print('\nEl número de obras de arte encontradas para la nacionalidad', nationality, 'es de', str(n_artworks),'obras.')

"""
Menu principal
"""
catalog = None
Artists = None
Artworks = None
list_type = None
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 0:
        listaValida = False
        while not listaValida:
            list_type = int(input("Seleccione el tipo de representación de lista\n (1.) ARRAY_LIST (2.) LINKED_LIST: "))
            if(list_type != 1 and list_type != 2):
                print("Por favor ingrese una opción válida")
            else:
                listaValida = True
        
        print("Cargando información de los archivos ....")
        start_time = controller.start_endPerfTest()
        catalog = controller.initCatalog(list_type)
        controller.loadArtists(catalog)
        controller.loadArtworks(catalog,list_type)
        stop_time = controller.start_endPerfTest()
        total_time = (stop_time - start_time)*1000

        Artists = catalog['artists']
        Artworks = catalog['artworks']
        print('Total de artistas cargados: ' + str(lt.size(Artists)))
        print('Total de obras cargadas: ' + str(lt.size(Artworks)))
        input('Presione "Enter" para continuar.')

        print('\nInformación de últimos artistas de la lista:\n')
        printLastArtists(Artists)
        input('Presione "Enter" para continuar.')

        print('\nInformación de últimas obras de la lista:\n')
        printLastArtworks(Artworks)
        input('Presione "Enter" para continuar.\n')
        
        print('\nEl tiempo usado para llevar a cabo el algoritmo es de ' + str(total_time) + ' mseg.')
        input('Presione "Enter" para continuar.\n')
        
    
    elif catalog == None:
        print('Debe cargar los datos antes de seleccionar cualquier opción.')
        input('Presione "Enter" para continuar.\n')
    
    elif int(inputs[0]) == 1:
        valid_medium = False
        while not(valid_medium):
            medium = input('Brinde el medio para el cual desea realizar el análisis: ')
            if controller.encounterMedium(catalog,medium):
                valid_medium = True
            else:
                print('Debe seleccionar un medio válido.')
                input('Presione "Enter" para continuar.\n')
        
        n = int(input('Establezca el número de obras: '))
        sort_type = 5
        n_artworks = controller.oldestArtworks(catalog,medium,sort_type,list_type)
        start_time = controller.start_endPerfTest()
        printReq0Answer(n_artworks,Artists,n)
        stop_time = controller.start_endPerfTest()
        total_time = (stop_time - start_time)*1000
        print('\nEl tiempo usado para llevar a cabo el algoritmo es de ' + str(total_time) + ' mseg.')
        input('Presione "Enter" para continuar.\n')
    
    elif int(inputs[0]) == 2:
        valid_map = False
        while not valid_map:
            print("--Métodos de colisión")
            print("1) Separate Chaining")
            print("2) Linear Probing")
            map_type = input("Seleccione el tipo de método de colisión a usar para el mapa: ")

            valid_types = ["1","2"]
            if map_type not in valid_types:
                print("\nDebe seleccionar una opción válida.")
                input('Presione "Enter" para continuar.\n')
            else:
                map_type = int(map_type)
                valid_map = True
        
        StartYear = int(input('Brinde el año inicial del rango: '))
        EndYear = int(input('Brinde el año final del rango: '))
        artistsInRange = controller.ArtistsInRange(Artists,StartYear,EndYear,list_type,map_type)
        SortedArtists = controller.SortChronologically(artistsInRange,StartYear,EndYear,list_type)
        printReq1Answer(SortedArtists,StartYear,EndYear)

    elif int(inputs[0]) == 3:
        valid_map = False
        while not valid_map:
            print("--Métodos de colisión")
            print("1) Separate Chaining")
            print("2) Linear Probing")
            map_type = input("Seleccione el tipo de método de colisión a usar para el mapa: ")

            valid_types = ["1","2"]
            if map_type not in valid_types:
                print("\nDebe seleccionar una opción válida.")
                input('Presione "Enter" para continuar.\n')
            else:
                map_type = int(map_type)
                valid_map = True

        StartYear = input('Brinde la fecha inicial del rango: ')
        EndYear = input('Brinde la fecha final del rango: ')
        artworksInRange = controller.ArtworksInRange(Artworks,StartYear,EndYear,list_type,valid_map)
        sort_type = 5
        sorted_artworks = controller.SortArtworks(artworksInRange,sort_type,list_type)

        printReq2Answer(sorted_artworks,StartYear,EndYear,Artists)

    elif int(inputs[0]) == 4:
        valid_map = False
        while not valid_map:
            print("--Métodos de colisión")
            print("1) Separate Chaining")
            print("2) Linear Probing")
            map_type = input("Seleccione el tipo de método de colisión a usar para el mapa: ")

            valid_types = ["1","2"]
            if map_type not in valid_types:
                print("\nDebe seleccionar una opción válida.")
                input('Presione "Enter" para continuar.\n')
            else:
                map_type = int(map_type)
                valid_map = True

        artist_name = input('Brinde el nombre del artista del cual desea obtener información: ')
        artist_ID = controller.encounterArtist(Artists,artist_name)
        if artist_ID == 'NotFound':
            'No se ha encontrado el artista escogido.'
        else:
            artist_info = controller.artistMediumInfo(Artworks,artist_ID,list_type,map_type)
        printReq3Answer(artist_name,artist_info)
        input('Presione "Enter" para continuar.\n')
        

    elif int(inputs[0]) == 5:
        print('\nSe organizarán las obras por nacionalidad.')
        valid_map = False
        while not valid_map:
            print("--Métodos de colisión")
            print("1) Separate Chaining")
            print("2) Linear Probing")
            map_type = input("Seleccione el tipo de método de colisión a usar para el mapa: ")

            valid_types = ["1","2"]
            if map_type not in valid_types:
                print("\nDebe seleccionar una opción válida.")
                input('Presione "Enter" para continuar.\n')
            else:
                map_type = int(map_type)
                valid_map = True
        
        artworksNationality,nations = controller.nationalityArtworks(Artworks,catalog,list_type,map_type)
        sort_type = 5
        sorted_nations,art_nation,artworks_nation = controller.sortNations(artworksNationality,nations,sort_type)
        printReq4Answer(art_nation,artworks_nation,sorted_nations,Artists)
        input('Presione "Enter" para continuar.\n')


    elif int(inputs[0]) == 6:
        valid_map = False
        while not valid_map:
            print("--Métodos de colisión")
            print("1) Separate Chaining")
            print("2) Linear Probing")
            map_type = input("Seleccione el tipo de método de colisión a usar para el mapa: ")

            valid_types = ["1","2"]
            if map_type not in valid_types:
                print("\nDebe seleccionar una opción válida.")
                input('Presione "Enter" para continuar.\n')
            else:
                map_type = int(map_type)
                valid_map = True
        
        department = input('Brinde el nombre del departamento para el cual desea calcular el costo: ')
        if controller.checkDepartment(Artworks,department):
            moveDepartmentAns = controller.moveDepartment(Artworks,department,map_type)
            sort_type = 5
            printReq5Answer(moveDepartmentAns,department,sort_type,Artists,list_type)
            input('Presione "Enter" para continuar.\n')
        else:
            print('Debe seleccionar un departamento válido.')
            input('Presione "Enter" para continuar.\n')
    

    elif int(inputs[0]) == 7:
        print('\nSe realizará una prueba de rendimiento.')
        input('Presione "Enter" para continuar.\n')
        reqValido = False
        while not reqValido:
            printPerfMenu()
            req = int(input('Escoja la tarea de la cual desea realizar la prueba de rendimiento: '))
            if req not in range(7):
                print('Debe seleccionar una opción válida.')
                input('Presione "Enter" para continuar.\n')
            else:
                reqValido = True
        
        sampleValido = False
        while not sampleValido:
            sample_size = input('Escoja el tamaño de muestra: ')
            if sample_size.isnumeric():
                sample_size = int(sample_size)
                sampleValido = True
            else:
                print("Por favor ingrese una opción válida")
        
        print('\nSe procederá a realizar el test de rendimiento con la tarea escogida.')
        input('Presione "Enter" para continuar.\n')
        if req == 1:
            StartYear = int(input('Brinde el año inicial del rango: '))
            EndYear = int(input('Brinde el año final del rango: '))
            sample = controller.createSample(Artists,sample_size)
            start_time = controller.start_endPerfTest()
            artistsInRange = controller.ArtistsInRange(sample,StartYear,EndYear,list_type)
            SortedArtists = controller.SortChronologically(artistsInRange)
            stop_time = controller.start_endPerfTest()
            total_time = (stop_time - start_time)*1000
            print('El tiempo usado para llevar a cabo el algoritmo es de ' + str(total_time) + ' mseg.')
            input('Presione "Enter" para continuar.\n')
        elif req == 2:
            StartYear = input('Brinde la fecha inicial del rango: ')
            EndYear = input('Brinde la fecha final del rango: ')
            sortValido = False
            while not sortValido:
                sort_type = int(input("Seleccione el tipo de sort\n (1.) QuickSort (2.) Insert (3.) Shell (4.) Selection (5.) Merge: "))
                if(sort_type != 1 and sort_type != 2 and sort_type != 3 and sort_type != 4 and sort_type != 5):
                    print("Por favor ingrese una opción válida\n")
                else:
                    sortValido = True
            
            validPerc = False
            while not validPerc:
                perc = float(input("Seleccione el porcentaje de los datos que desea usar: "))
                if perc > 0 and perc <= 1:
                    validPerc = True
                else:
                    print("Por favor ingrese una opción válida\n")
            
            sample = controller.createSample(Artworks,sample_size)
            start_time = controller.start_endPerfTest()
            artworksInRange = controller.ArtworksInRange(Artworks,StartYear,EndYear,list_type)
            samplePerc = controller.createPercSample(artworksInRange,perc)
            sorted_artworks = controller.SortArtworks(samplePerc,sort_type)
            stop_time = controller.start_endPerfTest()
            total_time = (stop_time - start_time)*1000
            print('El tiempo usado para llevar a cabo el algoritmo es de ' + str(total_time) + ' mseg.')
            input('Presione "Enter" para continuar.\n')
        elif req == 3:
            print('Nota: para este algoritmo se usará el tamaño de la muestra sobre el total de obras posibles.')
            artist_name = input('Brinde el nombre del artista del cual desea obtener información: ')
            sample = controller.createSample(Artworks,sample_size)
            start_time = controller.start_endPerfTest()
            artist_ID = controller.encounterArtist(Artists,artist_name)
            if artist_ID == 'NotFound':
                'No se ha encontrado el artista escogido.'
            else:
                artist_info = controller.artistMediumInfo(sample,artist_ID,list_type)
            stop_time = controller.start_endPerfTest()
            total_time = (stop_time - start_time)*1000
            print('El tiempo usado para llevar a cabo el algoritmo es de ' + str(total_time) + ' mseg.')
            input('Presione "Enter" para continuar.\n')
        elif req == 4:
            print('\nSe organizarán las obras por nacionalidad.')
            sample = controller.createSample(Artworks,sample_size)
            start_time = controller.start_endPerfTest()
            artworksNationality,nations = controller.nationalityArtworks(sample,Artists,list_type)
            sort_type = 5
            sorted_nations,art_nation,artworks_nation = controller.sortNations(artworksNationality,nations,sort_type)
            stop_time = controller.start_endPerfTest()
            total_time = (stop_time - start_time)*1000
            print('El tiempo usado para llevar a cabo el algoritmo es de ' + str(total_time) + ' mseg.')
            input('Presione "Enter" para continuar.\n')
        elif req == 5:
            validDepartment = False
            while not validDepartment:
                department = input('Brinde el nombre del departamento para el cual desea calcular el costo: ')
                if controller.checkDepartment(Artworks,department):
                    validDepartment = True
                else:
                    print('Debe seleccionar un departamento válido.')
                    input('Presione "Enter" para continuar.\n')
            sample = controller.createSample(Artworks,sample_size)
            start_time = controller.start_endPerfTest()
            moveDepartmentAns = controller.moveDepartment(sample,department,list_type)
            sortValido = False
            while not sortValido:
                sort_type = int(input("Seleccione el tipo de sort\n (1.) QuickSort (2.) Insert (3.) Shell (4.) Selection (5.) Merge: "))
                if(sort_type != 1 and sort_type != 2 and sort_type != 3 and sort_type != 4 and sort_type != 5):
                    print("Por favor ingrese una opción válida\n")
                else:
                    sortValido = True
            artworks_dep = moveDepartmentAns[3]
            artworks_wdate = controller.artworksWithDate(artworks_dep,list_type)
            artworks_date = controller.SortArtworksByDate(artworks_wdate,sort_type)
            artworks_price = controller.SortArtworksByPrice(artworks_dep,sort_type)
            stop_time = controller.start_endPerfTest()
            total_time = (stop_time - start_time)*1000
            print('El tiempo usado para llevar a cabo el algoritmo es de ' + str(total_time) + ' mseg.')
            input('Presione "Enter" para continuar.\n')
        else:
            pass
    elif int(inputs[0]) == 8:
        valid_nationality = False
        while not(valid_nationality):
            nationality = input('Brinde la nacionalidad para la cual desea conocer el número de obras: ')
            if controller.encounterNationality(catalog,nationality):
                valid_nationality= True
            else:
                print('Debe seleccionar una nacionalidad válida.')
                input('Presione "Enter" para continuar.\n')
        
        n_artworks = controller.countArtworksNationality(catalog,nationality)
        start_time = controller.start_endPerfTest()
        printReq7Answer(n_artworks,nationality)
        stop_time = controller.start_endPerfTest()
        total_time = (stop_time - start_time)*1000
        print('\nEl tiempo usado para llevar a cabo el algoritmo es de ' + str(total_time) + ' mseg.')
        input('Presione "Enter" para continuar.\n')
    
    elif int(inputs[0]) == 9:
        sys.exit(0)
    else:
        print('Debe seleccionar una opción válida')
        input('Presione "Enter" para continuar.\n')
sys.exit(0)