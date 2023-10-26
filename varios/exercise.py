#Bancolombia requiere calcular los salarios de su nueva start up Pagui...Esta debe registrar nombre, apellido,cargo,area,salario,id...Requiere listar a los empleados y calcular el salario neto de cada uno,teniendo presente que si gana menos de 2 SMLV se le paga aux transporte.
#Requiere imprimir colilla de pago.
#Un empleado podrá ingresar al sistema y buscar su pago e imprimir su colilla de pago.
#Un analista de recursos humanos podrá visualizar todos los empleados y todas las colillas,ademas buscar por empleado...
#Que el analista de recursos humanos pueda validar el pago total de la nómina general.  
#Todo debe estar dentro de una función.



nombre_Completo=input("Ingrese su nombre completo")
documento_Identidad=int(input("Ingrese su documento de identidad"))
cargo=input("Ingrese el cargo que desempeña")
Area=input("Cuál es su Area")
salario=int(input("Ingrese el valor de su sueldo"))





my_data = {
    'nombre_Completo': nombre_Completo,
    'documento_Identidad': documento_Identidad,
    'cargo': cargo,
    'Area': Area,
    'salario': salario
}


print("Su nombre completo es "+ my_data["nombre_Completo"])
print("Su número de documento de identidad  es "+ str(my_data["documento_Identidad"]))
print("El cargo que actualmente desempeña es "+ my_data["cargo"])
print("El area asignada es "+ my_data["Area"])
print("El valor de su salario es "+str (my_data["salario"]))





