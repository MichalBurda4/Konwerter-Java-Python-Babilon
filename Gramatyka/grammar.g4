parser grammar java_babilon_parser;

options { tokenVocab=java_babilon_lexer; }

program : importStatement* classDeclaration+;

classDeclaration : (PRIVATE | PUBLIC | PROTECTED)? CLASS IDENTIFIER (EXTENDS IDENTIFIER)? LBRACE classBody RBRACE;

classBody : (mainMethod | methodDefinition | fieldDefinition)* NEWLINE?;

importStatement : IMPORT ((IDENTIFIER (DOT IDENTIFIER)*) | ARRAY_LIST) SEMICOLON;

mainMethod : PUBLIC STATIC VOID MAIN LPAREN STRING_TOKEN LSQUARE RSQUARE IDENTIFIER RPAREN LBRACE statements RBRACE;

methodDefinition : (PUBLIC | PRIVATE | PROTECTED) STATIC? (INTEGER_TOKEN | FLOAT_TOKEN | STRING_TOKEN | VOID) IDENTIFIER LPAREN parametersDefinition RPAREN LBRACE statements RBRACE;

parameters : (expression (COMMA expression)*)?;

parametersDefinition : (oneParameterDefinition (COMMA oneParameterDefinition)*)?;

oneParameterDefinition: (INTEGER_TOKEN | FLOAT_TOKEN | STRING_TOKEN) IDENTIFIER;

fieldDefinition : (PUBLIC | PRIVATE) (INTEGER_TOKEN | FLOAT_TOKEN | STRING_TOKEN) IDENTIFIER (ASSIGN expression)? SEMICOLON;

variableDefinition : (INTEGER_TOKEN | FLOAT_TOKEN | STRING_TOKEN) IDENTIFIER (ASSIGN expression)? SEMICOLON;

methodCalling : IDENTIFIER LPAREN parameters RPAREN SEMICOLON;

fieldAccessing : IDENTIFIER (DOT IDENTIFIER)+;

statements : statement*;
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

printStatement : PRINTLN LPAREN expression RPAREN SEMICOLON;

doWhileStatement : DO LBRACE statements RBRACE WHILE LPAREN oneLogicalExpression RPAREN SEMICOLON;

continueStatement : CONTINUE SEMICOLON;

breakStatement : BREAK SEMICOLON;

returnStatement : RETURN (expression | literal)? SEMICOLON;

literal : INTEGER
        | FLOAT
        | STRING
        | TRUE
        | FALSE
        | NULL;

ifStatement : IF LPAREN logicalExpression RPAREN LBRACE statements RBRACE (ELSE LBRACE statements RBRACE)?;

forLoopStatement : FOR LPAREN forLoopVariable SEMICOLON oneLogicalExpression SEMICOLON forLoopVariable RPAREN LBRACE statements RBRACE;

forLoopVariable : ((INTEGER_TOKEN | FLOAT_TOKEN | STRING_TOKEN) IDENTIFIER (ASSIGN expression)? | IDENTIFIER ASSIGN expression | (IDENTIFIER INCREMENT | INCREMENT IDENTIFIER) | (IDENTIFIER DECREMENT | DECREMENT IDENTIFIER));

whileLoopStatement : WHILE LPAREN oneLogicalExpression RPAREN LBRACE statements RBRACE;

assignmentStatement : IDENTIFIER ASSIGN expression SEMICOLON;

incrementStatement : (IDENTIFIER INCREMENT | INCREMENT IDENTIFIER) SEMICOLON;

decrementStatement : (IDENTIFIER DECREMENT | DECREMENT IDENTIFIER) SEMICOLON;

expression : (additiveExpression | multiplicativeExpression | primaryExpression);

additiveExpression : multiplicativeExpression ((PLUS | MINUS) multiplicativeExpression)*;

multiplicativeExpression : primaryExpression ((MULT | DIV) primaryExpression)*;

primaryExpression : (INTEGER | FLOAT | STRING | methodCalling | fieldAccessing | IDENTIFIER );

logicalExpression : (oneLogicalExpression ((AND | OR) oneLogicalExpression)*);

oneLogicalExpression : (expression (LESS | EQUAL | GREATER | GREATER_EQUAL | LESS_EQUAL) expression) | TRUE | FALSE;

arrayDefinition : (INTEGER_TOKEN | FLOAT_TOKEN | STRING_TOKEN | DOUBLE) LSQUARE RSQUARE IDENTIFIER (ASSIGN) NEW (INTEGER_TOKEN | FLOAT_TOKEN | STRING_TOKEN | DOUBLE) LSQUARE expression RSQUARE SEMICOLON?;

listDefinition : ARRAY_LIST LESS (INTEGERB | DOUBLEB | FLOATB | LONGB | SHORTB | BYTEB | CHARACTERB | BOOLEANB) GREATER IDENTIFIER (ASSIGN NEW ARRAY_LIST LESS GREATER LPAREN RPAREN)? SEMICOLON;

listAddDefinition : IDENTIFIER DOT ADD LPAREN expression RPAREN SEMICOLON;

objectCreating : IDENTIFIER IDENTIFIER (ASSIGN NEW IDENTIFIER LPAREN parameters RPAREN)? SEMICOLON;
