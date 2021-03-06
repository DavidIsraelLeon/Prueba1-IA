from tkinter import ttk
from tkinter import*
import sqlite3

class Producto:




    def __init__(self,window):
        self.win=window
        self.win.title('VentanaProducto')

        frame = LabelFrame(self.win, text="Registrar Producto")
        frame.grid(row=0, column=0, columnspan=3, pady=80,padx=80)
        # Nombre
        Label(frame, text='Nombre').grid(row=1, column=0)
        self.name = Entry(frame)
        self.name.focus()
        self.name.grid(row=1, column=1)
        # Direccion
        Label(frame, text='precio').grid(row=2, column=0)
        self.price = Entry(frame)
        self.price.grid(row=2, column=1)

        # Telefono
        Label(frame, text='stock').grid(row=3, column=0)
        self.stock= Entry(frame)
        self.stock.grid(row=3, column=1)


        #Boton
        ttk.Button(frame,text = 'Guardar Producto', command=self.agregar_producto).grid(row=5,columnspan=2,sticky = W+E)
        #Mensaje

        self.message=Label(text='',fg='red')
        self.message.grid(row=4,column=0,columnspan=2,sticky=W+E)
        #Tabla

        self.tree=ttk.Treeview(frame,columns=('#0','#1','#2'))
        self.tree.grid(row=6,column=0,columnspan=8)
        self.tree.heading('#0',text='Nombre', anchor=CENTER)
        self.tree.heading('#1',text='Precio', anchor=CENTER)
        self.tree.heading('#2', text='Stock', anchor=CENTER)
        self.get_product()

    db_name = 'database.db'

    def run_query(self, query, parameters=()):
        with  sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            result = cursor.execute(query,parameters)
            conn.commit()
        return result

    def get_product(self):
        records=self.tree.get_children()
        for elemento in records:
            self.tree.delete(elemento)
        #query
        query = 'Select* from producto ORDER BY 1'
        db_rows = self.run_query(query)
        for row in db_rows:
            self.tree.insert('',0, text=row[1], values=(row[2],row[3]))
    def validacionPro(self):
        return len(self.name.get())!=0 and len(self.price.get())!=0 and len(self.stock.get())!=0

    def agregar_producto(self):
        if self.validacionPro():
            query='INSERT INTO producto VALUES(NULL,?,?,?)'
            parameters=(self.name.get(),self.price.get(),self.stock.get())
            self.run_query(query,parameters)
            self.message['text']='{} Agregado'.format(self.name.get())
            self.name.delete(0,END)
            self.price.delete(0,END)
            self.stock.delete(0, END)
        else:
            self.message['text']='Requiere colocar datos'
        self.get_product()
if __name__=='__main__':
    window= Tk()
    application=Producto(window)
    window.mainloop()



