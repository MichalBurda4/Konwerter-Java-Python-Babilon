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
