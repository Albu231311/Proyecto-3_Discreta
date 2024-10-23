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