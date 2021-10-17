﻿"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """

import config as cf
import time
import math
from DISClib.ADT import map
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as ss
from DISClib.Algorithms.Sorting import quicksort as qs
from DISClib.Algorithms.Sorting import mergesort as ms
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import selectionsort as scs
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Inicialización del Catálogo de MoMA

def newCatalog(list_type):
    """
    Inicializa el catálogo de artistas y obras.
    """
    catalog = {'artists': lt.newList(datastructure=list_type),'artworks':lt.newList(datastructure=list_type), 
    'ArtistID':map.newMap(), 'Medium':map.newMap(maptype='PROBING',loadfactor=0.50,numelements=42503), 
    'Nationality':map.newMap(maptype='PROBING',loadfactor=0.50,numelements=233)}
    return catalog

# Funciones para la carga de datos

def addArtists(catalog,artist):
    artists = catalog['artists']
    lt.addLast(artists,artist)

def addArtistsIDs(catalog,artist):
    artist_ID = artist['ConstituentID']
    artist_map = catalog['ArtistID']
    map.put(artist_map,artist_ID,artist)

def addArtworks(catalog, artwork):
    artworks = catalog['artworks']
    lt.addLast(artworks,artwork)

'''
def encMediums(list_type):
    return lt.newList(datastructure=list_type)

def addMedium(encMediums,artwork):
    medium = artwork['Medium']
    if not( lt.isPresent(encMediums,medium)):
        lt.addLast(encMediums,medium)
'''

def loadMedium(catalog, artwork, list_type):
    medium = artwork['Medium']
    if medium == '':
        medium = 'Unknown'
    map_medium = catalog['Medium']
    if not( map.contains(map_medium,medium) ):
        artworks_med = lt.newList(datastructure=list_type)
        lt.addLast(artworks_med,artwork)
        map.put(map_medium,medium,artworks_med)
    else:
        artworks_med = map.get(map_medium,medium)
        lt.addLast(artworks_med['value'],artwork)

def loadNationality(catalog, artwork, list_type):
    artist_IDs = artwork['ConstituentID']
    artistsIDs_map = catalog['ArtistID']
    nationalities = findArtistNationality(artistsIDs_map,artist_IDs,list_type)
    for nationality in lt.iterator(nationalities):
        if nationality == '':
            nationality = 'Unknown'
        map_nationality = catalog['Nationality']
        if not( map.contains(map_nationality,nationality) ):
            artworks_med = lt.newList(datastructure=list_type)
            lt.addLast(artworks_med,artwork)
            map.put(map_nationality,nationality,artworks_med)
        else:
            artworks_med = map.get(map_nationality,nationality)
            lt.addLast(artworks_med['value'],artwork)

# Funciones de consulta sobre el catálogo

#Requirement 0
def cmpArtworkByDate(artwork1, artwork2): 
    return artwork1["Date"] < artwork2['Date']

def encounterMedium(catalog,medium):
    return map.contains(catalog['Medium'],medium)

def sortArtworksByDate(artworks,sort_type):
    if sort_type == "QUICKSORT":
        sortedList = qs.sort(artworks,cmpArtworkByDate)
    elif sort_type == "INSERTION":
        sortedList = ins.sort(artworks,cmpArtworkByDate)
    elif sort_type == "SHELL":
        sortedList = ss.sort(artworks,cmpArtworkByDate)
    elif sort_type == "SELECTION":
        sortedList = scs.sort(artworks,cmpArtworkByDate)
    else:
        sortedList = ms.sort(artworks,cmpArtworkByDate)
    return sortedList

def artworksWithDate(artworks,list_type):
    artworksWithDate = lt.newList(datastructure=list_type)
    for artwork in lt.iterator(artworks):
        if artwork['Date'] != '':
            lt.addLast(artworksWithDate,artwork)
    return artworksWithDate

def oldestArtworks(catalog,medium,sort_type,list_type):
    mediums = catalog['Medium']
    artworks = map.get(mediums,medium)['value']
    artworks_dated = artworksWithDate(artworks,list_type)
    sorted_artworks = sortArtworksByDate(artworks_dated,sort_type)
    return sorted_artworks

