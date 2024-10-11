
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftPLUSMINUSleftTIMESDIVIDEleftORleftANDleftEQNEleftLTLEGTGErightUMINUSNOTAND ASSIGN BOOL COMMA DIVIDE DO ELSE EQ FALSE FI FLOAT GE GT IDENTIFIER IF INT LBRACE LE LPAREN LT MINUS NE NOT NUMBER OR PLUS PROGRAM RBRACE READ RPAREN SEMICOLON THEN TIMES TRUE UNTIL WHILE WRITEprogram : PROGRAM LBRACE declarations statements RBRACEdeclarations : declarations declaration\n                    | declaration\n                    | emptydeclaration : type var_list SEMICOLONvar_list : var_list COMMA IDENTIFIER\n                | var_list COMMA IDENTIFIER ASSIGN expression\n                | IDENTIFIER\n                | IDENTIFIER ASSIGN expressiontype : INT\n            | FLOAT\n            | BOOLstatements : statements statement\n                  | statement\n                  | emptystatement : assignment\n                 | if_statement\n                 | while_statement\n                 | do_while_statement\n                 | write_statement\n                 | read_statement\n                 | block\n                 | increment\n                 | decrementassignment : IDENTIFIER ASSIGN expression SEMICOLONincrement : IDENTIFIER PLUS PLUS SEMICOLONdecrement : IDENTIFIER MINUS MINUS SEMICOLONif_statement : IF expression block else_part FI\n                    | IF expression statement else_part FIelse_part : ELSE block\n                 | ELSE statement\n                 | emptywhile_statement : WHILE expression LBRACE statements RBRACEdo_while_statement : DO LBRACE statements RBRACE WHILE LPAREN expression RPAREN SEMICOLONwrite_statement : WRITE expression SEMICOLONread_statement : READ IDENTIFIER SEMICOLONblock : LBRACE statements RBRACEexpression : expression PLUS expression\n                  | expression MINUS expression\n                  | expression TIMES expression\n                  | expression DIVIDE expression\n                  | expression EQ expression\n                  | expression LT expression\n                  | expression GT expression\n                  | expression LE expression\n                  | expression GE expression\n                  | expression NE expression\n                  | expression AND expression\n                  | expression OR expressionexpression : MINUS expression %prec UMINUSexpression : NOT expressionexpression : LPAREN expression RPARENexpression : NUMBERexpression : IDENTIFIERexpression : TRUE\n                  | FALSEempty :'
    
