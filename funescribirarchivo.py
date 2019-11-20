def escribirarchivo():
	archivo= open("alumnos3.txt" , "a")
	archivo.write(input("ingrese datos: "))
	mas_datos = input("desea seguir agregando datos: ")

	while mas_datos== "si":
		archivo.write(input("ingrese datos: "))
		mas_datos = input("desea seguir agregando datos: ")

	if mas_datos== "no":
		print("Gracias por utilizar el programa")
	elif mas_datos!= "no" or "si":
		print("la respuesta es incorrecta")
	archivo.close()	