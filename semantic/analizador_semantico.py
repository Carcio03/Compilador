class SemanticNode:
    def __init__(self, node_type, value=None):
        self.node_type = node_type
        self.value = value
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def __repr__(self):
        return f"{self.node_type}: {self.value} -> {self.children}"

class SemanticNodeWithAnnotations(SemanticNode):
    def __init__(self, node_type, value=None):
        super().__init__(node_type, value)
        self.annotations = {}

    def add_annotation(self, key, value):
        self.annotations[key] = value

# Mueve la función fuera de la clase
def analyze_semantics_with_annotations(ast, symbol_table):
    if isinstance(ast, tuple):
        node_type = ast[0]
        semantic_node = SemanticNodeWithAnnotations(node_type)
        
        if node_type == 'declaration':
            var_type = ast[1]
            for var in ast[2]:
                if isinstance(var, tuple) and var[0] == 'assign':
                    symbol_table.add_symbol(var[1], {'type': var_type, 'value': None})
                    semantic_node.add_annotation(var[1], f"{var_type} declared")
                else:
                    symbol_table.add_symbol(var, {'type': var_type})
                    semantic_node.add_annotation(var, f"{var_type} declared")
        
        elif node_type == 'assignment':
            var_name = ast[1]
            expected_type = symbol_table.get_symbol(var_name).get('type', 'unknown')
            expression_value = evaluate_expression(ast[2], symbol_table, expected_type)
            
            # Actualizar la tabla de símbolos con el valor final
            symbol_table.update_symbol(var_name, {'type': expected_type, 'value': expression_value})
            semantic_node.add_annotation(var_name, f"assigned value {expression_value}")
        
        # Procesar recursivamente las otras partes del árbol
        for child in ast[1:]:
            semantic_child = analyze_semantics_with_annotations(child, symbol_table)
            semantic_node.add_child(semantic_child)
        
        return semantic_node

    elif isinstance(ast, list):
        semantic_node = SemanticNodeWithAnnotations("block")
        for node in ast:
            semantic_child = analyze_semantics_with_annotations(node, symbol_table)
            semantic_node.add_child(semantic_child)
        return semantic_node
    
    # Si es un número literal o variable
    elif isinstance(ast, (int, float)):
        return SemanticNodeWithAnnotations(f"number ({ast})", ast)

    # Si es un identificador o variable
    elif isinstance(ast, str):
        return SemanticNodeWithAnnotations(f"identifier ({ast})", ast)

    else:
        return SemanticNodeWithAnnotations("literal", ast)

def evaluate_expression(expr, symbol_table, expected_type=None):
    """Evalúa una expresión y devuelve el resultado."""
    if isinstance(expr, tuple):
        if expr[0] == 'binop':
            # Caso de una operación binaria (suma, resta, multiplicación, división)
            op = expr[1]
            left = evaluate_expression(expr[2], symbol_table, expected_type)
            right = evaluate_expression(expr[3], symbol_table, expected_type)
            
            # Realizar la operación binaria
            if op == '+':
                result = left + right
            elif op == '-':
                result = left - right
            elif op == '*':
                result = left * right
            elif op == '/':
                result = left / right
            else:
                raise ValueError(f"Unknown binary operator {op}")
            
            return result
        
        # Caso de un identificador (variable)
        elif len(expr) == 2 and expr[0] == 'identifier':
            var_name = expr[1]
            symbol_info = symbol_table.get_symbol(var_name)
            if symbol_info and 'value' in symbol_info:
                return symbol_info['value']
            else:
                raise ValueError(f"Unknown identifier '{var_name}'")
        
        # Caso de un número literal (como ('number', 45))
        elif len(expr) == 2 and expr[0] == 'number':
            literal_value = expr[1]
            
            # Si se espera un float y tenemos un int, convertir el valor a float
            if expected_type == 'float' and isinstance(literal_value, int):
                literal_value = float(literal_value)
                print(f"Converted {expr[1]} from int to float")
            
            return literal_value
        
        else:
            raise ValueError(f"Unexpected tuple format: {expr}")
    
    # Caso de un número directo (entero o flotante)
    elif isinstance(expr, (int, float)):
        if expected_type == 'float' and isinstance(expr, int):
            return float(expr)  # Convertir de int a float si es necesario
        return expr

    # Caso de un identificador directo (variable)
    elif isinstance(expr, str):
        symbol_info = symbol_table.get_symbol(expr)
        if symbol_info and 'value' in symbol_info:
            return symbol_info['value']
        else:
            raise ValueError(f"Unknown identifier '{expr}'")




class SymbolTable:
    def __init__(self):
        self.symbols = {}

    def add_symbol(self, name, symbol_info):
        if name in self.symbols:
            raise Exception(f"Error: El símbolo '{name}' ya está definido.")
        self.symbols[name] = symbol_info

    def get_symbol(self, name):
        return self.symbols.get(name, None)

    def update_symbol(self, name, symbol_info):
        if name not in self.symbols:
            raise Exception(f"Error: El símbolo '{name}' no está definido.")
        self.symbols[name] = symbol_info
