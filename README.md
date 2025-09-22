# 📘 Calculadora de Promedio de Notas

##  Integrantes
- Franklin Aldahir Portillo Flores  
- Jeremias Neftaly Fuentes Méndez  

##  Objetivo de la Actividad
Desarrollar interfaces gráficas funcionales mediante el uso de la biblioteca *PyQt5 en Python*, aplicando los conocimientos de la librería y resolviendo un problema de la vida real.

##  Planteamiento del Problema
En el ámbito educativo, estudiantes y docentes necesitan calcular promedios de notas de forma rápida y precisa. Hacerlo manualmente puede ser tedioso y propenso a errores, especialmente cuando se manejan varias calificaciones.

##  Solución Propuesta
Se creó una aplicación con *PyQt5* que permite ingresar tres notas a través de una interfaz gráfica sencilla y calcular automáticamente el promedio.  
La solución facilita el trabajo de estudiantes y docentes, mostrando el resultado de manera inmediata y validando que los datos ingresados sean correctos.



Explicación del código

Importaciones
Se importan las librerías necesarias:

sys para manejar la salida del programa.

PyQt5.QtWidgets para crear la interfaz gráfica (ventana, etiquetas, botones, cuadros de texto, etc.).

Clase CalculadoraPromedio

Hereda de QWidget, que es el contenedor básico de PyQt5.

En el constructor (_init_) se configuran la ventana y los elementos: etiquetas, cajas de texto para las notas, un botón y un label donde se muestra el resultado.

Se organiza todo con un QVBoxLayout (layout vertical).

Botón "Calcular Promedio"

Está conectado al método calcular_promedio().

Cuando se presiona, obtiene los valores de las cajas de texto, los convierte a float, calcula el promedio y lo muestra en la etiqueta de resultado.

Manejo de errores

Si el usuario escribe algo que no es un número, se lanza una advertencia con QMessageBox.warning.

Bloque principal

Verifica si el archivo se ejecuta directamente (if _name_ == "_main_":).

Se crea una instancia de la aplicación (QApplication) y de la ventana (CalculadoraPromedio).

Finalmente, se muestra la ventana y se mantiene abierta hasta que el usuario la cierre.