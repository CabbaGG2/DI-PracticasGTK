import gi
from gi.repository.Clutter import Orientation

import CaixaCor

gi.require_version("Gtk","3.0")
from gi.repository import Gtk, Gdk, GObject

class Ejemplo (Gtk.Window):
    def __init__(self):
        super().__init__()
        self.set_title("Ventana Windows")

        #Modelo de la lista, mucha mas facil de implementar que QT
        modeloLista = Gtk.ListStore (str, str)
        modeloLista.append(('Sara',"111111K"))
        modeloLista.append(('Dani',"222222R"))
        modeloLista.append(('Karli',"333333L"))
        modeloLista.append(('Diego',"444444J"))
        modeloLista.append(('Manuel',"5555555T"))
        modeloLista.append(('Samuel',"6666666Y"))
        modeloLista.append(('Jerson',"7777777O"))
        modeloLista.append(('Jose',"88888P"))

        panelC = Gtk.Frame(label = "PanelCaption")
        malla = Gtk.Grid()
        panelC.add(malla)
        panel = Gtk.Frame(label = "Panel")
        malla.add(panel)
        cajaH = Gtk.Box(orientation = Gtk.Orientation.HORIZONTAL, spacing = 4)
        panel.add(cajaH)
        treeList = Gtk.TreeView()
        treeList.set_model(modeloLista)
        celda = Gtk.CellRendererText ()
        columna = Gtk.TreeViewColumn("Elemento", celda, text = 0)
        treeList.append_column(columna)

        cajaH.pack_start(treeList, True, True, 2)


        cajaV = Gtk.Box(orientation = Gtk.Orientation.VERTICAL, spacing = 4)
        cajaH.pack_start(cajaV, True, True, 2)
        rbt1 = Gtk.RadioButton(label="RadioButton1")
        rbt1.connect("toggled", self.on_rbt_toggled,"1")
        rbt2 = Gtk.RadioButton.new_from_widget(rbt1)
        rbt2.set_label("RadioButton2")
        rbt2.connect("toggled", self.on_rbt_toggled,"2")
        rbt3 = Gtk.RadioButton.new_from_widget(rbt1)
        rbt3.set_label("RadioButton3")
        rbt3.connect("toggled", self.on_rbt_toggled,"3")
        cajaV.pack_start(rbt1,False,False,2)
        cajaV.pack_start(rbt2,False,False,2)
        cajaV.pack_start(rbt3,False,False,2)
        btnBoton = Gtk.Button(label = "Boton")
        cajaV.pack_end(btnBoton, False, False,2)

        carpeta = Gtk.Notebook()
        malla.attach_next_to(carpeta,panel,Gtk.PositionType.RIGHT,1,1)
        cajaV2 = Gtk.Box(orientation = Gtk.Orientation.VERTICAL,spacing = 2)
        chk1 = Gtk.CheckButton(label= "Caja no seleccionada")
        chk2 = Gtk.CheckButton(label= "Caja seleccionada")
        chk2.set_active(True)
        chk3 = Gtk.CheckButton(label= "Caja inactiva")
        chk3.set_sensitive(False)

        scl1 = Gtk.Scale(orientation = Gtk.Orientation.HORIZONTAL)

        cajaV2.pack_start(chk1,False,False,2)
        cajaV2.pack_start(chk2,False,False,2)
        cajaV2.pack_start(chk3,False,False,2)

        cajaV2.pack_end(scl1,False,False,2)

        carpeta.append_page(cajaV2,Gtk.Label(label = "Solapa seleccionada"))
        carpeta.append_page(Gtk.TextView(), Gtk.Image.new_from_icon_name("help-about", Gtk.IconSize.MENU))

        cajaV3 = Gtk.Box(orientation = Gtk.Orientation.VERTICAL, spacing = 2)
        txtCajaTexto = Gtk.Entry()

        txtCajaPassword = Gtk.Entry()
        txtCajaPassword.set_invisible_char('*')
        txtCajaPassword.set_visibility(False)

        cmbCombo = Gtk.ComboBox()
        cmbCombo.set_model(modeloLista)
        cmbCombo.connect("changed",self.on_cmbCombo_changed)

        celda2 = Gtk.CellRendererText()
        cmbCombo.pack_start(celda2, True)
        cmbCombo.add_attribute(celda2,"text", 0)
        cajaV3.pack_start(txtCajaTexto, True, True, 2)
        cajaV3.pack_start(txtCajaPassword, True, True, 2)
        cajaV3.pack_start(cmbCombo, True, True, 2)
        malla.attach_next_to(cajaV3,panel,Gtk.PositionType.BOTTOM,1,1)

        self.txVCajaTexto = Gtk.TextView()
        malla.attach_next_to(self.txVCajaTexto,carpeta,Gtk.PositionType.BOTTOM,1,1)

        self.add(panelC)
        self.connect("delete-event", Gtk.main_quit)
        self.show_all()

    def on_rbt_toggled(self,radioButton, numero):
        if radioButton.get_active():
            buffer = self.txVCajaTexto.get_buffer()

            """
            Una manera de realizar algo con los Radio buttons
            texto = buffer.get_text(buffer.get_start_iter(), buffer.get_end_iter(), False)
            texto = texto + "\nSeleccionado el RedioButton" + numero
            buffer.set_text(texto)
            """

            #Otra manera de utilizar los modelos de buffer de los TextView con el radio button.
            buffer.insert(buffer.get_end_iter(), "\nSeleccionado el RadioButton " + numero, -1)

    def on_cmbCombo_changed(self,combo):
        puntero = combo.get_active_iter()
        if puntero is not None:
            modelo = combo.get_model()
            elemento = modelo [puntero][1]
            buffer = self.txVCajaTexto.get_buffer()
            buffer.insert(buffer.get_end_iter(), "\nSeleccionado el DNI: " + elemento + " del Combo")

if __name__ == "__main__":
    Ejemplo()
    Gtk.main()