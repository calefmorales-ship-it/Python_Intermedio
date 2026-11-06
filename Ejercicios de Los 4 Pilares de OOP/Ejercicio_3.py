# Clase Printer: representa una impresora.
# Tiene un método para imprimir documentos.
class Printer:

    def print_document(self, document):
        print(f"Printing document: {document}")


# Clase Scanner: representa un escáner.
# Tiene un método para escanear documentos.
class Scanner:

    def scan_document(self, document):
        print(f"Scanning document: {document}")


# Clase MultifunctionDevice:
# Hereda de dos clases: Printer y Scanner.
# Por lo tanto, obtiene los métodos de ambas clases.
class MultifunctionDevice(Printer, Scanner):
    pass


# Creamos un objeto de la clase MultifunctionDevice.
device = MultifunctionDevice()


# Utilizamos el método heredado de la clase Printer.
device.print_document("Report.pdf")


# Utilizamos el método heredado de la clase Scanner.
device.scan_document("Contract.pdf")