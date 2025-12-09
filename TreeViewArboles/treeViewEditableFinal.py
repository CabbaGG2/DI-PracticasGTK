import  gi

gi.require_version("Gtk","3.0")
from gi.repository import Gtk,Gdk,GObject


class EjemploTree(Gtk.Window):


    def __init__(self):
        super().__init__()
        self.set_title("Ejemplo de Treeview en árbol")



        self.filtradoXenero=None
        self.filtradoEdade=0

        caixav = Gtk.Box(orientation= Gtk.Orientation.VERTICAL, spacing= 6)

        modelo = Gtk.ListStore(str,str,int,str,bool)
        listaUsuarios = [('1234H','Ana Perez',34,'Muller',False),
                         ('4321T','Pepe Diz',78,'Home',True),
                         ('5678U','Rosa Gil',56,'Muller',False),
                         ('8765R','Juan Vila',43,'Home',False),
                         ('4567P','Iris Vazquez',39,'Outros',True)]

        #filtramos el modelo
        for usuario in listaUsuarios:
            modelo.append(usuario)
        #set_sort_func ordena una lista segun algun algun criterio (columnba de datos, funcion que compara, user_data:none)
        modelo.set_sort_func(2, self.compara_edades,None)
        modelo_filtrado =modelo.filter_new()
        #filtrado tiene funcion para decir que elemento se muestra y que no
        modelo_filtrado.set_visible_func(self.filtro_usuarios_edade)

        #El filtrado y el ordenado funcionan por separado, no pueden juntarse.
        #con filtrado se puede usar el modelo_filtrado y con el ordenado se tiene que usar el modelo normal
        trvVista = Gtk.TreeView(model=modelo_filtrado)

        #creamos las columnas
        for i, tituloColumna in enumerate (('Dni','Nome')):
            celda = Gtk.CellRendererText()
            celda.set_property("editable",True)
            celda.connect("edited",self.on_celdaNome_edited,i,modelo)
            columna = Gtk.TreeViewColumn(tituloColumna,celda,text = i)
            trvVista.append_column(columna)

        celda = Gtk.CellRendererProgress()
        columna = Gtk.TreeViewColumn('Edade',celda, value = 2)

        #le decimos que esta es la columna que será criterio de ordenación por id, el indice es la columna 2
        columna.set_sort_column_id(2)
        trvVista.append_column(columna)

        modeloComboXenero = Gtk.ListStore(str)
        modeloComboXenero.append(("Home",))
        modeloComboXenero.append(("Muller",))
        modeloComboXenero.append(("Outros",))
        modeloComboXenero.append(("Decepción",))

        celda = Gtk.CellRendererCombo()

        celda.set_property("editable",True)
        celda.props.model = modeloComboXenero
        celda.set_property("text-column",0)
        celda.set_property("has-entry",False)
        celda.connect("changed",self.on_xenero_changed,modelo)

        columna = Gtk.TreeViewColumn('Xénero', celda, text=3)
        trvVista.append_column(columna)

        celda = Gtk.CellRendererToggle()
        celda.set_property("sensitive",True)
        celda.connect("toggled", self.on_celdaFalecido_toogled,modelo)
        columna = Gtk.TreeViewColumn('Falecido',celda,active=4)
        trvVista.append_column(columna)

        caixav.pack_start(trvVista, True, True, 5)


        caixaH = Gtk.Box (orientation = Gtk.Orientation.HORIZONTAL, spacing = 4)
        rbtHome = Gtk.RadioButton(label = 'Home')
        rbtMuller = Gtk.RadioButton.new_with_label_from_widget(rbtHome, label = 'Muller')
        rbtOutros = Gtk.RadioButton.new_with_label_from_widget(rbtHome, label = 'Outros')
        caixaH.pack_start(rbtHome,False,False,2)
        caixaH.pack_start(rbtMuller,False,False,2)
        caixaH.pack_start(rbtOutros,False,False,2)
        rbtHome.connect("toggled",self.on_xeneroToggled,"Home",modelo_filtrado)
        rbtMuller.connect("toggled",self.on_xeneroToggled,"Muller",modelo_filtrado)
        rbtOutros.connect("toggled",self.on_xeneroToggled,"Outros",modelo_filtrado)

        caixav.pack_start(caixaH,True,True,0)

        scaleEdad = Gtk.Scale.new_with_range(orientation = Gtk.Orientation.HORIZONTAL,min = 1, max = 100,step = 1)


        scaleEdad.connect("change-value",self.on_ScaleEdad_changeValue,modelo_filtrado)

        caixav.pack_start(scaleEdad,True,True,0)






        self.add(caixav)
        self.connect("delete_event",Gtk.main_quit)
        self.show_all()

    def on_celdaFalecido_toogled(self,celda,fila,modelo):
        print('Clicamos en ',fila)
        modelo [fila][4] = not modelo [fila][4]

    def on_celdaNome_edited(self,celda,fila,cadroTexto,numero,modelo):
        print("Editamos: ",numero,fila,cadroTexto)
        if numero == 1:
            modelo[fila][1] = cadroTexto

    def on_xenero_changed(self,celda,fila,indx,modeloTab):
        modeloTab[fila][3] = celda.props.model[indx][0]

    def compara_edades(self, modelo, fila1, fila2, datosUsuario):
        columna_ordear, _ = modelo.get_sort_column_id()
        edade1 = modelo.get_value (fila1, columna_ordear)
        edade2 = modelo.get_value (fila2, columna_ordear)
        if edade1 > edade2:
            return 1
        elif edade1 < edade2:
            return -1
        else:
            return 0

    def filtro_usuarios_xenero(self, modelo, fila,datos):
        if self.filtradoXenero is None or self.filtradoXenero == "None":
            return True
        else:
            return modelo[fila] [3] == self.filtradoXenero

    def on_xeneroToggled(self,rbtElexido,xenero,modelo_filtrado):
        if rbtElexido.get_active():
            self.filtradoXenero = rbtElexido.get_label()
            modelo_filtrado.refilter()
            print(rbtElexido.get_label())

    def filtro_usuarios_edade(self,modelo,fila,datos):
        return modelo[fila][2] <= self.filtradoEdade

    def on_ScaleEdad_changeValue(self,control,scroll,valor,modelo_filtrado):
        self.filtradoEdade = valor
        modelo_filtrado.refilter()



if __name__ == "__main__":
    EjemploTree()
    Gtk.main()