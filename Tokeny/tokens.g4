lexer grammar SimplifiedJavaLexer;

// Tokens
CLASS           : 'class';
PUBLIC          : 'public';                                                                                         
PRIVATE         : 'private';
IF              : 'if';
ELSE            : 'else';
OR              : '||';
AND             : '&&';
LESS            : '<';
GREATHER        : '>';
EQUAL           : '==';
LPAREN          : '(';
RPAREN          : ')';
LBRACE          : '{';
RBRACE          : '}';
ASSIGN          : '=';
COMMA           : ',';
SEMICOLON       : ';';
PLUS            : '+';
MINUS           : '-';
MULT            : '*';
DIV             : '/';
INTEGER         : '0' | [1-9] [0-9]*;
INTEGER_TOKEN   : 'int';
FLOAT           : [0-9]+ '.' [0-9]*;
FLOAT_TOKEN     : 'float';
VOID            : 'void';
STRING          : '"' (~["\\\r\n])* '"';
STRING_TOKEN    : 'string'; 
IDENTIFIER      : [a-zA-Z] [a-zA-Z_0-9]*;
DOT             : '.';



WHITESPACE : [ \t\n\r\f]+ -> skip ;
