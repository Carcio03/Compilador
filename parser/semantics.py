class SemanticAnalyzer:
    def __init__(self):
        self.symbol_table = {}

    def analyze(self, ast):
        self.check(ast)

    def check(self, node):
        if isinstance(node, tuple):
            node_type = node[0]

            # Ejemplo de comprobación de declaración de variable
            if node_type == 'declaration':
                var_type = node[1]
                var_name = node[2]
                if var_name in self.symbol_table:
                    raise Exception(f"Error semántico: variable '{var_name}' ya ha sido declarada.")
                self.symbol_table[var_name] = var_type
            
            # Ejemplo de comprobación de asignación
            elif node_type == 'assignment':
                var_name = node[1]
                if var_name not in self.symbol_table:
                    raise Exception(f"Error semántico: variable '{var_name}' no ha sido declarada.")
            
            # Recursividad para recorrer el AST
            for child in node[1:]:
                self.check(child)
