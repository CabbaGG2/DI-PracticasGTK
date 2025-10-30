import gi
import CaixaCor

gi.require_version("Gtk","3.0")
from gi.repository import Gtk, Gdk, GObject

class Ejemplo (Gtk.Window):
    def __init__(self):
        super().__init__()
        self.set_title("Ventana Windows")

        rojo = CaixaCor.CaixaCor("red")
        azul = CaixaCor.CaixaCor("blue")
        verde = CaixaCor.CaixaCor("green")
        naranja = CaixaCor.CaixaCor("orange")
        amarillo = CaixaCor.CaixaCor("yellow")
        rosa = CaixaCor.CaixaCor("pink")
        marron = CaixaCor.CaixaCor("brown")
        lila = CaixaCor.CaixaCor("purple")
        negro = CaixaCor.CaixaCor("black")
        listasHojas = ["Hoja1","Documento 2","Hoja3","Hoja4","Documento 5"]

        malla1 = Gtk.Grid()
        lista = Gtk.TreeView()
        boton1 = Gtk.RadioButton(label="boton 1")
        boton2 = Gtk.RadioButton(label="boton 2",group=boton1)
        boton3 = Gtk.RadioButton(label="boton 3",group=boton1)
        boton4 = Gtk.RadioButton(label="boton 4",group=boton1)
        boton5 = Gtk.Button(label="Cerrar")

        malla1.attach(lista,1,1,1,6)
        malla1.attach_next_to(boton1,lista, Gtk.PositionType.RIGHT,1,1)
        malla1.attach_next_to(boton2,boton1, Gtk.PositionType.BOTTOM,1,1)
        malla1.attach_next_to(boton3,boton2, Gtk.PositionType.BOTTOM,1,1)
        malla1.attach_next_to(boton4,boton3, Gtk.PositionType.BOTTOM,1,1)
        malla1.attach_next_to(boton5,boton4,Gtk.PositionType.BOTTOM,1,1)

        malla2 = Gtk.Grid()
        cuadroTexto1 = Gtk.Entry()
        cuadroTexto2 = Gtk.Entry()
        desplegable = Gtk.ComboBox()

        malla2.attach(cuadroTexto1,1,1,1,1)
        malla2.attach_next_to(cuadroTexto2,cuadroTexto1, Gtk.PositionType.BOTTOM,1,1)
        malla2.attach_next_to(desplegable,cuadroTexto2,Gtk.PositionType.BOTTOM,1,1)

        malla3 = Gtk.Grid()


        malla = Gtk.Grid()
        malla.attach(malla1, 1, 1, 4, 4)
        malla.attach_next_to(marron, malla1, Gtk.PositionType.RIGHT, 1, 1)
        malla.attach_next_to(verde, marron, Gtk.PositionType.BOTTOM, 1, 1)
        malla.attach_next_to(malla2, malla1, Gtk.PositionType.BOTTOM, 2, 1)

        self.add(malla)
        self.connect("delete-event", Gtk.main_quit)
        self.show_all()

if __name__ == "__main__":
    Ejemplo()
    Gtk.main()