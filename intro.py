#!/usr/bin/python
# -*- coding: utf-8 -*-

def intro (list_color, list_marca):
	#Color 
	intro_color = raw_input('>Color\n')
	comprobacion.comp(list_color, intro_color, 'el color', 'o.')
	#Marca
	intro_marca = raw_input('>Marca\n')
	comprobacion.comp(list_marca, intro_marca, 'la marca', 'a.')
