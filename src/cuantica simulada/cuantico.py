import tkinter as tk
from tkinter import ttk
import math
import random

class SimuladorQubit(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Simulador de Qubit Cuántico")
        self.geometry("850x700")
        self.configure(bg="#181825")
        self.resizable(False, False)

        self.alpha = complex(1.0, 0.0)
        self.beta = complex(0.0, 0.0)
        self.historial_puertas = []

        self.crear_interfaz()
        self.actualizar_pantalla()

    def crear_interfaz(self):
        # Encabezado
        frame_header = tk.Frame(self, bg="#181825")
        frame_header.pack(fill=tk.X, padx=20, pady=15)

        lbl_title = tk.Label(
            frame_header, 
            text="Simulador Cuántico de 1 Qubit", 
            font=("Helvetica", 18, "bold"), 
            fg="#cba6f7", 
            bg="#181825"
        )
        lbl_title.pack(anchor="w")

        lbl_sub = tk.Label(
            frame_header, 
            text="Estado:  |ψ⟩ = α|0⟩ + β|1⟩   |   Medición de 1000 disparos", 
            font=("Helvetica", 10), 
            fg="#a6adc8", 
            bg="#181825"
        )
        lbl_sub.pack(anchor="w", pady=2)

        # Contenedor principal
        main_frame = tk.Frame(self, bg="#181825")
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=5)

        # Panel Izquierdo: Control y Compuertas
        panel_left = tk.Frame(main_frame, bg="#1e1e2e", bd=1, relief=tk.SOLID)
        panel_left.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 10))

        # Sección Estado Inicial
        lbl_sec1 = tk.Label(panel_left, text="1. ESTADO INICIAL", font=("Helvetica", 11, "bold"), fg="#89b4fa", bg="#1e1e2e")
        lbl_sec1.pack(anchor="w", padx=15, pady=(15, 5))

        frame_init = tk.Frame(panel_left, bg="#1e1e2e")
        frame_init.pack(fill=tk.X, padx=15, pady=5)

        btn_init0 = tk.Button(frame_init, text="Reiniciar a |0⟩", font=("Helvetica", 10, "bold"), bg="#313244", fg="#cdd6f4", activebackground="#45475a", activeforeground="#ffffff", command=self.reset_qubit_0, bd=0, padx=10, pady=5)
        btn_init0.pack(side=tk.LEFT, padx=(0, 5))

        btn_init1 = tk.Button(frame_init, text="Reiniciar a |1⟩", font=("Helvetica", 10, "bold"), bg="#313244", fg="#cdd6f4", activebackground="#45475a", activeforeground="#ffffff", command=self.reset_qubit_1, bd=0, padx=10, pady=5)
        btn_init1.pack(side=tk.LEFT)

        # Sección Aplicar Compuertas
        lbl_sec2 = tk.Label(panel_left, text="2. COMPUERTAS CUÁNTICAS", font=("Helvetica", 11, "bold"), fg="#89b4fa", bg="#1e1e2e")
        lbl_sec2.pack(anchor="w", padx=15, pady=(20, 5))

        frame_gates = tk.Frame(panel_left, bg="#1e1e2e")
        frame_gates.pack(fill=tk.X, padx=15, pady=5)

        btn_x = tk.Button(frame_gates, text="Compuerta X\n(NOT)", font=("Helvetica", 10, "bold"), bg="#fab387", fg="#11111b", command=self.aplicar_x, width=10, height=2, bd=0)
        btn_x.pack(side=tk.LEFT, padx=3)

        btn_z = tk.Button(frame_gates, text="Compuerta Z\n(Fase)", font=("Helvetica", 10, "bold"), bg="#f9e2af", fg="#11111b", command=self.aplicar_z, width=10, height=2, bd=0)
        btn_z.pack(side=tk.LEFT, padx=3)

        btn_h = tk.Button(frame_gates, text="Compuerta H\n(Hadamard)", font=("Helvetica", 10, "bold"), bg="#a6e3a1", fg="#11111b", command=self.aplicar_h, width=10, height=2, bd=0)
        btn_h.pack(side=tk.LEFT, padx=3)

        # Sección Casos Obligatorios
        lbl_sec3 = tk.Label(panel_left, text="3. CASOS PRUEBA OBLIGATORIOS", font=("Helvetica", 11, "bold"), fg="#89b4fa", bg="#1e1e2e")
        lbl_sec3.pack(anchor="w", padx=15, pady=(20, 5))

        btn_c1 = tk.Button(panel_left, text="Prueba 1:  X |0⟩  →  |1⟩", font=("Helvetica", 9, "bold"), bg="#45475a", fg="#cdd6f4", anchor="w", padx=10, pady=6, bd=0, command=self.caso_obligatorio_1)
        btn_c1.pack(fill=tk.X, padx=15, pady=3)

        btn_c2 = tk.Button(panel_left, text="Prueba 2:  H |0⟩  →  50% / 50%", font=("Helvetica", 9, "bold"), bg="#45475a", fg="#cdd6f4", anchor="w", padx=10, pady=6, bd=0, command=self.caso_obligatorio_2)
        btn_c2.pack(fill=tk.X, padx=15, pady=3)

        btn_c3 = tk.Button(panel_left, text="Prueba 3:  H H |0⟩  →  |0⟩", font=("Helvetica", 9, "bold"), bg="#45475a", fg="#cdd6f4", anchor="w", padx=10, pady=6, bd=0, command=self.caso_obligatorio_3)
        btn_c3.pack(fill=tk.X, padx=15, pady=3)

        # Historial
        lbl_hist = tk.Label(panel_left, text="Historial de operaciones:", font=("Helvetica", 9, "italic"), fg="#a6adc8", bg="#1e1e2e")
        lbl_hist.pack(anchor="w", padx=15, pady=(15, 2))

        self.lbl_historial = tk.Label(panel_left, text="|0⟩", font=("Consolas", 10), fg="#f5e0dc", bg="#313244", padx=10, pady=5, anchor="w")
        self.lbl_historial.pack(fill=tk.X, padx=15, pady=(0, 15))

        # Panel Derecho: Visualización y Resultados
        panel_right = tk.Frame(main_frame, bg="#1e1e2e", bd=1, relief=tk.SOLID)
        panel_right.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        lbl_sec4 = tk.Label(panel_right, text="ESTADO Y RESULTADOS DE MEDICIÓN", font=("Helvetica", 11, "bold"), fg="#89b4fa", bg="#1e1e2e")
        lbl_sec4.pack(anchor="w", padx=15, pady=(15, 5))

        self.lbl_vector = tk.Label(panel_right, text="", font=("Consolas", 11), fg="#cdd6f4", bg="#1e1e2e", justify=tk.LEFT)
        self.lbl_vector.pack(anchor="w", padx=15, pady=5)

        # Canvas para Gráfico
        self.canvas = tk.Canvas(panel_right, bg="#181825", highlightthickness=0)
        self.canvas.pack(fill=tk.BOTH, expand=True, padx=15, pady=10)

        # Botón Medición
        btn_medir = tk.Button(panel_right, text="Simular 1000 Mediciones", font=("Helvetica", 11, "bold"), bg="#f38ba8", fg="#11111b", command=self.actualizar_pantalla, bd=0, pady=8)
        btn_medir.pack(fill=tk.X, padx=15, pady=(0, 15))

    def reset_qubit_0(self):
        self.alpha = complex(1.0, 0.0)
        self.beta = complex(0.0, 0.0)
        self.historial_puertas = []
        self.actualizar_pantalla()

    def reset_qubit_1(self):
        self.alpha = complex(0.0, 0.0)
        self.beta = complex(1.0, 0.0)
        self.historial_puertas = ["X"]
        self.actualizar_pantalla()

    def normalizar(self):
        norma = math.sqrt(abs(self.alpha)**2 + abs(self.beta)**2)
        if norma > 0:
            self.alpha /= norma
            self.beta /= norma

    def aplicar_x(self):
        self.alpha, self.beta = self.beta, self.alpha
        self.historial_puertas.append("X")
        self.normalizar()
        self.actualizar_pantalla()

    def aplicar_z(self):
        self.beta = -self.beta
        self.historial_puertas.append("Z")
        self.normalizar()
        self.actualizar_pantalla()

    def aplicar_h(self):
        inv_sqrt2 = 1.0 / math.sqrt(2)
        nuevo_alpha = inv_sqrt2 * (self.alpha + self.beta)
        nuevo_beta = inv_sqrt2 * (self.alpha - self.beta)
        self.alpha, self.beta = nuevo_alpha, nuevo_beta
        self.historial_puertas.append("H")
        self.normalizar()
        self.actualizar_pantalla()

    def caso_obligatorio_1(self):
        self.reset_qubit_0()
        self.aplicar_x()

    def caso_obligatorio_2(self):
        self.reset_qubit_0()
        self.aplicar_h()

    def caso_obligatorio_3(self):
        self.reset_qubit_0()
        self.aplicar_h()
        self.aplicar_h()

    def formatear_complejo(self, c):
        r = round(c.real, 4)
        i = round(c.imag, 4)
        if abs(i) < 1e-6:
            return f"{r:.4f}"
        if abs(r) < 1e-6:
            return f"{i:.4f}i"
        signo = "+" if i >= 0 else "-"
        return f"({r:.4f} {signo} {abs(i):.4f}i)"

    def actualizar_pantalla(self):
        # Texto del vector
        str_a = self.formatear_complejo(self.alpha)
        str_b = self.formatear_complejo(self.beta)
        
        txt_vec = f"Vector de Estado:\n  |ψ⟩ = [ {str_a} ] |0⟩\n        [ {str_b} ] |1⟩"
        self.lbl_vector.config(text=txt_vec)

        # Historial
        cadena_hist = " |0⟩"
        if self.historial_puertas:
            cadena_hist += " → " + " → ".join(self.historial_puertas)
        self.lbl_historial.config(text=cadena_hist)

        # Probabilidades Teóricas
        p0_teorica = abs(self.alpha)**2
        p1_teorica = abs(self.beta)**2

        # Simulación 1000 tiros
        tiros = 1000
        resultados = random.choices([0, 1], weights=[p0_teorica, p1_teorica], k=tiros)
        c0 = resultados.count(0)
        c1 = resultados.count(1)
        p0_obs = c0 / tiros
        p1_obs = c1 / tiros

        # Dibujar Gráfico Canvas
        self.dibujar_grafico(p0_teorica, p1_teorica, c0, c1, p0_obs, p1_obs)

    def dibujar_grafico(self, p0_t, p1_t, c0, c1, p0_o, p1_o):
        self.canvas.delete("all")
        
        w = self.canvas.winfo_width()
        h = self.canvas.winfo_height()

        if w <= 1:
            w, h = 350, 320

        # Barras de Estado |0> y |1>
        col_w = w / 2
        bar_max_h = h - 110

        # Graficar Estado |0>
        h0_t = p0_t * bar_max_h
        h0_o = p0_o * bar_max_h

        x0_base = 40
        y_base = h - 60

        # Teórica |0>
        self.canvas.create_rectangle(x0_base, y_base - h0_t, x0_base + 35, y_base, fill="#89b4fa", outline="")
        # Observada |0>
        self.canvas.create_rectangle(x0_base + 40, y_base - h0_o, x0_base + 75, y_base, fill="#b4befe", outline="")

        self.canvas.create_text(x0_base + 37, y_base + 20, text="|0⟩", font=("Helvetica", 12, "bold"), fill="#cdd6f4")
        self.canvas.create_text(x0_base + 37, y_base + 38, text=f"Obs: {c0}/1000", font=("Helvetica", 9), fill="#a6adc8")
        self.canvas.create_text(x0_base + 37, y_base + 52, text=f"({p0_o*100:.1f}%)", font=("Helvetica", 9, "bold"), fill="#89b4fa")

        # Graficar Estado |1>
        x1_base = col_w + 40
        h1_t = p1_t * bar_max_h
        h1_o = p1_o * bar_max_h

        # Teórica |1>
        self.canvas.create_rectangle(x1_base, y_base - h1_t, x1_base + 35, y_base, fill="#cba6f7", outline="")
        # Observada |1>
        self.canvas.create_rectangle(x1_base + 40, y_base - h1_o, x1_base + 75, y_base, fill="#f5c2e7", outline="")

        self.canvas.create_text(x1_base + 37, y_base + 20, text="|1⟩", font=("Helvetica", 12, "bold"), fill="#cdd6f4")
        self.canvas.create_text(x1_base + 37, y_base + 38, text=f"Obs: {c1}/1000", font=("Helvetica", 9), fill="#a6adc8")
        self.canvas.create_text(x1_base + 37, y_base + 52, text=f"({p1_o*100:.1f}%)", font=("Helvetica", 9, "bold"), fill="#cba6f7")

        # Leyenda
        self.canvas.create_rectangle(20, 15, 35, 25, fill="#89b4fa", outline="")
        self.canvas.create_text(80, 20, text="Prob. Teórica", font=("Helvetica", 8), fill="#a6adc8")

        self.canvas.create_rectangle(140, 15, 155, 25, fill="#b4befe", outline="")
        self.canvas.create_text(210, 20, text="Frecuencia 1000 tiros", font=("Helvetica", 8), fill="#a6adc8")


if __name__ == "__main__":
    app = SimuladorQubit()
    app.mainloop()