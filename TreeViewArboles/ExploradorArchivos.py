from math import trunc

import gi
import pathlib
gi.require_version('Clutter', '1.0')
from gi.repository.Clutter import Orientation

import CaixaCor

gi.require_version("Gtk","3.0")
from gi.repository import Gtk, Gdk, GObject

class VentanaGlade (Gtk.Window):
    def __init__(self):
        super().__init__()
        self.set_title("Ejemplo Explorador de archivos en arbol")

        cajaV = Gtk.Box(orientation = Gtk.Orientation.VERTICAL, spacing = 6)

        modelo = Gtk.TreeStore(str,str)

        trvVista = Gtk.TreeView(model = modelo)

        #Cuando hay un cambio notifica
        objSeleccion = trvVista.get_selection()

        #el objSelection podemos seleccionarlo y leo lo que hay si es directorio leo lo que hay adentro.
        objSeleccion.connect("changed", self.on_selection_changed)

        tvcColumna = Gtk.TreeViewColumn()
        trvVista.append_column(tvcColumna)
        celda = Gtk.CellRendererPixbuf()
        tvcColumna.pack_start(celda, True)
        tvcColumna.add_attribute(celda,'icon_name',0)

        tvcColumna2 = Gtk.TreeViewColumn()
        trvVista.append_column(tvcColumna2)
        celda = Gtk.CellRendererText()
        tvcColumna2.pack_start(celda, True)
        tvcColumna2.add_attribute(celda,'text', 1)
        self.explorarDirectorio('/home/dam/AccesoDatos', None, modelo)

        cajaV.pack_start(trvVista,True,True,10)

        self.add(cajaV)
        self.connect("delete-event", Gtk.main_quit)
        self.show_all()

    def explorarDirectorio (self, ruta, punteiroPai, modelo):
        contenidoDir = pathlib.Path(ruta)

        for entrada in contenidoDir.iterdir():
            if entrada.is_dir():
                punteroFillo = modelo.append(punteiroPai,("folder", entrada.name))
                #esta linea sirve para verificar si es directorio o fichero, si es directorio vuelve a llamar a "explorarDirectorio"
                #self.explorarDirectorio(ruta + '/' + entrada.name, punteroFillo, modelo)

            else:
                modelo.append(punteiroPai,("emblem-documents",entrada.name))


    def on_selection_changed (self, objSeleccion):
        ruta = ""
        #objSelection tiene un metodo que da referencia al modelo y asu fila referenciada get_selected()
        modelo, fila = objSeleccion.get_selected()
        print(modelo[fila][0], modelo[fila][1])
        """if modelo [fila][0] == "folder":
            ruta = self.obtenerRuta(modelo, fila,"")
        print(ruta)
        """
        #self.explorarDirectorio(ruta + modelo [fila][1], puntero, modelo)

    def obtenerRuta (self,modelo, fila, ruta ):
        punteroPadre = modelo.iter_parent(fila)
        if punteroPadre is None:
            return fila.row()[1] + '/' + ruta
        else:
            ruta = ruta + '/' + fila [1]
            self.obtenerRuta(modelo, fila, ruta)

if __name__ == "__main__":
    VentanaGlade()
    Gtk.main()