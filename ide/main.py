import sys
import os

# Añadir el directorio raíz al path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog, messagebox
from lexer.lexer import lexer as custom_lexer
from parser.parser import parser
from semantic.analizador_semantico import analyze_semantics_with_annotations, SymbolTable, SemanticNodeWithAnnotations
import re

class IDE(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("IDE")
        self.geometry("1200x800")  # Ajustar la altura según sea necesario
        self.filepath = None

        # Definir palabras reservadas aquí
        self.reserved_words = {
            'program', 'if', 'else', 'fi', 'do', 'until', 'while', 'read', 'write',
            'float', 'int', 'bool', 'not', 'and', 'or', 'true', 'false'
        }

        self.create_widgets()
        self.bind_events()

    def create_widgets(self):
        # Crear el menú de barra
        menubar = tk.Menu(self)
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Abrir", command=self.open_file)
        file_menu.add_command(label="Guardar", command=self.save_file)
        file_menu.add_command(label="Guardar como...", command=self.save_file_as)
        file_menu.add_separator()
        file_menu.add_command(label="Salir", command=self.quit)
        menubar.add_cascade(label="Archivo", menu=file_menu)

        compile_menu = tk.Menu(menubar, tearoff=0)
        compile_menu.add_command(label="Compilar", command=self.compile_code)
        menubar.add_cascade(label="Compilar", menu=compile_menu)

        self.config(menu=menubar)

        # Crear el frame principal con dos filas
        main_frame = tk.Frame(self, bg='#2b2b2b')
        main_frame.pack(expand=1, fill='both')
        main_frame.grid_rowconfigure(0, weight=4)  # Editor y panel
        main_frame.grid_rowconfigure(1, weight=1)  # Área de errores
        main_frame.grid_columnconfigure(0, weight=2)  # Editor de texto
        main_frame.grid_columnconfigure(1, weight=3)  # Pestañas (Tokens, Parser, etc.)

        # Crear el editor de texto en la primera fila y primera columna
        text_frame = tk.Frame(main_frame, padx=10, pady=10, bg='#2b2b2b')
        text_frame.grid(row=0, column=0, sticky='nsew')

        self.line_numbers = tk.Text(text_frame, width=4, bg='#1e1e1e', fg='#ffffff', state='disabled',
                                    font=('Consolas', 12), relief='flat')
        self.line_numbers.pack(side='left', fill='y')

        self.text_area = tk.Text(text_frame, wrap='word', bg='#1e1e1e', fg='#ffffff', insertbackground='white',
                                 font=('Consolas', 12), relief='flat')
        self.text_area.pack(expand=1, fill='both', padx=5, pady=5)

        self.text_area.bind('<KeyRelease>', self.update_line_numbers)
        self.text_area.bind('<MouseWheel>', self.update_line_numbers)  # Actualizar al desplazarse con el ratón

        # Crear el panel de pestañas en la primera fila y segunda columna
        notebook_frame = tk.Frame(main_frame, bg='#2b2b2b')
        notebook_frame.grid(row=0, column=1, sticky='nsew', padx=10, pady=10)

        notebook = ttk.Notebook(notebook_frame)

        # Pestaña para la Tabla de Tokens
        token_frame = tk.Frame(notebook, bg='#2b2b2b')
        self.token_table = ttk.Treeview(token_frame, columns=("clave", "lexema", "fila", "columna"), show='headings', style="Treeview")
        self.token_table.heading("clave", text="Clave")
        self.token_table.heading("lexema", text="Lexema")
        self.token_table.heading("fila", text="Fila")
        self.token_table.heading("columna", text="Columna")
        self.token_table.column("clave", width=80)
        self.token_table.column("lexema", width=150)
        self.token_table.column("fila", width=50)
        self.token_table.column("columna", width=70)
        self.token_table.pack(expand=1, fill='both')
        notebook.add(token_frame, text="Tokens")

        # Pestaña para la salida del Parser (árbol gramatical) usando Treeview
        parser_output_frame = tk.Frame(notebook, bg='#2b2b2b')
        self.parser_tree = ttk.Treeview(parser_output_frame)
        self.parser_tree.pack(expand=1, fill='both', padx=5, pady=5)
        notebook.add(parser_output_frame, text="Árbol Gramatical")

        # Pestaña para la salida Semántica usando Treeview
        semantic_tree_frame = tk.Frame(notebook, bg='#2b2b2b')
        self.semantic_tree = ttk.Treeview(semantic_tree_frame)
        self.semantic_tree.pack(expand=1, fill='both', padx=5, pady=5)
        notebook.add(semantic_tree_frame, text="Árbol Semántico")

        # Pestaña para la Tabla de Símbolos
        symbol_table_frame = tk.Frame(notebook, bg='#2b2b2b')
        self.symbol_table = ttk.Treeview(symbol_table_frame, columns=("name", "type", "value"), show='headings', style="Treeview")
        self.symbol_table.heading("name", text="Name")
        self.symbol_table.heading("type", text="Type")
        self.symbol_table.heading("value", text="Value")
        self.symbol_table.pack(expand=1, fill='both')
        notebook.add(symbol_table_frame, text="Tabla de Símbolos")

        # Empacar las pestañas
        notebook.pack(expand=1, fill='both')

        # Crear el frame de errores en la segunda fila y ocupar ambas columnas
        error_frame = tk.Frame(main_frame, padx=10, pady=10, bg='#2b2b2b')
        error_frame.grid(row=1, column=0, columnspan=2, sticky='nsew')

        self.error_area = tk.Text(error_frame, height=5, bg='#1e1e1e', fg='#ff5555', state='disabled', font=('Consolas', 12), relief='flat', insertbackground='white')
        self.error_area.pack(expand=1, fill='both', padx=5, pady=5)

    def bind_events(self):
        self.text_area.bind("<<Modified>>", self.on_modified)

    def update_line_numbers(self, event=None):
        line_numbers = self.get_line_numbers()
        self.line_numbers.config(state='normal')
        self.line_numbers.delete('1.0', 'end')
        self.line_numbers.insert('1.0', line_numbers)
        self.line_numbers.config(state='disabled')

    def get_line_numbers(self):
        output = ''
        if self.text_area.index('end') != '1.0':
            row, _ = self.text_area.index('end').split('.')
            for i in range(1, int(row)):
                output += f'{i}\n'
        return output

    def open_file(self):
        filepath = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if filepath:
            with open(filepath, 'r') as file:
                content = file.read()
            self.text_area.delete('1.0', tk.END)
            self.text_area.insert(tk.END, content)
            self.filepath = filepath
            self.update_line_numbers()
            self.highlight_reserved_words()

    def save_file(self):
        if self.filepath:
            with open(self.filepath, 'w') as file:
                file.write(self.text_area.get('1.0', tk.END))
        else:
            self.save_file_as()

    def save_file_as(self):
        filepath = filedialog.asksaveasfilename(defaultextension=".txt",
                                                filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if filepath:
            with open(filepath, 'w') as file:
                file.write(self.text_area.get('1.0', tk.END))
            self.filepath = filepath

    def compile_code(self):
        # Limpiar las áreas de errores
        self.error_area.config(state='normal')
        self.error_area.delete('1.0', tk.END)
        self.error_area.config(state='disabled')

        # Limpiar la tabla de tokens
        self.token_table.delete(*self.token_table.get_children())
        self.parser_tree.delete(*self.parser_tree.get_children())
        self.semantic_tree.delete(*self.semantic_tree.get_children())
        self.symbol_table.delete(*self.symbol_table.get_children())

        # Obtener el contenido del editor de texto
        source_code = self.text_area.get('1.0', tk.END)
        
        # Crear una instancia del Lexer y analizar el código fuente
        custom_lexer.input(source_code)
        custom_lexer.errors.clear()
        tokens = []
        for tok in custom_lexer:
            tokens.append(tok)
            self.token_table.insert("", "end", values=(tok.type, tok.value, tok.lineno, tok.lexpos))

        # Mostrar errores léxicos en el área de errores
        if custom_lexer.errors:
            self.error_area.config(state='normal')
            for error in custom_lexer.errors:
                self.error_area.insert(tk.END, f"Lexer Error: {error}\n")
            self.error_area.config(state='disabled')

        # Parsear el código fuente y manejar errores
        parser.errors.clear()
        result = None
        try:
            result = parser.parse(source_code)
        except Exception as e:
            self.error_area.config(state='normal')
            self.error_area.insert(tk.END, f"Parser Error: {e}\n")
            self.error_area.config(state='disabled')

        # Si hubo errores sintácticos, mostrar pero seguir generando el árbol
        if parser.errors:
            self.error_area.config(state='normal')
            for error in parser.errors:
                self.error_area.insert(tk.END, f"Parser Error: {error}\n")
            self.error_area.config(state='disabled')

        # Generar el árbol gramatical, incluso si hubo errores
        if result:
            self.display_parser_tree(result)
        else:
            # Si no se pudo generar el árbol completo debido a errores, generar un árbol parcial con los errores
            result = ('error', 'Parser Error', parser.errors)
            self.display_parser_tree(result)

        # Realizar análisis semántico y seguir si hay errores
        if result:
            self.generate_semantic_analysis(result)

    def generate_semantic_analysis(self, result):
        # Realizar análisis semántico
        symbol_table = SymbolTable()
        try:
            annotated_tree = analyze_semantics_with_annotations(result, symbol_table)
            self.populate_symbol_table(symbol_table)
            self.display_semantic_tree_with_annotations(annotated_tree)
        except Exception as e:
            self.error_area.config(state='normal')
            self.error_area.insert(tk.END, f"Semantic Error: {str(e)}\n")
            self.error_area.config(state='disabled')
            
        # Incluso si hay errores semánticos, debemos seguir mostrando el árbol semántico
        self.display_semantic_tree_with_annotations(result)

    def display_parser_tree(self, root_node):
        def add_nodes_to_tree(tree, node, parent=""):
            if isinstance(node, tuple):
                node_id = tree.insert(parent, "end", text=str(node[0]), open=True)
                for child in node[1:]:
                    add_nodes_to_tree(tree, child, node_id)
            elif isinstance(node, list):
                for item in node:
                    add_nodes_to_tree(tree, item, parent)
            else:
                tree.insert(parent, "end", text=str(node))

        # Limpiar el árbol antes de añadir nodos
        self.parser_tree.delete(*self.parser_tree.get_children())
        add_nodes_to_tree(self.parser_tree, root_node)

    def display_semantic_tree_with_annotations(self, root_node):
        def add_nodes_to_tree(tree, node, parent=""):
            # Verifica si es una tupla, en cuyo caso la procesamos como nodo básico
            if isinstance(node, tuple):
                node_text = str(node[0])  # El primer elemento es el tipo de nodo
                node_id = tree.insert(parent, "end", text=node_text, open=True)
                
                # Recorremos los hijos de la tupla
                for child in node[1:]:
                    add_nodes_to_tree(tree, child, node_id)

            elif isinstance(node, SemanticNodeWithAnnotations):
                # Verifica si el nodo tiene anotaciones válidas
                if hasattr(node, 'annotations') and isinstance(node.annotations, dict):
                    annotations = ", ".join(f"{k}: {v}" for k, v in node.annotations.items())
                else:
                    annotations = "No annotations"

                # Agregar el nodo con anotaciones
                node_id = tree.insert(parent, "end", text=f"{node.node_type} ({annotations})", open=True)

                # Recursivamente agregar los hijos
                for child in node.children:
                    add_nodes_to_tree(tree, child, node_id)

            else:
                # Si el nodo es de otro tipo (como literal o identificador), lo procesamos de forma simple
                node_id = tree.insert(parent, "end", text=str(node), open=True)

        # Llamar a la función de forma recursiva para el nodo raíz
        add_nodes_to_tree(self.semantic_tree, root_node)


    
    def populate_symbol_table(self, symbol_table):
        # Llenar la tabla de símbolos en la pestaña correspondiente
        for name, info in symbol_table.symbols.items():
            value = info.get('value', '')
            # Limitar los floats a 4 caracteres
            if isinstance(value, float):
                value = f"{value:.4f}"
            self.symbol_table.insert("", "end", values=(name, info['type'], value))

    def on_modified(self, event=None):
        self.highlight_reserved_words()
        self.text_area.edit_modified(False)

    def highlight_reserved_words(self):
         # Eliminar resaltado anterior
        self.text_area.tag_remove("reserved", "1.0", "end")
        
        # Obtener el contenido del área de texto
        text = self.text_area.get("1.0", "end-1c")
        
        # Resaltar cada palabra reservada
        for keyword in self.reserved_words:
            pattern = r'\b' + keyword + r'\b'
            for match in re.finditer(pattern, text):
                start = f"1.0 + {match.start()} chars"
                end = f"1.0 + {match.end()} chars"
                self.text_area.tag_add("reserved", start, end)

        # Configurar el estilo de la etiqueta "reserved" para el resaltado
        self.text_area.tag_configure("reserved", foreground="#00ff00")

if __name__ == "__main__":
    app = IDE()
    app.mainloop()
