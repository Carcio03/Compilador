
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftORleftANDleftEQNEleftLTLEGTGEleftPLUSMINUSleftTIMESDIVIDErightUMINUSNOTAND ASSIGN BOOL COMMA DIVIDE DO ELSE EQ FALSE FI FLOAT GE GT IDENTIFIER IF INT LBRACE LE LPAREN LT MINUS NE NOT NUMBER OR PLUS POWER PROGRAM RBRACE READ RPAREN SEMICOLON THEN TIMES TRUE UNTIL WHILE WRITEprogram : PROGRAM LBRACE declarations statements RBRACEdeclarations : declarations declaration\n                    | declaration\n                    | emptydeclaration : type var_list SEMICOLONvar_list : var_list COMMA IDENTIFIER\n                | var_list COMMA IDENTIFIER ASSIGN expression\n                | IDENTIFIER\n                | IDENTIFIER ASSIGN expressiontype : INT\n            | FLOAT\n            | BOOLstatements : statements statement\n                  | statement\n                  | emptystatement : assignment\n                 | if_statement\n                 | while_statement\n                 | do_while_statement\n                 | write_statement\n                 | read_statement\n                 | blockassignment : IDENTIFIER ASSIGN expression SEMICOLONif_statement : IF expression block else_part FI\n                    | IF expression statement else_part FIelse_part : ELSE block\n                 | ELSE statement\n                 | emptywhile_statement : WHILE expression LBRACE statements RBRACEdo_while_statement : DO LBRACE statements RBRACE WHILE LPAREN expression RPAREN SEMICOLONwrite_statement : WRITE expression SEMICOLONread_statement : READ IDENTIFIER SEMICOLONblock : LBRACE statements RBRACEexpression : expression PLUS expression\n                  | expression MINUS expression\n                  | expression TIMES expression\n                  | expression DIVIDE expression\n                  | expression POWER expression\n                  | expression EQ expression\n                  | expression LT expression\n                  | expression GT expression\n                  | expression LE expression\n                  | expression GE expression\n                  | expression NE expression\n                  | expression AND expression\n                  | expression OR expressionexpression : MINUS expression %prec UMINUSexpression : NOT expressionexpression : LPAREN expression RPARENexpression : NUMBERexpression : IDENTIFIERexpression : TRUE\n                  | FALSEempty :'
    
