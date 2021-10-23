"""
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
 """

import config as cf
from DISClib.ADT import list as lt
import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros
def initCatalog(list_type):
    """
    Llama la funcion de inicializacion del catalogo del modelo.
    """
    if(list_type == 1):
        list_type = "ARRAY_LIST"
    else:
        list_type = "SINGLE_LINKED"
    catalog = model.newCatalog(list_type)
    return catalog

# Funciones para la carga de datos
def loadArtists(catalog):
    filename = cf.data_dir + 'MoMA/Artists-utf8-large.csv'
    input_file = csv.DictReader(open(filename, encoding='utf-8'))
    for artist in input_file:
        model.addArtists(catalog,artist)
        model.addArtistsIDs(catalog,artist)

def loadArtworks(catalog,list_type):
    filename = cf.data_dir + 'MoMA/Artworks-utf8-large.csv'
    input_file = csv.DictReader(open(filename, encoding='utf-8'))
    for artwork in input_file:
        model.addArtworks(catalog,artwork)
        model.loadMedium(catalog,artwork,list_type)
        model.loadNationality(catalog,artwork,list_type)

#Funciones generales
def selectMapType(map_type):
    if map_type == 1:
        map_type = "CHAINING"
    else:
        map_type = "PROBING"
    return map_type

#Requirement 0
def encounterMedium(catalog,medium):
    return model.encounterMedium(catalog,medium)

def sortArtworksByDate(artworks_dep,sort_type):
    if(sort_type == 1):
        sort_type = "QUICKSORT"
    elif(sort_type == 2):
        sort_type = "INSERTION"
    elif(sort_type == 3):
        sort_type = "SHELL"
    elif(sort_type == 4):
        sort_type = "SELECTION"
    else:
        sort_type = "MERGE"
    return model.SortArtworksByDate(artworks_dep,sort_type)

def oldestArtworks(catalog,medium,sort_type,list_type):
    return model.oldestArtworks(catalog,medium,sort_type,list_type)  

#Requirement 1
def ArtistsInRange(Artists,StartYear,EndYear,list_type,map_type):
    map_type = selectMapType(map_type)
    return model.ArtistsInRange(Artists,StartYear,EndYear,list_type,map_type)

def SortChronologically(artistsInRange,StartYear,EndYear,list_type):
    return model.SortChronologically(artistsInRange,StartYear,EndYear,list_type)

#Requirement 2
def findArtist(artists,artist_IDs):
    return model.findArtist(artists,artist_IDs)

def ArtworksInRange(Artworks,StartYear,EndYear,list_type,map_type):
    return model.ArtworksInRange(Artworks,StartYear,EndYear,list_type,map_type)

def SortArtworks(artworks,sort_type,list_type):
    if(sort_type == 1):
        sort_type = "QUICKSORT"
    elif(sort_type == 2):
        sort_type = "INSERTION"
    elif(sort_type == 3):
        sort_type = "SHELL"
    elif(sort_type == 4):
        sort_type = "SELECTION"
    else:
        sort_type = "MERGE"
    return model.SortArtworks(artworks,sort_type,list_type)

#Requirement 3
def encounterArtist(artists,artist_name):
    return model.encounterArtist(artists,artist_name)

def artistMediumInfo(artworks,artist_ID,list_type,map_type):
    return model.artistMediumInfo(artworks,artist_ID,list_type,map_type)

#Requirement 4
def nationalityArtworks(artworks,catalog,list_type,map_type):
    return model.nationalityArtworks(artworks,catalog,list_type,map_type)

def sortNations(artworksNationality,nation,sort_type):
    return model.sortNations(artworksNationality,nation,sort_type)

#Requirement 5
def checkDepartment(artworks,department):
    return model.checkDeparment(artworks,department)

def moveDepartment(artworks,department,map_type):
    return model.moveDepartment(artworks,department,map_type)

def SortArtworksByDate(artworks_dep,sort_type,list_type):
    if(sort_type == 1):
        sort_type = "QUICKSORT"
    elif(sort_type == 2):
        sort_type = "INSERTION"
    elif(sort_type == 3):
        sort_type = "SHELL"
    elif(sort_type == 4):
        sort_type = "SELECTION"
    else:
        sort_type = "MERGE"
    return model.SortArtworksByDate(artworks_dep,sort_type,list_type)

def SortArtworksByPrice(artworks_dep,sort_type,list_type):
    if(sort_type == 1):
        sort_type = "QUICKSORT"
    elif(sort_type == 2):
        sort_type = "INSERTION"
    elif(sort_type == 3):
        sort_type = "SHELL"
    elif(sort_type == 4):
        sort_type = "SELECTION"
    else:
        sort_type = "MERGE"
    return model.SortArtworksByPrice(artworks_dep,sort_type,list_type)

#Requirement 7
def encounterNationality(catalog,nationality):
    return model.encounterNationality(catalog,nationality)

def countArtworksNationality(catalog,nationality):
    return model.countArtworksNationality(catalog,nationality)

#Performance & Efficiency
def createSample(listArt,sample_size):
    return model.createSample(listArt,sample_size)

def createPercSample(artlist,percentage):
    return model.createPercSample(artlist,percentage)

def start_endPerfTest():
    return model.start_endPerfTest()