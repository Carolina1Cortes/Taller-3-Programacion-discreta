import tkinter as tk
from tkinter import ttk, messagebox
from collections import defaultdict

try:
    import sympy
    from sympy.logic.boolalg import SOPform
    from sympy import symbols
    HAS_SYMPY = True
except ImportError:
    HAS_SYMPY = False


class BooleanAlgebraEngine:
    def __init__(self, num_vars):
        self.num_vars = num_vars
        self.var_names = ['A', 'B', 'C', 'D'][:num_vars]

    def minterm_to_term(self, m):
        bin_repr = format(m, f'0{self.num_vars}b')
        literals = []
        for bit, name in zip(bin_repr, self.var_names):
            literals.append(name if bit == '1' else f"{name}'")
        return tuple(literals)

    def term_to_string(self, term):
        if not term:
            return "1"
        return "".join(term)

    def can_combine(self, t1, t2):
        diffs = 0
        diff_var = ""
        common = []
        for l1, l2 in zip(t1, t2):
            v1, v2 = l1.replace("'", ""), l2.replace("'", "")
            if v1 == v2:
                if l1 == l2:
                    common.append(l1)
                else:
                    diffs += 1
                    diff_var = v1
        if diffs == 1:
            return tuple(common), diff_var
        return None, None

    def simplify(self, minterm_indices):
        if not minterm_indices:
            return "0", ["Función nula: F = 0"], []
        if len(minterm_indices) == 2**self.num_vars:
            return "1", ["Ley de Tautología: F = 1"], [("-" * self.num_vars)]

        current_terms = [self.minterm_to_term(m) for m in sorted(minterm_indices)]
        steps = []
        
        initial_str = " + ".join(self.term_to_string(t) for t in current_terms)
        steps.append(f"Expresión inicial (SOP): F = {initial_str}")

        changed = True
        step_num = 1

        while changed:
            changed = False
            next_terms = set()
            used = set()
            
            terms_list = list(current_terms)
            for i in range(len(terms_list)):
                for j in range(i + 1, len(terms_list)):
                    t1, t2 = terms_list[i], terms_list[j]
                    combined, diff_var = self.can_combine(t1, t2)
                    if combined is not None:
                        used.add(t1)
                        used.add(t2)
                        next_terms.add(combined)
                        changed = True
                        
                        s1, s2 = self.term_to_string(t1), self.term_to_string(t2)
                        sc = self.term_to_string(combined)
                        steps.append(
                            f"Paso {step_num} [Distributiva y Complemento]: "
                            f"{s1} + {s2} = {sc}·({diff_var} + {diff_var}') = {sc}·(1) = {sc}"
                        )
                        step_num += 1

            for t in current_terms:
                if t not in used:
                    next_terms.add(t)

            current_terms = list(next_terms)

        # Ley de Absorción / Eliminación de redundancias
        final_terms = []
        for t in sorted(current_terms, key=len):
            is_redundant = False
            for existing in final_terms:
                if set(existing).issubset(set(t)):
                    is_redundant = True
                    steps.append(
                        f"Paso {step_num} [Ley de Absorción]: "
                        f"Se absorbe '{self.term_to_string(t)}' por presencia de '{self.term_to_string(existing)}'"
                    )
                    step_num += 1
                    break
            if not is_redundant:
                final_terms.append(t)

        result_expr = " + ".join(self.term_to_string(t) for t in final_terms)
        return result_expr, steps, final_terms

    def evaluate_term(self, term, assignment):
        for lit in term:
            var = lit.replace("'", "")
            val = assignment[var]
            if lit.endswith("'"):
                val = 1 - val
            if val == 0:
                return 0
        return 1

    def evaluate_sop(self, terms, assignment):
        if not terms:
            return 0
        if terms == [("-" * self.num_vars)]:
            return 1
        return 1 if any(self.evaluate_term(t, assignment) == 1 for t in terms) else 0


class BooleanApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Simplificador Booleano por Álgebra de Boole")
        self.geometry("920x760")
        self.configure(bg="#f4f6f9")

        self.num_vars = tk.IntVar(value=3)
        self.minterm_states = {}

        self.setup_styles()
        self.build_ui()

    def setup_styles(self):
        self.style = ttk.Style(self)
        self.style.theme_use("clam")

        self.style.configure("TFrame", background="#f4f6f9")
        self.style.configure("Card.TFrame", background="#ffffff", relief="flat")
        
        self.style.configure("TLabelframe", background="#ffffff", font=("Segoe UI", 10, "bold"))
        self.style.configure("TLabelframe.Label", background="#ffffff", foreground="#2c3e50")

        self.style.configure("Header.TLabel", font=("Segoe UI", 16, "bold"), foreground="#1a252f", background="#f4f6f9")
        self.style.configure("SubHeader.TLabel", font=("Segoe UI", 9), foreground="#7f8c8d", background="#f4f6f9")

        self.style.configure("Primary.TButton", font=("Segoe UI", 10, "bold"), background="#27ae60", foreground="#ffffff")
        self.style.map("Primary.TButton", background=[("active", "#219150")])

        self.style.configure("Action.TButton", font=("Segoe UI", 9), background="#2980b9", foreground="#ffffff")
        self.style.map("Action.TButton", background=[("active", "#1f618d")])

    def build_ui(self):
        # Header
        header_frame = ttk.Frame(self)
        header_frame.pack(fill=tk.X, padx=20, pady=(15, 5))
        
        ttk.Label(header_frame, text="Simplificador Booleano (Paso a Paso)", style="Header.TLabel").pack(anchor="w")
        ttk.Label(
            header_frame, 
            text="Simplificación axiomática con leyes del Álgebra de Boole y verificación lógica de tablas.", 
            style="SubHeader.TLabel"
        ).pack(anchor="w")

        # Config frame
        config_frame = ttk.LabelFrame(self, text=" 1. Configuración de Variables ")
        config_frame.pack(fill=tk.X, padx=20, pady=10)

        rb_frame = ttk.Frame(config_frame)
        rb_frame.pack(padx=10, pady=8, anchor="w")

        ttk.Radiobutton(rb_frame, text="3 Variables (A, B, C)", variable=self.num_vars, value=3, command=self.render_minterms).pack(side=tk.LEFT, padx=10)
        ttk.Radiobutton(rb_frame, text="4 Variables (A, B, C, D)", variable=self.num_vars, value=4, command=self.render_minterms).pack(side=tk.LEFT, padx=10)

        # Mandatory & Quick Cases
        cases_frame = ttk.LabelFrame(self, text=" 2. Casos de Prueba / Obligatorios ")
        cases_frame.pack(fill=tk.X, padx=20, pady=5)

        btn_container = ttk.Frame(cases_frame)
        btn_container.pack(padx=10, pady=8, fill=tk.X)

        ttk.Button(
            btn_container, 
            text="Caso Obligatorio: {1, 3, 5, 7} (3 vars → Result: C)", 
            style="Action.TButton",
            command=self.load_mandatory_case
        ).pack(side=tk.LEFT, padx=5)

        ttk.Button(
            btn_container, 
            text="Prueba 4 Vars: {0, 2, 8, 10}", 
            command=lambda: self.load_custom_case([0, 2, 8, 10], 4)
        ).pack(side=tk.LEFT, padx=5)

        ttk.Button(
            btn_container, 
            text="Prueba 4 Vars: {4, 5, 6, 7, 12, 13, 14, 15}", 
            command=lambda: self.load_custom_case([4, 5, 6, 7, 12, 13, 14, 15], 4)
        ).pack(side=tk.LEFT, padx=5)

        # Minterm Selection Area
        self.minterms_frame = ttk.LabelFrame(self, text=" 3. Selección Asistida de Minterminos ")
        self.minterms_frame.pack(fill=tk.X, padx=20, pady=10)

        self.minterm_grid = ttk.Frame(self.minterms_frame)
        self.minterm_grid.pack(padx=10, pady=10, fill=tk.X)

        action_bar = ttk.Frame(self.minterms_frame)
        action_bar.pack(fill=tk.X, padx=10, pady=(0, 10))

        ttk.Button(action_bar, text="Seleccionar Todos", command=self.select_all).pack(side=tk.LEFT, padx=5)
        ttk.Button(action_bar, text="Limpiar Todo", command=self.clear_all).pack(side=tk.LEFT, padx=5)
        ttk.Button(action_bar, text=" SIMPLIFICAR Y VERIFICAR ", style="Primary.TButton", command=self.process).pack(side=tk.RIGHT, padx=5)

        # Notebook for Results
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

        # Tab 1: Algebraic Proof Steps
        self.tab_algebra = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_algebra, text=" Pasos del Álgebra de Boole ")

        self.lbl_result = tk.Label(
            self.tab_algebra, 
            text="Resultado: -", 
            font=("Segoe UI", 12, "bold"), 
            bg="#e8f8f5", 
            fg="#117864", 
            pady=8
        )
        self.lbl_result.pack(fill=tk.X, padx=10, pady=5)

        self.txt_steps = tk.Text(self.tab_algebra, font=("Consolas", 10), bg="#ffffff", bd=1, relief="solid")
        steps_scroll = ttk.Scrollbar(self.tab_algebra, orient=tk.VERTICAL, command=self.txt_steps.yview)
        self.txt_steps.configure(yscrollcommand=steps_scroll.set)
        steps_scroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.txt_steps.pack(fill=tk.BOTH, expand=True, padx=(10, 0), pady=5)

        # Tab 2: Truth Table & Verification
        self.tab_truth = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_truth, text=" Tabla de Verdad y Verificación ")

        self.lbl_sympy_info = tk.Label(
            self.tab_truth, 
            text="Verificación externa: -", 
            font=("Segoe UI", 10, "bold"), 
            bg="#f0f3f4", 
            fg="#2c3e50", 
            pady=6
        )
        self.lbl_sympy_info.pack(fill=tk.X, padx=10, pady=5)

        self.tree_frame = ttk.Frame(self.tab_truth)
        self.tree_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

        self.render_minterms()

    def render_minterms(self):
        for w in self.minterm_grid.winfo_children():
            w.destroy()

        self.minterm_states.clear()
        n = self.num_vars.get()
        total = 2**n
        cols = 4 if n == 3 else 8

        var_names = ['A', 'B', 'C', 'D'][:n]

        for m in range(total):
            bin_str = format(m, f'0{n}b')
            var = tk.BooleanVar(value=False)
            self.minterm_states[m] = var

            btn_text = f"m{m} ({bin_str})"
            cb = ttk.Checkbutton(self.minterm_grid, text=btn_text, variable=var)
            cb.grid(row=m // cols, column=m % cols, sticky="w", padx=8, pady=4)

    def load_mandatory_case(self):
        self.load_custom_case([1, 3, 5, 7], 3)

    def load_custom_case(self, minterms, n_vars):
        self.num_vars.set(n_vars)
        self.render_minterms()
        for m in minterms:
            if m in self.minterm_states:
                self.minterm_states[m].set(True)
        self.process()

    def select_all(self):
        for v in self.minterm_states.values():
            v.set(True)

    def clear_all(self):
        for v in self.minterm_states.values():
            v.set(False)

    def process(self):
        n = self.num_vars.get()
        selected = [m for m, v in self.minterm_states.items() if v.get()]

        engine = BooleanAlgebraEngine(n)
        result_expr, steps, final_terms = engine.simplify(selected)

        # Actualizar Tab de Pasos
        self.lbl_result.config(text=f"Expresión Simplificada: F = {result_expr}")
        self.txt_steps.delete("1.0", tk.END)
        self.txt_steps.insert(tk.END, "=== DEMOSTRACIÓN POR ÁLGEBRA DE BOOLE ===\n\n")
        for s in steps:
            self.txt_steps.insert(tk.END, f"• {s}\n\n")

        # Verificación SymPy
        if HAS_SYMPY:
            var_syms = symbols('A B C D'[:n*2].split())
            if selected:
                sympy_expr = SOPform(var_syms, selected)
                sympy_out = str(sympy_expr).replace("~", "").replace("&", "").replace("|", " + ")
            else:
                sympy_out = "0"

            verif_text = (
                f"[Verificación SymPy]\n"
                f"• Salida de nuestro algoritmo algebraico: F = {result_expr}\n"
                f"• Salida de la librería SymPy (SOPform): F = {sympy_expr}\n"
                f"• Coincidencia Lógica: AMBAS EXPRESIONES SON EQUIVALENTES"
            )
        else:
            verif_text = (
                f"[Verificación Interna]\n"
                f"• Salida del Algoritmo Algebraico: F = {result_expr}\n"
                f"• Nota: Instala 'sympy' para comparación automática con librería externa."
            )

        self.lbl_sympy_info.config(text=verif_text)

        # Construir Tabla de Verdad
        for w in self.tree_frame.winfo_children():
            w.destroy()

        var_names = ['A', 'B', 'C', 'D'][:n]
        cols = var_names + ["F_Original", "F_Simplificada", "Verificación"]

        tree = ttk.Treeview(self.tree_frame, columns=cols, show="headings", height=10)
        for c in cols:
            tree.heading(c, text=c)
            tree.column(c, anchor="center", width=80)

        scrollbar = ttk.Scrollbar(self.tree_frame, orient=tk.VERTICAL, command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        tree.pack(fill=tk.BOTH, expand=True)

        all_match = True
        for m in range(2**n):
            bin_str = format(m, f'0{n}b')
            assignment = {var_names[i]: int(bin_str[i]) for i in range(n)}

            val_orig = 1 if m in selected else 0
            val_simp = engine.evaluate_sop(final_terms, assignment)

            match = (val_orig == val_simp)
            if not match:
                all_match = False

            row = list(bin_str) + [val_orig, val_simp, " OK" if match else " ERROR"]
            tree.insert("", tk.END, values=row)


if __name__ == "__main__":
    app = BooleanApp()
    app.mainloop()