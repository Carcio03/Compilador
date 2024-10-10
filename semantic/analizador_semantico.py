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

            semantic_node.add_child(analyze_semantics_with_annotations(ast[2], symbol_table, tokens, error_list))
            return semantic_node

        # Procesar binop
        if node_type == 'binop':
            left_value = evaluate_expression(ast[2], symbol_table, error_list=error_list)
            right_value = evaluate_expression(ast[3], symbol_table, error_list=error_list)
            operator = ast[1]

            operation = f"{left_value} {operator} {right_value}"
            result = evaluate_expression(ast, symbol_table, error_list=error_list)

            semantic_node.add_annotation("operation", operation)
            semantic_node.add_annotation("result", result)

            semantic_node.add_child(analyze_semantics_with_annotations(ast[2], symbol_table, tokens, error_list))
            semantic_node.add_child(analyze_semantics_with_annotations(ast[3], symbol_table, tokens, error_list))

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
        node.add_annotation("type", "bool")  # Asegurarse de que el tipo sea 'bool'
        node.add_annotation("value", value)  # El valor será True o False
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
    if isinstance(expr, tuple) and expr[0] == 'binop':
        op = expr[1]
        left_value = evaluate_expression(expr[2], symbol_table, error_list=error_list)
        right_value = evaluate_expression(expr[3], symbol_table, error_list=error_list)

        try:
            # Evaluar operadores aritméticos, de comparación y lógicos
            if op == '+':
                result = left_value + right_value
            elif op == '-':
                result = left_value - right_value
            elif op == '*':
                result = left_value * right_value
            elif op == '/':
                result = left_value / right_value
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
            elif op == 'and':
                result = left_value and right_value  # Evaluación de 'and'
            elif op == 'or':
                result = left_value or right_value   # Evaluación de 'or'
            else:
                result = None

        except (TypeError, ValueError) as e:
            error_message = f"Error en la operación {left_value} {op} {right_value}: {e}"
            if error_list is not None:
                error_list.append(error_message)
            return f"Error: {error_message}"

        return result

    elif isinstance(expr, tuple) and expr[0] == 'bool':
        # Devolver True o False según el valor
        return True if expr[1] == 'true' else False

    elif isinstance(expr, tuple) and expr[0] == 'number':
        return expr[1]

    elif isinstance(expr, tuple) and expr[0] == 'identifier':
        symbol_info = symbol_table.get_symbol(expr[1])
        if symbol_info:
            return symbol_info.get('value', 0)
        else:
            error_message = f"Error: La variable '{expr[1]}' no está definida."
            if error_list is not None:
                error_list.append(error_message)
            return 0  # Valor predeterminado si no existe la variable

    return expr




       
class SymbolTable:
    def __init__(self):
        self.symbols = {}

    def add_symbol(self, name, symbol_info):
        # Verificar si la variable ya ha sido declarada con un tipo diferente
        if name in self.symbols:
            existing_type = self.symbols[name]['type']
            if existing_type != symbol_info['type']:
                print(f"Error: La variable '{name}' ya ha sido declarada como {existing_type}.")
                return  # No sobreescribir la entrada existente con un tipo diferente
        # Asegurarnos de que siempre exista la clave 'lines'
        if 'lines' not in symbol_info:
            symbol_info['lines'] = []
        self.symbols[name] = symbol_info

    def get_symbol(self, name):
        return self.symbols.get(name, None)

    def update_symbol(self, name, symbol_info):
        if 'lines' not in symbol_info:
            symbol_info['lines'] = []
        self.symbols[name] = symbol_info

