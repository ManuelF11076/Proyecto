  # Agregar un título en la parte superior
        title_label = tk.Label(root, text="     Panadería ''El Divino Maestro''", font=("Script MT Bold", 22, "bold"), bg="#F0F8FF", fg="#B8860B")
        title_label.grid(row=0, column=0, columnspan=6, padx=10, pady=10, sticky='w')


        # titulos para los datos de entrada, oferta y demanda
        self.labels = ["Producción Panadería 1:", "Producción Panadería 2:", "Demanda Sucursal 1:", "Demanda Sucursal 2:", "Demanda Sucursal 3:"]
        self.entries = []