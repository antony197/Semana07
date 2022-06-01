# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 09:37:33 2022

@author: ANTONY
"""
# Importamos la libreria

import camelcase

## Tenemos una cadena llamada nombre y se desea que se muestre en formato
## titulo
nombre = "Antony Ccaccya Huaman"

print(nombre.upper())
print(nombre.title())

#Creamos un objeto llamado cam
cam = camelcase.CamelCase()
print("con camelcase....")

#Imprimimos el nombre en formato titulo
#Utilizamos camelcase
print(cam.hump(nombre))

#Para resolver el problema 
#Creamos otro objeto cam2
#Al definir el objeto, incluimos los argumentos
# 'flor' y 'leon'

cam2 = camelcase.CamelCase('ccaccya', 'huaman')
print(cam2.hump(nombre))