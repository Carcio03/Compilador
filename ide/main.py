import sys
import os

# Añadir el directorio raíz al path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog, messagebox
from lexer.lexer import lexer as custom_lexer
from parser.parser import parser
from semantic.analizador_semantico import SymbolTable, analyze_semantics
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

        # Pestaña para la salida del Parser (árbol gramatical)
        parser_output_frame = tk.Frame(notebook, bg='#2b2b2b')
        self.parser_output_area = tk.Text(parser_output_frame, bg='#1e1e1e', fg='#00ff00', state='disabled', font=('Consolas', 12), relief='flat')
        self.parser_output_area.pack(expand=1, fill='both', padx=5, pady=5)
        notebook.add(parser_output_frame, text="Árbol Gramatical")

        # Pestaña para la salida Semántica
        semantic_tree_frame = tk.Frame(notebook, bg='#2b2b2b')
        self.semantic_tree_area = tk.Text(semantic_tree_frame, bg='#1e1e1e', fg='#00ff00', state='disabled', font=('Consolas', 12), relief='flat')
        self.semantic_tree_area.pack(expand=1, fill='both', padx=5, pady=5)
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
        self.clear_output_areas()

        # Limpiar la tabla de tokens
        self.token_table.delete(*self.token_table.get_children())
        self.parser_output_area.config(state='normal')
        self.parser_output_area.delete('1.0', tk.END)
        self.parser_output_area.config(state='disabled')
        self.semantic_output_area.config(state='normal')
        self.semantic_output_area.delete('1.0', tk.END)
        self.semantic_output_area.config(state='disabled')
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
        try:
            result = parser.parse(source_code)
            self.display_parser_output(result)
             # Realizar análisis semántico
            self.generate_semantic_analysis(result)
        except Exception as e:
            self.error_area.config(state='normal')
            self.error_area.insert(tk.END, f"Parser Error: {e}\n")
            self.error_area.config(state='disabled')
            # try:
            #     analyze_semantics(result, symbol_table)
            #     self.populate_symbol_table(symbol_table)
            #     self.display_semantic_tree(result)
            # except Exception as e:
            #     self.error_area.config(state='normal')
            #     self.error_area.insert(tk.END, f"Semantic Error: {str(e)}\n")
            #     self.error_area.config(state='disabled')
            
        # Mostrar errores sintácticos en el área de errores
        if parser.errors:
            self.error_area.config(state='normal')
            for error in parser.errors:
                self.error_area.insert(tk.END, f"Parser Error: {error}\n")
            self.error_area.config(state='disabled')
        
        self.display_semantic_tree(result)

    def generate_semantic_analysis(self, result):
    # Realizar análisis semántico
        symbol_table = SymbolTable()
        try:
            annotated_tree = self.analyze_semantics_with_annotations(result, symbol_table)
            self.populate_symbol_table(symbol_table)
            self.display_semantic_tree_with_annotations(annotated_tree)
        except Exception as e:
            self.error_area.config(state='normal')
            self.error_area.insert(tk.END, f"Semantic Error: {str(e)}\n")
            self.error_area.config(state='disabled')

    def display_semantic_tree_with_annotations(self, root_node):
        def format_node(node, indent=0):
            output = "  " * indent + str(node.node_type) + " (" + ", ".join(f"{k}: {v}" for k, v in node.annotations.items()) + ")\n"
            for child in node.children:
                output += format_node(child, indent + 1)
            return output

        formatted_tree = format_node(root_node)
        self.semantic_tree_area.config(state='normal')
        self.semantic_tree_area.insert(tk.END, formatted_tree)
        self.semantic_tree_area.config(state='disabled')
    
    def populate_symbol_table(self, symbol_table):
        # Llenar la tabla de símbolos en la pestaña correspondiente
        for name, info in symbol_table.symbols.items():
            self.symbol_table.insert("", "end", values=(name, info['type'], info.get('value', '')))

    def display_semantic_tree(self, root_node):
        def format_node(node, indent=0):
            output = "  " * indent + str(node) + "\n"
            for child in node.children:
                output += format_node(child, indent + 1)
            return output

        formatted_tree = format_node(root_node)
        self.semantic_output_area.config(state='normal')
        self.semantic_output_area.insert(tk.END, formatted_tree)
        self.semantic_output_area.config(state='disabled')

    def display_parser_output(self, result):
        def format_result(node, indent=0):
            if isinstance(node, tuple):
                output = "  " * indent + str(node[0]) + "\n"
                for child in node[1:]:
                    output += format_result(child, indent + 1)
                return output
            elif isinstance(node, list):
                output = ""
                for item in node:
                    output += format_result(item, indent)
                return output
            else:
                return "  " * indent + str(node) + "\n"

        formatted_result = format_result(result)
        self.parser_output_area.config(state='normal')
        self.parser_output_area.insert(tk.END, formatted_result)
        self.parser_output_area.config(state='disabled')

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
