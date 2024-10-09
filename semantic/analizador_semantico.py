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

# Función de análisis semántico
def analyze_semantics_with_annotations(ast, symbol_table, tokens):
    if isinstance(ast, tuple):
        node_type = ast[0]
        semantic_node = SemanticNodeWithAnnotations(node_type)
        
        if node_type == 'binop':
            # Obtener los valores de los operandos
            left_value = evaluate_expression(ast[2], symbol_table)
            right_value = evaluate_expression(ast[3], symbol_table)
            
            # Realizar la operación y agregar el resultado al nodo
            if ast[1] == '+':
                result = left_value + right_value
            elif ast[1] == '-':
                result = left_value - right_value
            elif ast[1] == '*':
                result = left_value * right_value
            elif ast[1] == '/':
                result = left_value / right_value
            else:
                result = None

            # Añadir una anotación con el resultado
            semantic_node.add_annotation("result", f"{left_value} {ast[1]} {right_value} = {result}")
            
            # Agregar los hijos (operandos) al nodo
            semantic_node.add_child(analyze_semantics_with_annotations(ast[2], symbol_table, tokens))
            semantic_node.add_child(analyze_semantics_with_annotations(ast[3], symbol_table, tokens))
            
            return semantic_node
        
        # Procesar el resto de nodos recursivamente
        for child in ast[1:]:
            semantic_child = analyze_semantics_with_annotations(child, symbol_table, tokens)
            semantic_node.add_child(semantic_child)
        
        return semantic_node

    elif isinstance(ast, list):
        semantic_node = SemanticNodeWithAnnotations("block")
        for node in ast:
            semantic_child = analyze_semantics_with_annotations(node, symbol_table, tokens)
            semantic_node.add_child(semantic_child)
        return semantic_node

    # Literales numéricos
    elif isinstance(ast, (int, float)):
        node = SemanticNodeWithAnnotations(f"number ({ast})", ast)
        node.add_annotation("type", "int" if isinstance(ast, int) else "float")
        node.add_annotation("value", ast)
        return node

    # Identificadores
    elif isinstance(ast, str):
        symbol_info = symbol_table.get_symbol(ast)
        if symbol_info:
            value = symbol_info.get('value', 'undefined')
            node = SemanticNodeWithAnnotations(f"identifier ({ast})", value)
            node.add_annotation("type", symbol_info['type'])
            node.add_annotation("value", value)
        else:
            node = SemanticNodeWithAnnotations(f"identifier ({ast})", "undefined")
        return node

    return SemanticNodeWithAnnotations("literal", ast)




def evaluate_expression(expr, symbol_table, expected_type=None):
    if isinstance(expr, tuple) and expr[0] == 'binop':
        op = expr[1]
        left_value = evaluate_expression(expr[2], symbol_table, expected_type)
        right_value = evaluate_expression(expr[3], symbol_table, expected_type)
        
        # Asegurarse de que los valores no sean None
        if left_value is None:
            left_value = 0  # Valor por defecto para None
        if right_value is None:
            right_value = 0  # Valor por defecto para None
        
        # Realizar la operación y calcular el resultado
        if op == '+':
            result = left_value + right_value
        elif op == '-':
            result = left_value - right_value
        elif op == '*':
            result = left_value * right_value
        elif op == '/':
            result = left_value / right_value
        else:
            result = None
        
        return result

    elif isinstance(expr, tuple) and expr[0] == 'number':
        return expr[1]

    elif isinstance(expr, tuple) and expr[0] == 'identifier':
        symbol_info = symbol_table.get_symbol(expr[1])
        if symbol_info:
            return symbol_info.get('value', 0)  # Valor por defecto si no está definido
        else:
            return 0  # Valor predeterminado si no existe la variable

    return expr



class SymbolTable:
    def __init__(self):
        self.symbols = {}

    def add_symbol(self, name, symbol_info):
        # Asegurarnos de que siempre exista la clave 'lines'
        if 'lines' not in symbol_info:
            symbol_info['lines'] = []
        self.symbols[name] = symbol_info

    def get_symbol(self, name):
        return self.symbols.get(name, None)

    def update_symbol(self, name, symbol_info):
        # Asegurarnos de que siempre exista la clave 'lines'
        if 'lines' not in symbol_info:
            symbol_info['lines'] = []
        self.symbols[name] = symbol_info