def findArtist(artists,artist_IDs):
    artists_artworks = []
    for artist_ID in (artist_IDs.replace('[','')).replace(']','').split(','):
        pos = 0
        while pos < lt.size(artists):
            artist = lt.getElement(artists,pos)
            if artist['ConstituentID'] == artist_ID:
                artists_artworks.append(artist['DisplayName'])
            pos += 1
    return artists_artworks

#Requirement 1
def ArtistsInRange(Artists,StartYear,EndYear,list_type):
    artistsInRange = lt.newList(datastructure=list_type)
    posList = 0
    while posList < lt.size(Artists):
        Artist = lt.getElement(Artists,posList)
        Year = int(Artist['BeginDate'])
        if Year >= StartYear and Year <= EndYear:
            lt.addLast(artistsInRange,Artist)
        posList += 1
    return artistsInRange


def SortChronologically(artistsInRange):
    for pos1 in range(lt.size(artistsInRange)):
        minPos = pos1
        for pos2 in range(pos1+1, lt.size(artistsInRange)):
            YearMin = lt.getElement(artistsInRange,minPos)['BeginDate'] 
            Year2 = lt.getElement(artistsInRange,pos2)['BeginDate'] 
            if Year2 < YearMin:
                minPos = pos2

        lt.exchange(artistsInRange,minPos,pos1)
    sortedArtists = artistsInRange
    return sortedArtists

#Requirement 2
def ArtworksInRange(Artworks,StartYear,EndYear,list_type):
    artworksInRange = lt.newList(datastructure=list_type)
    posList = 0
    while posList < lt.size(Artworks):
        Artwork = lt.getElement(Artworks,posList)
        Year = Artwork['DateAcquired']
        if Year >= StartYear and Year <= EndYear:
            lt.addLast(artworksInRange,Artwork)
        posList += 1
    return artworksInRange

def SortArtworks(artworksInRange,sort_type):
    if sort_type == "QUICKSORT":
        sortedList = qs.sort(artworksInRange,cmpArtworkByDate)
    elif sort_type == "INSERTION":
        sortedList = ins.sort(artworksInRange,cmpArtworkByDate)
    elif sort_type == "SHELL":
        sortedList = ss.sort(artworksInRange,cmpArtworkByDate)
    elif sort_type == "SELECTION":
        sortedList = scs.sort(artworksInRange,cmpArtworkByDate)
    else:
        sortedList = ms.sort(artworksInRange,cmpArtworkByDate)
    return sortedList

#Requirement 3
def encounterArtist(artists,artist_name):
    for artist in lt.iterator(artists):
        if artist['DisplayName'] == artist_name:
            return artist['ConstituentID']
    return 'NotFound'

def artistMediumInfo(artworks,artist_ID,list_type):
    mediums = {}
    maxIteUses = 0
    artist_mediums = 0
    artist_artworks = 0
    for artwork in lt.iterator(artworks):
        if artwork['ConstituentID'] == '[' + artist_ID + ']':
            artist_artworks += 1
            medium = artwork['Medium']
            if medium not in mediums:
                artist_mediums += 1
                mediums[medium] = lt.newList(datastructure=list_type)
                lt.addLast(mediums[medium],artwork)
                if maxIteUses == 0:
                    maxIteUses = 1
                    mostUsed = medium
            else:
                lt.addLast(mediums[medium],artwork)
                IteUses = lt.size(mediums[medium])
                if IteUses > maxIteUses:
                    maxIteUses = IteUses
                    mostUsed = medium
    return artist_artworks, artist_mediums, mostUsed, mediums[mostUsed]

#Requirement 4
def findArtistNationality(artistsIDs_map,artist_IDs,list_type):
    artwork_nationalities = lt.newList(datastructure=list_type)
    for artist_ID in (artist_IDs.replace('[','')).replace(']','').split(','):
        if map.contains(artistsIDs_map,artist_ID):
            artist = map.get(artistsIDs_map,artist_ID)['value']
            lt.addLast(artwork_nationalities,artist['Nationality']) 
    return artwork_nationalities

