#!/usr/bin/env python
# -*- coding: utf-8 -*-

###
#Importacion
###

import comp
import lista.list
import random
import intro

###
#Recoleccion y comprobacion
###

letra=random.randrange(1, 31)

#Letra A
if letra==1:
	intro.intro(list_color_A, lista_marca_A)
	
#Letra B
if letra==2:
	intro.intro(list_color_B, lista_marca_B)

#Letra C
if letra==3:
	intro.intro(list_color_C, lista_marca_C)
#
###
#Final
###

#Puntuacion
raw_input()
