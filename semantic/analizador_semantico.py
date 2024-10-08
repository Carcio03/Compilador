class SemanticNodeWithAnnotations(SemanticNode):
    def __init__(self, node_type, value=None):
        super().__init__(node_type, value)
        self.annotations = {}

    def add_annotation(self, key, value):
        self.annotations[key] = value

def analyze_semantics_with_annotations(ast, symbol_table):
    if isinstance(ast, tuple):
        node_type = ast[0]
        semantic_node = SemanticNodeWithAnnotations(node_type)
        
        if node_type == 'declaration':
            var_type = ast[1]
            for var in ast[2]:
                if isinstance(var, tuple) and var[0] == 'assign':
                    symbol_table.add_symbol(var[1], {'type': var_type, 'value': var[2]})
                    semantic_node.add_annotation(var[1], f"{var_type} assigned")
                else:
                    symbol_table.add_symbol(var, {'type': var_type})
                    semantic_node.add_annotation(var, f"{var_type} declared")

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
    else:
        return SemanticNodeWithAnnotations("literal", ast)
