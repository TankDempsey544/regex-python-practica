import re
import tkinter as tk
from tkinter import filedialog

def checar(email):
    return bool(re.match(r'^[\w.%+-]+@[\w.-]+\.[A-Za-z]{2,}$', email))

print("1 - Ver en terminal")
print("2 - Ver gráfica")
opcion = input("Tu opción: ")

# abre explorador
root = tk.Tk()
root.withdraw()
archivo = filedialog.askopenfilename(filetypes=[("Textos", "*.txt")])

if archivo:
    with open(archivo, 'r') as f:
        texto = f.read()
    
    correos = re.findall(r'\S+@\S+', texto)
    buenos = sum(1 for c in correos if checar(c))
    malos = len(correos) - buenos
    
    if opcion == "1":
        print(f"Buenos: {buenos}")
        print(f"Malos: {malos}")
        
    elif opcion == "2":
        #ventana
        win = tk.Tk()
        win.title("Resultados")
        win.geometry("300x200")
        
        canvas = tk.Canvas(win, width=250, height=150, bg='white')
        canvas.pack(pady=10)
        
        #grafica
        max_val = max(buenos, malos, 1)
        canvas.create_rectangle(30, 120, 100, 120 - (buenos/max_val)*80, fill="green")
        canvas.create_rectangle(130, 120, 200, 120 - (malos/max_val)*80, fill="red")
        canvas.create_text(65, 130, text=f"Buenos: {buenos}")
        canvas.create_text(165, 130, text=f"Malos: {malos}")
        
        win.mainloop()