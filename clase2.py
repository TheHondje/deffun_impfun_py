def creararchivo():
	archivo= open("alumnos3.txt", "w")
	archivo.close()

#leer un archivo

def leer_archivo():
	archivo=open("alumnos3.txt", "r")
	linea=archivo.readline()
	while linea!="":
		print(linea)
		linea=archivo.readline()
	archivo.close()	


def escribirarchivo():
	archivo= open("alumnos3.txt" , "a")
	archivo.write(input("ingrese datos: "))
	mas_datos = input("desea seguir agregando datos: ")

	while mas_datos== "si":
		archivo.write(input("ingrese datos:"))
		mas_datos = input("desea seguir agregando datos: ")

	if mas_datos== "no":
		print("Gracias por utilizar el programa")
	elif mas_datos!= "no" or "si":
		print("la respuesta es incorrecta")
	archivo.close()	

			




escribirarchivo()

leer_archivo()
