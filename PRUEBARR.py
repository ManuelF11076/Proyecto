class TransportProblemSolverGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Modelo De Optimizacion")
        self.solution_count = 1  # Variable para contar las soluciones 

        # Agregar un título en la parte superior
        title_label = tk.Label(root, text="PANADERIA <<EL DIVINO MAESTRO>>")
        title_label.grid(row=0, column=0, columnspan=6, padx=10, pady=10)

        # titulos para los datos de entrada, oferta y demanda
        self.labels = ["Produccion Panaderia 1:", "Produccion Panaderia 2:", "Demanda Sucursal 1:", "Demanda Sucursal 2:", "Demanda Sucursal 3:"]
        self.entries = []
        for i, label in enumerate(self.labels):
            tk.Label(root, text=label).grid(row=i + 1, column=0, padx=10, pady=10, sticky='w')
            entry = tk.Entry(root)
            entry.grid(row=i + 1, column=1, padx=10, pady=10, columnspan=2, sticky='w')
            self.entries.append(entry)