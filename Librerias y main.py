import tkinter as tk
from tkinter import PhotoImage  # Importa PhotoImage para manejar imágenes
from ortools.linear_solver import pywraplp
import os

if __name__ == "__main__":
    root = tk.Tk()
    app = TransportProblemSolverGUI(root)
    root.mainloop()
