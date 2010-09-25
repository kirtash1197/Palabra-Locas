#!/usr/bin/env python
#
#Listas
#

list_color = ['amarillo', 'rojo', 'azul', 'verde', 'negro', 'blanco', 'violeta', 'naranja', 'gris', 'dorado', 'plateado']
list_marca = ['coca-cola', 'nike']

#
#Plantilla
#

def comp (list, intro, clas, gen):
		if list.count(intro)>0:
			print 'Felicidades, ' + clas + intro + ' es correct' + gen
		if list.count(intro)==0:
			print 'No existe ' + clas + intro + ' , lo siento.'
#
#Recoleccion y comprobacion
#

#Color
print '>Color'
intro_color = raw_input()
comp(list_color, intro_color, 'el color ', 'o.')
#Marca
print '>Marca'
intro_marca = raw_input()
comp(list_marca, intro_marca, 'la marca ', 'a.')

#
#Final
#

#Puntuacion
