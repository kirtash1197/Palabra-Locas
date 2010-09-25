#!/usr/bin/env python
salir='no'
while salir=='no':
	colores = ['amarillo', 'rojo', 'azul', 'verde', 'negro', 'blanco', 'violeta', 'naranja', 'gris', 'dorado', 'plateado']
	print 'Color'
	color_introducido = raw_input()
	if colores.count(color_introducido)>0:
		print 'Felicidades, el color ' + color_introducido + ' es correcto.'
	if colores.count (color_introducido)==0:
		print 'No existe el color ' + color_introducido + ' , lo siento.'
	print 'Si desea salir, teclee "si". Si no, teclee "no"'
	salir=raw_input()

if salir=='si':
	print 'Gracias por usar el script'
raw_input()
