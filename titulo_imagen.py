#******Personalización del programa******
    def _init_(self, root):
        self.root = root
        self.root.configure(bg="#F0F8FF")  # Cambia el color de fondo de la ventana
        self.root.title("Modelo de Optimización")
        self.solution_count = 1  # Variable para contar las soluciones 

        # Agregar una imagen
        img = PhotoImage(file="C:\\Users\\keisy\\OneDrive\\Desktop\\UMG\\6o. Ciclo\\Operaciones\\Proyecto\\3.png") 
        img_label = tk.Label(root, image=img, bg="#F0F8FF")
        img_label.image = img  
        img_label.grid(row=0, column=4, rowspan=2, padx=10, pady=10, sticky='e')  