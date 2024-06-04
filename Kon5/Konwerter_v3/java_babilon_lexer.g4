lexer grammar java_babilon_lexer;

// Tokens

//Keyword
CLASS           : 'class';
PUBLIC          : 'public';                                                                                         
PRIVATE         : 'private';
PROTECTED       : 'protected';
IF              : 'if';
DO              : 'do';
ELSE            : 'else';
RETURN          : 'return';
BREAK           : 'break';
WHILE           : 'while';
FOR             : 'for';
CONTINUE        : 'continue';
STATIC          : 'static';
EXTENDS         : 'extends';
NEW             : 'new';
IMPORT          : 'import';
ADD             : 'add';
MAIN            : 'main';

//Operator
PLUS            : '+';
MINUS           : '-';
MULT            : '*';
DIV             : '/';
EQUAL           : '==';
ASSIGN          : '=';
NOT_EQUAL       : '!=';
OR              : '||';
AND             : '&&';
MOD             : '%' ;
LESS            : '<';
GREATER         : '>';
GREATER_EQUAL   : '>=' ;
LESS_EQUAL      : '<=' ;
LOGICAL_NOT     : '!' ;
ADD_ASSIGN      : '+=' ;
SUB_ASSIGN      : '-=' ;
MUL_ASSIGN      : '*=' ;
DIV_ASSIGN      : '/=' ;
MOD_ASSIGN      : '%=' ;


//Delimiter
LPAREN          : '(';
RPAREN          : ')';
LBRACE          : '{';
RBRACE          : '}';
SEMICOLON       : ';';
LSQUARE         : '[' ;
RSQUARE         : ']' ;


//incremantation/decrementation
INCREMENT       : '++' ;
DECREMENT       : '--' ;

//whitespace characters
NEWLINE         : '\n';  // Token dla znaku nowej lini
TAB             : '\t';      // Token dla tabulatora


//type token
INTEGER         : '0' | [1-9] [0-9]*;
INTEGER_TOKEN   : 'int';
FLOAT           : [0-9]+ '.' [0-9]*;
FLOAT_TOKEN     : 'float';
VOID            : 'void';
STRING          : '"' (~["\\\r\n])* '"';
STRING_TOKEN    : 'String';
DOUBLE          : 'double';
LONG            : 'long';
SHORT           : 'short';
BYTE            : 'byte';
CHAR            : 'char';
BOOLEAN         : 'boolean';
INTEGERB        : 'Integer';
DOUBLEB         : 'Double';
FLOATB          : 'Float';
LONGB           : 'Long';
SHORTB          : 'Short';
BYTEB           : 'Byte';
CHARACTERB      : 'Character';
BOOLEANB        : 'Boolean';
ARRAY_LIST      : 'ArrayList';


//pirnt
PRINT : 'System.out.print';
PRINTLN : 'System.out.println';

//identifier
IDENTIFIER      : [a-zA-Z] [a-zA-Z_0-9]*;

//stale logiczne
TRUE            : 'true';
FALSE           : 'false';
NULL            : 'null';

//other tokens
DOT             : '.';
COMMA           : ',';
WHITESPACE      : [ \t\n\r\f]+ -> skip ;