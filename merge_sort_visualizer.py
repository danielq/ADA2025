import tkinter as tk
from tkinter import ttk, messagebox
import random
import time
from typing import List, Tuple
import threading

class MergeSortVisualizer:
    def __init__(self, root):
        self.root = root
        self.root.title("Visualizador de Merge Sort - Divide y Vencerás")
        self.root.geometry("1000x700")
        self.root.configure(bg='#f0f0f0')
        
        # Variables de control
        self.array = []
        self.original_array = []
        self.steps = []
        self.current_step = 0
        self.is_running = False
        self.speed = 500  # milisegundos entre pasos
        
        # Configurar tema oscuro
        self.setup_dark_theme()
        
        # Configurar la interfaz
        self.setup_ui()
        
    def setup_dark_theme(self):
        """Configura el tema oscuro para la aplicación"""
        # Colores del tema oscuro
        self.colors = {
            'bg_primary': '#2c3e50',      # Azul oscuro para fondo principal
            'bg_secondary': '#34495e',    # Gris oscuro para frames secundarios
            'bg_canvas': '#1a252f',       # Negro azulado para canvas
            'text_primary': '#ecf0f1',    # Blanco para texto principal
            'text_secondary': '#bdc3c7',  # Gris claro para texto secundario
            'accent': '#3498db',          # Azul para elementos de acento
            'success': '#27ae60',         # Verde para botones de éxito
            'warning': '#e74c3c',         # Rojo para botones de advertencia
            'info': '#f39c12'             # Naranja para información
        }
        
        # Configurar el fondo principal
        self.root.configure(bg=self.colors['bg_primary'])
        
    def setup_ui(self):
        """Configura la interfaz de usuario"""
        # Título
        title_label = tk.Label(
            self.root, 
            text="Visualizador de Merge Sort - Algoritmo Divide y Vencerás",
            font=("Arial", 16, "bold"),
            bg=self.colors['bg_primary'],
            fg=self.colors['text_primary']
        )
        title_label.pack(pady=10)
        
        # Frame de controles
        control_frame = tk.Frame(self.root, bg=self.colors['bg_primary'])
        control_frame.pack(pady=10)
        
        # Botón para generar nuevo arreglo
        tk.Button(
            control_frame,
            text="Generar Nuevo Arreglo",
            command=self.generate_new_array,
            bg=self.colors['accent'],
            fg=self.colors['text_primary'],
            font=("Arial", 10, "bold"),
            padx=20,
            pady=5,
            relief=tk.RAISED,
            bd=2
        ).pack(side=tk.LEFT, padx=5)
        
        # Botón para iniciar ordenamiento
        self.start_button = tk.Button(
            control_frame,
            text="Iniciar Ordenamiento",
            command=self.start_sorting,
            bg=self.colors['success'],
            fg=self.colors['text_primary'],
            font=("Arial", 10, "bold"),
            padx=20,
            pady=5,
            relief=tk.RAISED,
            bd=2
        )
        self.start_button.pack(side=tk.LEFT, padx=5)
        
        # Botón para pausar/reanudar
        self.pause_button = tk.Button(
            control_frame,
            text="Pausar",
            command=self.pause_sorting,
            bg=self.colors['warning'],
            fg=self.colors['text_primary'],
            font=("Arial", 10, "bold"),
            padx=20,
            pady=5,
            relief=tk.RAISED,
            bd=2,
            state=tk.DISABLED
        )
        self.pause_button.pack(side=tk.LEFT, padx=5)
        
        # Botón para paso a paso
        tk.Button(
            control_frame,
            text="Paso a Paso",
            command=self.step_by_step,
            bg=self.colors['info'],
            fg=self.colors['text_primary'],
            font=("Arial", 10, "bold"),
            padx=20,
            pady=5,
            relief=tk.RAISED,
            bd=2
        ).pack(side=tk.LEFT, padx=5)
        
        # Control de velocidad
        speed_frame = tk.Frame(self.root, bg=self.colors['bg_primary'])
        speed_frame.pack(pady=5)
        
        tk.Label(
            speed_frame, 
            text="Velocidad:", 
            bg=self.colors['bg_primary'], 
            fg=self.colors['text_primary'],
            font=("Arial", 10, "bold")
        ).pack(side=tk.LEFT)
        
        self.speed_var = tk.IntVar(value=500)
        speed_scale = tk.Scale(
            speed_frame,
            from_=100,
            to=2000,
            orient=tk.HORIZONTAL,
            variable=self.speed_var,
            command=self.update_speed,
            bg=self.colors['bg_secondary'],
            fg=self.colors['text_primary'],
            highlightbackground=self.colors['bg_primary'],
            troughcolor=self.colors['bg_secondary'],
            activebackground=self.colors['accent'],
            length=200,
            relief=tk.FLAT,
            bd=1
        )
        speed_scale.pack(side=tk.LEFT, padx=10)
        
        # Frame principal de visualización
        self.canvas_frame = tk.Frame(self.root, bg=self.colors['bg_primary'])
        self.canvas_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        # Canvas para dibujar el arreglo
        self.canvas = tk.Canvas(
            self.canvas_frame,
            bg=self.colors['bg_canvas'],
            height=400,
            relief=tk.RAISED,
            bd=3,
            highlightthickness=2,
            highlightbackground=self.colors['accent']
        )
        self.canvas.pack(fill=tk.BOTH, expand=True)
        
        # Frame de información
        info_frame = tk.Frame(self.root, bg=self.colors['bg_primary'])
        info_frame.pack(fill=tk.X, padx=20, pady=5)
        
        self.info_label = tk.Label(
            info_frame,
            text="Arreglo original: []",
            bg=self.colors['bg_primary'],
            fg=self.colors['text_primary'],
            font=("Arial", 10, "bold"),
            anchor='w'
        )
        self.info_label.pack(fill=tk.X)
        
        self.step_label = tk.Label(
            info_frame,
            text="Paso: 0/0",
            bg=self.colors['bg_primary'],
            fg=self.colors['text_secondary'],
            font=("Arial", 10),
            anchor='w'
        )
        self.step_label.pack(fill=tk.X)
        
        # Generar arreglo inicial
        self.generate_new_array()
        
    def generate_new_array(self):
        """Genera un nuevo arreglo aleatorio"""
        if self.is_running:
            messagebox.showwarning("Advertencia", "El ordenamiento está en progreso. Detén la ejecución primero.")
            return
            
        self.array = [random.randint(1, 100) for _ in range(12)]
        self.original_array = self.array.copy()
        self.steps = []
        self.current_step = 0
        
        self.update_info()
        self.draw_array()
        self.start_button.config(state=tk.NORMAL)
        
    def update_speed(self, value):
        """Actualiza la velocidad de animación"""
        self.speed = int(value)
        
    def start_sorting(self):
        """Inicia el proceso de ordenamiento"""
        if not self.array:
            messagebox.showwarning("Advertencia", "Genera un arreglo primero.")
            return
            
        self.is_running = True
        self.start_button.config(state=tk.DISABLED)
        self.pause_button.config(state=tk.NORMAL, text="Pausar")
        
        # Ejecutar en un hilo separado para no bloquear la UI
        thread = threading.Thread(target=self.merge_sort_visualization)
        thread.daemon = True
        thread.start()
        
    def pause_sorting(self):
        """Pausa o reanuda el ordenamiento"""
        if self.pause_button.cget('text') == 'Pausar':
            self.is_running = False
            self.pause_button.config(text='Reanudar')
        else:
            self.is_running = True
            self.pause_button.config(text='Pausar')
            thread = threading.Thread(target=self.merge_sort_visualization)
            thread.daemon = True
            thread.start()
            
    def step_by_step(self):
        """Ejecuta un paso del algoritmo"""
        if not self.steps:
            self.prepare_steps()
            
        if self.current_step < len(self.steps):
            step = self.steps[self.current_step]
            self.execute_step(step)
            self.current_step += 1
            self.update_info()
            
    def prepare_steps(self):
        """Prepara todos los pasos del algoritmo para visualización"""
        self.steps = []
        self.merge_sort_with_steps(self.array.copy(), 0, len(self.array) - 1, [])
        
    def merge_sort_with_steps(self, arr, left, right, path):
        """Merge sort que guarda cada paso para visualización"""
        if left < right:
            mid = (left + right) // 2
            
            # Paso de división
            self.steps.append({
                'type': 'divide',
                'array': arr.copy(),
                'left': left,
                'right': right,
                'mid': mid,
                'path': path.copy(),
                'description': f"Dividir arreglo [{left}:{right}] en [{left}:{mid}] y [{mid+1}:{right}]"
            })
            
            # Recursión izquierda
            left_path = path + ['izquierda']
            self.merge_sort_with_steps(arr, left, mid, left_path)
            
            # Recursión derecha
            right_path = path + ['derecha']
            self.merge_sort_with_steps(arr, mid + 1, right, right_path)
            
            # Paso de fusión
            self.steps.append({
                'type': 'merge',
                'array': arr.copy(),
                'left': left,
                'right': right,
                'mid': mid,
                'path': path.copy(),
                'description': f"Fusionar subarreglos [{left}:{mid}] y [{mid+1}:{right}]"
            })
            
            # Simular el proceso de fusión paso a paso
            self.simulate_merge_steps(arr, left, mid, right, path)
            
    def simulate_merge_steps(self, arr, left, mid, right, path):
        """Simula el proceso de fusión paso a paso"""
        left_arr = arr[left:mid + 1]
        right_arr = arr[mid + 1:right + 1]
        
        i = j = 0
        k = left
        
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] <= right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            
            self.steps.append({
                'type': 'compare',
                'array': arr.copy(),
                'left': left,
                'right': right,
                'comparing': [k],
                'path': path.copy(),
                'description': f"Comparar y colocar elemento en posición {k}"
            })
            k += 1
            
        # Agregar elementos restantes
        while i < len(left_arr):
            arr[k] = left_arr[i]
            self.steps.append({
                'type': 'compare',
                'array': arr.copy(),
                'left': left,
                'right': right,
                'comparing': [k],
                'path': path.copy(),
                'description': f"Agregar elemento restante en posición {k}"
            })
            i += 1
            k += 1
            
        while j < len(right_arr):
            arr[k] = right_arr[j]
            self.steps.append({
                'type': 'compare',
                'array': arr.copy(),
                'left': left,
                'right': right,
                'comparing': [k],
                'path': path.copy(),
                'description': f"Agregar elemento restante en posición {k}"
            })
            j += 1
            k += 1
            
    def merge_sort_visualization(self):
        """Ejecuta la visualización completa del merge sort"""
        if not self.steps:
            self.prepare_steps()
            
        while self.current_step < len(self.steps) and self.is_running:
            step = self.steps[self.current_step]
            self.execute_step(step)
            self.current_step += 1
            self.update_info()
            
            time.sleep(self.speed / 1000)
            
        if self.current_step >= len(self.steps):
            self.is_running = False
            self.start_button.config(state=tk.NORMAL)
            self.pause_button.config(state=tk.DISABLED, text='Pausar')
            messagebox.showinfo("Completado", "¡El arreglo ha sido ordenado completamente!")
            
    def execute_step(self, step):
        """Ejecuta un paso específico del algoritmo"""
        self.array = step['array']
        self.root.after(0, self.draw_array_with_highlight, step)
        
    def draw_array(self):
        """Dibuja el arreglo en el canvas"""
        self.canvas.delete("all")
        
        if not self.array:
            return
            
        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()
        
        if canvas_width <= 1:  # Canvas no está listo aún
            self.root.after(100, self.draw_array)
            return
            
        bar_width = (canvas_width - 40) / len(self.array)
        max_height = canvas_height - 80
        
        for i, value in enumerate(self.array):
            x = 20 + i * bar_width
            bar_height = (value / 100) * max_height
            y = canvas_height - 40 - bar_height
            
            # Color base
            color = self.colors['accent']
            
            self.canvas.create_rectangle(
                x, y, x + bar_width - 2, canvas_height - 40,
                fill=color, outline=self.colors['text_primary'], width=1
            )
            
            # Valor del elemento
            self.canvas.create_text(
                x + bar_width/2, canvas_height - 20,
                text=str(value), font=("Arial", 8, "bold"),
                fill=self.colors['text_primary']
            )
            
    def draw_array_with_highlight(self, step):
        """Dibuja el arreglo con elementos destacados según el paso"""
        self.canvas.delete("all")
        
        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()
        
        if canvas_width <= 1:
            self.root.after(100, lambda: self.draw_array_with_highlight(step))
            return
            
        bar_width = (canvas_width - 40) / len(self.array)
        max_height = canvas_height - 80
        
        for i, value in enumerate(self.array):
            x = 20 + i * bar_width
            bar_height = (value / 100) * max_height
            y = canvas_height - 40 - bar_height
            
            # Determinar color según el tipo de paso
            if step['type'] == 'divide':
                if 'left' in step and 'right' in step:
                    if step['left'] <= i <= step['right']:
                        color = self.colors['warning']  # Rojo para división
                    else:
                        color = '#7f8c8d'  # Gris oscuro para elementos no afectados
                else:
                    color = self.colors['accent']
            elif step['type'] == 'merge':
                if 'left' in step and 'right' in step:
                    if step['left'] <= i <= step['right']:
                        color = self.colors['success']  # Verde para fusión
                    else:
                        color = '#7f8c8d'
                else:
                    color = self.colors['accent']
            elif step['type'] == 'compare':
                if 'comparing' in step and i in step['comparing']:
                    color = self.colors['info']  # Naranja para comparación
                elif 'left' in step and 'right' in step:
                    if step['left'] <= i <= step['right']:
                        color = self.colors['accent']  # Azul para rango de fusión
                    else:
                        color = '#7f8c8d'
                else:
                    color = self.colors['accent']
            else:
                color = self.colors['accent']
            
            self.canvas.create_rectangle(
                x, y, x + bar_width - 2, canvas_height - 40,
                fill=color, outline=self.colors['text_primary'], width=1
            )
            
            # Valor del elemento
            self.canvas.create_text(
                x + bar_width/2, canvas_height - 20,
                text=str(value), font=("Arial", 8, "bold"),
                fill=self.colors['text_primary']
            )
            
        # Mostrar información del paso actual
        if 'description' in step:
            self.canvas.create_text(
                canvas_width/2, 20,
                text=step['description'],
                font=("Arial", 12, "bold"),
                fill=self.colors['text_primary']
            )
            
        # Mostrar ruta de recursión
        if 'path' in step and step['path']:
            path_text = " → ".join(step['path'])
            self.canvas.create_text(
                canvas_width/2, 40,
                text=f"Ruta: {path_text}",
                font=("Arial", 10),
                fill=self.colors['text_secondary']
            )
            
    def update_info(self):
        """Actualiza la información mostrada"""
        self.info_label.config(text=f"Arreglo original: {self.original_array}")
        self.step_label.config(text=f"Paso: {self.current_step}/{len(self.steps)}")

def main():
    root = tk.Tk()
    app = MergeSortVisualizer(root)
    root.mainloop()

if __name__ == "__main__":
    main()
