from math import trunc

import gi
gi.require_version('Clutter', '1.0')
from gi.repository.Clutter import Orientation

import CaixaCor

gi.require_version("Gtk","3.0")
from gi.repository import Gtk, Gdk, GObject

class VentanaGlade (Gtk.Window):
    def __init__(self):
        super().__init__()
        self.set_title("Ejemplo de TreeView editable")

        cajaV = Gtk.Box(orientation = Gtk.Orientation.VERTICAL, spacing = 6)

        listaUsuarios = [('Y123456','Ana Perez',34,'M',False),
                         ('K123485','Pepe Diaz',78,'H',True)]

        modelo = Gtk.ListStore(str, str, int, str, bool)

        for usuario in listaUsuarios:
            modelo.append(usuario)

        trvVista = Gtk.TreeView (model = modelo)

        for i, tituloColumna in enumerate (('Dni','Nombre')):
            celda = Gtk.CellRendererText()
            celda.set_property("editable",True)
            celda.connect("edited", self.on_celdaTexto_edited, i)
            columna = Gtk.TreeViewColumn(tituloColumna, celda, text = i)
            trvVista.append_column(columna)

        celda = Gtk.CellRendererProgress()
        #Edad sera el nombre de la columna, de celda sacara el modelo de datos en este caso una barra de progreso y el value sacara los datos del espacio "2"
        #de la lista de usuarios.
        columna = Gtk.TreeViewColumn("Edad", celda, value = 2)
        trvVista.append_column(columna)

        #Esto es para generar la columna de Genero con sus datos
        celda = Gtk.CellRendererText()
        columna = Gtk.TreeViewColumn("Genero", celda, text=3)
        trvVista.append_column(columna)

        #Al ser un tipo de dato booleano es atributo "active" no "text"
        celda = Gtk.CellRendererToggle()
        #set_property modifica propiedades, en este caso queremos que la columna Fallecido sea editable (el toogle)
        #no funciono jajajas
        #celda.set_property("sensitive", True)
        celda.connect("toggled",self.on_celdaFallecido_toggle, modelo)
        columna = Gtk.TreeViewColumn("Fallecido",celda, active = 4)
        trvVista.append_column(columna)

        cajaV.pack_start(trvVista,True,True,5)


        self.add(cajaV)
        self.connect("delete-event", Gtk.main_quit)
        self.show_all()

    def on_celdaFallecido_toggle(self, check, fila, modelo):
        print("Clicamos la fila", str(fila))
        #si el modelo esta checkeado quita el check, sino al reves.
        modelo [fila][4] =  not modelo [fila][4]


    def on_celdaTexto_edited(self, cuadroTexto, fila, texto, numeroColumna):
        print("Editamos el ", "nombre" if numeroColumna  == 1 else "Dni")


if __name__ == "__main__":
    VentanaGlade()
    Gtk.main()