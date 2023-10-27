# Etiqueta para mostrar los resultados en la interfaz
       self.result_label = tk.Label(root, text="", font=("Berlin Sans FB", 12), bg="#F0F8FF")
       self.result_label.grid(row=len(self.labels) + len(self.cost_labels) + 4, column=0, columnspan=6, padx=10, pady=10, sticky='w')

       Botón para resolver el problema y mostrar la solución en la interfaz
        solve_button = tk.Button(root, text="Resolver", command=self.solve_and_display, font=("Berlin Sans FB", 14), bg="green", fg="white")
        solve_button.grid(row=len(self.labels) + len(self.cost_labels) + 2, column=0, padx=10, pady=10, sticky='w')
       Botón para limpiar las entradas
        clear_button = tk.Button(root, text="Limpiar", command=self.clear_entries, font=("Berlin Sans FB", 14), bg="orange")
        clear_button.grid(row=len(self.labels) + len(self.cost_labels) + 2, column=1, padx=10, pady=10, sticky='w')
       Botón para guardar resultados en un archivo
        save_button = tk.Button(root, text="Guardar", command=self.save_to_file, font=("Berlin Sans FB", 14), bg="blue", fg="white")
        save_button.grid(row=len(self.labels) + len(self.cost_labels) + 2, column=2, padx=10, pady=10, sticky='w')
  
       
    
    def clear_entries(self):
       for entry in self.entries + self.cost_entries:
            entry.delete(0, tk.END)

         Limpiar las etiquetas de resultados
        for i in range(2):
           for j in range(3):
                self.result_labels[i][j].config(text="")
