# Calculadora de Declaración de Renta (Colombia)

Este repositorio contiene un programa en **Python** que determina si una persona debe declarar renta en Colombia, de acuerdo con los topes establecidos por la DIAN.

## Descripción

El programa solicita al usuario la siguiente información financiera:

- Patrimonio bruto
- Ingreso bruto
- Consumo con tarjeta de crédito
- Consignaciones y compras

Con estos datos, el sistema los compara frente a los topes definidos por la DIAN y muestra si el usuario debe o no declarar renta.

## Topes de referencia (DIAN)

Los valores utilizados en este programa son:

- Patrimonio bruto: `211,793,000`
- Ingreso bruto: `65,981,000`
- Consumo con tarjeta de crédito: `69,718,600`
- Consignaciones y compras: `69,718,600`

**Nota**: Estos valores corresponden a una vigencia específica y pueden cambiar cada año fiscal. Se recomienda actualizarlos periódicamente según la normativa de la DIAN.

## Instalación y uso

1. Clonar este repositorio:

   ```bash
   git clone https://github.com/tuusuario/calculadora-renta.git
   cd calculadora-renta

