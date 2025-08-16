
def calcular_renta(patrimonio, ingreso, tarjetacred, consignacionesycompras):
    """valores asignados por la DIAN,"""
    tope_patrimonio = 211793000
    tope_ingreso = 65981000
    tope_consumo = 69718600
    tope_consignaciones = 69718600

    if (patrimonio > tope_patrimonio or
        ingreso > tope_ingreso or
        tarjetacred > tope_consumo or
        consignacionesycompras > tope_consignaciones):
        print("Debe declarar renta")
    else:
        print("No debe declarar renta")

def valores_declaracion():
    patrimonio = float(input("Ingrese su patrimonio bruto: "))
    ingreso = float(input("Ingrese su ingreso bruto: "))
    tarjetacred = float(input("Ingrese el consumo con tarjeta de crédito: "))
    consignacionesycompras = float(input("Ingrese las consignaciones y compras: "))
    calcular_renta(patrimonio, ingreso, tarjetacred, consignacionesycompras)

valores_declaracion()