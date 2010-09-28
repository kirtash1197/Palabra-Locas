#!/usr/bin/python
# -*- coding: utf-8 -*-

###
#Plantilla
###
def comp (list, intro, clas, gen):
		if list.count(intro)>0:
			print 'Felicidades,', clas, intro, 'es correct', gen
		if list.count(intro)==0:
			print 'No existe', clas, intro, ', lo siento.'

