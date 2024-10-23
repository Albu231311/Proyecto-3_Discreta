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
