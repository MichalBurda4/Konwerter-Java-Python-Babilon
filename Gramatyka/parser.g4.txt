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