def nationalityArtworks(artworks,artists,list_type):
    artworksNationality = lt.newList(datastructure=list_type)
    nations = {}
    for artwork in lt.iterator(artworks):
        artists_ID = artwork['ConstituentID']
        artists_nationality = findArtistNationality(artists,artists_ID)
        nations_ite = []
        for nation in artists_nationality:
            if nation == '':
                nation = 'Unknown'
            if nation not in nations_ite:
                nations_ite.append(nation)
                if nation not in nations:
                    nations[nation] = lt.newList(datastructure=list_type)
                    lt.addLast(nations[nation], artwork)
                else:
                    lt.addLast(nations[nation], artwork)
    
    for nation in nations:
        num_artworks = lt.size(nations[nation])
        nationDict = {'Nation':nation,'NumbArtworks':num_artworks}
        lt.addLast(artworksNationality,nationDict)
    return artworksNationality, nations

def cmpArtworkByNumbWorks(nationality1, nationality2): 
    return nationality1['NumbArtworks'] > nationality2['NumbArtworks']

def sortNations(artworksNationality,nations,sort_type):
    if sort_type == "QUICKSORT":
        sortedList = qs.sort(artworksNationality,cmpArtworkByNumbWorks)
    elif sort_type == "INSERTION":
        sortedList = ins.sort(artworksNationality,cmpArtworkByNumbWorks)
    elif sort_type == "SHELL":
        sortedList = ss.sort(artworksNationality,cmpArtworkByNumbWorks)
    elif sort_type == "SELECTION":
        sortedList = scs.sort(artworksNationality,cmpArtworkByNumbWorks)
    else:
        sortedList = ms.sort(artworksNationality,cmpArtworkByNumbWorks)
    art_nation = lt.getElement(sortedList,0)['Nation']
    artworks_nation = nations[art_nation]
    return sortedList,art_nation,artworks_nation


#Requirement 5
def estimatePrice(artwork):
    measurements = ['Diameter (cm)','Height (cm)','Length (cm)','Weight (kg)','Width (cm)']
    enc_info = {}
    weight = 0
    radius = 0
    for measurement in measurements:
        if artwork[measurement] != '':
            if measurement == 'Weight (kg)':
                weight = float(artwork[measurement])
            elif measurement == 'Diameter (cm)':
                radius = float(artwork[measurement])/200
            else:
                amount = float(artwork[measurement])
                enc_info[measurement] = amount/100
    
    max_price = 0.0

    #Weight
    if weight != 0:
        if weight * 72 > max_price:
            max_price = weight * 72
    
    #Areas and Volumes with Radius
    if radius > 0:
        if len(list(enc_info.keys())) > 0:
            price = 0
            for measure in list(enc_info.keys()):
                price = (enc_info[measure]*radius*math.pi*2 + math.pi*radius**2)*72
                if price > max_price:
                    max_price = price
                price = (enc_info[measure]*math.pi*radius**2)*72
                if price > max_price:
                    max_price = price
        else:
            price = 4*math.pi*radius**2
            if price > max_price:
                    max_price = price
            price = (4*math.pi*radius**3)/3
            if price > max_price:
                    max_price = price
    #Areas
    elif len(list(enc_info.keys())) > 1:
        i = 0
        while i < len(list(enc_info.keys())) - 1:
            j = i + 1
            while j < len(list(enc_info.keys())): 
                M1 = enc_info[list(enc_info.keys())[i]]
                M2 = enc_info[list(enc_info.keys())[j]]
                price = M1*M2*72
                if price > max_price:
                    max_price = price
                j += 1
            i += 1
    #Volumes
    elif len(list(enc_info.keys())) > 2:
        i = 0
        while i < len(list(enc_info.keys())) - 2:
            j = i + 1
            while j < len(list(enc_info.keys()))-1: 
                k = j +1 
                while k < len(list(enc_info.keys())): 
                    M1 = enc_info[list(enc_info.keys())[i]]
                    M2 = enc_info[list(enc_info.keys())[j]]
                    M3 = enc_info[list(enc_info.keys())[k]]
                    price = M1*M2*M3*72
                    if price > max_price:
                        max_price = price
                    k += 1
                j += 1
            i += 1
    
    if max_price == 0.0:
        max_price = 48.0
    
    return max_price

