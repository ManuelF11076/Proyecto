    def save_to_file(self):
        # Obtener la ruta completa a la carpeta donde se guardarán los archivos
        output_directory = os.path.expanduser("C:\\Users\\mynor\\Desktop\\Modelo transporte")  # Cambia esta ruta según tu necesidad
        
        # Verificar si la carpeta de salida existe, si no, crearla
        if not os.path.exists(output_directory):
            os.makedirs(output_directory)

        # Crear la ruta completa al archivo de solución
        file_name = os.path.join(output_directory, f"solucion{self.solution_count}.txt")

        # Guardar los resultados en un archivo de texto
        with open(file_name, "w") as file:
            file.write(self.result_label.cget("text"))

        self.result_label.config(text=f"Resultados guardados en '{file_name}'")
        self.solution_count += 1