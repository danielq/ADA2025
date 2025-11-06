import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
from empleados import GeneradorEmpleados, BusquedaLineal
import threading

class InterfazBusquedaEmpleados:
    """Interfaz gráfica para búsqueda lineal de empleados"""
    
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Búsqueda Lineal - Empleados")
        self.root.geometry("1200x800")
        self.root.configure(bg='#f0f0f0')
        
        # Inicializar datos
        self.empleados = []
        self.busqueda = None
        self.resultados = []
        
        # Configurar estilo
        self.configurar_estilo()
        
        # Crear interfaz
        self.crear_interfaz()
        
        # Cargar empleados en un hilo separado
        self.cargar_empleados()
    
    def configurar_estilo(self):
        """Configura el estilo de la interfaz"""
        style = ttk.Style()
        style.theme_use('clam')
        
        # Configurar colores
        style.configure('TLabel', background='#f0f0f0', font=('Arial', 10))
        style.configure('TButton', font=('Arial', 10))
        style.configure('TEntry', font=('Arial', 10))
        style.configure('TCombobox', font=('Arial', 10))
        style.configure('Treeview', font=('Arial', 9))
        style.configure('Treeview.Heading', font=('Arial', 10, 'bold'))
    
    def crear_interfaz(self):
        """Crea todos los elementos de la interfaz"""
        # Frame principal
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configurar grid
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        main_frame.rowconfigure(3, weight=1)
        
        # Título
        titulo = ttk.Label(main_frame, text="Sistema de Búsqueda Lineal - 1000 Empleados", 
                          font=('Arial', 16, 'bold'))
        titulo.grid(row=0, column=0, columnspan=3, pady=(0, 20))
        
        # Frame de búsqueda
        self.crear_frame_busqueda(main_frame)
        
        # Frame de resultados
        self.crear_frame_resultados(main_frame)
        
        # Frame de estadísticas
        self.crear_frame_estadisticas(main_frame)
    
    def crear_frame_busqueda(self, parent):
        """Crea el frame de búsqueda"""
        frame_busqueda = ttk.LabelFrame(parent, text="Opciones de Búsqueda", padding="10")
        frame_busqueda.grid(row=1, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(0, 10))
        frame_busqueda.columnconfigure(1, weight=1)
        
        # Campo de búsqueda
        ttk.Label(frame_busqueda, text="Buscar:").grid(row=0, column=0, sticky=tk.W, padx=(0, 5))
        self.entry_busqueda = ttk.Entry(frame_busqueda, width=40)
        self.entry_busqueda.grid(row=0, column=1, sticky=(tk.W, tk.E), padx=(0, 10))
        self.entry_busqueda.bind('<Return>', lambda e: self.buscar())
        
        # Campo específico
        ttk.Label(frame_busqueda, text="Campo específico:").grid(row=0, column=2, sticky=tk.W, padx=(10, 5))
        self.combo_campo = ttk.Combobox(frame_busqueda, values=[
            "Todos los campos", "ID", "Nombre", "Apellido", "Departamento", 
            "Salario", "Edad", "Email", "Teléfono"
        ], state="readonly", width=15)
        self.combo_campo.set("Todos los campos")
        self.combo_campo.grid(row=0, column=3, padx=(0, 10))
        
        # Botones
        btn_buscar = ttk.Button(frame_busqueda, text="Buscar", command=self.buscar)
        btn_buscar.grid(row=0, column=4, padx=(0, 5))
        
        btn_limpiar = ttk.Button(frame_busqueda, text="Limpiar", command=self.limpiar_busqueda)
        btn_limpiar.grid(row=0, column=5)
        
        # Botón para mostrar todos
        btn_mostrar_todos = ttk.Button(frame_busqueda, text="Mostrar Todos", command=self.mostrar_todos)
        btn_mostrar_todos.grid(row=1, column=0, columnspan=6, pady=(10, 0))
    
    def crear_frame_resultados(self, parent):
        """Crea el frame de resultados"""
        frame_resultados = ttk.LabelFrame(parent, text="Resultados de la Búsqueda", padding="10")
        frame_resultados.grid(row=2, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(0, 10))
        frame_resultados.columnconfigure(0, weight=1)
        frame_resultados.rowconfigure(0, weight=1)
        
        # Treeview para mostrar resultados
        columns = ('ID', 'Nombre', 'Apellido', 'Departamento', 'Salario', 'Edad', 'Email', 'Teléfono')
        self.tree_resultados = ttk.Treeview(frame_resultados, columns=columns, show='headings', height=15)
        
        # Configurar columnas
        self.tree_resultados.heading('ID', text='ID')
        self.tree_resultados.heading('Nombre', text='Nombre')
        self.tree_resultados.heading('Apellido', text='Apellido')
        self.tree_resultados.heading('Departamento', text='Departamento')
        self.tree_resultados.heading('Salario', text='Salario (€)')
        self.tree_resultados.heading('Edad', text='Edad')
        self.tree_resultados.heading('Email', text='Email')
        self.tree_resultados.heading('Teléfono', text='Teléfono')
        
        # Configurar ancho de columnas
        self.tree_resultados.column('ID', width=50)
        self.tree_resultados.column('Nombre', width=100)
        self.tree_resultados.column('Apellido', width=100)
        self.tree_resultados.column('Departamento', width=120)
        self.tree_resultados.column('Salario', width=100)
        self.tree_resultados.column('Edad', width=60)
        self.tree_resultados.column('Email', width=200)
        self.tree_resultados.column('Teléfono', width=120)
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(frame_resultados, orient=tk.VERTICAL, command=self.tree_resultados.yview)
        self.tree_resultados.configure(yscrollcommand=scrollbar.set)
        
        # Grid
        self.tree_resultados.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))
    
    def crear_frame_estadisticas(self, parent):
        """Crea el frame de estadísticas"""
        frame_estadisticas = ttk.LabelFrame(parent, text="Estadísticas de Búsqueda", padding="10")
        frame_estadisticas.grid(row=3, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(0, 10))
        frame_estadisticas.columnconfigure(1, weight=1)
        
        # Labels de estadísticas
        self.label_total = ttk.Label(frame_estadisticas, text="Total empleados: 0")
        self.label_total.grid(row=0, column=0, sticky=tk.W, padx=(0, 20))
        
        self.label_resultados = ttk.Label(frame_estadisticas, text="Resultados encontrados: 0")
        self.label_resultados.grid(row=0, column=1, sticky=tk.W, padx=(0, 20))
        
        self.label_comparaciones = ttk.Label(frame_estadisticas, text="Comparaciones realizadas: 0")
        self.label_comparaciones.grid(row=0, column=2, sticky=tk.W, padx=(0, 20))
        
        self.label_tiempo = ttk.Label(frame_estadisticas, text="Tiempo de búsqueda: 0.000000s")
        self.label_tiempo.grid(row=1, column=0, sticky=tk.W, padx=(0, 20))
        
        # Barra de progreso
        self.progress = ttk.Progressbar(frame_estadisticas, mode='indeterminate')
        self.progress.grid(row=1, column=1, columnspan=2, sticky=(tk.W, tk.E), padx=(0, 0))
    
    def cargar_empleados(self):
        """Carga los empleados en un hilo separado"""
        def cargar():
            self.progress.start()
            self.empleados = GeneradorEmpleados.generar_lista_empleados(1000)
            self.busqueda = BusquedaLineal(self.empleados)
            self.progress.stop()
            self.actualizar_estadisticas()
            messagebox.showinfo("Carga Completada", f"Se han cargado {len(self.empleados)} empleados exitosamente.")
        
        threading.Thread(target=cargar, daemon=True).start()
    
    def buscar(self):
        """Realiza la búsqueda según los parámetros seleccionados"""
        if not self.empleados:
            messagebox.showwarning("Advertencia", "Los empleados aún se están cargando. Por favor, espere.")
            return
        
        valor_busqueda = self.entry_busqueda.get().strip()
        if not valor_busqueda:
            messagebox.showwarning("Advertencia", "Por favor, ingrese un valor para buscar.")
            return
        
        campo = self.combo_campo.get()
        
        # Realizar búsqueda
        if campo == "Todos los campos":
            self.resultados = self.busqueda.buscar_por_cualquier_campo(valor_busqueda)
        else:
            # Mapear nombres de campos
            campo_mapping = {
                "ID": "id",
                "Nombre": "nombre",
                "Apellido": "apellido",
                "Departamento": "departamento",
                "Salario": "salario",
                "Edad": "edad",
                "Email": "email",
                "Teléfono": "telefono"
            }
            campo_real = campo_mapping[campo]
            self.resultados = self.busqueda.buscar_por_campo(campo_real, valor_busqueda)
        
        # Mostrar resultados
        self.mostrar_resultados()
        self.actualizar_estadisticas()
    
    def mostrar_resultados(self):
        """Muestra los resultados en el TreeView"""
        # Limpiar resultados anteriores
        for item in self.tree_resultados.get_children():
            self.tree_resultados.delete(item)
        
        # Agregar nuevos resultados
        for empleado in self.resultados:
            self.tree_resultados.insert('', 'end', values=(
                empleado.id,
                empleado.nombre,
                empleado.apellido,
                empleado.departamento,
                f"{empleado.salario:,.2f}",
                empleado.edad,
                empleado.email,
                empleado.telefono
            ))
    
    def mostrar_todos(self):
        """Muestra todos los empleados"""
        if not self.empleados:
            messagebox.showwarning("Advertencia", "Los empleados aún se están cargando. Por favor, espere.")
            return
        
        self.resultados = self.empleados
        self.mostrar_resultados()
        self.actualizar_estadisticas()
    
    def limpiar_busqueda(self):
        """Limpia la búsqueda y los resultados"""
        self.entry_busqueda.delete(0, tk.END)
        self.combo_campo.set("Todos los campos")
        self.resultados = []
        self.mostrar_resultados()
        self.actualizar_estadisticas()
    
    def actualizar_estadisticas(self):
        """Actualiza las estadísticas mostradas"""
        total_empleados = len(self.empleados)
        resultados_encontrados = len(self.resultados)
        
        self.label_total.config(text=f"Total empleados: {total_empleados}")
        self.label_resultados.config(text=f"Resultados encontrados: {resultados_encontrados}")
        
        if self.busqueda:
            stats = self.busqueda.obtener_estadisticas()
            self.label_comparaciones.config(text=f"Comparaciones realizadas: {stats['comparaciones']}")
            self.label_tiempo.config(text=f"Tiempo de búsqueda: {stats['tiempo_busqueda']}s")
        else:
            self.label_comparaciones.config(text="Comparaciones realizadas: 0")
            self.label_tiempo.config(text="Tiempo de búsqueda: 0.000000s")

def main():
    """Función principal para ejecutar la aplicación"""
    root = tk.Tk()
    app = InterfazBusquedaEmpleados(root)
    root.mainloop()

if __name__ == "__main__":
    main()
