import json
import math
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from collections import defaultdict

COLOR_PALETTE = [
    "#E74C3C", "#3498DB", "#2ECC71", "#F1C40F", "#9B59B6", 
    "#E67E22", "#1ABC9C", "#34495E", "#D35400", "#27AE60",
    "#8E44AD", "#16A085", "#2C3E50", "#F39C12", "#C0392B"
]

class AppColoreadoGrafo:
    def __init__(self, root):
        self.root = root
        self.root.title("Asignador de Horarios de Exámenes (Coloreado de Grafos)")
        self.root.geometry("1000x650")
        self.root.minsize(900, 600)

        style = ttk.Style()
        style.theme_use("clam")

        self.crear_interfaz()

    def crear_interfaz(self):
        panel_superior = ttk.Frame(self.root, padding=10)
        panel_superior.pack(side=tk.TOP, fill=tk.X)

        lbl_titulo = ttk.Label(
            panel_superior, 
            text="Asignación Voraz de Horarios de Exámenes", 
            font=("Helvetica", 14, "bold")
        )
        lbl_titulo.pack(side=tk.LEFT, padx=10)

        btn_cargar = ttk.Button(
            panel_superior, 
            text="Cargar Grafo JSON", 
            command=self.cargar_y_procesar_json
        )
        btn_cargar.pack(side=tk.RIGHT, padx=10)

        self.lbl_estado = ttk.Label(
            self.root, 
            text="Cargue un archivo JSON para iniciar.", 
            font=("Helvetica", 10, "italic"),
            foreground="#555555"
        )
        self.lbl_estado.pack(side=tk.TOP, fill=tk.X, padx=20, pady=2)

        panel_principal = ttk.PanedWindow(self.root, orient=tk.HORIZONTAL)
        panel_principal.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        frame_canvas = ttk.LabelFrame(panel_principal, text="Visualización del Grafo", padding=5)
        panel_principal.add(frame_canvas, weight=3)

        self.canvas = tk.Canvas(frame_canvas, bg="#ffffff", highlightthickness=0)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        frame_texto = ttk.LabelFrame(panel_principal, text="Resultado y Reporte", padding=5)
        panel_principal.add(frame_texto, weight=2)

        self.txt_resultados = tk.Text(
            frame_texto, 
            wrap=tk.WORD, 
            font=("Consolas", 10),
            bg="#f8f9fa",
            bd=1,
            relief=tk.SOLID
        )
        scrollbar = ttk.Scrollbar(
            frame_texto, 
            orient=tk.VERTICAL, 
            command=self.txt_resultados.yview
        )
        self.txt_resultados.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.txt_resultados.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    def cargar_y_procesar_json(self):
        ruta_archivo = filedialog.askopenfilename(
            filetypes=[("Archivos JSON", "*.json"), ("Todos", "*.*")]
        )
        if not ruta_archivo:
            return

        try:
            with open(ruta_archivo, 'r', encoding='utf-8') as file:
                data = json.load(file)

            grafo = defaultdict(set)
            vertices = set()

            if isinstance(data, list):
                for elemento in data:
                    u = elemento.get("origen")
                    v = elemento.get("destino")
                    if u:
                        vertices.add(u)
                        if u not in grafo:
                            grafo[u] = set()
                    if v:
                        vertices.add(v)
                        if v not in grafo:
                            grafo[v] = set()
                    if u and v and u != v:
                        grafo[u].add(v)
                        grafo[v].add(u)
            elif isinstance(data, dict):
                for v in data.get("nodos", []):
                    vertices.add(v)
                    if v not in grafo:
                        grafo[v] = set()
                for arista in data.get("aristas", []):
                    u, v = arista.get("origen"), arista.get("destino")
                    if u and v:
                        vertices.add(u)
                        vertices.add(v)
                        grafo[u].add(v)
                        grafo[v].add(u)

            num_vertices = len(vertices)

            if num_vertices < 10:
                messagebox.showwarning(
                    "Advertencia",
                    f"El grafo cargado tiene {num_vertices} vértices.\nSe requieren mínimo 10 vértices."
                )

            asignacion_colores = self.colorear_grafo_voraz(grafo)
            es_valido = self.verificar_coloreado(grafo, asignacion_colores)

            self.dibujar_grafo(grafo, vertices, asignacion_colores)
            self.mostrar_resultados(vertices, grafo, asignacion_colores, es_valido)

        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error al procesar el archivo:\n{str(e)}")

    def colorear_grafo_voraz(self, grafo):
        asignacion = {}
        nodos_ordenados = sorted(grafo.keys(), key=lambda x: len(grafo[x]), reverse=True)

        for nodo in nodos_ordenados:
            colores_vecinos = {
                asignacion[vecino] 
                for vecino in grafo[nodo] 
                if vecino in asignacion
            }

            color_disponible = 0
            while color_disponible in colores_vecinos:
                color_disponible += 1

            asignacion[nodo] = color_disponible

        return asignacion

    def verificar_coloreado(self, grafo, asignacion):
        for nodo, vecinos in grafo.items():
            for vecino in vecinos:
                if asignacion[nodo] == asignacion[vecino]:
                    return False
        return True

    def dibujar_grafo(self, grafo, vertices, asignacion):
        self.canvas.delete("all")

        ancho = self.canvas.winfo_width()
        alto = self.canvas.winfo_height()

        if ancho <= 1 or alto <= 1:
            ancho, alto = 500, 500

        centro_x, centro_y = ancho / 2, alto / 2
        radio_grafo = min(ancho, alto) * 0.38
        radio_nodo = 22

        lista_vertices = sorted(list(vertices))
        total_v = len(lista_vertices)
        posiciones = {}

        for i, nodo in enumerate(lista_vertices):
            angulo = (2 * math.pi * i) / total_v
            x = centro_x + radio_grafo * math.cos(angulo)
            y = centro_y + radio_grafo * math.sin(angulo)
            posiciones[nodo] = (x, y)

        aristas_dibujadas = set()
        for u in grafo:
            for v in grafo[u]:
                pair = tuple(sorted([u, v]))
                if pair not in aristas_dibujadas:
                    aristas_dibujadas.add(pair)
                    x1, y1 = posiciones[u]
                    x2, y2 = posiciones[v]
                    self.canvas.create_line(x1, y1, x2, y2, fill="#bdc3c7", width=2)

        for nodo, (x, y) in posiciones.items():
            idx_color = asignacion.get(nodo, 0)
            hex_color = COLOR_PALETTE[idx_color % len(COLOR_PALETTE)]

            self.canvas.create_oval(
                x - radio_nodo, y - radio_nodo,
                x + radio_nodo, y + radio_nodo,
                fill=hex_color, outline="#2c3e50", width=2
            )

            self.canvas.create_text(
                x, y,
                text=nodo[:4],
                fill="#ffffff" if idx_color not in [3, 6] else "#000000",
                font=("Helvetica", 8, "bold")
            )

            self.canvas.create_text(
                x, y + radio_nodo + 12,
                text=nodo,
                fill="#333333",
                font=("Helvetica", 9, "bold")
            )

    def mostrar_resultados(self, vertices, grafo, asignacion, es_valido):
        self.txt_resultados.delete("1.0", tk.END)

        total_colores = max(asignacion.values()) + 1 if asignacion else 0
        num_vertices = len(vertices)

        franjas = defaultdict(list)
        for nodo, color in asignacion.items():
            franjas[color].append(nodo)

        texto_salida = f"=== RESUMEN DE PROCESAMIENTO ===\n"
        texto_salida += f"• Materias (vértices): {num_vertices}\n"
        texto_salida += f"• Cumple Mínimo (≥10): {'SÍ' if num_vertices >= 10 else 'NO'}\n"
        texto_salida += f"• Verificación Sin Conflicto: {'CORRECTA' if es_valido else 'FALLIDA'}\n"
        texto_salida += f"• Total Franjas Horarias: {total_colores}\n\n"
        texto_salida += "===================================\n"
        texto_salida += "   DISTRIBUCIÓN DE CADA FRANJA\n"
        texto_salida += "===================================\n\n"

        for color in sorted(franjas.keys()):
            materias = ", ".join(franjas[color])
            hex_c = COLOR_PALETTE[color % len(COLOR_PALETTE)]
            texto_salida += f"Franja {color + 1} [Color {color + 1} - {hex_c}]:\n"
            texto_salida += f"  └─ Cursos: {materias}\n\n"

        self.txt_resultados.insert(tk.END, texto_salida)

        if es_valido:
            self.lbl_estado.config(
                text=f"Procesado correctamente. Se usaron {total_colores} franjas horarias.", 
                foreground="green"
            )
        else:
            self.lbl_estado.config(
                text="Error: Vértices adyacentes tienen el mismo color.", 
                foreground="red"
            )

if __name__ == "__main__":
    root = tk.Tk()
    app = AppColoreadoGrafo(root)
    root.mainloop()