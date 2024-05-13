lexer grammar SimplifiedJavaLexer;

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
ENUM            : 'enum';
DO              : 'do';
CONTINUE        : 'continue';
CASE            : 'case';
SWITCH          : 'switch';
STATIC          : 'static';
FINAL           : 'final';
ABSTRACT        : 'abstract';
DEFAULT         : 'default';
EXTENDS         : 'extends';
IMPLEMENTS      : 'implements';
VOLATAILE       : 'volataile';
THROWS          : 'throws';
TRY             : 'try';
CATCH           : 'catch';
FINALLY         : 'finally';
NEW             : 'new';
THIS            : 'this';
ASSERT          : 'assert';
IMPORT          : 'import';
PACKAGE         : 'package';
ADD             : 'add';


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
LESS            : '<';
GREATHER        : '>';
MOD             : '%' ;
GREATER         : '>=' ;
LESS            : '<=' ;
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


//Comment
SINGLE_LINE_COMMENT : '//' ~[\r\n]* -> skip;  // Komentarz jednoliniowy
MULTI_LINE_COMMENT : '/*' .*? '*/' -> skip;    // Komentarz wieloliniowy


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


//identifier
IDENTIFIER      : [a-zA-Z] [a-zA-Z_0-9]*;

//stale logiczne
TRUE            : 'true';
FALSE           : 'false';
NULL            : 'null';
fragment DIGIT
    :   [0-9]
    ;

INTEGER_NUMBER
    :   DIGIT+
    ;

FLOAT_NUMBER
    :   DIGIT+.DIGIT+
    ;
//other tokens
DOT             : '.';
COMMA           : ',';
TERNARY         : '?' ;
THE_DOUBLE_COLON : '::' ;
WHITESPACE      : [ \t\n\r\f]+ -> skip ;
