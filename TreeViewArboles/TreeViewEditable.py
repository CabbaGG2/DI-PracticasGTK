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

        self.listaUsuarios = [('Y123456','Ana Perez',34,'M',False),
                         ('K123485','Pepe Diaz',78,'H',True)]

        modelo = Gtk.ListStore(str, str, int, str, bool)

        for usuario in self.listaUsuarios:
            modelo.append(usuario)

        trvVista = Gtk.TreeView (model = modelo)

        for i, tituloColumna in enumerate (('Dni','Nombre')):
            celda = Gtk.CellRendererText()
            celda.set_property("editable",True)
            celda.connect("edited", self.on_celdaTexto_edited, i, modelo)
            columna = Gtk.TreeViewColumn(tituloColumna, celda, text = i)
            trvVista.append_column(columna)

        celda = Gtk.CellRendererProgress()
        #Edad sera el nombre de la columna, de celda sacara el modelo de datos en este caso una barra de progreso y el value sacara los datos del espacio "2"
        #de la lista de usuarios.
        columna = Gtk.TreeViewColumn("Edad", celda, value = 2)
        trvVista.append_column(columna)

        #Esto es para generar la columna de Genero con sus datos
        #celda = Gtk.CellRendererText()

        #para utilizar combos en GTK se tiene que crear un modelo
        modeloComboGenero = Gtk.ListStore(str)

        #se añaden tulplas de una en una porque GTK funcion asi: la coma vuelve el string en colección
        modeloComboGenero.append(("Hombre",))
        modeloComboGenero.append(("Mujer",))
        modeloComboGenero.append(("Otros",))

        celda = Gtk.CellRendererCombo()
        celda.set_property("editable",True)

        #hay que decirle a la celda cual es el modelo con props.model
        celda.props.model = modeloComboGenero

        #coje el texto de la posición 0 en la colecciones
        celda.set_property("text-column",0)

        #has-entry permite meter nuevas entradas en el modelo a traves del combobox
        celda.set_property("has-entry", False)

        celda.connect("changed", self.on_comboGenero_changed, modelo)

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


    def on_celdaTexto_edited(self, cuadroTexto, fila, texto, numeroColumna, modelo):
        """metodo que actualiza el valor en el nombre o dni en la tabla modificando la lista

        :param cuadroTexto:
        :param fila:
        :param texto: Nuevo texto que se inserta en el cuadro de texto
        :param numeroColumna:
        :param modelo:
        :return:
        """
        modelo[fila][numeroColumna] = texto
        print("Editamos el ", "nombre" if numeroColumna  == 1 else "Dni")

    def on_comboGenero_changed(self, celda, fila, indice, modelo):
        modelo [fila][3] = celda.props.model [indice][0]


if __name__ == "__main__":
    VentanaGlade()
    Gtk.main()