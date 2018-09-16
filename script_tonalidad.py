#!/usr/bin/python
# -*- coding: utf-8 -*-


#import stdin
#import argparse
import re


"""
Script para determinar las posibles tonalidades a partir de las notas insertadas
Las notas se puede insertar del siguiente modo:
C
Cmaj7
Cmin7
Csus
C#

Por ahora, no se soporta poner "b". Cualquier bemol debe meterse como "#"
"""

def modo_jonico(nota):
	candidata = 0
	#Cadencia jonico 7: 1 - 1 - 1/2 - 1 - 1 - 1 - 1/2
	cadencia = (2, 2, 1, 2, 2, 2, 1)
	tonos = ('maj7', 'min7', 'min7', 'maj7', 'dom', 'min7', 'semi', 'maj7')
	abanico_notas = ('C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B')
	
	base = abanico_notas.index(nota.replace('maj7','').replace('min7',''))

	#print ' posicion para', nota,' en mayor', base

	tono = []
	index = 0
	varTmp1 = abanico_notas[base] 
	varTmp2 = tonos[index]
	varTmp3 = ''.join([varTmp1, varTmp2])
	tono.append(varTmp3)

	for value in cadencia:
		index = index + 1
		#print 'index es', index
		#print 'buscara posicion', (base+value) % len(abanico_notas)
		varTmp1 = abanico_notas[(base+value) % len(abanico_notas)] 
		#print ' nota encontrada', varTmp1
		varTmp2 = tonos[index]
		#print ' tono para nota encontrada', varTmp2
		varTmp3 = ''.join([varTmp1, varTmp2])
		tono.append(varTmp3)
		base += value
	
	#print 'Tonalidad', nota,'mayor:'
	#for value in tono:
	#	print '  ', value
	return (tono)

def modo_dorico(nota):
	candidata = 0
	#Cadencia dorico 7: 1 - 1/2 - 1 - 1 - 1 - 1/2 - 1
	cadencia = (2, 1, 2, 2, 2, 1, 2)
	tonos = ('min7', 'semi', 'maj7', 'min7', 'min7', 'maj7', 'dom', 'min7')
	abanico_notas = ('C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B')
	
	base = abanico_notas.index(nota.replace('maj7','').replace('min7',''))
	#print ' posicion para', nota,' en mayor', base

	tono = []
	index = 0
	varTmp1 = abanico_notas[base] 
	varTmp2 = tonos[index]
	varTmp3 = ''.join([varTmp1, varTmp2])
	tono.append(varTmp3)

	for value in cadencia:
		index = index + 1
		#print 'index es', index
		#print 'buscara posicion', (base+value) % len(abanico_notas)
		varTmp1 = abanico_notas[(base+value) % len(abanico_notas)] 
		#print ' nota encontrada', varTmp1
		varTmp2 = tonos[index]
		#print ' tono para nota encontrada', varTmp2
		varTmp3 = ''.join([varTmp1, varTmp2])
		tono.append(varTmp3)
		base += value
	
	#print 'Tonalidad', nota,'mayor:'
	#for value in tono:
	#	print '  ', value
	return (tono)

def modo_frigio(nota):
	candidata = 0
	#Cadencia frigio 7: 1/2 - 1 - 1 - 1- 1/2 - 1 - 1
	cadencia = (1, 2, 2, 2, 1, 2, 2)
	tonos = ('min7', 'maj7', 'dom', 'min7', 'dism', 'maj7', 'min7', 'min7')
	abanico_notas = ('C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B')
	
	base = abanico_notas.index(nota.replace('maj7','').replace('min7',''))
	#print ' posicion para', nota,' en mayor', base

	tono = []
	index = 0
	varTmp1 = abanico_notas[base] 
	varTmp2 = tonos[index]
	varTmp3 = ''.join([varTmp1, varTmp2])
	tono.append(varTmp3)

	for value in cadencia:
		index = index + 1
		#print 'index es', index
		#print 'buscara posicion', (base+value) % len(abanico_notas)
		varTmp1 = abanico_notas[(base+value) % len(abanico_notas)] 
		#print ' nota encontrada', varTmp1
		varTmp2 = tonos[index]
		#print ' tono para nota encontrada', varTmp2
		varTmp3 = ''.join([varTmp1, varTmp2])
		tono.append(varTmp3)
		base += value
	
	#print 'Tonalidad', nota,'mayor:'
	#for value in tono:
	#	print '  ', value
	return (tono)

