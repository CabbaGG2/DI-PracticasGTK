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
        self.set_title("Ejemplo de TreeView en arbol")

        cajaV = Gtk.Box(orientation = Gtk.Orientation.VERTICAL, spacing = 6)

        modelo = Gtk.TreeStore(str,int)

        #avo es abuelo, no es un padre, abuelo no tiene padre
        for avo in range(5):
            punteroAvo = modelo.append(None,["Avó %i" %(avo,), avo])
            for pai in range(4):
                punteroPai = modelo.append(punteroAvo, ["Pai %i do avó % i" %(pai,avo), pai])
                for fillo in range(3):
                    modelo.append(punteroPai,["Fillo %i, do pai %i, do avó %i" % (fillo,pai,avo), fillo])

        #modelo
        trvVista = Gtk.TreeView (model = modelo)

        #-----columnas------
        tvcColumna = Gtk.TreeViewColumn("Parentesco")
        trvVista.append_column(tvcColumna)

        celda = Gtk.CellRendererText(   )

        tvcColumna.pack_start(celda, True)
        tvcColumna.add_attribute(celda,'text',0)

        tvcColumna2 = Gtk.TreeViewColumn("Orden")
        trvVista.append_column(tvcColumna2)

        celda = Gtk.CellRendererText()

        tvcColumna2.pack_start(celda, True)
        tvcColumna2.add_attribute(celda, 'text', 1)

        cajaV.pack_start(trvVista,True,True,5)

        self.add(cajaV)
        self.connect("delete-event", Gtk.main_quit)
        self.show_all()




if __name__ == "__main__":
    VentanaGlade()
    Gtk.main()