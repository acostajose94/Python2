import tkinter as tk

# Crear la ventana principal
root = tk.Tk()
root.title("Mi reproductor")

# Establecer la posición y el tamaño de la ventana
root.geometry("300x100+700+200")

# Crear el marco para los botones
button_frame = tk.Frame(root)
button_frame.pack(side="right", padx=10)

# Crear los botones
play_button = tk.Button(button_frame, text="Play")
play_button.pack(pady=5)

pause_button = tk.Button(button_frame, text="Pausa")
pause_button.pack(pady=5)

stop_button = tk.Button(button_frame, text="Stop")
stop_button.pack(pady=5)

# Centrar verticalmente los botones
button_frame.place(relx=1.0, rely=0.5, anchor="e")

# Ejecutar el bucle principal de la aplicación
root.mainloop()
