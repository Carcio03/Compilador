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

    def __repr__(self):
        annotations_str = ', '.join([f'{k}: {v}' for k, v in self.annotations.items()])
        return f"{self.node_type} (annotations: {annotations_str}) -> {self.children}"
    
def analyze_semantics_with_annotations(ast, symbol_table, tokens, error_list=None):
    if isinstance(ast, tuple):
        node_type = ast[0]
        semantic_node = SemanticNodeWithAnnotations(node_type)

        # Procesar declaraciones de variables
        if node_type == 'declaration':
            var_type = ast[1]
            var_list = ast[2]
            semantic_node.add_annotation("type", var_type)
            semantic_node.add_annotation("value", "undefined")

            for var in var_list:
                if symbol_table.get_symbol(var):
                    error_message = f"Error: La variable '{var}' ya ha sido declarada."
                    if error_list is not None:
                        error_list.append(error_message)
                else:
                    symbol_table.add_symbol(var, {'type': var_type, 'value': 'undefined'})
                    identifier_node = SemanticNodeWithAnnotations(f"identifier ({var})", "undefined")
                    identifier_node.add_annotation("type", var_type)
                    identifier_node.add_annotation("value", "undefined")
                    semantic_node.add_child(identifier_node)

            return semantic_node

        # Procesar asignaciones
        elif node_type == 'assignment':
            var_name = ast[1]
            value = evaluate_expression(ast[2], symbol_table, error_list=error_list)
            symbol_info = symbol_table.get_symbol(var_name)
            if symbol_info:
                symbol_info['value'] = value
                symbol_table.update_symbol(var_name, symbol_info)
                semantic_node.add_annotation("variable", var_name)
                semantic_node.add_annotation("type", symbol_info['type'])
                semantic_node.add_annotation("value", value)
            else:
                error_message = f"Error: La variable '{var_name}' no está definida."
                if error_list is not None:
                    error_list.append(error_message)

            expr_node = analyze_semantics_with_annotations(ast[2], symbol_table, tokens, error_list)
            semantic_node.add_child(expr_node)
            return semantic_node

       # Procesar binop (operaciones binarias)
        elif node_type == 'binop':
            operator = ast[1]

            # **Procesar primero el operando izquierdo para que sea el primero en evaluarse**
            left_child = analyze_semantics_with_annotations(ast[2], symbol_table, tokens, error_list)
            right_child = analyze_semantics_with_annotations(ast[3], symbol_table, tokens, error_list)

            left_value = evaluate_expression(ast[2], symbol_table, error_list=error_list)
            right_value = evaluate_expression(ast[3], symbol_table, error_list=error_list)

            operation = f"{left_value} {operator} {right_value}"
            result = evaluate_expression(ast, symbol_table, error_list=error_list)

            semantic_node.add_annotation("operation", operation)
            semantic_node.add_annotation("result", result)

            # **Agregar el hijo izquierdo primero para que quede más profundo y se evalúe antes**
            semantic_node.add_child(left_child)
            semantic_node.add_child(right_child)

            return semantic_node


        # Procesar nodos recursivamente
        for child in ast[1:]:
            semantic_child = analyze_semantics_with_annotations(child, symbol_table, tokens, error_list)
            semantic_node.add_child(semantic_child)

        return semantic_node

    elif isinstance(ast, list):
        semantic_node = SemanticNodeWithAnnotations("block")
        for node in ast:
            semantic_child = analyze_semantics_with_annotations(node, symbol_table, tokens, error_list)
            semantic_node.add_child(semantic_child)
        return semantic_node

    # Literales numéricos
    elif isinstance(ast, (int, float)):
        node = SemanticNodeWithAnnotations(f"number ({ast})", ast)
        node.add_annotation("type", "int" if isinstance(ast, int) else "float")
        node.add_annotation("value", ast)
        return node

    # Booleanos: manejar explícitamente los valores 'true' y 'false'
    elif isinstance(ast, tuple) and ast[0] == 'bool':
        value = True if ast[1] == 'true' else False
        node = SemanticNodeWithAnnotations(f"bool ({ast[1]})", value)
        node.add_annotation("type", "bool")
        node.add_annotation("value", value)
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
            error_message = f"Error: La variable '{ast}' no está definida."
            if error_list is not None:
                error_list.append(error_message)
            node = SemanticNodeWithAnnotations(f"identifier ({ast})", "undefined")
            node.add_annotation("type", "undefined")
            node.add_annotation("value", "undefined")
        return node

    return SemanticNodeWithAnnotations("literal", ast)





def evaluate_expression(expr, symbol_table, error_list=None):
    # Verificamos si es un binop (operación binaria)
    if isinstance(expr, tuple) and expr[0] == 'binop':
        op = expr[1]
        # Evaluamos primero el operando izquierdo, y luego el derecho
        left_value = evaluate_expression(expr[2], symbol_table, error_list=error_list)
        right_value = evaluate_expression(expr[3], symbol_table, error_list=error_list)

        try:
            # Evaluar operaciones aritméticas de izquierda a derecha
            if op == '+':
                result = left_value + right_value
            elif op == '-':
                result = left_value - right_value
            elif op == '*':
                result = left_value * right_value
            elif op == '/':
                result = left_value / right_value

            # Evaluar operadores de comparación
            elif op == '>':
                result = left_value > right_value
            elif op == '<':
                result = left_value < right_value
            elif op == '>=':
                result = left_value >= right_value
            elif op == '<=':
                result = left_value <= right_value
            elif op == '==':
                result = left_value == right_value
            elif op == '!=':
                result = left_value != right_value

            # Evaluar operadores lógicos
            elif op == 'and':
                result = left_value and right_value
            elif op == 'or':
                result = left_value or right_value

            return result

        except (TypeError, ValueError) as e:
            error_message = f"Error en la operación {left_value} {op} {right_value}: {e}"
            if error_list is not None:
                error_list.append(error_message)
            return f"Error: {error_message}"

    # Si es un número, debemos desglosar el valor numérico de la tupla
    elif isinstance(expr, tuple) and expr[0] == 'number':
        return expr[1]  # Devolvemos el valor numérico

    # Si es un identificador
    elif isinstance(expr, tuple) and expr[0] == 'identifier':
        symbol_info = symbol_table.get_symbol(expr[1])
        if symbol_info:
            return symbol_info.get('value', 0)
        else:
            error_message = f"Error: La variable '{expr[1]}' no está definida."
            if error_list is not None:
                error_list.append(error_message)
            return 0  # Valor predeterminado si no existe la variable

    # En otros casos, devolver el valor tal cual
    return expr




class SymbolTable:
    def __init__(self):
        self.symbols = {}

    def add_symbol(self, name, symbol_info):
        if 'lines' not in symbol_info:
            symbol_info['lines'] = []
        self.symbols[name] = symbol_info

    def get_symbol(self, name):
        return self.symbols.get(name, None)

    def update_symbol(self, name, symbol_info):
        if 'lines' not in symbol_info:
            symbol_info['lines'] = []
        self.symbols[name] = symbol_info