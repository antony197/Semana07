# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 10:32:58 2022

@author: ANTONY
"""

noticia = open("noticia.txt","rt",encoding='utf8')
datos_noticias = noticia.read()
print(datos_noticias)