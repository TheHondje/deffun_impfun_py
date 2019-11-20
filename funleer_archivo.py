def leer_archivo():
	archivo=open("alumnos3.txt", "r")
	linea=archivo.readline()
	while linea!="":
		print(linea)
		linea=archivo.readline()
	archivo.close()	
	"""esta funcion lee un archivo X y cuando no hay mas lineas se cierra"""



	