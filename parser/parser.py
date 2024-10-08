import ply.yacc as yacc

# Definir los tokens
tokens = (
    'IDENTIFIER',
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'POWER',
    'LT',
    'LE',
    'GT',
    'GE',
    'EQ',
    'NE',
    'ASSIGN',
    'SEMICOLON',
    'COMMA',
    'LPAREN',
    'RPAREN',
    'LBRACE',
    'RBRACE',
    'AND',
    'OR',
    'NOT',
    'PROGRAM',
    'IF',
    'THEN',
    'ELSE',
    'FI',
    'DO',
    'UNTIL',
    'WHILE',
    'READ',
    'WRITE',
    'FLOAT',
    'INT',
    'BOOL',
    'TRUE',
    'FALSE'
)

# Definir la precedencia de los operadores
precedence = (
    ('left', 'OR'),
    ('left', 'AND'),
    ('left', 'EQ', 'NE'),
    ('left', 'LT', 'LE', 'GT', 'GE'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
    ('right', 'UMINUS', 'NOT'),
)

# Definir la gramática
def p_program(p):
    '''program : PROGRAM LBRACE declarations statements RBRACE'''
    p[0] = ('program', p[3], p[4])

def p_declarations(p):
    '''declarations : declarations declaration
                    | declaration
                    | empty'''
    if len(p) == 3:
        p[0] = p[1] + [p[2]]
    elif len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = []

def p_declaration(p):
    '''declaration : type var_list SEMICOLON'''
    p[0] = ('declaration', p[1], p[2])

def p_var_list(p):
    '''var_list : var_list COMMA IDENTIFIER
                | var_list COMMA IDENTIFIER ASSIGN expression
                | IDENTIFIER
                | IDENTIFIER ASSIGN expression'''
    if len(p) == 4 and p[2] == ',':
        p[0] = p[1] + [p[3]]
    elif len(p) == 6:
        p[0] = p[1] + [('assign', p[3], p[5])]
    elif len(p) == 4:
        p[0] = [('assign', p[1], p[3])]
    else:
        p[0] = [p[1]]

def p_type(p):
    '''type : INT
            | FLOAT
            | BOOL'''
    p[0] = p[1]

def p_statements(p):
    '''statements : statements statement
                  | statement
                  | empty'''
    if len(p) == 3:
        p[0] = p[1] + [p[2]]
    elif len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = []

def p_statement(p):
    '''statement : assignment
                 | if_statement
                 | while_statement
                 | do_while_statement
                 | write_statement
                 | read_statement
                 | block'''
    p[0] = p[1]

def p_assignment(p):
    '''assignment : IDENTIFIER ASSIGN expression SEMICOLON'''
    p[0] = ('assignment', p[1], p[3])

def p_if_statement(p):
    '''if_statement : IF expression THEN statements else_part FI'''
    p[0] = ('if', p[2], p[4], p[5])

def p_else_part(p):
    '''else_part : ELSE statements
                 | empty'''
    if len(p) == 3:
        p[0] = p[2]
    else:
        p[0] = None

def p_while_statement(p):
    '''while_statement : WHILE expression LBRACE statements RBRACE'''
    p[0] = ('while', p[2], p[4])

def p_do_while_statement(p):
    '''do_while_statement : DO LBRACE statements RBRACE WHILE LPAREN expression RPAREN SEMICOLON'''
    p[0] = ('do_while', p[3], p[7])

def p_write_statement(p):
    '''write_statement : WRITE expression SEMICOLON'''
    p[0] = ('write', p[2])

def p_read_statement(p):
    '''read_statement : READ IDENTIFIER SEMICOLON'''
    p[0] = ('read', p[2])

def p_block(p):
    '''block : LBRACE statements RBRACE'''
    p[0] = ('block', p[2])

def p_expression_binop(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression
                  | expression POWER expression
                  | expression EQ expression
                  | expression LT expression
                  | expression GT expression
                  | expression LE expression
                  | expression GE expression
                  | expression NE expression
                  | expression AND expression
                  | expression OR expression'''
    p[0] = ('binop', p[2], p[1], p[3])

def p_expression_uminus(p):
    'expression : MINUS expression %prec UMINUS'
    p[0] = ('uminus', p[2])

def p_expression_not(p):
    'expression : NOT expression'
    p[0] = ('not', p[2])

def p_expression_group(p):
    'expression : LPAREN expression RPAREN'
    p[0] = p[2]

def p_expression_number(p):
    '''expression : NUMBER'''
    p[0] = ('number', p[1])

def p_expression_identifier(p):
    '''expression : IDENTIFIER'''
    p[0] = ('identifier', p[1])

def p_expression_bool(p):
    '''expression : TRUE
                  | FALSE'''
    p[0] = ('bool', p[1])

def p_empty(p):
    'empty :'
    p[0] = []

def p_error(p):
    if p:
        error_message = f"Syntax error at '{p.value}', line {p.lineno}"
        parser.errors.append(error_message)
        # En lugar de detenernos, retornamos un nodo de error en el árbol
        return ('error', f"Error at '{p.value}' on line {p.lineno}")
    else:
        parser.errors.append("Syntax error at EOF")
        return ('error', "Error at EOF")

parser = yacc.yacc()
parser.errors = []
