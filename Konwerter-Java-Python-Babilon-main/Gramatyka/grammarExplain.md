# Opis  Gramatyki (pliku grammar.g4)

## Parser Rules:
#### program:
Składa się z jednej lub więcej deklaracji klas.
####  classDeclaration:
Definicja klasy, która może zaczynać się od PRIVATE lub PUBLIC (opcjonalnie), a następnie zawiera słowo kluczowe class, nazwę klasy (IDENTIFIER), ciało klasy (classBody) między nawiasami klamrowymi.
####  classBody:
Zawiera definicje metod (methodDefinition) lub pól (fieldDefinition) klasy.
####  methodDefinition:
Definicja metody, która składa się z modyfikatora dostępu (PUBLIC lub PRIVATE), typu zwracanego (INTEGER_TOKEN, FLOAT_TOKEN, STRING_TOKEN, VOID), nazwy metody (IDENTIFIER), listy parametrów  (parametersDefinition) w nawiasach okrągłych oraz ciała metody (statements) między nawiasami klamrowymi.
####  parametersDefinition:
Lista definicji parametrów metody, gdzie każdy parametr składa się z typu (INTEGER_TOKEN, FLOAT_TOKEN, STRING_TOKEN) i nazwy (IDENTIFIER).
####  fieldDefinition:
Definicja pola klasy, składająca się z modyfikatora dostępu (PUBLIC lub PRIVATE), typu pola (INTEGER_TOKEN, FLOAT_TOKEN, STRING_TOKEN), nazwy pola (IDENTIFIER) i opcjonalnej inicjalizacji (ASSIGN expression SEMICOLON).
####  variableDefinition:
Definicja zmiennej lokalnej, która może być używana w ciele metody. Składa się z typu (INTEGER_TOKEN, FLOAT_TOKEN, STRING_TOKEN), nazwy (IDENTIFIER) i opcjonalnej inicjalizacji (ASSIGN expression) przed średnikiem (SEMICOLON).
####  methodCalling:
Wywołanie metody, gdzie używana jest nazwa metody (IDENTIFIER), lista argumentów (parameters) w nawiasach okrągłych i zakończenie średnikiem.
####  statements:
Lista instrukcji w ciele metody.
####  statement:
Poszczególne instrukcje, takie jak ifStatement, assignmentStatement, variableDefinition lub methodCalling.
#### ifStatement:
Instrukcja warunkowa if z opcjonalnym blokiem else.
#### assignmentStatement:
Instrukcja przypisania, gdzie IDENTIFIER jest przypisywany wartości (expression) za pomocą operatora ASSIGN.
#### expression:
Wyrażenie arytmetyczne lub logiczne.
#### additiveExpression:
Wyrażenie arytmetyczne składające się z dodawania (PLUS) lub odejmowania (MINUS) wyrażeń mnożenia (multiplicativeExpression).
#### multiplicativeExpression:
Wyrażenie arytmetyczne składające się z mnożenia (MULT) lub dzielenia (DIV) podstawowych wyrażeń (primaryExpression).
#### logicalExpression:
Wyrażenie logiczne, które łączy różne wyrażenia logiczne za pomocą operatorów logicznych AND lub OR.
#### oneLogicalExpression:
Jedno wyrażenie logiczne, które składa się z wyrażeń (expression) i operatorów porównania (LESS, EQUAL, GREATHER).
#### primaryExpression:
Podstawowe wyrażenie, które może być liczbą całkowitą (INTEGER), liczbą zmiennoprzecinkową (FLOAT), łańcuchem znaków (STRING), wywołaniem metody (methodCalling) lub identyfikatorem (IDENTIFIER).


Ta gramatyka parsera umożliwia analizę i parsowanie prostych konstrukcji języka Java, takich jak deklaracje klas, definicje metod, instrukcje warunkowe, przypisania, wywołania metod oraz wyrażeń arytmetycznych i logicznych.





