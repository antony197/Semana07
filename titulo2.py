# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 09:52:15 2022

@author: ANTONY
"""

# Importamos la librería

import camelcase

# Tenemos una cadena llamada nombre y se desea 
# que se muestre en formato título
nombre = "flor elizabeth Cerdán león"

print(nombre.upper())
print(nombre.title())

# Creamos un objeto llamado cam
cam= camelcase.CamelCase()
print("Con camelcase....")

# Imprimimos el nombre en formato título
#Utilizamos camelcase
print(cam.hump(nombre))

# Para resolver el problema
# Creamos otro objeto cam2
# Al definir el objeto, incluimos los argumentos
# 'flor' y