# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 10:57:59 2022

@author: ANTONY
"""

archivo = open("noticia.txt","at")
#\n es para agregar el contenido de una linea final
contenido="\nFuente : RPP"

archivo.write(contenido)
archivo.close()