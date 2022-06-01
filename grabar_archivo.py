# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 10:47:24 2022

@author: ANTONY
"""

archivo = open("archivo_de_prueba.txt","wt")
contenido = "Linea1 Hola amigos ¿Cómo están?\nLinea2 Bienvenido"
archivo.write(contenido)
archivo.close()