def modo_lidio(nota):
	candidata = 0
	#Cadencia lidio 7: 1 - 1 - 1 - 1/2 - 1 - 1- 1/2
	cadencia = (2, 2, 2, 1, 2, 2, 1)
	tonos = ('maj7', 'dom', 'min7', 'dism', 'maj7', 'min7', 'min7', 'maj7')
	abanico_notas = ('C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B')
	
	base = abanico_notas.index(nota.replace('maj7','').replace('min7',''))
	#print ' posicion para', nota,' en mayor', base

	tono = []
	index = 0
	varTmp1 = abanico_notas[base] 
	varTmp2 = tonos[index]
	varTmp3 = ''.join([varTmp1, varTmp2])
	tono.append(varTmp3)

	for value in cadencia:
		index = index + 1
		#print 'index es', index
		#print 'buscara posicion', (base+value) % len(abanico_notas)
		varTmp1 = abanico_notas[(base+value) % len(abanico_notas)] 
		#print ' nota encontrada', varTmp1
		varTmp2 = tonos[index]
		#print ' tono para nota encontrada', varTmp2
		varTmp3 = ''.join([varTmp1, varTmp2])
		tono.append(varTmp3)
		base += value
	
	#print 'Tonalidad', nota,'mayor:'
	#for value in tono:
	#	print '  ', value
	return (tono)

def modo_mixolidio(nota):
	candidata = 0
	#Cadencia mixolidio 7: 1 - 1 - 1/2 - 1 - 1 - 1/2 - 1
	cadencia = (2, 2, 1, 2, 2, 1, 2)
	tonos = ('dom', 'min7', 'dism', 'maj7', 'min7', 'min7', 'maj7', 'dom')
	abanico_notas = ('C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B')
	
	base = abanico_notas.index(nota.replace('maj7','').replace('min7',''))
	#print ' posicion para', nota,' en mayor', base

	tono = []
	index = 0
	varTmp1 = abanico_notas[base] 
	varTmp2 = tonos[index]
	varTmp3 = ''.join([varTmp1, varTmp2])
	tono.append(varTmp3)

	for value in cadencia:
		index = index + 1
		#print 'index es', index
		#print 'buscara posicion', (base+value) % len(abanico_notas)
		varTmp1 = abanico_notas[(base+value) % len(abanico_notas)] 
		#print ' nota encontrada', varTmp1
		varTmp2 = tonos[index]
		#print ' tono para nota encontrada', varTmp2
		varTmp3 = ''.join([varTmp1, varTmp2])
		tono.append(varTmp3)
		base += value
	
	#print 'Tonalidad', nota,'mayor:'
	#for value in tono:
	#	print '  ', value
	return (tono)


def modo_eolico(nota):
	candidata = 0
	#Cadencia eolico 7: 1 - 1/2 - 1 - 1- 1/2 - 1 - 1
	cadencia = (2, 1, 2, 2, 1, 2, 2)
	tonos = ('min7', 'dism', 'maj7', 'min7', 'min7', 'maj7', 'dom', 'min7')
	abanico_notas = ('C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B')
	
	base = abanico_notas.index(nota.replace('maj7','').replace('min7',''))
	#print ' posicion para', nota,' en mayor', base

	tono = []
	index = 0
	varTmp1 = abanico_notas[base] 
	varTmp2 = tonos[index]
	varTmp3 = ''.join([varTmp1, varTmp2])
	tono.append(varTmp3)

	for value in cadencia:
		index = index + 1
		#print 'index es', index
		#print 'buscara posicion', (base+value) % len(abanico_notas)
		varTmp1 = abanico_notas[(base+value) % len(abanico_notas)] 
		#print ' nota encontrada', varTmp1
		varTmp2 = tonos[index]
		#print ' tono para nota encontrada', varTmp2
		varTmp3 = ''.join([varTmp1, varTmp2])
		tono.append(varTmp3)
		base += value
	
	#print 'Tonalidad', nota,'mayor:'
	#for value in tono:
	#	print '  ', value
	return (tono)


def modo_locria(nota):
	candidata = 0
	#Cadencia locria 7: 1/2 - 1 - 1- 1/2 - 1 - 1 - 1
	cadencia = (1, 2, 2, 1, 2, 2, 2)
	tonos = ('dism', 'maj7', 'min7', 'min7', 'maj7', 'dom', 'min7', 'dism')
	abanico_notas = ('C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B')
	
	base = abanico_notas.index(nota.replace('maj7','').replace('min7',''))
	#print ' posicion para', nota,' en mayor', base

	tono = []
	index = 0
	varTmp1 = abanico_notas[base] 
	varTmp2 = tonos[index]
	varTmp3 = ''.join([varTmp1, varTmp2])
	tono.append(varTmp3)

	for value in cadencia:
		index = index + 1
		#print 'index es', index
		#print 'buscara posicion', (base+value) % len(abanico_notas)
		varTmp1 = abanico_notas[(base+value) % len(abanico_notas)] 
		#print ' nota encontrada', varTmp1
		varTmp2 = tonos[index]
		#print ' tono para nota encontrada', varTmp2
		varTmp3 = ''.join([varTmp1, varTmp2])
		tono.append(varTmp3)
		base += value
	
	#print 'Tonalidad', nota,'mayor:'
	#for value in tono:
	#	print '  ', value
	return (tono)

