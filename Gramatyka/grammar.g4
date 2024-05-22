
grammar java_babilon;


// Parser rules
program : (classDeclaration)+;

//Deklaracja klasy
classDeclaration : (PRIVATE | PUBLIC | PROTECTED)? CLASS IDENTIFIER (EXTENDS IDENTIFIER)? LBRACE classBody RBRACE;

//Ciało klasy
classBody : (methodDefinition | fieldDefinition)* NEWLINE?;

//Deklaracja metody
methodDefinition : (PUBLIC | PRIVATE | PROTECTED) STATIC? (INTEGER_TOKEN | FLOAT_TOKEN | STRING_TOKEN | VOID) IDENTIFIER LPAREN parametersDefinition RPAREN LBRACE statements RBRACE;

parameters : (expression (COMMA expression)*)?;

parametersDefinition : (oneParameterDefinition (COMMA oneParameterDefinition)*)?;

oneParameterDefinition: (INTEGER_TOKEN | FLOAT_TOKEN | STRING_TOKEN) IDENTIFIER;

fieldDefinition : (PUBLIC | PRIVATE) (INTEGER_TOKEN | FLOAT_TOKEN | STRING_TOKEN) IDENTIFIER (ASSIGN expression SEMICOLON)?;

variableDefinition : (INTEGER_TOKEN | FLOAT_TOKEN | STRING_TOKEN) IDENTIFIER (ASSIGN expression)? SEMICOLON; 
 
methodCalling : IDENTIFIER LPAREN parameters RPAREN SEMICOLON;

fieldAccesing : IDENTIFIER DOT IDENTIFIER;

//Wnętrze metody instrukcje
statements : (statement)*;
statement : (ifStatement
          | forLoopStatement 
          | whileLoopStatement 
          | assignmentStatement 
          | variableDefinition 
          | methodCalling 
          | incrementStatement 
          | decrementStatement 
          | arrayDefinition 
          | listDefinition 
          | listAddDefinition
          | objectCreating
          | returnStatement
          | breakStatement
          | continueStatement
          | doWhileStatement
          | printStatement
);

//print
//Obsługa lini komend
printStatement
    : PRINTLN LPAREN expression RPAREN SEMICOLON
    ;
//dowhile
doWhileStatement : DO LBRACE statement RBRACE WHILE LPAREN (oneLogicalExpression) RPAREN SEMICOLON ;

//continue 
continueStatement : CONTINUE SEMICOLON ;
//brake 
breakStatement : BREAK SEMICOLON ;

//return
returnStatement : RETURN (expression | literal)? SEMICOLON ;
//Dane
literal : INTEGER_NUMBER 
        | FLOAT_NUMBER 
        | STRING
        | TRUE 
        | FALSE 
        | NULL 
        ;
//If
ifStatement : IF LPAREN logicalExpression RPAREN LBRACE statements RBRACE (ELSE LBRACE statements RBRACE)?;

//Petla for
forLoopStatement : (FOR LPAREN  forLoopVariable SEMICOLON oneLogicalExpression SEMICOLON forLoopVariable RPAREN LBRACE statements RBRACE) | (FOR LPAREN SEMICOLON SEMICOLON RPAREN LBRACE statements RBRACE);
forLoopVariable : ((INTEGER_TOKEN | FLOAT_TOKEN | STRING_TOKEN) IDENTIFIER (ASSIGN expression)? | IDENTIFIER ASSIGN expression | (IDENTIFIER INCREMENT | INCREMENT IDENTIFIER) | (IDENTIFIER DECREMENT | DECREMENT IDENTIFIER)); 

//Petla while
whileLoopStatement : WHILE LPAREN oneLogicalExpression RPAREN LBRACE statements RBRACE;

assignmentStatement : IDENTIFIER ASSIGN expression SEMICOLON;

incrementStatement : (IDENTIFIER INCREMENT | INCREMENT IDENTIFIER) SEMICOLON ; 

decrementStatement : (IDENTIFIER DECREMENT | DECREMENT IDENTIFIER) SEMICOLON ; 

expression : (additiveExpression | multiplicativeExpression | primaryExpression);

additiveExpression : multiplicativeExpression ((PLUS | MINUS) multiplicativeExpression)*;

multiplicativeExpression : primaryExpression ((MULT | DIV) primaryExpression)*;

primaryExpression : (INTEGER | FLOAT | STRING | methodCalling | fieldAccesing | IDENTIFIER );

logicalExpression : (oneLogicalExpression ((AND | OR) oneLogicalExpression)*);

oneLogicalExpression : (expression (LESS | EQUAL | GREATHER) expression) | TRUE | FALSE;

//Tablice
arrayDefinition : (INTEGER_TOKEN | FLOAT_TOKEN | STRING_TOKEN | DOUBLE) LSQUARE RSQUARE IDENTIFIER (ASSIGN) NEW (INTEGER_TOKEN | FLOAT_TOKEN | STRING_TOKEN | DOUBLE) LSQUARE expression RSQUARE SEMICOLON?; 

//Listy
listDefinition : ARRAY_LIST LESS (INTEGERB | DOUBLEB | FLOATB | LONGB | SHORTB | BYTEB | CHARACTERB | BOOLEANB) GREATHER IDENTIFIER (ASSIGN NEW ARRAY_LIST LESS GREATHER LPAREN RPAREN)? SEMICOLON;

//Dodanie elementu do listy
listAddDefinition : IDENTIFIER DOT ADD LPAREN expression RPAREN SEMICOLON;

objectCreating : IDENTIFIER IDENTIFIER (ASSIGN NEW IDENTIFIER LPAREN parameters RPAREN)? SEMICOLON;

