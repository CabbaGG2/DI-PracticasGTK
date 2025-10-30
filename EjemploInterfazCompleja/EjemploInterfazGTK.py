import gi
import CaixaCor

gi.require_version("Gtk","3.0")
from gi.repository import Gtk, Gdk, GObject

class Ejemplo (Gtk.Window):
    def __init__(self):
        super().__init__()
        self.set_title("Ventana Windows")

        modeloLista = Gtk.ListStore (str)
        modeloLista.append(('Elemento 1',))
        modeloLista.append(('Elemento 2',))
        modeloLista.append(('Elemento 3',))

        panelC = Gtk.Frame(label = "PanelCaption")
        malla = Gtk.Grid()
        panelC.add(malla)
        panel = Gtk.Frame(label = "Panel")
        malla.add(panel)
        cajaH = Gtk.Box(orientation = Gtk.Orientation.HORIZONTAL, spacing = 4)
        panel.add(cajaH)
        treeList = Gtk.TreeView()
        treeList.set_model(modeloLista)
        cajaH.pack_start(treeList, True, True, 2)
        cajaV = Gtk.Box(orientation = Gtk.Orientation.VERTICAL, spacing = 4)
        cajaH.pack_start(cajaV, True, True, 2)
        rbt1 = Gtk.RadioButton(label="RadioButton1")
        rbt2 = Gtk.RadioButton.new_from_widget(rbt1)
        rbt2.set_label("RadioButton2")
        rbt3 = Gtk.RadioButton.new_from_widget(rbt1)
        rbt3.set_label("RadioButton3")
        cajaV.pack_start(rbt1,False,False,2)
        cajaV.pack_start(rbt2,False,False,2)
        cajaV.pack_start(rbt3,False,False,2)

        self.add(panelC)
        self.connect("delete-event", Gtk.main_quit)
        self.show_all()

if __name__ == "__main__":
    Ejemplo()
    Gtk.main()