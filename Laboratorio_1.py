import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox

# Clase principal de la calculadora
class CalculadoraPromedio(QWidget):
    def _init_(self):
        super()._init_()  # Llama al constructor de QWidget
        self.setWindowTitle("Calculadora de Promedio de Notas")  # Título de la ventana
        self.setGeometry(100, 100, 300, 200)  # Posición (x,y) y tamaño (ancho, alto)

        # === Crear los widgets ===
        self.label1 = QLabel("Ingrese Nota 1:")  # Etiqueta
        self.nota1 = QLineEdit()  # Caja de texto

        self.label2 = QLabel("Ingrese Nota 2:")
        self.nota2 = QLineEdit()

        self.label3 = QLabel("Ingrese Nota 3:")
        self.nota3 = QLineEdit()

        self.boton = QPushButton("Calcular Promedio")  # Botón
        self.resultado = QLabel("Promedio: -")  # Etiqueta de resultado

        # Conectar el botón con la función calcular_promedio
        self.boton.clicked.connect(self.calcular_promedio)

        # === Layout vertical ===
        layout = QVBoxLayout()
        layout.addWidget(self.label1)
        layout.addWidget(self.nota1)
        layout.addWidget(self.label2)
        layout.addWidget(self.nota2)
        layout.addWidget(self.label3)
        layout.addWidget(self.nota3)
        layout.addWidget(self.boton)
        layout.addWidget(self.resultado)

        # Asignar el layout a la ventana
        self.setLayout(layout)

    # Método que calcula el promedio
    def calcular_promedio(self):
        try:
            # Obtener y convertir las notas
            n1 = float(self.nota1.text())
            n2 = float(self.nota2.text())
            n3 = float(self.nota3.text())

            # Calcular el promedio
            promedio = (n1 + n2 + n3) / 3
            # Mostrar resultado en la etiqueta
            self.resultado.setText(f"Promedio: {promedio:.2f}")
        except ValueError:
            # Si se ingresan valores no numéricos
            QMessageBox.warning(self, "Error", "Por favor ingrese solo números.")

# === Ejecutar aplicación ===
if __name__ == "__main__":
    app = QApplication(sys.argv)  # Crear aplicación
    ventana = CalculadoraPromedio()  # Crear ventana
    ventana.show()  # Mostrar ventana
    sys.exit(app.exec_())  # Ejecutar el loop de eventos