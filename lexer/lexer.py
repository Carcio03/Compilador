import ply.lex as lex

# Lista de tokens
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

# Definición de tokens simples
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_POWER = r'\^'
t_LT = r'<'
t_LE = r'<='
t_GT = r'>'
t_GE = r'>='
t_EQ = r'=='
t_NE = r'!='
t_ASSIGN = r'='
t_SEMICOLON = r';'
t_COMMA = r','
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'

# Palabras reservadas
reserved = {
    'program': 'PROGRAM',
    'if': 'IF',
    'then': 'THEN',
    'else': 'ELSE',
    'fi': 'FI',
    'do': 'DO',
    'until': 'UNTIL',
    'while': 'WHILE',
    'read': 'READ',
    'write': 'WRITE',
    'float': 'FLOAT',
    'int': 'INT',
    'bool': 'BOOL',
    'not': 'NOT',
    'and': 'AND',
    'or': 'OR',
    'true': 'TRUE',
    'false': 'FALSE'
}

# Identificadores y números
def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'IDENTIFIER')
    return t

def t_NUMBER(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value) if '.' in t.value else int(t.value)
    return t

# Ignorar espacios en blanco y tabulaciones
t_ignore = ' \t'

# Ignorar comentarios de bloque
def t_block_comment(t):
    r'/\*(.|\n)*?\*/'
    pass

# Ignorar comentarios de línea
def t_line_comment(t):
    r'//.*'
    pass

# Manejo de nuevas líneas
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Manejo de errores
def t_error(t):
    error_message = f"Illegal character '{t.value[0]}' at line {t.lineno}"
    t.lexer.errors.append(error_message)
    t.lexer.skip(1)

lexer = lex.lex()
lexer.errors = []
