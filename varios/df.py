saludo="Hola python"

def imprimir(saludo):
    print(saludo)
    
imprimir(saludo)

#calcular masa corporal"""

def calcularImc(peso, altura):
    imc=peso/(altura*altura)
    print(imc)
    
calcularImc(90,1.78)

salario=2000000

def calcularSalud(salario):
    eps= salario*0.04
    return eps

def calcularPension(salario):
    pension = salario*0.04
    return pension
#---------------------------------------
def calcularSalarioNeto(salario,eps,pension):
    salario_neto=salario-eps-pension
    print(salario_neto)
    
eps=calcularSalud(salario)
pension=calcularPension(salario)
calcularSalarioNeto(salario,eps,pension)
#---------------------------------------------
def calcularSalarioNeto2(salario):
    eps=calcularSalud(salario)
    pension=calcularPension(salario)
    salario_neto=salario-eps-pension
    print(salario_neto)

calcularSalarioNeto2(salario)

#---------------------------------------------

def registro(*items):
    print(f"Los datos son: {items[:4]}")

registro("pepito","perez",25,"pepito@gmail.com")


def calcularPagoNomina(salario):
    pago_eps=lambda salario: salario*0.04
    pago_pension=lambda salario: salario*0.04
    salario_neto= salario-pago_eps(salario)-pago_pension(salario)
    print (salario_neto)
    
calcularPagoNomina(1000000)



nombre="giovanni"

Edad= 28

Bienvenida=(f"Bienvenido  + {nombre} +  tu edad es de {Edad}")

print(Bienvenida)


print("edad"  in Bienvenida)



