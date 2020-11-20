from tkinter import ttk
from tkinter import*
import sqlite3

class Persona:

    def __init__(self,window):
        self.win=window
        self.win.title('VentanaPersona')

        frame = LabelFrame(self.win, text="Registrar Persona")
        frame.grid(row=0, column=0, columnspan=3, pady=80,padx=80)
        # Nombre
        Label(frame, text='Nombre').grid(row=1, column=0)
        self.name = Entry(frame)
        self.name.focus()
        self.name.grid(row=1, column=1)
        # Direccion
        Label(frame, text='Direccion').grid(row=2, column=0)
        self.direcc = Entry(frame)
        self.direcc.grid(row=2, column=1)

        # Telefono
        Label(frame, text='Telefono').grid(row=3, column=0)
        self.telf= Entry(frame)
        self.telf.grid(row=3, column=1)

        Label(frame, text='Correo').grid(row=4, column=0)
        self.correo = Entry(frame)
        self.correo.grid(row=4, column=1)


        #Boton
        ttk.Button(frame,text = 'Guardar Persona', command=self.agregar_producto).grid(row=5,columnspan=2,sticky = W+E)
        #Mensaje


        #Tabla

        self.tree=ttk.Treeview(frame,columns=('#0','#1','#2','#3'))
        self.tree.grid(row=6,column=0,columnspan=8)
        self.tree.heading('#0',text='Nombre', anchor=CENTER)
        self.tree.heading('#1',text='Direccion', anchor=CENTER)
        self.tree.heading('#2', text='Telefono', anchor=CENTER)
        self.tree.heading('#3', text='Correo', anchor=CENTER)

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
        query = 'Select* from personas ORDER BY nombre ASC'
        db_rows = self.run_query(query)
        for row in db_rows:
            self.tree.insert('',0, text=row[1], values=(row[2],row[3],row[4]))
    def validacionPro(self):
        return len(self.name.get())!=0 and len(self.direcc.get())!=0 and len(self.telf.get())!=0 and len(self.correo.get())!=0

    def agregar_producto(self):
        if self.validacionPro():
            query='INSERT INTO personas VALUES(NULL,?,?,?,?)'
            parameters=(self.name.get(),self.direcc.get(),self.telf.get(),self.correo.get())
            self.run_query(query,parameters)

            self.name.delete(0,END)
            self.direcc.delete(0,END)
            self.telf.delete(0, END)
            self.correo.delete(0, END)
        else:
            self.message['text']='Requiere colocar datos'
        self.get_product()
if __name__=='__main__':
    window= Tk()
    application=Persona(window)
    window.mainloop()