def checkDeparment(artworks,department):
    encountered = False
    pos = 0
    while not encountered and pos < lt.size(artworks):
        artwork = lt.getElement(artworks,pos)
        if artwork['Department'] == department:
            encountered = True
        pos += 1
    return encountered

def moveDepartment(artworks,department,list_type):
    art2trans = 0
    est_price = 0
    est_weight = 0
    artworks_dep = lt.newList(datastructure=list_type)

    pos = 0
    while pos < lt.size(artworks):
        artwork = lt.getElement(artworks,pos)
        if artwork['Department'] == department:
            price = estimatePrice(artwork)
            if artwork['Weight (kg)'] != '':
                est_weight += float(artwork['Weight (kg)'])
            est_price += price
            art2trans += 1
            artwork['EstPrice'] = price
            lt.addLast(artworks_dep,artwork)
        pos += 1
    return est_price, art2trans, est_weight, artworks_dep

def cmpArtworkByDate(artwork1, artwork2): 
    return artwork1["DateAcquired"] < artwork2['DateAcquired']

def cmpArtworkByDate(artwork1, artwork2): 
    return artwork1["Date"] < artwork2['Date']

def cmpArtworkByEstPrice(artwork1, artwork2): 
    return artwork1["EstPrice"] > artwork2['EstPrice']

def artworksWithDate(artworks_dep,list_type):
    artworksWithDate = lt.newList(datastructure=list_type)
    for artwork in lt.iterator(artworks_dep):
        if artwork['Date'] != '':
            lt.addLast(artworksWithDate,artwork)
    return artworksWithDate
 
def SortArtworksByDate(artworks_dep,sort_type):
    if sort_type == "QUICKSORT":
        sortedList = qs.sort(artworks_dep,cmpArtworkByDate)
    elif sort_type == "INSERTION":
        sortedList = ins.sort(artworks_dep,cmpArtworkByDate)
    elif sort_type == "SHELL":
        sortedList = ss.sort(artworks_dep,cmpArtworkByDate)
    elif sort_type == "SELECTION":
        sortedList = scs.sort(artworks_dep,cmpArtworkByDate)
    else:
        sortedList = ms.sort(artworks_dep,cmpArtworkByDate)
    return sortedList

def SortArtworksByPrice(artworks_dep,sort_type):
    if sort_type == "QUICKSORT":
        sortedList = qs.sort(artworks_dep,cmpArtworkByEstPrice)
    elif sort_type == "INSERTION":
        sortedList = ins.sort(artworks_dep,cmpArtworkByEstPrice)
    elif sort_type == "SHELL":
        sortedList = ss.sort(artworks_dep,cmpArtworkByEstPrice)
    elif sort_type == "SELECTION":
        sortedList = scs.sort(artworks_dep,cmpArtworkByEstPrice)
    else:
        sortedList = ms.sort(artworks_dep,cmpArtworkByEstPrice)
    return sortedList

#Requirement 7
def encounterNationality(catalog,nationality):
    return map.contains(catalog['Nationality'],nationality)

def countArtworksNationality(catalog,nationality):
    artworks = map.get(catalog['Nationality'],nationality)
    return lt.size(artworks['value'])

#Performance & Efficiency
def createSample(listArt,sample_size):
    sub_list = lt.subList(listArt, 1, sample_size)
    sub_list = sub_list.copy()
    return sub_list

def createPercSample(artlist,percentage):
    sub_list = lt.subList(artlist, 1,lt.size(artlist)*percentage)
    sub_list = sub_list.copy()
    return sub_list

def start_endPerfTest():
    se_time = time.process_time()
    return se_time