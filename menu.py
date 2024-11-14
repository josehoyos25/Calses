import tkinter as tk
from tkinter import messagebox, simpledialog

ventana = tk.Tk()
ventana.title('Menu Principal')

barra_menu = tk.Menu(ventana)
ventana.config(menu=barra_menu)

def salir():
    resp = messagebox.askquestion("Salir", "Desea salir?")
    if resp == 'yes':
        ventana.destroy()
    
def acerca_de():
    messagebox.showinfo("Acerca de", "Desarrollado por Jose")

def restar():
    num1 = simpledialog.askinteger("Resta", "Ingresa el primer valor: ")
    num2 = simpledialog.askinteger("Resta", "Ingresa el segundo valor: ")
    rest = num1 - num2 
    messagebox.showinfo("Resultado", f"la respuesta es {rest}")
    
    
def ventana_sumar():
    v1 = tk.Toplevel(ventana)
    v1.title('Suma')
    titulo = tk.Label(v1, text="Sumar 2 numeros")
    v1.geometry("250x250")
    def sumar():
        n1 = int(text1.get())   
        n2 = int(text2.get())
        suma = n1 + n2
        messagebox.showinfo("Resultado", f"La suma es: {suma}")   
    text1 = tk.Entry(v1)
    text2 = tk.Entry(v1)
    btn1 = tk.Button(v1, text="Sumar", command=sumar)
    titulo.pack() 
    text1.pack()
    text2.pack()
    btn1.pack() 
    
def multiplicar():
    num1 = simpledialog.askinteger("Multiplicacion", "Ingresa el primer valor: ")
    num2 = simpledialog.askinteger("Multiplicacion", "Ingresa el segundo valor: ")
    mult = num1 * num2 
    messagebox.showinfo("Resultado", f"la respuesta es {mult}")


def ventana_dividir():
    v1 = tk.Toplevel(ventana)
    v1.title('Dividir')
    titulo = tk.Label(v1, text="Dividir 2 numeros")
    v1.geometry("250x250")
    def dividir():
        n1 = int(text1.get())   
        n2 = int(text2.get())
        divid = n1 / n2
        messagebox.showinfo("Resultado", f"La divicion es: {divid}")   
    text1 = tk.Entry(v1)
    text2 = tk.Entry(v1)
    btn1 = tk.Button(v1, text="Dividir", command=dividir)
    titulo.pack() 
    text1.pack()
    text2.pack()
    btn1.pack() 


menu_inicio = tk.Menu(barra_menu, tearoff=0)
barra_menu.add_cascade(label="Inicio", menu=menu_inicio) 
menu_inicio.add_command(label="Salir", command=salir)

menu_operaciones = tk.Menu(barra_menu, tearoff=0)
barra_menu.add_cascade(label="Operaciones", menu=menu_operaciones)
menu_operaciones.add_command(labe="Sumar", command=ventana_sumar)  
menu_operaciones.add_command(labe="Restar", command=restar)
menu_operaciones.add_command(labe="Multiplicar", command=multiplicar)
menu_operaciones.add_command(labe="Dividir", command=ventana_dividir) 

menu_ayuda = tk.Menu(barra_menu, tearoff=0)
barra_menu.add_cascade(label="Ayuda", menu=menu_ayuda)
menu_ayuda.add_command(labe="Acerca de", command=acerca_de)


ventana.mainloop()
    