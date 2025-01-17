import tkinter as tk
from tkinter import messagebox

# Función para verificar si un número es primo
def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Función para actualizar el contenido de la pantalla de la calculadora
def click(boton_texto):
    actual = entry_pantalla.get()
    entry_pantalla.delete(0, tk.END)
    entry_pantalla.insert(tk.END, actual + boton_texto)

# Función para limpiar la pantalla
def clear():
    entry_pantalla.delete(0, tk.END)

# Función para borrar un solo carácter (el último)
def borrar_ultimo():
    actual = entry_pantalla.get()
    if actual:
        # Borra el último carácter de la cadena
        entry_pantalla.delete(len(actual) - 1, tk.END)

# Función para evaluar la expresión
def evaluar_expresion():
    try:
        expresion = entry_pantalla.get()  # Obtener la expresión de la pantalla
        p = int(entry_modulo.get())  # Obtener el valor del módulo
        
        if not es_primo(p):
            messagebox.showerror("Error", "El módulo debe ser un número primo.")
            return
        
        # Evaluar la expresión
        resultado = eval(expresion.replace("^", "*"))  # Reemplazar ^ con * para exponenciación en Python
        # Aplicar el módulo
        resultado_mod = resultado % p
        entry_pantalla.delete(0, tk.END)
        entry_pantalla.insert(tk.END, str(resultado_mod))
    except ZeroDivisionError:
        messagebox.showerror("Error", "División por cero no permitida.")
    except Exception as e:
        messagebox.showerror("Error", str(e))
        # Configuración de la ventana principal
root = tk.Tk()
root.title("Calculadora Modular")
root.geometry("400x650")

# Entrada de la expresión
entry_pantalla = tk.Entry(root, font=("Arial", 24), bd=10, insertwidth=2, width=14, borderwidth=4)
entry_pantalla.grid(row=0, column=0, columnspan=4)

# Entrada para el módulo
entry_modulo = tk.Entry(root, font=("Arial", 18), width=8)
entry_modulo.grid(row=1, column=2, columnspan=2)
label_modulo = tk.Label(root, text="Modulo:", font=("Arial", 18))
label_modulo.grid(row=1, column=0,columnspan=2)

# Crear los botones de la calculadora
botones = [
    ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('/', 2, 3),
    ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('*', 3, 3),
    ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('-', 4, 3),
    ('0', 5, 0), ('(', 5, 1), (')', 5, 2), ('+', 5, 3),
    ('AC', 6, 0), ('^', 6, 1), ('DEL', 6, 2), ('=', 6, 3),
]

# Función para asignar los botones
for (texto, fila, columna) in botones:
    if texto == 'AC':
        boton = tk.Button(root, text=texto, padx=20, pady=20, font=("Arial", 18), command=clear)
    elif texto == 'DEL':
        boton = tk.Button(root, text=texto, padx=20, pady=20, font=("Arial", 18), command=borrar_ultimo)
    elif texto == '=':
        boton = tk.Button(root, text=texto, padx=20, pady=20, font=("Arial", 18), command=evaluar_expresion)
    else:
        boton = tk.Button(root, text=texto, padx=20, pady=20, font=("Arial", 18), command=lambda txt=texto: click(txt))
    boton.grid(row=fila, column=columna)

# Ejecutar la interfaz
root.mainloop()
