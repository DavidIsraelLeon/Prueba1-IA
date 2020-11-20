from tkinter import ttk
from tkinter import*
import sqlite3

class Compras:

    def __init__(self,window):
        self.win=window
        self.win.title('VentanaCompras')

        frame = LabelFrame(self.win, text="Productos")
        frame.grid(row=0, column=0, columnspan=3, pady=10,padx=0)
        #Boton
        #ttk.Button(frame,text = 'Guardar Persona', command=self.agregar_producto).grid(row=5,columnspan=2,sticky = W+E)
        #Mensaje
        #Tabla
        self.tree = ttk.Treeview(frame, columns=('#0', '#1', '#2'))
        self.tree.grid(row=1, column=0, columnspan=12)
        self.tree.heading('#0', text='Nombre', anchor=CENTER)
        self.tree.heading('#1', text='Precio', anchor=CENTER)
        self.tree.heading('#2', text='Stock', anchor=CENTER)
        self.get_product()
        frame = LabelFrame(self.win, text="Persona")
        frame.grid(row=1, column=0, columnspan=3, pady=20, padx=20)

        self.tree = ttk.Treeview(frame, columns=('#0', '#1', '#2', '#3'))
        self.tree.grid(row=2, column=0, columnspan=10)
        self.tree.heading('#0', text='Nombre', anchor=CENTER)
        self.tree.heading('#1', text='Direccion', anchor=CENTER)
        self.tree.heading('#2', text='Telefono', anchor=CENTER)
        self.tree.heading('#3', text='Correo', anchor=CENTER)

        self.get_persona()

    db_name = 'database.db'

    def run_query(self, query, parameters=()):
        with  sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            result = cursor.execute(query,parameters)
            conn.commit()
        return result

    def get_product(self):
            records = self.tree.get_children()
            for elemento in records:
                self.tree.delete(elemento)
            # query
            query = 'Select* from producto ORDER BY 1'
            db_rows = self.run_query(query)
            for row in db_rows:
                self.tree.insert('', 0, text=row[1], values=(row[2], row[3]))
    def validacionPro(self):
        return len(self.name.get())!=0 and len(self.direcc.get())!=0 and len(self.telf.get())!=0 and len(self.correo.get())!=0

    def get_persona(self):
        records=self.tree.get_children()
        for elemento in records:
            self.tree.delete(elemento)
        #query
        query = 'Select* from personas ORDER BY nombre ASC'
        db_rows = self.run_query(query)
        for row in db_rows:
            self.tree.insert('',0, text=row[1], values=(row[2],row[3],row[4]))
if __name__=='__main__':
    window= Tk()
    application=Compras(window)
    window.mainloop()







