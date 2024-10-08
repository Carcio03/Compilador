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
def analyze_semantics_with_annotations(ast, symbol_table):
    if isinstance(ast, tuple):
        node_type = ast[0]
        semantic_node = SemanticNodeWithAnnotations(node_type)
        
        try:
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
        except Exception as e:
            semantic_node.add_annotation("error", f"Semantic Error: {str(e)}")

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
    
    elif isinstance(ast, (int, float)):
        return SemanticNodeWithAnnotations(f"number ({ast})", ast)

    elif isinstance(ast, str):
        return SemanticNodeWithAnnotations(f"identifier ({ast})", ast)

    else:
        return SemanticNodeWithAnnotations("literal", ast)



def evaluate_expression(expr, symbol_table, expected_type=None):
    # Función de evaluación de expresiones simplificada
    if isinstance(expr, tuple) and expr[0] == 'binop':
        op = expr[1]
        left = evaluate_expression(expr[2], symbol_table, expected_type)
        right = evaluate_expression(expr[3], symbol_table, expected_type)
        if op == '+':
            return left + right
        elif op == '-':
            return left - right
        elif op == '*':
            return left * right
        elif op == '/':
            return left / right
        else:
            raise ValueError(f"Unknown operator {op}")

    elif isinstance(expr, tuple) and expr[0] == 'number':
        return expr[1]

    elif isinstance(expr, tuple) and expr[0] == 'identifier':
        symbol_info = symbol_table.get_symbol(expr[1])
        if symbol_info and 'value' in symbol_info:
            return symbol_info['value']
        else:
            return 0

    return expr

class SymbolTable:
    def __init__(self):
        self.symbols = {}

    def add_symbol(self, name, symbol_info):
        self.symbols[name] = symbol_info

    def get_symbol(self, name):
        return self.symbols.get(name, None)

    def update_symbol(self, name, symbol_info):
        self.symbols[name] = symbol_info
