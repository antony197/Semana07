# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 08:39:41 2022

@author: ANTONY

Los modulos te permitiran crear librerias de funcionalidades que puedas
utilizar o reutilizar en cualquier momento
"""

igv = 0.18

def obtenerIGVSubtotal(subtotal):
    return subtotal*igv
    
def obtenerTotalconSubtotal(subtotal):
    # subtotal + igv*subtotal
    # subtotal*(1+0.18)
    return subtotal*(1+igv)

def obtenerSubtotalconTotal(total):
    return total/(1+igv)

def obtenerIGVconTotal(total):
    return total-obtenerSubtotalconTotal(total)