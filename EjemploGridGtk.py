import gi
import CaixaCor

gi.require_version("Gtk","3.0")
from gi.repository import Gtk, Gdk, GObject

class EjemploBoxColor (Gtk.Window):
    def __init__(self):
        super().__init__()
        self.set_title("Ejemplo de uso de Layout")

        rojo = CaixaCor.CaixaCor("red")
        azul = CaixaCor.CaixaCor("blue")
        verde = CaixaCor.CaixaCor("green")
        naranja = CaixaCor.CaixaCor("orange")
        amarillo = CaixaCor.CaixaCor("yellow")
        rosa = CaixaCor.CaixaCor("pink")
        marron = CaixaCor.CaixaCor("brown")
        lila = CaixaCor.CaixaCor("purple")
        negro = CaixaCor.CaixaCor("black")

        malla = Gtk.Grid()
        malla.attach(rojo,1,1,1,3)
        malla.attach_next_to(marron,rojo,Gtk.PositionType.RIGHT,1,1)
        malla.attach_next_to(amarillo,marron,Gtk.PositionType.RIGHT,1,1)
        malla.attach_next_to(naranja,amarillo,Gtk.PositionType.RIGHT,1,1)
        malla.attach_next_to(verde,marron,Gtk.PositionType.BOTTOM,2,2)
        malla.attach_next_to(lila,verde,Gtk.PositionType.RIGHT,1,2)
        malla.attach_next_to(azul,rojo,Gtk.PositionType.BOTTOM,2,1)
        malla.attach_next_to(rosa,azul,Gtk.PositionType.RIGHT,1,1)
        malla.attach_next_to(negro,rosa,Gtk.PositionType.RIGHT,1,1)

        self.add(malla)
        self.connect("delete-event", Gtk.main_quit)
        self.show_all()

if __name__ == "__main__":
    EjemploBoxColor()
    Gtk.main()