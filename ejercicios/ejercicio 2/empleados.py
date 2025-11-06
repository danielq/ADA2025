import random
from dataclasses import dataclass
from typing import List, Optional
import time

@dataclass
class Empleado:
    """Clase para representar un empleado con sus datos básicos"""
    id: int
    nombre: str
    apellido: str
    departamento: str
    salario: float
    edad: int
    email: str
    telefono: str

class GeneradorEmpleados:
    """Clase para generar empleados con datos aleatorios"""
    
    NOMBRES = [
        "Ana", "Carlos", "María", "José", "Laura", "David", "Carmen", "Antonio",
        "Isabel", "Francisco", "Elena", "Manuel", "Pilar", "Rafael", "Teresa",
        "Miguel", "Cristina", "Javier", "Mónica", "Alejandro", "Patricia", "Sergio",
        "Raquel", "Fernando", "Silvia", "Roberto", "Beatriz", "Álvaro", "Natalia",
        "Rubén", "Sandra", "Diego", "Lorena", "Pablo", "Marta", "Adrián", "Eva",
        "Víctor", "Claudia", "Iván", "Rocío", "Óscar", "Cristina", "Gonzalo",
        "Nuria", "Héctor", "Miriam", "Jorge", "Leticia", "Raúl", "Alicia"
    ]
    
    APELLIDOS = [
        "García", "Rodríguez", "González", "Fernández", "López", "Martínez",
        "Sánchez", "Pérez", "Gómez", "Martín", "Jiménez", "Ruiz", "Hernández",
        "Díaz", "Moreno", "Muñoz", "Álvarez", "Romero", "Alonso", "Gutiérrez",
        "Navarro", "Torres", "Domínguez", "Vázquez", "Ramos", "Gil", "Ramírez",
        "Serrano", "Blanco", "Suárez", "Molina", "Morales", "Ortega", "Delgado",
        "Castro", "Ortiz", "Rubio", "Marín", "Sanz", "Iglesias", "Medina",
        "Cortés", "Garrido", "Castillo", "Santos", "Lozano", "Guerrero", "Cano"
    ]
    
    DEPARTAMENTOS = [
        "Ventas", "Marketing", "Recursos Humanos", "Tecnología", "Finanzas",
        "Producción", "Logística", "Atención al Cliente", "Investigación y Desarrollo",
        "Administración", "Contabilidad", "Legal", "Compras", "Calidad"
    ]
    
    @classmethod
    def generar_empleado(cls, id_empleado: int) -> Empleado:
        """Genera un empleado con datos aleatorios"""
        nombre = random.choice(cls.NOMBRES)
        apellido = random.choice(cls.APELLIDOS)
        departamento = random.choice(cls.DEPARTAMENTOS)
        salario = round(random.uniform(25000, 120000), 2)
        edad = random.randint(22, 65)
        email = f"{nombre.lower()}.{apellido.lower()}{random.randint(1, 999)}@empresa.com"
        telefono = f"+34 {random.randint(600000000, 799999999)}"
        
        return Empleado(
            id=id_empleado,
            nombre=nombre,
            apellido=apellido,
            departamento=departamento,
            salario=salario,
            edad=edad,
            email=email,
            telefono=telefono
        )
    
    @classmethod
    def generar_lista_empleados(cls, cantidad: int = 1000) -> List[Empleado]:
        """Genera una lista de empleados con datos aleatorios"""
        empleados = []
        for i in range(1, cantidad + 1):
            empleados.append(cls.generar_empleado(i))
        return empleados

class BusquedaLineal:
    """Clase para implementar búsqueda lineal en la lista de empleados"""
    
    def __init__(self, empleados: List[Empleado]):
        self.empleados = empleados
        self.comparaciones = 0
        self.tiempo_busqueda = 0
    
    def buscar_por_campo(self, campo: str, valor_busqueda: str) -> List[Empleado]:
        """
        Busca empleados por cualquier campo usando búsqueda lineal
        """
        self.comparaciones = 0
        inicio_tiempo = time.time()
        resultados = []
        
        # Normalizar el valor de búsqueda
        valor_busqueda = str(valor_busqueda).lower().strip()
        
        for empleado in self.empleados:
            self.comparaciones += 1
            
            # Obtener el valor del campo del empleado
            if campo == "id":
                valor_empleado = str(empleado.id).lower()
            elif campo == "nombre":
                valor_empleado = empleado.nombre.lower()
            elif campo == "apellido":
                valor_empleado = empleado.apellido.lower()
            elif campo == "departamento":
                valor_empleado = empleado.departamento.lower()
            elif campo == "salario":
                valor_empleado = str(empleado.salario).lower()
            elif campo == "edad":
                valor_empleado = str(empleado.edad).lower()
            elif campo == "email":
                valor_empleado = empleado.email.lower()
            elif campo == "telefono":
                valor_empleado = empleado.telefono.lower()
            else:
                continue
            
            # Verificar si coincide (búsqueda parcial)
            if valor_busqueda in valor_empleado:
                resultados.append(empleado)
        
        self.tiempo_busqueda = time.time() - inicio_tiempo
        return resultados
    
    def buscar_por_cualquier_campo(self, valor_busqueda: str) -> List[Empleado]:
        """
        Busca empleados en todos los campos usando búsqueda lineal
        """
        self.comparaciones = 0
        inicio_tiempo = time.time()
        resultados = []
        
        # Normalizar el valor de búsqueda
        valor_busqueda = str(valor_busqueda).lower().strip()
        
        for empleado in self.empleados:
            self.comparaciones += 1
            
            # Lista de todos los valores de campos del empleado
            valores_empleado = [
                str(empleado.id).lower(),
                empleado.nombre.lower(),
                empleado.apellido.lower(),
                empleado.departamento.lower(),
                str(empleado.salario).lower(),
                str(empleado.edad).lower(),
                empleado.email.lower(),
                empleado.telefono.lower()
            ]
            
            # Verificar si el valor de búsqueda está en algún campo
            if any(valor_busqueda in valor for valor in valores_empleado):
                resultados.append(empleado)
        
        self.tiempo_busqueda = time.time() - inicio_tiempo
        return resultados
    
    def obtener_estadisticas(self) -> dict:
        """Retorna estadísticas de la última búsqueda"""
        return {
            "comparaciones": self.comparaciones,
            "tiempo_busqueda": round(self.tiempo_busqueda, 6),
            "total_empleados": len(self.empleados)
        }
