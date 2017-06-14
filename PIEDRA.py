CREAR EL JUEGO PIEDRA PAPEL Y TIJERA

-Usar while 
-Diccionario
-argparse

La app debera solicitar al usuario 'piedra' ,'papel' o 'tijera'
la app debera de generar un valor aleatorio entre 'piedra','papel' o 'tijera'
la app debera de imprimir el resultado de cada mano 
la app debera de imprimir el ganador entre maquina y usuario (El que gane 3 rondas)


import random
from time import sleep


print"Bienvenida chama a jugar esto"
print""
sleep(2)
print"Jugamos al mejor de tres o queres cambiar"
sleep(1)
print""




#Funcion que realiza la logica del juego
def juego(intentos):
x = 0
tu = 0
pc = 0
while str(x)!= intentos:
print"Piedra,papel o tijera"
opcion = raw_input()
opcion = opcion.lower()
azar = ramdom.choice(["piedra", "papel", o "tijera"])
if opcion == azar:
	print"El pc tambien quiso jugar",azar
	print""
	elif azar == "tijera" and opcion == "papel":
	x += 1
	pc += 1
	print "El PC elijio",azar
	print"TU",tu,"PC",pc 
	print""
	elif azar == "tijera" and opcion =="piedra":
	x +=1
	tu +=1
	print "El PC saco",azar
	print"TU",tu,"PC",pc 
	print""
elif azar=="piedra" and opcion=="tijera":
	x +=1
	pc +=1
	print "El PC saco",azar
	print"TU",tu,"PC",pc 
	print""
elif azar =="piedra" and opcion =="papel":
	x +=1
	tu +=1
print "El PC saco",azar
	print"TU",tu,"PC",pc 
	print""
elif azar =="papel" and opcion =="tijera":
	x +=1
	tu +=
	print "El PC saco",azar
	print"TU",tu,"PC",pc 
	print""
else:
	print"Opcion incorrecta,vuelva a intentarlo"


	print""

	if pc >tu:
		print"gano el PC",pc,"a",tu
	elif pc==tu:
		print"Empataron",tu."a",pc
		else:
		print"Ganaste",tu,"a",pc

		print""
		print"PARTIDA TERMINADA"


		def main():
			print"Escribe 1 para jugar al mejor de tres"
			print"Escribe 2 para cambiar al tipo de juego"


			opcion = input()

			if opcion ==1:
				juego("3")
				print""
				restart =raw_input("Queres jugar de nuevo chama?(s/n")
				restart = restart.lower()
				if restart =="s":
					print""
					main()
				else:
				intentos = raw_input("Vos decis,jugamos al mejor de:")
				juego(intentos)
				print""
				restart = raw_input("Queres jugar de nuevo chama?(s/n):")
				restart = restart.lowe()
				if restart =="s":
					print""
					main()
				else:
					print"FIN"
					main()