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
PROTECTED       : 'protected';
IF              : 'if';
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

//Deklaracja klasy
classDeclaration : (PRIVATE | PUBLIC | PROTECTED)? CLASS IDENTIFIER LBRACE classBody RBRACE;

//Ciało klasy
classBody : (methodDefinition | fieldDefinition)* NEWLINE?;

//Deklaracja metody
methodDefinition : (PUBLIC | PRIVATE | PROTECTED) (INTEGER_TOKEN | FLOAT_TOKEN | STRING_TOKEN | VOID) IDENTIFIER LPAREN parametersDefinition RPAREN LBRACE statements RBRACE;

parameters : (expression (COMMA expression)*)?;

parametersDefinition : (oneParameterDefinition (COMMA oneParameterDefinition)*)?;

oneParameterDefinition: (INTEGER_TOKEN | FLOAT_TOKEN | STRING_TOKEN) IDENTIFIER;

fieldDefinition : (PUBLIC | PRIVATE) (INTEGER_TOKEN | FLOAT_TOKEN | STRING_TOKEN) IDENTIFIER (ASSIGN expression SEMICOLON)?;

variableDefinition : (INTEGER_TOKEN | FLOAT_TOKEN | STRING_TOKEN) IDENTIFIER (ASSIGN expression)? SEMICOLON; 
 
methodCalling : IDENTIFIER LPAREN parameters RPAREN SEMICOLON;

//Wnętrze metody
statements : (statement)*;
statement : (ifStatement| forLoopStatement | whileLoopStatement | assignmentStatement | variableDefinition | methodCalling | incrementStatement | decrementStatement | arrayDefinition | listDefinition | listAddDefinition);

ifStatement : IF LPAREN logicalExpression RPAREN LBRACE statements RBRACE (ELSE LBRACE statements RBRACE)?;

forLoopStatement : (FOR LPAREN  forLoopVariable SEMICOLON oneLogicalExpression SEMICOLON forLoopVariable RPAREN LBRACE statements RBRACE) | (FOR LPAREN SEMICOLON SEMICOLON RPAREN LBRACE statements RBRACE);

forLoopVariable : ((INTEGER_TOKEN | FLOAT_TOKEN | STRING_TOKEN) IDENTIFIER (ASSIGN expression)? | IDENTIFIER ASSIGN expression | (IDENTIFIER INCREMENT | INCREMENT IDENTIFIER) | (IDENTIFIER DECREMENT | DECREMENT IDENTIFIER)); 

whileLoopStatement : WHILE LPAREN oneLogicalExpression RPAREN LBRACE statements RBRACE;

assignmentStatement : IDENTIFIER ASSIGN expression SEMICOLON;

incrementStatement : (IDENTIFIER INCREMENT | INCREMENT IDENTIFIER) SEMICOLON ; 

decrementStatement : (IDENTIFIER DECREMENT | DECREMENT IDENTIFIER) SEMICOLON ; 

expression : (additiveExpression | multiplicativeExpression | primaryExpression);

additiveExpression : multiplicativeExpression ((PLUS | MINUS) multiplicativeExpression)*;

multiplicativeExpression : primaryExpression ((MULT | DIV) primaryExpression)*;

logicalExpression : (oneLogicalExpression ((AND | OR) oneLogicalExpression)*);

oneLogicalExpression : expression (LESS | EQUAL | GREATHER) expression;

primaryExpression : (INTEGER | FLOAT | STRING | methodCalling | IDENTIFIER );

//Tablice
arrayDefinition : (INTEGER_TOKEN | FLOAT_TOKEN | STRING_TOKEN | DOUBLE) LSQUARE RSQUARE IDENTIFIER (ASSIGN) NEW (INTEGER_TOKEN | FLOAT_TOKEN | STRING_TOKEN | DOUBLE) LSQUARE expression RSQUARE SEMICOLON?; 

//Listy
listDefinition : IDENTIFIER LESS (INTEGERB | DOUBLEB | FLOATB | LONGB | SHORTB | BYTEB | CHARACTERB | BOOLEANB) GREATHER IDENTIFIER (ASSIGN) NEW IDENTIFIER LESS GREATHER LPAREN RPAREN SEMICOLON?;
//Dodanie elementu do listy
listAddDefinition : IDENTIFIER DOT ADD LPAREN expression RPAREN SEMICOLON?;



```

## Drzewo składniowe kodu źródłowego języka Java 🌳:
![image](https://github.com/MichalBurda4/Konwerter-Java-Python-Babilon/assets/163707785/0c8c640b-a850-499c-8b69-e09d02b06aee)
![image](https://github.com/MichalBurda4/Konwerter-Java-Python-Babilon/assets/163707785/2a0754d3-f25d-48b7-b0c2-0c7f54b16f80)
![image](https://github.com/MichalBurda4/Konwerter-Java-Python-Babilon/assets/163707785/d36004c1-75ac-4dfe-96b0-fd3fa84d5e95)

Podane obrazy przedstawiają drzewo składniowe kodu źródłowego w języku Java. Drzewo składniowe, znane również jako drzewo wyprowadzeń (parse tree), reprezentuje strukturalne części programu i sposób, w jaki są one zagnieżdżone w kodzie.

### Prolog:

Program zaczyna się od klasy MainClass z metodą main, która zawiera kilka deklaracji zmiennych i operacji matematycznych.
Główna struktura to klasa MainClass z metodą main, która zawiera dwie klasy wewnętrzne ChildClass1 i ChildClass2.

- Klasa MainClass zawiera dwie klasy wewnętrzne ChildClass1 i ChildClass2.

- Klasa ChildClass1 ma dwie zmienne prywatne a i b, oraz metodę addNumbers.

- Klasa ChildClass2 ma jedną zmienną prywatną x oraz metodę subtractNumbers.

- Metoda main zawiera:
Deklarację i inicjalizację zmiennej result.
Tworzenie instancji klas ChildClass1 i ChildClass2.
Wywołanie metod addNumbers i subtractNumbers na instancjach klas wewnętrznych.

- ChildClass1.addNumbers dodaje dwie liczby.
ChildClass2.subtractNumbers odejmuje dwie liczby.

Drzewo składniowe szczegółowo przedstawia każdy element kodu, pokazując strukturę kodu źródłowego. Każdy węzeł reprezentuje składniowy element, taki jak deklaracja klasy, metoda, operacja matematyczna, wyrażenie itp. Drzewo rozgałęzia się, pokazując hierarchię i zagnieżdżenie składniowe elementów programu.





## Narzędzia z jakich korzystamy:
Antlr: http://lab.antlr.org/
