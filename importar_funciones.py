from funescribirarchivo import escribirarchivo
from funleer_archivo import leer_archivo
from funcreararchivo import creararchivo



print("bienvenidos al programa para cargar datos de alumnos")

print("-----------------------------------------------------------------------")
print("si desea crear un archivo ingrese: 1")
print("si desea modificar un archivo ingrese: 2")
print("si desea leer un archivo ingrese: 3")
print("-----------------------------------------------------------------------")
operacion= input("ingrese la operacion q desea realizar: ")




if operacion == "1":
	print(creararchivo())

elif operacion == "2":
	print(escribirarchivo())

elif operacion ==	"3":
	print(leer_archivo())
else:
	Print("opcion incorrecta")
















