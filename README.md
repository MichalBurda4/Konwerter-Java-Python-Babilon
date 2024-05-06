# Konwerter-Java-Python-Babilon

## Opis projektu: 
Projekt polega na stworzeniu prostego narzędzia do konwersji kodu z języka Java na język Python, obejmującego analizę składniową kodu Java i generowanie odpowiedniego kodu Pythona.

## Autorzy: 
* Michał Burda
* Radosław Barszczak

## Kontakt: 📞
* michalburda@student.agh.edu.pl
* rbarszczak@student.agh.edu.pl

## Tokeny:
```
lexer grammar SimplifiedJavaLexer;

// Tokens

//Keyword
CLASS           : 'class';
PUBLIC          : 'public';                                                                                         
PRIVATE         : 'private';
IF              : 'if';
ELSE            : 'else';
RETURN          : 'return';
BREAK           : 'break';
WHILE           : 'while';
ENUM            : 'enum';
DO              : 'do';
CONTINUE        : 'continue';
CASE            : 'case';
SWITCH          : 'switch';
PROTECTED       : 'protected;
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
GREATER_THAN_OR_EQUAL : '>=' ;
LESS_THAN_OR_EQUAL : '<=' ;
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
STRING_TOKEN    : 'string'; 
DOUBLE          : 'double';
LONG            : 'long';
SHORT           : 'short';
BYTE            : 'byte';
CHAR            : 'char';
BOOLEAN         : 'boolean';


//identifier
IDENTIFIER      : [a-zA-Z] [a-zA-Z_0-9]*;

//stale logiczne
TRUE            : 'true';
FALSE           : 'false';
NULL            : 'null';

//other tokens
DOT             : '.';
COMMA           : ',';
TERNARY         : '?' ;
THE_DOUBLE_COLON : '::' ;
WHITESPACE      : [ \t\n\r\f]+ -> skip ;
```

## Gramatyka

```
grammar SimplifiedJavaParser;


// Parser rules
program : (classDeclaration)+;

classDeclaration : (PRIVATE | PUBLIC)? CLASS IDENTIFIER LBRACE classBody RBRACE;

classBody : (methodDefinition | fieldDefinition)*;

methodDefinition : (PUBLIC | PRIVATE) (INTEGER_TOKEN | FLOAT_TOKEN | STRING_TOKEN | VOID) IDENTIFIER LPAREN parametersDefinition RPAREN LBRACE statements RBRACE;

parameters : (expression (COMMA expression)*)?;

parametersDefinition : (oneParameterDefinition (COMMA oneParameterDefinition)*)?;

oneParameterDefinition: (INTEGER_TOKEN | FLOAT_TOKEN | STRING_TOKEN) IDENTIFIER;

fieldDefinition : (PUBLIC | PRIVATE) (INTEGER_TOKEN | FLOAT_TOKEN | STRING_TOKEN) IDENTIFIER (ASSIGN expression SEMICOLON)?;

variableDefinition : (INTEGER_TOKEN | FLOAT_TOKEN | STRING_TOKEN) IDENTIFIER (ASSIGN expression)? SEMICOLON?;

methodCalling : IDENTIFIER LPAREN parameters RPAREN SEMICOLON;

statements : (statement)*;

statement : (ifStatement | assignmentStatement | variableDefinition | methodCalling);

ifStatement : IF LPAREN logicalExpression RPAREN LBRACE statements RBRACE (ELSE LBRACE statements RBRACE)?;

assignmentStatement : IDENTIFIER ASSIGN expression SEMICOLON;

expression : (additiveExpression | multiplicativeExpression | primaryExpression);

additiveExpression : multiplicativeExpression ((PLUS | MINUS) multiplicativeExpression)*;

multiplicativeExpression : primaryExpression ((MULT | DIV) primaryExpression)*;

logicalExpression : (oneLogicalExpression ((AND | OR) oneLogicalExpression)*);

oneLogicalExpression : expression (LESS | EQUAL | GREATHER) expression;

primaryExpression : (INTEGER | FLOAT | STRING | methodCalling | IDENTIFIER );
```

## Narzędzia z jakich korzystamy:
Antlr: http://lab.antlr.org/