def chequeo_tono(tono, notas_array):
	#print 'tono es', tono
	for value in notas_array:
		candidata = 0
		#print 'value vale', value
		if (value.find('#') != -1):
			for nota in tono:
				#print 'nota es', nota
				if nota.startswith(value):
					candidata = 1
					break 
		else:
			for nota in tono:
				#print 'nota vale', nota
				if (nota.startswith(value) and not (nota.find('#') != -1)):
					candidata = 1
					#print 'hizo match'
					break
		if not(candidata):
			break
	return(candidata)


def main():

	notas_input = raw_input("Inserta las notas separadas por espacio: ")
	notas_array = notas_input.split(' ')

	while ('' in notas_array):
		notas_array.remove('')
		#index = notas_array.index('')
		#notas_array.pop(index)

	posibles_tonos = []

	for index in range(0,len(notas_array)):
		#Chequeo Jonico Mayor7 (I)
		tono = modo_jonico(notas_array[index])
		candidata = chequeo_tono(tono, notas_array)
		if (candidata):
			posibles_tonos.append({})
			posibles_tonos[-1]['modo'] = 'Jonico I (maj7)'
			posibles_tonos[-1]['escala'] = []
			posibles_tonos[-1]['escala'].append(tono)

		#Chequeo Dorico Min7 (II)
		tono = modo_dorico(notas_array[index])
		candidata = chequeo_tono(tono, notas_array)
		if (candidata):
			posibles_tonos.append({})
			posibles_tonos[-1]['modo'] = 'Dorico II (min7)'
			posibles_tonos[-1]['escala'] = []
			posibles_tonos[-1]['escala'].append(tono)

		#Chequeo Frigio Min7  (III)
		tono = modo_frigio(notas_array[index])
		candidata = chequeo_tono(tono, notas_array)
		if (candidata):
			posibles_tonos.append({})
			posibles_tonos[-1]['modo'] = 'Frigio III (min7)'
			posibles_tonos[-1]['escala'] = []
			posibles_tonos[-1]['escala'].append(tono)

		#Chequeo Lidio Maj (IV)
		tono = modo_lidio(notas_array[index])
		candidata = chequeo_tono(tono, notas_array)
		if (candidata):
			posibles_tonos.append({})
			posibles_tonos[-1]['modo'] = 'Lidio IV (maj7)'
			posibles_tonos[-1]['escala'] = []
			posibles_tonos[-1]['escala'].append(tono)

		#Chequeo Mixolidio Dom (V)
		tono = modo_mixolidio(notas_array[index])
		candidata = chequeo_tono(tono, notas_array)
		if (candidata):
			posibles_tonos.append({})
			posibles_tonos[-1]['modo'] = 'Mixolidio V (dom)'
			posibles_tonos[-1]['escala'] = []
			posibles_tonos[-1]['escala'].append(tono)

		#Chequeo Eolico Min7 (VI)
		tono = modo_eolico(notas_array[index])
		candidata = chequeo_tono(tono, notas_array)
		if (candidata):
			posibles_tonos.append({})
			posibles_tonos[-1]['modo'] = 'Eolico VI (min7)'
			posibles_tonos[-1]['escala'] = []
			posibles_tonos[-1]['escala'].append(tono)

		#Chequeo Locria (VII)
		tono = modo_locria(notas_array[index])
		candidata = chequeo_tono(tono, notas_array)
		if (candidata):
			posibles_tonos.append({})
			posibles_tonos[-1]['modo'] = 'Locria VII (dism)'
			posibles_tonos[-1]['escala'] = []
			posibles_tonos[-1]['escala'].append(tono)

	if (len(posibles_tonos)):
		print '\nPosibles tonalidades:'
		for index in range(0,len(posibles_tonos)):
			print ' # Tonalidad', posibles_tonos[index]['modo']
			print '   Escala', posibles_tonos[index]['escala']
	else:
		print '\nNo se han encontrado posibles tonos'

	#for line in sys.stdin:
    #	print line

##############
#Main Program
##############

if __name__ == "__main__":
	print '\n## Script started\n'
	main()
	print '\n## Script finished\n'