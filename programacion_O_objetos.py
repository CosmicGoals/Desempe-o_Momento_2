"""Programaciòn Orientada a objetos


-Abtracción = Concreyto fisico, conceptual(Identificar que atributos tiene y caractaristicas de esos onjetos y su comportamiento)
Reutilizacion de codigo, evitar redundar
-Hereencia
-Encapsulamiento
-Polimorfismo

Polismorfismo=Metodos =Sobreescritura (teniendo dos clases donde se evidencie acciones diferente pero usando el mismo metodo), sobrecarga(Dos formas de hacer algo usando Mismo metodo dentro de la misma clase)"""

def imprimir(valor):
    print(valor)
    
def calcular_area(base,altura,imprimir):
    area= base*altura   
    imprimir(area)
    
base=50
altura=5
calcular_area(base,altura,imprimir)

salario=float(input("Ingrese el valor de su salario"))
def aux_trans(salario,pago_neto):
    if (salario<2320000):
        print(f"salario Neto if: {pago_neto+140606}")
    else:
        print(f"salario neto else: {pago_neto}")


def pago_neto(salario,aux_trans):
    eps=lambda salario:salario*0.04
    pension=lambda salario:salario*0.04
    pago_neto=salario-eps(salario)-pension(salario)
    
    aux_trans(salario,pago_neto)
    
pago_neto(salario,aux_trans)