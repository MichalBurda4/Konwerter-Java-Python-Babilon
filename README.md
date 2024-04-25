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


WHITESPACE : [ \t\n\r\f]+ -> skip ;
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

logicalExpression : expression (LESS | EQUAL | GREATHER) expression;   

primaryExpression : (INTEGER | FLOAT | STRING | methodCalling | IDENTIFIER );

```
