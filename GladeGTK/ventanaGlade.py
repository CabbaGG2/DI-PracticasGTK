
import gi
gi.require_version('Clutter', '1.0')
from gi.repository.Clutter import Orientation

import CaixaCor

gi.require_version("Gtk","3.0")
from gi.repository import Gtk, Gdk, GObject

class VentanaGlade:
    def __init__(self):

        listaCabeceraAlbaran = ["Código","Descripción","Cantidades","Precio unidad","Precio total"]
        listaDetalleAlbaran = [["000012", "Parafoxo M8", 100, 0.02, 0.2],
                               ["000013", "Arandela 10", 200, 0.001, 0.2],
                               ["000014", "Porca M6", 10, 0.002, 8.81],
                               ["000015", "Varilla roscada M6", 10, 0.50, 5],]

        #Asi invocamos la ventana que creamos en Glade
        builder = Gtk.Builder()
        builder.add_from_file("/home/dam/PythonProject/GTK2526/GladeGTK/formularioAlbaranGlade.glade")

        #ventana principal no se cierra por la siguiente linea, hay que tratar un evento
        wndVentanaPrincipal = builder.get_object("wndVentanaPrincipal")

        #cojemos el treeview del Glade con el ID que le asignamos en Glade duh
        trwDetalleAlbaran = builder.get_object("trwDetalleAlbaran")

        #manera de tomar señales
        signal = {"on_wndVentanaPrincipal_delete_event": Gtk.main_quit,
                  "on_cmbNumerAlbaran_changed": self.on_cmbNumerAlbaran_changed,
                  "on_btnAñadir_clicked": self.on_btnAñadir_clicked,
                  "on_btnEditar_clicked": self.on_btnEditar_clicked,
                  "on_btnBorrar_clicked": self.on_btnBorrar_clicked,
                  "on_btnAceptar_clicked": self.on_btnAceptar_clicked,
                  "on_btnCancelar_clicked": self.on_btnCancelar_clicked}

        builder.connect_signals(signal)

        #creamos el modelo del albaran
        modelo = Gtk.ListStore(str,str,int,float,float)

        #Cargamos la lista en el modelo
        for entrada in listaDetalleAlbaran:
            modelo.append(entrada)
        # le asignamos un modelo
        trwDetalleAlbaran.set_model(modelo)


        #repetira tantas veces la logica dentro del for segun la cantidad de elementos dentro de la listaCabeceraAlabaran
        for i, columna in enumerate (listaCabeceraAlbaran):
            #Aqui pasamos las columnas segun su indice (de la lista cabezera) para ingresar en la cabezera de las columnas segun su indice
            celda = Gtk.CellRendererText()
            columna = Gtk.TreeViewColumn (columna, celda, text = i)
            trwDetalleAlbaran.append_column(columna)


    def on_cmbNumerAlbaran_changed (self, combo):
        pass

    def on_btnAñadir_clicked (self,boton):
        pass

    def on_btnEditar_clicked (self,boton):
        pass

    def on_btnBorrar_clicked (self,boton):
        pass

    def on_btnAceptar_clicked (self,boton):
        pass

    def on_btnCancelar_clicked (self,boton):
        pass


if __name__ == "__main__":
    VentanaGlade()
    Gtk.main()