_lr_action_items = {'PROGRAM':([0,],[2,]),'$end':([1,34,],[0,-1,]),'LBRACE':([2,3,4,5,6,11,12,13,14,15,16,17,18,19,20,21,22,23,24,28,33,35,39,43,44,45,46,47,48,51,54,72,73,75,76,77,78,81,82,83,85,88,89,90,91,92,93,94,95,96,97,98,99,100,101,104,107,108,114,],[3,-57,11,-3,-4,11,11,-2,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,48,11,-13,11,-53,-54,-55,-56,75,11,-5,-37,-50,-51,11,11,-35,-36,-25,-26,-27,11,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-52,11,-28,-29,-33,-34,]),'INT':([3,4,5,6,13,51,],[8,8,-3,-4,-2,-5,]),'FLOAT':([3,4,5,6,13,51,],[9,9,-3,-4,-2,-5,]),'BOOL':([3,4,5,6,13,51,],[10,10,-3,-4,-2,-5,]),'IDENTIFIER':([3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,26,27,29,30,33,35,36,39,40,41,42,43,44,45,46,48,51,52,53,54,60,61,62,63,64,65,66,67,68,69,70,71,72,73,75,76,77,78,81,82,83,85,88,89,90,91,92,93,94,95,96,97,98,99,100,101,103,104,107,108,111,114,],[-57,25,-3,-4,32,-10,-11,-12,25,25,-2,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,44,44,44,50,25,-13,44,25,44,44,44,-53,-54,-55,-56,25,-5,79,44,-37,44,44,44,44,44,44,44,44,44,44,44,44,-50,-51,25,25,-35,-36,-25,-26,-27,25,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-52,25,44,-28,-29,-33,44,-34,]),'IF':([3,4,5,6,11,12,13,14,15,16,17,18,19,20,21,22,23,24,33,35,39,43,44,45,46,48,51,54,72,73,75,76,77,78,81,82,83,85,88,89,90,91,92,93,94,95,96,97,98,99,100,101,104,107,108,114,],[-57,26,-3,-4,26,26,-2,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,26,-13,26,-53,-54,-55,-56,26,-5,-37,-50,-51,26,26,-35,-36,-25,-26,-27,26,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-52,26,-28,-29,-33,-34,]),'WHILE':([3,4,5,6,11,12,13,14,15,16,17,18,19,20,21,22,23,24,33,35,39,43,44,45,46,48,51,54,72,73,75,76,77,78,81,82,83,85,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,104,107,108,114,],[-57,27,-3,-4,27,27,-2,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,27,-13,27,-53,-54,-55,-56,27,-5,-37,-50,-51,27,27,-35,-36,-25,-26,-27,27,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-52,27,109,-28,-29,-33,-34,]),'DO':([3,4,5,6,11,12,13,14,15,16,17,18,19,20,21,22,23,24,33,35,39,43,44,45,46,48,51,54,72,73,75,76,77,78,81,82,83,85,88,89,90,91,92,93,94,95,96,97,98,99,100,101,104,107,108,114,],[-57,28,-3,-4,28,28,-2,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,28,-13,28,-53,-54,-55,-56,28,-5,-37,-50,-51,28,28,-35,-36,-25,-26,-27,28,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-52,28,-28,-29,-33,-34,]),'WRITE':([3,4,5,6,11,12,13,14,15,16,17,18,19,20,21,22,23,24,33,35,39,43,44,45,46,48,51,54,72,73,75,76,77,78,81,82,83,85,88,89,90,91,92,93,94,95,96,97,98,99,100,101,104,107,108,114,],[-57,29,-3,-4,29,29,-2,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,29,-13,29,-53,-54,-55,-56,29,-5,-37,-50,-51,29,29,-35,-36,-25,-26,-27,29,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-52,29,-28,-29,-33,-34,]),'READ':([3,4,5,6,11,12,13,14,15,16,17,18,19,20,21,22,23,24,33,35,39,43,44,45,46,48,51,54,72,73,75,76,77,78,81,82,83,85,88,89,90,91,92,93,94,95,96,97,98,99,100,101,104,107,108,114,],[-57,30,-3,-4,30,30,-2,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,30,-13,30,-53,-54,-55,-56,30,-5,-37,-50,-51,30,30,-35,-36,-25,-26,-27,30,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-52,30,-28,-29,-33,-34,]),'RBRACE':([3,4,5,6,11,12,13,14,15,16,17,18,19,20,21,22,23,24,33,35,48,51,54,75,76,77,78,81,82,83,101,104,107,108,114,],[-57,-57,-3,-4,-57,34,-2,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,54,-13,-57,-5,-37,-57,102,-35,-36,-25,-26,-27,108,-28,-29,-33,-34,]),'ELSE':([16,17,18,19,20,21,23,24,54,58,59,77,78,81,82,83,104,107,108,114,],[-16,-17,-18,-19,-20,-21,-23,-24,-37,85,85,-35,-36,-25,-26,-27,-28,-29,-33,-34,]),'FI':([16,17,18,19,20,21,23,24,54,58,59,77,78,81,82,83,84,86,87,104,105,106,107,108,114,],[-16,-17,-18,-19,-20,-21,-23,-24,-37,-22,-57,-35,-36,-25,-26,-27,104,-32,107,-28,-22,-31,-29,-33,-34,]),'ASSIGN':([25,32,79,],[36,53,103,]),'PLUS':([25,37,39,43,44,45,46,47,49,55,72,73,74,80,88,89,90,91,92,93,94,95,96,97,98,99,100,110,112,],[37,56,60,-53,-54,-55,-56,60,60,60,-50,-51,60,60,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-52,60,60,]),'MINUS':([25,26,27,29,36,38,39,40,41,42,43,44,45,46,47,49,53,55,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,80,88,89,90,91,92,93,94,95,96,97,98,99,100,103,110,111,112,],[38,40,40,40,40,57,61,40,40,40,-53,-54,-55,-56,61,61,40,61,40,40,40,40,40,40,40,40,40,40,40,40,-50,-51,61,61,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-52,40,61,40,61,]),'NOT':([26,27,29,36,40,41,42,53,60,61,62,63,64,65,66,67,68,69,70,71,103,111,],[41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,]),'LPAREN':([26,27,29,36,40,41,42,53,60,61,62,63,64,65,66,67,68,69,70,71,103,109,111,],[42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,111,42,]),'NUMBER':([26,27,29,36,40,41,42,53,60,61,62,63,64,65,66,67,68,69,70,71,103,111,],[43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,]),'TRUE':([26,27,29,36,40,41,42,53,60,61,62,63,64,65,66,67,68,69,70,71,103,111,],[45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,]),'FALSE':([26,27,29,36,40,41,42,53,60,61,62,63,64,65,66,67,68,69,70,71,103,111,],[46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,]),'SEMICOLON':([31,32,43,44,45,46,49,50,55,56,57,72,73,79,80,88,89,90,91,92,93,94,95,96,97,98,99,100,110,113,],[51,-8,-53,-54,-55,-56,77,78,81,82,83,-50,-51,-6,-9,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-52,-7,114,]),'COMMA':([31,32,43,44,45,46,72,73,79,80,88,89,90,91,92,93,94,95,96,97,98,99,100,110,],[52,-8,-53,-54,-55,-56,-50,-51,-6,-9,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-52,-7,]),'TIMES':([39,43,44,45,46,47,49,55,72,73,74,80,88,89,90,91,92,93,94,95,96,97,98,99,100,110,112,],[62,-53,-54,-55,-56,62,62,62,-50,-51,62,62,62,62,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-52,62,62,]),'DIVIDE':([39,43,44,45,46,47,49,55,72,73,74,80,88,89,90,91,92,93,94,95,96,97,98,99,100,110,112,],[63,-53,-54,-55,-56,63,63,63,-50,-51,63,63,63,63,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-52,63,63,]),'EQ':([39,43,44,45,46,47,49,55,72,73,74,80,88,89,90,91,92,93,94,95,96,97,98,99,100,110,112,],[64,-53,-54,-55,-56,64,64,64,-50,-51,64,64,64,64,64,64,-42,-43,-44,-45,-46,-47,64,64,-52,64,64,]),'LT':([39,43,44,45,46,47,49,55,72,73,74,80,88,89,90,91,92,93,94,95,96,97,98,99,100,110,112,],[65,-53,-54,-55,-56,65,65,65,-50,-51,65,65,65,65,65,65,65,-43,-44,-45,-46,65,65,65,-52,65,65,]),'GT':([39,43,44,45,46,47,49,55,72,73,74,80,88,89,90,91,92,93,94,95,96,97,98,99,100,110,112,],[66,-53,-54,-55,-56,66,66,66,-50,-51,66,66,66,66,66,66,66,-43,-44,-45,-46,66,66,66,-52,66,66,]),'LE':([39,43,44,45,46,47,49,55,72,73,74,80,88,89,90,91,92,93,94,95,96,97,98,99,100,110,112,],[67,-53,-54,-55,-56,67,67,67,-50,-51,67,67,67,67,67,67,67,-43,-44,-45,-46,67,67,67,-52,67,67,]),'GE':([39,43,44,45,46,47,49,55,72,73,74,80,88,89,90,91,92,93,94,95,96,97,98,99,100,110,112,],[68,-53,-54,-55,-56,68,68,68,-50,-51,68,68,68,68,68,68,68,-43,-44,-45,-46,68,68,68,-52,68,68,]),'NE':([39,43,44,45,46,47,49,55,72,73,74,80,88,89,90,91,92,93,94,95,96,97,98,99,100,110,112,],[69,-53,-54,-55,-56,69,69,69,-50,-51,69,69,69,69,69,69,-42,-43,-44,-45,-46,-47,69,69,-52,69,69,]),'AND':([39,43,44,45,46,47,49,55,72,73,74,80,88,89,90,91,92,93,94,95,96,97,98,99,100,110,112,],[70,-53,-54,-55,-56,70,70,70,-50,-51,70,70,70,70,70,70,-42,-43,-44,-45,-46,-47,-48,70,-52,70,70,]),'OR':([39,43,44,45,46,47,49,55,72,73,74,80,88,89,90,91,92,93,94,95,96,97,98,99,100,110,112,],[71,-53,-54,-55,-56,71,71,71,-50,-51,71,71,71,71,71,71,-42,-43,-44,-45,-46,-47,-48,-49,-52,71,71,]),'RPAREN':([43,44,45,46,72,73,74,88,89,90,91,92,93,94,95,96,97,98,99,100,112,],[-53,-54,-55,-56,-50,-51,100,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-52,113,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'declarations':([3,],[4,]),'declaration':([3,4,],[5,13,]),'empty':([3,4,11,48,58,59,75,],[6,15,15,15,86,86,15,]),'type':([3,4,],[7,7,]),'statements':([4,11,48,75,],[12,33,76,101,]),'statement':([4,11,12,33,39,48,75,76,85,101,],[14,14,35,35,59,14,14,35,106,35,]),'assignment':([4,11,12,33,39,48,75,76,85,101,],[16,16,16,16,16,16,16,16,16,16,]),'if_statement':([4,11,12,33,39,48,75,76,85,101,],[17,17,17,17,17,17,17,17,17,17,]),'while_statement':([4,11,12,33,39,48,75,76,85,101,],[18,18,18,18,18,18,18,18,18,18,]),'do_while_statement':([4,11,12,33,39,48,75,76,85,101,],[19,19,19,19,19,19,19,19,19,19,]),'write_statement':([4,11,12,33,39,48,75,76,85,101,],[20,20,20,20,20,20,20,20,20,20,]),'read_statement':([4,11,12,33,39,48,75,76,85,101,],[21,21,21,21,21,21,21,21,21,21,]),'block':([4,11,12,33,39,48,75,76,85,101,],[22,22,22,22,58,22,22,22,105,22,]),'increment':([4,11,12,33,39,48,75,76,85,101,],[23,23,23,23,23,23,23,23,23,23,]),'decrement':([4,11,12,33,39,48,75,76,85,101,],[24,24,24,24,24,24,24,24,24,24,]),'var_list':([7,],[31,]),'expression':([26,27,29,36,40,41,42,53,60,61,62,63,64,65,66,67,68,69,70,71,103,111,],[39,47,49,55,72,73,74,80,88,89,90,91,92,93,94,95,96,97,98,99,110,112,]),'else_part':([58,59,],[84,87,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> PROGRAM LBRACE declarations statements RBRACE','program',5,'p_program','parser.py',57),
  ('declarations -> declarations declaration','declarations',2,'p_declarations','parser.py',61),
  ('declarations -> declaration','declarations',1,'p_declarations','parser.py',62),
  ('declarations -> empty','declarations',1,'p_declarations','parser.py',63),
  ('declaration -> type var_list SEMICOLON','declaration',3,'p_declaration','parser.py',72),
  ('var_list -> var_list COMMA IDENTIFIER','var_list',3,'p_var_list','parser.py',76),
  ('var_list -> var_list COMMA IDENTIFIER ASSIGN expression','var_list',5,'p_var_list','parser.py',77),
  ('var_list -> IDENTIFIER','var_list',1,'p_var_list','parser.py',78),
  ('var_list -> IDENTIFIER ASSIGN expression','var_list',3,'p_var_list','parser.py',79),
  ('type -> INT','type',1,'p_type','parser.py',90),
  ('type -> FLOAT','type',1,'p_type','parser.py',91),
  ('type -> BOOL','type',1,'p_type','parser.py',92),
  ('statements -> statements statement','statements',2,'p_statements','parser.py',96),
  ('statements -> statement','statements',1,'p_statements','parser.py',97),
  ('statements -> empty','statements',1,'p_statements','parser.py',98),
  ('statement -> assignment','statement',1,'p_statement','parser.py',107),
  ('statement -> if_statement','statement',1,'p_statement','parser.py',108),
  ('statement -> while_statement','statement',1,'p_statement','parser.py',109),
  ('statement -> do_while_statement','statement',1,'p_statement','parser.py',110),
  ('statement -> write_statement','statement',1,'p_statement','parser.py',111),
  ('statement -> read_statement','statement',1,'p_statement','parser.py',112),
  ('statement -> block','statement',1,'p_statement','parser.py',113),
  ('statement -> increment','statement',1,'p_statement','parser.py',114),
  ('statement -> decrement','statement',1,'p_statement','parser.py',115),
  ('assignment -> IDENTIFIER ASSIGN expression SEMICOLON','assignment',4,'p_assignment','parser.py',119),
  ('increment -> IDENTIFIER PLUS PLUS SEMICOLON','increment',4,'p_increment','parser.py',124),
  ('decrement -> IDENTIFIER MINUS MINUS SEMICOLON','decrement',4,'p_decrement','parser.py',128),
  ('if_statement -> IF expression block else_part FI','if_statement',5,'p_if_statement','parser.py',132),
  ('if_statement -> IF expression statement else_part FI','if_statement',5,'p_if_statement','parser.py',133),
  ('else_part -> ELSE block','else_part',2,'p_else_part','parser.py',137),
  ('else_part -> ELSE statement','else_part',2,'p_else_part','parser.py',138),
  ('else_part -> empty','else_part',1,'p_else_part','parser.py',139),
  ('while_statement -> WHILE expression LBRACE statements RBRACE','while_statement',5,'p_while_statement','parser.py',146),
  ('do_while_statement -> DO LBRACE statements RBRACE WHILE LPAREN expression RPAREN SEMICOLON','do_while_statement',9,'p_do_while_statement','parser.py',150),
  ('write_statement -> WRITE expression SEMICOLON','write_statement',3,'p_write_statement','parser.py',154),
  ('read_statement -> READ IDENTIFIER SEMICOLON','read_statement',3,'p_read_statement','parser.py',158),
  ('block -> LBRACE statements RBRACE','block',3,'p_block','parser.py',162),
  ('expression -> expression PLUS expression','expression',3,'p_expression_binop','parser.py',166),
  ('expression -> expression MINUS expression','expression',3,'p_expression_binop','parser.py',167),
  ('expression -> expression TIMES expression','expression',3,'p_expression_binop','parser.py',168),
  ('expression -> expression DIVIDE expression','expression',3,'p_expression_binop','parser.py',169),
  ('expression -> expression EQ expression','expression',3,'p_expression_binop','parser.py',170),
  ('expression -> expression LT expression','expression',3,'p_expression_binop','parser.py',171),
  ('expression -> expression GT expression','expression',3,'p_expression_binop','parser.py',172),
  ('expression -> expression LE expression','expression',3,'p_expression_binop','parser.py',173),
  ('expression -> expression GE expression','expression',3,'p_expression_binop','parser.py',174),
  ('expression -> expression NE expression','expression',3,'p_expression_binop','parser.py',175),
  ('expression -> expression AND expression','expression',3,'p_expression_binop','parser.py',176),
  ('expression -> expression OR expression','expression',3,'p_expression_binop','parser.py',177),
  ('expression -> MINUS expression','expression',2,'p_expression_uminus','parser.py',181),
  ('expression -> NOT expression','expression',2,'p_expression_not','parser.py',185),
  ('expression -> LPAREN expression RPAREN','expression',3,'p_expression_group','parser.py',189),
  ('expression -> NUMBER','expression',1,'p_expression_number','parser.py',193),
  ('expression -> IDENTIFIER','expression',1,'p_expression_identifier','parser.py',197),
  ('expression -> TRUE','expression',1,'p_expression_bool','parser.py',201),
  ('expression -> FALSE','expression',1,'p_expression_bool','parser.py',202),
  ('empty -> <empty>','empty',0,'p_empty','parser.py',206),
]
