# Generated from java_babilon_parser.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .java_babilon_parser import java_babilon_parser
else:
    from java_babilon_parser import java_babilon_parser

# This class defines a complete listener for a parse tree produced by java_babilon_parser.
class java_babilon_parserListener(ParseTreeListener):

    def __init__(self):
        self.params = []
        self.mainFunc = ""
        self.ifMainFunc = ""
        self.python_code = ""
        self.paramsDefinition = []
        self.fields = []
        self.statements = []
        self.expressions = []
        self.indentation_level = 0
        self.indentation = ""  # Inicjalizacja wcięcia jako pustego ciągu

    def increase_indent(self):
        self.indentation_level += 1
        #self.indentation += "    "  # Dodaj 4 spacje dla każdego poziomu wcięcia

    def decrease_indent(self):
        if self.indentation_level > 0:
            self.indentation_level -= 1

    def get_indent(self):
        return " " * (self.indentation_level * 4)



    #DZIALA
    # Enter a parse tree produced by java_babilon_parser#program.
    def enterProgram(self, ctx:java_babilon_parser.ProgramContext):
        pass

    # Exit a parse tree produced by java_babilon_parser#program.
    def exitProgram(self, ctx:java_babilon_parser.ProgramContext):
        pass



    #DZIALA
    # Enter a parse tree produced by java_babilon_parser#classDeclaration.
    def enterClassDeclaration(self, ctx:java_babilon_parser.ClassDeclarationContext):
        self.fields = []
        if ctx.EXTENDS():
            self.python_code += f"\nclass({ctx.IDENTIFIER()[1].getText()}): \n"
        else:
            self.python_code += "\nclass " + ctx.IDENTIFIER()[0].getText() + ":\n"
        self.increase_indent()

    # Exit a parse tree produced by java_babilon_parser#classDeclaration.
    def exitClassDeclaration(self, ctx:java_babilon_parser.ClassDeclarationContext):
        if self.fields:
            self.python_code += "\n" + self.get_indent() + "def __init__(self):\n"
            self.increase_indent()
            tabs = "\n" + self.get_indent()
            self.python_code += self.get_indent() + tabs.join(self.fields)
        self.decrease_indent()



    #DZIALA
    # Enter a parse tree produced by java_babilon_parser#classBody.
    def enterClassBody(self, ctx:java_babilon_parser.ClassBodyContext):
        pass

    # Exit a parse tree produced by java_babilon_parser#classBody.
    def exitClassBody(self, ctx:java_babilon_parser.ClassBodyContext):
        pass



    #DZIALA
    # Enter a parse tree produced by java_babilon_parser#importStatement.
    def enterImportStatement(self, ctx:java_babilon_parser.ImportStatementContext):
        if ctx.ARRAY_LIST():
            self.python_code += "import numpy as np\n"
        else:
            self.python_code += "import " + ctx.IDENTIFIER()[0].getText() + "\n"

    # Exit a parse tree produced by java_babilon_parser#importStatement.
    def exitImportStatement(self, ctx:java_babilon_parser.ImportStatementContext):
        pass



    #DZIALA
    # Enter a parse tree produced by java_babilon_parser#mainMethod.
    def enterMainMethod(self, ctx:java_babilon_parser.MainMethodContext):
        self.ifMainFunc = True
        self.mainFunc += "def main():"

    # Exit a parse tree produced by java_babilon_parser#mainMethod.
    def exitMainMethod(self, ctx:java_babilon_parser.MainMethodContext):
        pass



    #DZIALA
    # Enter a parse tree produced by java_babilon_parser#methodDefinition.
    def enterMethodDefinition(self, ctx:java_babilon_parser.MethodDefinitionContext):
        self.increase_indent()
        if ctx.PRIVATE():
            self.python_code += f"\n\tdef __{ctx.IDENTIFIER().getText()}("
        else:
            self.python_code += f"\n\tdef {ctx.IDENTIFIER().getText()}("

    # Exit a parse tree produced by java_babilon_parser#methodDefinition.
    def exitMethodDefinition(self, ctx:java_babilon_parser.MethodDefinitionContext):
        self.decrease_indent()



    #DZIALA
    # Enter a parse tree produced by java_babilon_parser#parameters.
    def enterParameters(self, ctx:java_babilon_parser.ParametersContext):
        self.python_code += ctx.getText()

    # Exit a parse tree produced by java_babilon_parser#parameters.
    def exitParameters(self, ctx:java_babilon_parser.ParametersContext):
        pass



    #DZIALA
    # Enter a parse tree produced by java_babilon_parser#parametersDefinition.
    def enterParametersDefinition(self, ctx:java_babilon_parser.ParametersDefinitionContext):
        self.paramsDefinition = []
        if ctx.oneParameterDefinition():
            self.python_code += "self, "
        else:
            self.python_code += "self"

    # Exit a parse tree produced by java_babilon_parser#parametersDefinition.
    def exitParametersDefinition(self, ctx:java_babilon_parser.ParametersDefinitionContext):
        self.python_code += ", ".join(self.paramsDefinition) + "):\n"


    #DZIALA
    # Enter a parse tree produced by java_babilon_parser#listParemeter.
    def enterListParemeter(self, ctx:java_babilon_parser.ListParemeterContext):
        #nie trzeba nic uzupełniać, działa
        pass

    # Exit a parse tree produced by java_babilon_parser#listParemeter.
    def exitListParemeter(self, ctx:java_babilon_parser.ListParemeterContext):
        pass



    #DZIALA
    # Enter a parse tree produced by java_babilon_parser#oneParameterDefinition.
    def enterOneParameterDefinition(self, ctx:java_babilon_parser.OneParameterDefinitionContext):
        self.paramsDefinition.append(ctx.IDENTIFIER().getText())

    # Exit a parse tree produced by java_babilon_parser#oneParameterDefinition.
    def exitOneParameterDefinition(self, ctx:java_babilon_parser.OneParameterDefinitionContext):
        pass



    #DZIALA
    # Enter a parse tree produced by java_babilon_parser#fieldDefinition.
    def enterFieldDefinition(self, ctx:java_babilon_parser.FieldDefinitionContext):
        if ctx.PRIVATE():
            if ctx.ASSIGN():
                self.fields.append("__" + ctx.IDENTIFIER().getText() + " = " + ctx.expression().getText())
            else:
                self.fields.append("__" + ctx.IDENTIFIER().getText() + " = None")
        else:
            if ctx.ASSIGN():
                self.fields.append(ctx.IDENTIFIER().getText() + " = " + ctx.expression().getText())
            else:
                self.fields.append(ctx.IDENTIFIER().getText() + " = None")

    # Exit a parse tree produced by java_babilon_parser#fieldDefinition.
    def exitFieldDefinition(self, ctx:java_babilon_parser.FieldDefinitionContext):
        pass



    #DZIALA
    # Enter a parse tree produced by java_babilon_parser#variableDefinition.
    def enterVariableDefinition(self, ctx:java_babilon_parser.VariableDefinitionContext):
        variable_name = ctx.IDENTIFIER().getText()
        expression_ctx = ctx.expression()

        if expression_ctx is not None:
            variable_value = expression_ctx.getText()
            self.python_code += self.get_indent() + f"{variable_name} = {variable_value}\n"
        else:
            self.python_code += self.get_indent() + f"{variable_name} = None\n"

    # Exit a parse tree produced by java_babilon_parser#variableDefinition.
    def exitVariableDefinition(self, ctx:java_babilon_parser.VariableDefinitionContext):
        pass



    #DZIALA
    # Enter a parse tree produced by java_babilon_parser#methodCalling.
    def enterMethodCalling(self, ctx:java_babilon_parser.MethodCallingContext):
        if ctx.parentCtx.methodCalling():
            self.python_code += self.get_indent() + "self." + ctx.IDENTIFIER().getText() + "("

    # Exit a parse tree produced by java_babilon_parser#methodCalling.
    def exitMethodCalling(self, ctx:java_babilon_parser.MethodCallingContext):
        self.python_code += ")\n"



    #TODO nie wiem czy nie trzeba będzie zmienić w gramatyce czegoś z deklarowaniem zmiennej żeby to poprawnie działo
    # Enter a parse tree produced by java_babilon_parser#fieldAccessing.
    def enterFieldAccessing(self, ctx:java_babilon_parser.FieldAccessingContext):
        # variable = ctx.IDENTIFIER(0)
        # variable2 = ctx.IDENTIFIER(-1)
        # field =ctx.IDENTIFIER(1)
        # self.python_code += self.get_indent() + f"{variable2} = {variable}.{field}\n"
        pass

    # Exit a parse tree produced by java_babilon_parser#fieldAccessing.
    def exitFieldAccessing(self, ctx:java_babilon_parser.FieldAccessingContext):
        pass



    #DZIALA
    # Enter a parse tree produced by java_babilon_parser#statements.
    def enterStatements(self, ctx:java_babilon_parser.StatementsContext):
        pass

    # Exit a parse tree produced by java_babilon_parser#statements.
    def exitStatements(self, ctx:java_babilon_parser.StatementsContext):
        pass



    #DZIALA
    # Enter a parse tree produced by java_babilon_parser#statement.
    def enterStatement(self, ctx:java_babilon_parser.StatementContext):
        pass

    # Exit a parse tree produced by java_babilon_parser#statement.
    def exitStatement(self, ctx:java_babilon_parser.StatementContext):
        pass



    #DZIALA
    # Enter a parse tree produced by java_babilon_parser#printStatement.
    def enterPrintStatement(self, ctx:java_babilon_parser.PrintStatementContext):
        # Pobierz treść do wydrukowania
        print_content = ctx.expression().getText()
        self.python_code += self.get_indent() + f"print({print_content})\n"

    # Exit a parse tree produced by java_babilon_parser#printStatement.
    def exitPrintStatement(self, ctx:java_babilon_parser.PrintStatementContext):
        pass



    #DZIALA
    # Enter a parse tree produced by java_babilon_parser#doWhileStatement.
    def enterDoWhileStatement(self, ctx:java_babilon_parser.DoWhileStatementContext):
        self.python_code += self.get_indent() + f"while True:\n"
        self.increase_indent()

    # Exit a parse tree produced by java_babilon_parser#doWhileStatement.
    def exitDoWhileStatement(self, ctx:java_babilon_parser.DoWhileStatementContext):
        self.decrease_indent()



    #DZIALA
    # Enter a parse tree produced by java_babilon_parser#continueStatement.
    def enterContinueStatement(self, ctx:java_babilon_parser.ContinueStatementContext):
        self.python_code += self.get_indent() + f"continue\n"

    # Exit a parse tree produced by java_babilon_parser#continueStatement.
    def exitContinueStatement(self, ctx:java_babilon_parser.ContinueStatementContext):
        self.decrease_indent()



    #DZIALA
    # Enter a parse tree produced by java_babilon_parser#breakStatement.
    def enterBreakStatement(self, ctx:java_babilon_parser.BreakStatementContext):
        self.python_code += self.get_indent() + f"break\n"

    # Exit a parse tree produced by java_babilon_parser#breakStatement.
    def exitBreakStatement(self, ctx:java_babilon_parser.BreakStatementContext):
        self.decrease_indent()



    #DZIALA
    # Enter a parse tree produced by java_babilon_parser#returnStatement.
    def enterReturnStatement(self, ctx:java_babilon_parser.ReturnStatementContext):
        value = ctx.expression().getText()
        self.python_code += self.get_indent() + f"return {value}\n"

    # Exit a parse tree produced by java_babilon_parser#returnStatement.
    def exitReturnStatement(self, ctx:java_babilon_parser.ReturnStatementContext):
        pass



    #DZIALA
    # Enter a parse tree produced by java_babilon_parser#literal.
    def enterLiteral(self, ctx:java_babilon_parser.LiteralContext):
        pass

    # Exit a parse tree produced by java_babilon_parser#literal.
    def exitLiteral(self, ctx:java_babilon_parser.LiteralContext):
        pass



    #DZIALA
    # Enter a parse tree produced by java_babilon_parser#ifStatement.
    def enterIfStatement(self, ctx:java_babilon_parser.IfStatementContext):
        condition_text = ctx.logicalExpression().getText()
        self.python_code += self.get_indent() + "if " + condition_text + ":\n"
        self.increase_indent()

    def constructConditionText(self, logical_expression):
        # Sprawdź, czy logical_expression jest pustą listą
        if not logical_expression:
            return ""

        # Sprawdź, czy logical_expression jest już gotowym warunkiem
        if isinstance(logical_expression, str):
            return logical_expression

        # Sprawdź, czy logical_expression zawiera więcej niż trzy elementy
        if len(logical_expression) > 3:
            raise ValueError("Logical expression should contain at most three elements.")

        # Wyciągnij lewą, operatora i prawą wartość z logical_expression
        left_expression, operator, right_expression = logical_expression

        # Skonstruuj tekst warunku
        condition_text = f"{left_expression} {operator} {right_expression}"

        return condition_text

    # Exit a parse tree produced by java_babilon_parser#ifStatement.
    def exitIfStatement(self, ctx:java_babilon_parser.IfStatementContext):
        self.decrease_indent()



    #DZIALA
    # Enter a parse tree produced by java_babilon_parser#elseStatement.
    def enterElseStatement(self, ctx:java_babilon_parser.ElseStatementContext):
        self.python_code += f"\t\telse:\n"
        pass

    # Exit a parse tree produced by java_babilon_parser#elseStatement.
    def exitElseStatement(self, ctx:java_babilon_parser.ElseStatementContext):
        self.decrease_indent()
        pass



    #DZIALA
    # Enter a parse tree produced by java_babilon_parser#forLoopStatement.
    def enterForLoopStatement(self, ctx:java_babilon_parser.ForLoopStatementContext):
        loop_variable_ctx = ctx.forLoopVariable(0)
        loop_variable = self.enterForLoopVariable(loop_variable_ctx)

        step_variable_ctx = ctx.forLoopVariable(1)
        step_variable = self.getStepValue(step_variable_ctx)

        logical_expression_ctx = ctx.oneLogicalExpression()
        loop_range = self.enterOneLogicalExpression(logical_expression_ctx)

        self.python_code += self.get_indent() + f"for {loop_variable[0]} in range({loop_range[2]}):\n"
        self.increase_indent()
        pass

    # Exit a parse tree produced by java_babilon_parser#forLoopStatement.
    def exitForLoopStatement(self, ctx:java_babilon_parser.ForLoopStatementContext):
        self.decrease_indent()
        pass



    #PETLA DZIALA
    # Enter a parse tree produced by java_babilon_parser#forLoopVariable.
    def enterForLoopVariable(self, ctx:java_babilon_parser.ForLoopVariableContext):
        if ctx.IDENTIFIER():
            if ctx.expression():
                initial_value = ctx.expression().getText()
                return (ctx.IDENTIFIER().getText(), initial_value)
        else:
            return (ctx.getChildren()[1].getText(), ctx.getChildren()[3].getText())

    # Exit a parse tree produced by java_babilon_parser#forLoopVariable.
    def exitForLoopVariable(self, ctx:java_babilon_parser.ForLoopVariableContext):
        pass

    # metoda pomocnicza do pobierania wartosci kroku w petli for
    def getStepValue(self, ctx: java_babilon_parser.ForLoopVariableContext):
        # Wydobycie wartości kroku pętli
        if ctx.getChildCount() == 2 and ctx.getChild(1).getText() == '++':
            return 1
        elif ctx.getChildCount() == 2 and ctx.getChild(1).getText() == '--':
            return -1
        elif ctx.getChildCount() == 3 and ctx.getChild(1).getText() == '=':
            step_value = ctx.getChild(2).additiveExpression().multiplicativeExpression()[1].getText()
            step_string = ctx.getChild(2).getText()
            if "+" in step_string:
                return step_value
            elif "-" in step_string:
                return "-" + step_value
            else:
                return step_value
        return 1



    #DZIALA
    # Enter a parse tree produced by java_babilon_parser#whileLoopStatement.
    def enterWhileLoopStatement(self, ctx:java_babilon_parser.WhileLoopStatementContext):
        # Pobranie treści instrukcji warunkowej
        condition_text = ctx.oneLogicalExpression().getText()

        self.python_code += "\twhile " + condition_text + ":\n"

    # Exit a parse tree produced by java_babilon_parser#whileLoopStatement.
    def exitWhileLoopStatement(self, ctx:java_babilon_parser.WhileLoopStatementContext):
        pass



    #DZIALA
    # Enter a parse tree produced by java_babilon_parser#assignmentStatement.
    def enterAssignmentStatement(self, ctx:java_babilon_parser.AssignmentStatementContext):
        variable_name = ctx.IDENTIFIER().getText()
        expression_ctx = ctx.expression().getText()
        self.python_code += f"\t\t{variable_name} = {expression_ctx}\n"
        pass

    # Exit a parse tree produced by java_babilon_parser#assignmentStatement.
    def exitAssignmentStatement(self, ctx:java_babilon_parser.AssignmentStatementContext):
        pass



    #DZIALA
    # Enter a parse tree produced by java_babilon_parser#incrementStatement.
    def enterIncrementStatement(self, ctx:java_babilon_parser.IncrementStatementContext):
        variable_name = ctx.IDENTIFIER().getText()

        self.python_code += self.get_indent() + f"{variable_name}+=1\n"


    # Exit a parse tree produced by java_babilon_parser#incrementStatement.
    def exitIncrementStatement(self, ctx:java_babilon_parser.IncrementStatementContext):
        pass



    #DZIALA
    # Enter a parse tree produced by java_babilon_parser#decrementStatement.
    def enterDecrementStatement(self, ctx:java_babilon_parser.DecrementStatementContext):
        variable_name = ctx.IDENTIFIER().getText()
        self.python_code += self.get_indent() + f"{variable_name}-=1\n"

    # Exit a parse tree produced by java_babilon_parser#decrementStatement.
    def exitDecrementStatement(self, ctx:java_babilon_parser.DecrementStatementContext):
        pass



    #DZIALA
    # Enter a parse tree produced by java_babilon_parser#expression.
    def enterExpression(self, ctx:java_babilon_parser.ExpressionContext):
        pass

    # Exit a parse tree produced by java_babilon_parser#expression.
    def exitExpression(self, ctx:java_babilon_parser.ExpressionContext):
        pass



    #DZIALA
    # Enter a parse tree produced by java_babilon_parser#additiveExpression.
    def enterAdditiveExpression(self, ctx:java_babilon_parser.AdditiveExpressionContext):
        pass

    # Exit a parse tree produced by java_babilon_parser#additiveExpression.
    def exitAdditiveExpression(self, ctx:java_babilon_parser.AdditiveExpressionContext):
        pass



    #DZIALA
    # Enter a parse tree produced by java_babilon_parser#multiplicativeExpression.
    def enterMultiplicativeExpression(self, ctx:java_babilon_parser.MultiplicativeExpressionContext):
        pass

    # Exit a parse tree produced by java_babilon_parser#multiplicativeExpression.
    def exitMultiplicativeExpression(self, ctx:java_babilon_parser.MultiplicativeExpressionContext):
        pass



    #DZIALA
    # Enter a parse tree produced by java_babilon_parser#primaryExpression.
    def enterPrimaryExpression(self, ctx:java_babilon_parser.PrimaryExpressionContext):
        pass

    # Exit a parse tree produced by java_babilon_parser#primaryExpression.
    def exitPrimaryExpression(self, ctx:java_babilon_parser.PrimaryExpressionContext):
        pass



    #TODO nie wykrywa operatora nie wiem czemu
    # Enter a parse tree produced by java_babilon_parser#logicalExpression.
    def enterLogicalExpression(self, ctx:java_babilon_parser.LogicalExpressionContext):

        logical1_ctx = ctx.oneLogicalExpression(0).getText()
        logical2_ctx = ctx.oneLogicalExpression(1).getText()


        # Determine the logical operator
        if ctx.OR() is not None:
            operator = "or"
        else:
            operator = "and"


        # Construct the logical expression
        logical = self.get_indent() + f"{logical1_ctx} {operator} {logical2_ctx}\n"
        return logical
        pass

    # Exit a parse tree produced by java_babilon_parser#logicalExpression.
    def exitLogicalExpression(self, ctx:java_babilon_parser.LogicalExpressionContext):
        pass

    #DZIALA
    # Enter a parse tree produced by java_babilon_parser#oneLogicalExpression.
    def enterOneLogicalExpression(self, ctx:java_babilon_parser.OneLogicalExpressionContext):
        # Pobierz lewe i prawe wyrażenie z kontekstu
        left_expression = ctx.expression(0).getText()
        right_expression = ctx.expression(1).getText()

        # Pobierz operator logiczny z kontekstu
        operator = ctx.getChild(1).getText()

        # Skonstruuj wyrażenie logiczne
        logical_expression = (left_expression, operator, right_expression)
        return logical_expression

    # Exit a parse tree produced by java_babilon_parser#oneLogicalExpression.
    def exitOneLogicalExpression(self, ctx:java_babilon_parser.OneLogicalExpressionContext):
        pass



    #DZIALA
    # Enter a parse tree produced by java_babilon_parser#arrayDefinition.
    def enterArrayDefinition(self, ctx:java_babilon_parser.ArrayDefinitionContext):
        variable_name = ctx.IDENTIFIER().getText()
        size = ctx.expression().getText()

        # Dodaj linię kodu definicji tablicy do kodu Pythona
        if size:
            self.python_code += self.get_indent() + f"{variable_name} = [0] * {size}\n"
        else:
            self.python_code += self.get_indent() + f"{variable_name} = []\n"

    # Exit a parse tree produced by java_babilon_parser#arrayDefinition.
    def exitArrayDefinition(self, ctx:java_babilon_parser.ArrayDefinitionContext):
        pass



    #DZIALA
    # Enter a parse tree produced by java_babilon_parser#listDefinition.
    def enterListDefinition(self, ctx:java_babilon_parser.ListDefinitionContext):
        variable_name = ctx.IDENTIFIER().getText()
        self.python_code += self.get_indent() + f"{variable_name} = []\n"

    # Exit a parse tree produced by java_babilon_parser#listDefinition.
    def exitListDefinition(self, ctx:java_babilon_parser.ListDefinitionContext):
        pass



    #DZIALA
    # Enter a parse tree produced by java_babilon_parser#listAddDefinition.
    def enterListAddDefinition(self, ctx:java_babilon_parser.ListAddDefinitionContext):
        variable_name = ctx.IDENTIFIER().getText()
        value = ctx.expression().getText()
        self.python_code += self.get_indent() + f"{variable_name}.append({value})\n"

    # Exit a parse tree produced by java_babilon_parser#listAddDefinition.
    def exitListAddDefinition(self, ctx:java_babilon_parser.ListAddDefinitionContext):
        pass



    #DZIALA
    # Enter a parse tree produced by java_babilon_parser#objectCreating.
    def enterObjectCreating(self, ctx:java_babilon_parser.ObjectCreatingContext):
        variable_name = ctx.IDENTIFIER(1).getText()
        # Pobierz nazwę klasy (dla której tworzymy obiekt)
        class_name = ctx.IDENTIFIER(0).getText()
        # Pobierz parametry konstruktora
        parameters = ctx.parameters().getText()
        # Konwertuj tworzenie obiektu z Javy na Pythona
        self.python_code += self.get_indent() + f"{variable_name} = {class_name}({parameters})\n"
        pass

    # Exit a parse tree produced by java_babilon_parser#objectCreating.
    def exitObjectCreating(self, ctx:java_babilon_parser.ObjectCreatingContext):
        pass





