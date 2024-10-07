import sys
import os

# Añadir el directorio raíz al path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog, messagebox
from lexer.lexer import lexer as custom_lexer
from parser.parser import parser, analyze_semantics
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

        # Crear el frame principal con tres filas
        main_frame = tk.Frame(self, bg='#2b2b2b')
        main_frame.pack(expand=1, fill='both')
        main_frame.grid_rowconfigure(0, weight=4)
        main_frame.grid_rowconfigure(1, weight=1)
        main_frame.grid_rowconfigure(2, weight=1)
        main_frame.grid_columnconfigure(0, weight=1)
        main_frame.grid_columnconfigure(1, weight=1)

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

        # Crear la tabla de tokens en la primera fila y segunda columna
        style = ttk.Style()
        style.theme_use("default")
        style.configure("Treeview", background="#1e1e1e", foreground="#ffffff", fieldbackground="#1e1e1e", font=('Consolas', 12))
        style.map("Treeview", background=[('selected', '#4d4d4d')], foreground=[('selected', '#ffffff')])
        style.configure("Treeview.Heading", background="#2b2b2b", foreground="#ffffff", font=('Consolas', 12, 'bold'))

        table_frame = tk.Frame(main_frame, padx=10, pady=10, bg='#2b2b2b')
        table_frame.grid(row=0, column=1, sticky='nsew')

        self.token_table = ttk.Treeview(table_frame, columns=("clave", "lexema", "fila", "columna"), show='headings', style="Treeview")
        self.token_table.heading("clave", text="Clave")
        self.token_table.heading("lexema", text="Lexema")
        self.token_table.heading("fila", text="Fila")
        self.token_table.heading("columna", text="Columna")

        # Ajustar el ancho de las columnas
        self.token_table.column("clave", width=80)
        self.token_table.column("lexema", width=150)
        self.token_table.column("fila", width=50)
        self.token_table.column("columna", width=70)

        self.token_table.pack(expand=1, fill='both', padx=5, pady=5)

        # Crear el frame de errores en la segunda fila y ocupar ambas columnas
        error_frame = tk.Frame(main_frame, padx=10, pady=10, bg='#2b2b2b')
        error_frame.grid(row=1, column=0, columnspan=2, sticky='nsew')

        self.error_area = tk.Text(error_frame, height=5, bg='#1e1e1e', fg='#ff5555', state='disabled',
                                  font=('Consolas', 12), relief='flat', insertbackground='white')
        self.error_area.pack(expand=1, fill='both', padx=5, pady=5)

        # Crear el frame de salida del parser en la tercera fila y ocupar ambas columnas
        parser_output_frame = tk.Frame(main_frame, padx=10, pady=10, bg='#2b2b2b')
        parser_output_frame.grid(row=2, column=0, columnspan=2, sticky='nsew')

        self.parser_output_area = tk.Text(parser_output_frame, height=10, bg='#1e1e1e', fg='#00ff00', state='disabled',
                                          font=('Consolas', 12), relief='flat', insertbackground='white')
        self.parser_output_area.pack(expand=1, fill='both', padx=5, pady=5)

        self.text_area.tag_configure("reserved", foreground="#00ff00")

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

        # Limpiar el área de salida del parser
        self.parser_output_area.config(state='normal')
        self.parser_output_area.delete('1.0', tk.END)
        self.parser_output_area.config(state='disabled')

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
        except Exception as e:
            self.error_area.config(state='normal')
            self.error_area.insert(tk.END, f"Parser Error: {e}\n")
            self.error_area.config(state='disabled')

        # Mostrar errores sintácticos en el área de errores
        if parser.errors:
            self.error_area.config(state='normal')
            for error in parser.errors:
                self.error_area.insert(tk.END, f"Parser Error: {error}\n")
            self.error_area.config(state='disabled')

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
        self.text_area.tag_remove("reserved", "1.0", "end")
        text = self.text_area.get("1.0", "end-1c")
        for keyword in self.reserved_words:
            pattern = r'\b' + keyword + r'\b'
            for match in re.finditer(pattern, text):
                start = f"1.0 + {match.start()} chars"
                end = f"1.0 + {match.end()} chars"
                self.text_area.tag_add("reserved", start, end)

if __name__ == "__main__":
    app = IDE()
    app.mainloop()
