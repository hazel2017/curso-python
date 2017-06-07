variable_uno = 'Hola'
variable_dos = 1
variable_tres = 2.3

#concatenacion 
cadena = 'cadena uno' +  'cadena dos'

#Interpolacion
otra_cadena = 'Hola{}'.format('un valor')
variable_cuatro = 'Hola {0} {1}'.format('val', 'val2')
var = 'Hola {variable1} {variable2}'.format(variable1='val', variable2='val2')

def mi_funcion(val):
	print('dentro de mi funcion') # un comentario 
	print(otra_cadena)
	print(variable_cuatro)
	print(var)

if __name__== '__main__':
 print('hola mundo')
 mi_funcion(10)

 parser = argparse.ArgumentParse()
 parser.add_argument('nombre')
 parser.add_argument('apellido')
 args = parser.parser_args()

 print(args.nombre)
 print(args.apellido)
 variable_cuatro.format(args.nombre, args.apellido)
 print(variable_cuatro)
