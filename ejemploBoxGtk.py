import gi
import CaixaCor

gi.require_version("Gtk","3.0")
from gi.repository import Gtk, Gdk, GObject

class EjemploBoxColor (Gtk.Window):
    def __init__(self, caixaCor=None):
        super().__init__()
        self.set_title("Ejemplo de uso de Layout de caja")

        caja = Gtk.Box (orientation = Gtk.Orientation.HORIZONTAL, spacing = 10)
        cajaV1 = Gtk.Box (orientation = Gtk.Orientation.VERTICAL, spacing = 10)
        cajaV1.pack_start(CaixaCor.CaixaCor("red"),True,True,5)
        cajaV1.pack_start(CaixaCor.CaixaCor("blue"),True,True,5)
        cajaV1.pack_start(CaixaCor.CaixaCor("green"),True,True,5)
        caja.pack_start(cajaV1, True, True, 5)
        caja.pack_start(CaixaCor.CaixaCor('yellow'), True,True,5)
        cajaV2 = Gtk.Box (orientation = Gtk.Orientation.VERTICAL, spacing = 10)
        cajaV2.pack_start(CaixaCor.CaixaCor('orange'),True,True,5)
        cajaV2.pack_start(CaixaCor.CaixaCor('purple'),True,True,5)
        caja.pack_start(cajaV2,True,True,5)

        self.add(caja)
        self.connect("delete-event", Gtk.main_quit)
        self.show_all()

if __name__ == "__main__":
    EjemploBoxColor()
    Gtk.main()
