from cProfile import label

import gi
gi.require_version("Gtk","3.0")
from gi.repository import Gtk

class VentanaPrincipal(Gtk.Window):
    def __init__(self):
        super().__init__()
        self.set_title("Primera aplicación con GTK")

        cajaV = Gtk.Box (orientation = Gtk.Orientation.VERTICAL, spacing = 10)

        lblSaludo = Gtk.Label(label = "Introduce tu nombre")
        cajaV.pack_start(lblSaludo, True, True, 5)
        txtSaludo = Gtk.Entry()
        cajaV.pack_start(txtSaludo, False, True, 5)
        btnSaludo = Gtk.Button(label = "Saludar")
        btnSaludo.connect("clicked", self.on_btnSaludo_clicked, txtSaludo, lblSaludo)
        txtSaludo.connect("activate", self.on_btnSaludo_clicked, txtSaludo, lblSaludo)
        cajaV.pack_start(btnSaludo, False, False, 5)

        self.add(cajaV)
        self.connect("delete-event", Gtk.main_quit)
        self.show_all()

    def on_btnSaludo_clicked (self, boton, cuadroTexto, etiqueta):

        if cuadroTexto.get_text() == "":
            etiqueta.set_text("Escribe un nombre...")
            return

        nombre = cuadroTexto.get_text()
        etiqueta.set_text("Hola " + nombre)
        cuadroTexto.set_text("")


if __name__ == "__main__":
    VentanaPrincipal()
    Gtk.main()