_lr_action_items = {'PROGRAM':([0,],[2,]),'$end':([1,32,],[0,-1,]),'LBRACE':([2,3,4,5,6,11,12,13,14,15,16,17,18,19,20,21,22,26,31,33,35,39,40,41,42,43,44,47,50,67,68,70,71,72,73,76,78,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,98,101,102,108,],[3,-54,11,-3,-4,11,11,-2,-14,-15,-16,-17,-18,-19,-20,-21,-22,44,11,-13,11,-50,-51,-52,-53,70,11,-5,-33,-47,-48,11,11,-31,-32,-23,11,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-49,11,-24,-25,-29,-30,]),'INT':([3,4,5,6,13,47,],[8,8,-3,-4,-2,-5,]),'FLOAT':([3,4,5,6,13,47,],[9,9,-3,-4,-2,-5,]),'BOOL':([3,4,5,6,13,47,],[10,10,-3,-4,-2,-5,]),'IDENTIFIER':([3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,24,25,27,28,31,33,34,35,36,37,38,39,40,41,42,44,47,48,49,50,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,70,71,72,73,76,78,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,97,98,101,102,105,108,],[-54,23,-3,-4,30,-10,-11,-12,23,23,-2,-14,-15,-16,-17,-18,-19,-20,-21,-22,40,40,40,46,23,-13,40,23,40,40,40,-50,-51,-52,-53,23,-5,74,40,-33,40,40,40,40,40,40,40,40,40,40,40,40,40,-47,-48,23,23,-31,-32,-23,23,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-49,23,40,-24,-25,-29,40,-30,]),'IF':([3,4,5,6,11,12,13,14,15,16,17,18,19,20,21,22,31,33,35,39,40,41,42,44,47,50,67,68,70,71,72,73,76,78,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,98,101,102,108,],[-54,24,-3,-4,24,24,-2,-14,-15,-16,-17,-18,-19,-20,-21,-22,24,-13,24,-50,-51,-52,-53,24,-5,-33,-47,-48,24,24,-31,-32,-23,24,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-49,24,-24,-25,-29,-30,]),'WHILE':([3,4,5,6,11,12,13,14,15,16,17,18,19,20,21,22,31,33,35,39,40,41,42,44,47,50,67,68,70,71,72,73,76,78,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,98,101,102,108,],[-54,25,-3,-4,25,25,-2,-14,-15,-16,-17,-18,-19,-20,-21,-22,25,-13,25,-50,-51,-52,-53,25,-5,-33,-47,-48,25,25,-31,-32,-23,25,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-49,25,103,-24,-25,-29,-30,]),'DO':([3,4,5,6,11,12,13,14,15,16,17,18,19,20,21,22,31,33,35,39,40,41,42,44,47,50,67,68,70,71,72,73,76,78,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,98,101,102,108,],[-54,26,-3,-4,26,26,-2,-14,-15,-16,-17,-18,-19,-20,-21,-22,26,-13,26,-50,-51,-52,-53,26,-5,-33,-47,-48,26,26,-31,-32,-23,26,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-49,26,-24,-25,-29,-30,]),'WRITE':([3,4,5,6,11,12,13,14,15,16,17,18,19,20,21,22,31,33,35,39,40,41,42,44,47,50,67,68,70,71,72,73,76,78,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,98,101,102,108,],[-54,27,-3,-4,27,27,-2,-14,-15,-16,-17,-18,-19,-20,-21,-22,27,-13,27,-50,-51,-52,-53,27,-5,-33,-47,-48,27,27,-31,-32,-23,27,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-49,27,-24,-25,-29,-30,]),'READ':([3,4,5,6,11,12,13,14,15,16,17,18,19,20,21,22,31,33,35,39,40,41,42,44,47,50,67,68,70,71,72,73,76,78,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,98,101,102,108,],[-54,28,-3,-4,28,28,-2,-14,-15,-16,-17,-18,-19,-20,-21,-22,28,-13,28,-50,-51,-52,-53,28,-5,-33,-47,-48,28,28,-31,-32,-23,28,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-49,28,-24,-25,-29,-30,]),'RBRACE':([3,4,5,6,11,12,13,14,15,16,17,18,19,20,21,22,31,33,44,47,50,70,71,72,73,76,95,98,101,102,108,],[-54,-54,-3,-4,-54,32,-2,-14,-15,-16,-17,-18,-19,-20,-21,-22,50,-13,-54,-5,-33,-54,96,-31,-32,-23,102,-24,-25,-29,-30,]),'ELSE':([16,17,18,19,20,21,50,52,53,72,73,76,98,101,102,108,],[-16,-17,-18,-19,-20,-21,-33,78,78,-31,-32,-23,-24,-25,-29,-30,]),'FI':([16,17,18,19,20,21,50,52,53,72,73,76,77,79,80,98,99,100,101,102,108,],[-16,-17,-18,-19,-20,-21,-33,-22,-54,-31,-32,-23,98,-28,101,-24,-22,-27,-25,-29,-30,]),'ASSIGN':([23,30,74,],[34,49,97,]),'MINUS':([24,25,27,34,35,36,37,38,39,40,41,42,43,45,49,51,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,75,81,82,83,84,85,86,87,88,89,90,91,92,93,94,97,104,105,106,],[36,36,36,36,55,36,36,36,-50,-51,-52,-53,55,55,36,55,36,36,36,36,36,36,36,36,36,36,36,36,36,-47,-48,55,55,-34,-35,-36,-37,55,55,55,55,55,55,55,55,55,-49,36,55,36,55,]),'NOT':([24,25,27,34,36,37,38,49,54,55,56,57,58,59,60,61,62,63,64,65,66,97,105,],[37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,]),'LPAREN':([24,25,27,34,36,37,38,49,54,55,56,57,58,59,60,61,62,63,64,65,66,97,103,105,],[38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,105,38,]),'NUMBER':([24,25,27,34,36,37,38,49,54,55,56,57,58,59,60,61,62,63,64,65,66,97,105,],[39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,]),'TRUE':([24,25,27,34,36,37,38,49,54,55,56,57,58,59,60,61,62,63,64,65,66,97,105,],[41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,]),'FALSE':([24,25,27,34,36,37,38,49,54,55,56,57,58,59,60,61,62,63,64,65,66,97,105,],[42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,]),'SEMICOLON':([29,30,39,40,41,42,45,46,51,67,68,74,75,81,82,83,84,85,86,87,88,89,90,91,92,93,94,104,107,],[47,-8,-50,-51,-52,-53,72,73,76,-47,-48,-6,-9,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-49,-7,108,]),'COMMA':([29,30,39,40,41,42,67,68,74,75,81,82,83,84,85,86,87,88,89,90,91,92,93,94,104,],[48,-8,-50,-51,-52,-53,-47,-48,-6,-9,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-49,-7,]),'PLUS':([35,39,40,41,42,43,45,51,67,68,69,75,81,82,83,84,85,86,87,88,89,90,91,92,93,94,104,106,],[54,-50,-51,-52,-53,54,54,54,-47,-48,54,54,-34,-35,-36,-37,54,54,54,54,54,54,54,54,54,-49,54,54,]),'TIMES':([35,39,40,41,42,43,45,51,67,68,69,75,81,82,83,84,85,86,87,88,89,90,91,92,93,94,104,106,],[56,-50,-51,-52,-53,56,56,56,-47,-48,56,56,56,56,-36,-37,56,56,56,56,56,56,56,56,56,-49,56,56,]),'DIVIDE':([35,39,40,41,42,43,45,51,67,68,69,75,81,82,83,84,85,86,87,88,89,90,91,92,93,94,104,106,],[57,-50,-51,-52,-53,57,57,57,-47,-48,57,57,57,57,-36,-37,57,57,57,57,57,57,57,57,57,-49,57,57,]),'POWER':([35,39,40,41,42,43,45,51,67,68,69,75,81,82,83,84,85,86,87,88,89,90,91,92,93,94,104,106,],[58,-50,-51,-52,-53,58,58,58,-47,-48,58,58,-34,-35,-36,-37,58,-39,-40,-41,-42,-43,-44,-45,-46,-49,58,58,]),'EQ':([35,39,40,41,42,43,45,51,67,68,69,75,81,82,83,84,85,86,87,88,89,90,91,92,93,94,104,106,],[59,-50,-51,-52,-53,59,59,59,-47,-48,59,59,-34,-35,-36,-37,59,-39,-40,-41,-42,-43,-44,59,59,-49,59,59,]),'LT':([35,39,40,41,42,43,45,51,67,68,69,75,81,82,83,84,85,86,87,88,89,90,91,92,93,94,104,106,],[60,-50,-51,-52,-53,60,60,60,-47,-48,60,60,-34,-35,-36,-37,60,60,-40,-41,-42,-43,60,60,60,-49,60,60,]),'GT':([35,39,40,41,42,43,45,51,67,68,69,75,81,82,83,84,85,86,87,88,89,90,91,92,93,94,104,106,],[61,-50,-51,-52,-53,61,61,61,-47,-48,61,61,-34,-35,-36,-37,61,61,-40,-41,-42,-43,61,61,61,-49,61,61,]),'LE':([35,39,40,41,42,43,45,51,67,68,69,75,81,82,83,84,85,86,87,88,89,90,91,92,93,94,104,106,],[62,-50,-51,-52,-53,62,62,62,-47,-48,62,62,-34,-35,-36,-37,62,62,-40,-41,-42,-43,62,62,62,-49,62,62,]),'GE':([35,39,40,41,42,43,45,51,67,68,69,75,81,82,83,84,85,86,87,88,89,90,91,92,93,94,104,106,],[63,-50,-51,-52,-53,63,63,63,-47,-48,63,63,-34,-35,-36,-37,63,63,-40,-41,-42,-43,63,63,63,-49,63,63,]),'NE':([35,39,40,41,42,43,45,51,67,68,69,75,81,82,83,84,85,86,87,88,89,90,91,92,93,94,104,106,],[64,-50,-51,-52,-53,64,64,64,-47,-48,64,64,-34,-35,-36,-37,64,-39,-40,-41,-42,-43,-44,64,64,-49,64,64,]),'AND':([35,39,40,41,42,43,45,51,67,68,69,75,81,82,83,84,85,86,87,88,89,90,91,92,93,94,104,106,],[65,-50,-51,-52,-53,65,65,65,-47,-48,65,65,-34,-35,-36,-37,65,-39,-40,-41,-42,-43,-44,-45,65,-49,65,65,]),'OR':([35,39,40,41,42,43,45,51,67,68,69,75,81,82,83,84,85,86,87,88,89,90,91,92,93,94,104,106,],[66,-50,-51,-52,-53,66,66,66,-47,-48,66,66,-34,-35,-36,-37,66,-39,-40,-41,-42,-43,-44,-45,-46,-49,66,66,]),'RPAREN':([39,40,41,42,67,68,69,81,82,83,84,85,86,87,88,89,90,91,92,93,94,106,],[-50,-51,-52,-53,-47,-48,94,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-49,107,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'declarations':([3,],[4,]),'declaration':([3,4,],[5,13,]),'empty':([3,4,11,44,52,53,70,],[6,15,15,15,79,79,15,]),'type':([3,4,],[7,7,]),'statements':([4,11,44,70,],[12,31,71,95,]),'statement':([4,11,12,31,35,44,70,71,78,95,],[14,14,33,33,53,14,14,33,100,33,]),'assignment':([4,11,12,31,35,44,70,71,78,95,],[16,16,16,16,16,16,16,16,16,16,]),'if_statement':([4,11,12,31,35,44,70,71,78,95,],[17,17,17,17,17,17,17,17,17,17,]),'while_statement':([4,11,12,31,35,44,70,71,78,95,],[18,18,18,18,18,18,18,18,18,18,]),'do_while_statement':([4,11,12,31,35,44,70,71,78,95,],[19,19,19,19,19,19,19,19,19,19,]),'write_statement':([4,11,12,31,35,44,70,71,78,95,],[20,20,20,20,20,20,20,20,20,20,]),'read_statement':([4,11,12,31,35,44,70,71,78,95,],[21,21,21,21,21,21,21,21,21,21,]),'block':([4,11,12,31,35,44,70,71,78,95,],[22,22,22,22,52,22,22,22,99,22,]),'var_list':([7,],[29,]),'expression':([24,25,27,34,36,37,38,49,54,55,56,57,58,59,60,61,62,63,64,65,66,97,105,],[35,43,45,51,67,68,69,75,81,82,83,84,85,86,87,88,89,90,91,92,93,104,106,]),'else_part':([52,53,],[77,80,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> PROGRAM LBRACE declarations statements RBRACE','program',5,'p_program','parser.py',58),
  ('declarations -> declarations declaration','declarations',2,'p_declarations','parser.py',62),
  ('declarations -> declaration','declarations',1,'p_declarations','parser.py',63),
  ('declarations -> empty','declarations',1,'p_declarations','parser.py',64),
  ('declaration -> type var_list SEMICOLON','declaration',3,'p_declaration','parser.py',73),
  ('var_list -> var_list COMMA IDENTIFIER','var_list',3,'p_var_list','parser.py',77),
  ('var_list -> var_list COMMA IDENTIFIER ASSIGN expression','var_list',5,'p_var_list','parser.py',78),
  ('var_list -> IDENTIFIER','var_list',1,'p_var_list','parser.py',79),
  ('var_list -> IDENTIFIER ASSIGN expression','var_list',3,'p_var_list','parser.py',80),
  ('type -> INT','type',1,'p_type','parser.py',91),
  ('type -> FLOAT','type',1,'p_type','parser.py',92),
  ('type -> BOOL','type',1,'p_type','parser.py',93),
  ('statements -> statements statement','statements',2,'p_statements','parser.py',97),
  ('statements -> statement','statements',1,'p_statements','parser.py',98),
  ('statements -> empty','statements',1,'p_statements','parser.py',99),
  ('statement -> assignment','statement',1,'p_statement','parser.py',108),
  ('statement -> if_statement','statement',1,'p_statement','parser.py',109),
  ('statement -> while_statement','statement',1,'p_statement','parser.py',110),
  ('statement -> do_while_statement','statement',1,'p_statement','parser.py',111),
  ('statement -> write_statement','statement',1,'p_statement','parser.py',112),
  ('statement -> read_statement','statement',1,'p_statement','parser.py',113),
  ('statement -> block','statement',1,'p_statement','parser.py',114),
  ('assignment -> IDENTIFIER ASSIGN expression SEMICOLON','assignment',4,'p_assignment','parser.py',118),
  ('if_statement -> IF expression block else_part FI','if_statement',5,'p_if_statement','parser.py',122),
  ('if_statement -> IF expression statement else_part FI','if_statement',5,'p_if_statement','parser.py',123),
  ('else_part -> ELSE block','else_part',2,'p_else_part','parser.py',127),
  ('else_part -> ELSE statement','else_part',2,'p_else_part','parser.py',128),
  ('else_part -> empty','else_part',1,'p_else_part','parser.py',129),
  ('while_statement -> WHILE expression LBRACE statements RBRACE','while_statement',5,'p_while_statement','parser.py',136),
  ('do_while_statement -> DO LBRACE statements RBRACE WHILE LPAREN expression RPAREN SEMICOLON','do_while_statement',9,'p_do_while_statement','parser.py',140),
  ('write_statement -> WRITE expression SEMICOLON','write_statement',3,'p_write_statement','parser.py',144),
  ('read_statement -> READ IDENTIFIER SEMICOLON','read_statement',3,'p_read_statement','parser.py',148),
  ('block -> LBRACE statements RBRACE','block',3,'p_block','parser.py',152),
  ('expression -> expression PLUS expression','expression',3,'p_expression_binop','parser.py',156),
  ('expression -> expression MINUS expression','expression',3,'p_expression_binop','parser.py',157),
  ('expression -> expression TIMES expression','expression',3,'p_expression_binop','parser.py',158),
  ('expression -> expression DIVIDE expression','expression',3,'p_expression_binop','parser.py',159),
  ('expression -> expression POWER expression','expression',3,'p_expression_binop','parser.py',160),
  ('expression -> expression EQ expression','expression',3,'p_expression_binop','parser.py',161),
  ('expression -> expression LT expression','expression',3,'p_expression_binop','parser.py',162),
  ('expression -> expression GT expression','expression',3,'p_expression_binop','parser.py',163),
  ('expression -> expression LE expression','expression',3,'p_expression_binop','parser.py',164),
  ('expression -> expression GE expression','expression',3,'p_expression_binop','parser.py',165),
  ('expression -> expression NE expression','expression',3,'p_expression_binop','parser.py',166),
  ('expression -> expression AND expression','expression',3,'p_expression_binop','parser.py',167),
  ('expression -> expression OR expression','expression',3,'p_expression_binop','parser.py',168),
  ('expression -> MINUS expression','expression',2,'p_expression_uminus','parser.py',172),
  ('expression -> NOT expression','expression',2,'p_expression_not','parser.py',176),
  ('expression -> LPAREN expression RPAREN','expression',3,'p_expression_group','parser.py',180),
  ('expression -> NUMBER','expression',1,'p_expression_number','parser.py',184),
  ('expression -> IDENTIFIER','expression',1,'p_expression_identifier','parser.py',188),
  ('expression -> TRUE','expression',1,'p_expression_bool','parser.py',192),
  ('expression -> FALSE','expression',1,'p_expression_bool','parser.py',193),
  ('empty -> <empty>','empty',0,'p_empty','parser.py',197),
]
