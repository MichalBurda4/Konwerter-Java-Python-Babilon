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
        self.indentation_level_main = 0

    def increase_indent(self):
        self.indentation_level += 1

    def decrease_indent(self):
        if self.indentation_level > 0:
            self.indentation_level -= 1

    def get_indent(self):
        return " " * (self.indentation_level * 4)

    def increase_indent_main(self):
        self.indentation_level_main += 1

    def decrease_indent_main(self):
        if self.indentation_level_main > 0:
            self.indentation_level_main -= 1

    def get_indent_main(self):
        return " " * (self.indentation_level_main * 4)

    # Enter a parse tree produced by java_babilon_parser#program.
    def enterProgram(self, ctx: java_babilon_parser.ProgramContext):
        pass

    # Exit a parse tree produced by java_babilon_parser#program.
    def exitProgram(self, ctx: java_babilon_parser.ProgramContext):
        self.python_code += self.mainFunc + "\n"
        self.python_code += "if __name__ == " + "\"__main__\":\n"
        self.increase_indent()
        self.python_code += self.get_indent() + "main()"

    # Enter a parse tree produced by java_babilon_parser#classDeclaration.
    def enterClassDeclaration(self, ctx: java_babilon_parser.ClassDeclarationContext):
        self.fields = []
        if ctx.EXTENDS():
            self.python_code += f"\nclass({ctx.IDENTIFIER()[1].getText()}): \n"
        else:
            self.python_code += "\nclass " + ctx.IDENTIFIER()[0].getText() + ":\n"
        self.increase_indent()

    # Exit a parse tree produced by java_babilon_parser#classDeclaration.
    def exitClassDeclaration(self, ctx: java_babilon_parser.ClassDeclarationContext):
        if self.fields:
            self.python_code += "\n" + self.get_indent() + "def __init__(self):\n"
            self.increase_indent()
            tabs = "\n" + self.get_indent()
            self.python_code += self.get_indent() + tabs.join(self.fields)
        self.decrease_indent()

    # Enter a parse tree produced by java_babilon_parser#classBody.
    def enterClassBody(self, ctx: java_babilon_parser.ClassBodyContext):
        pass

    # Exit a parse tree produced by java_babilon_parser#classBody.
    def exitClassBody(self, ctx: java_babilon_parser.ClassBodyContext):
        pass

    # Enter a parse tree produced by java_babilon_parser#importStatement.
    def enterImportStatement(self, ctx: java_babilon_parser.ImportStatementContext):
        if ctx.ARRAY_LIST():
            self.python_code += "import numpy as np\n"
        else:
            self.python_code += "import " + ctx.IDENTIFIER()[0].getText() + "\n"

    # Exit a parse tree produced by java_babilon_parser#importStatement.
    def exitImportStatement(self, ctx: java_babilon_parser.ImportStatementContext):
        pass

    # Enter a parse tree produced by java_babilon_parser#mainMethod.
    def enterMainMethod(self, ctx: java_babilon_parser.MainMethodContext):
        self.ifMainFunc = True
        self.mainFunc += "\ndef main():\n"
        self.increase_indent_main()


    # Exit a parse tree produced by java_babilon_parser#mainMethod.
    def exitMainMethod(self, ctx: java_babilon_parser.MainMethodContext):
        self.ifMainFunc = False
        self.decrease_indent_main()

    # Enter a parse tree produced by java_babilon_parser#methodDefinition.
    def enterMethodDefinition(self, ctx: java_babilon_parser.MethodDefinitionContext):
        if ctx.STATIC():
            self.python_code += "\n" + self.get_indent() + "@staticmethod"
        if ctx.PRIVATE():
            # tutaj usunalem z nazwy metody "__" bo byly problemy dalej a to i tak nic nie dawalo
            self.python_code += "\n" + self.get_indent() + f"def {ctx.IDENTIFIER().getText()}("
        else:
            self.python_code += "\n" + self.get_indent() + f"def {ctx.IDENTIFIER().getText()}("
        self.increase_indent()

    # Exit a parse tree produced by java_babilon_parser#methodDefinition.
    def exitMethodDefinition(self, ctx: java_babilon_parser.MethodDefinitionContext):
        self.decrease_indent()

    # Enter a parse tree produced by java_babilon_parser#parameters.
    def enterParameters(self, ctx: java_babilon_parser.ParametersContext):
        if self.ifMainFunc:
            self.mainFunc += ctx.getText()
        else:
            self.python_code += ctx.getText()

    # Exit a parse tree produced by java_babilon_parser#parameters.
    def exitParameters(self, ctx: java_babilon_parser.ParametersContext):
        pass

    # Enter a parse tree produced by java_babilon_parser#parametersDefinition.
    def enterParametersDefinition(self, ctx: java_babilon_parser.ParametersDefinitionContext):
        self.paramsDefinition = []
        if ctx.parentCtx.STATIC():
            return
        if ctx.oneParameterDefinition():
            self.python_code += "self, "
        else:
            self.python_code += "self"

    # Exit a parse tree produced by java_babilon_parser#parametersDefinition.
    def exitParametersDefinition(self, ctx: java_babilon_parser.ParametersDefinitionContext):
        self.python_code += ", ".join(self.paramsDefinition) + "):\n"

    # Enter a parse tree produced by java_babilon_parser#listParemeter.
    def enterListParemeter(self, ctx: java_babilon_parser.ListParemeterContext):
        pass

    # Exit a parse tree produced by java_babilon_parser#listParemeter.
    def exitListParemeter(self, ctx: java_babilon_parser.ListParemeterContext):
        pass

    # Enter a parse tree produced by java_babilon_parser#oneParameterDefinition.
    def enterOneParameterDefinition(self, ctx: java_babilon_parser.OneParameterDefinitionContext):
        self.paramsDefinition.append(ctx.IDENTIFIER().getText())

    # Exit a parse tree produced by java_babilon_parser#oneParameterDefinition.
    def exitOneParameterDefinition(self, ctx: java_babilon_parser.OneParameterDefinitionContext):
        pass

    # Enter a parse tree produced by java_babilon_parser#fieldDefinition.
    def enterFieldDefinition(self, ctx: java_babilon_parser.FieldDefinitionContext):
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
    def exitFieldDefinition(self, ctx: java_babilon_parser.FieldDefinitionContext):
        pass

    # Enter a parse tree produced by java_babilon_parser#variableDefinition.
    def enterVariableDefinition(self, ctx: java_babilon_parser.VariableDefinitionContext):
        if self.ifMainFunc:
            variable_name = ctx.IDENTIFIER().getText()
            expression_ctx = ctx.expression()
            if expression_ctx is not None:
                variable_value = expression_ctx.getText()
                if variable_value == "true":
                    self.mainFunc += self.get_indent_main() + f"{variable_name} = True\n"
                elif variable_value == "false":
                    self.mainFunc += self.get_indent_main() + f"{variable_name} = False\n"
                elif ".length" in variable_value or ".size()" in variable_value:
                    array_len = f"len({ctx.expression().additiveExpression().multiplicativeExpression(0).primaryExpression(0).fieldAccessing().IDENTIFIER(0).getText()})"
                    self.mainFunc += self.get_indent_main() + f"{variable_name} = {array_len}\n"
                else:
                    if ctx.INTEGER_TOKEN():
                        self.mainFunc += self.get_indent_main() + f"{variable_name} = int({variable_value})\n"
                    else:
                        self.mainFunc += self.get_indent_main() + f"{variable_name} = {variable_value}\n"
            else:
                self.mainFunc += self.get_indent_main() + f"{variable_name} = None\n"
        else:
            variable_name = ctx.IDENTIFIER().getText()
            expression_ctx = ctx.expression()
            if expression_ctx is not None:
                variable_value = expression_ctx.getText()
                if variable_value == "true":
                    self.python_code += self.get_indent() + f"{variable_name} = True\n"
                elif variable_value == "false":
                    self.python_code += self.get_indent() + f"{variable_name} = False\n"
                if ".length" in variable_value or ".size()" in variable_value:
                    array_len = f"len({ctx.expression().additiveExpression().multiplicativeExpression(0).primaryExpression(0).fieldAccessing().IDENTIFIER(0).getText()})"
                    self.python_code += self.get_indent() + f"{variable_name} = {array_len}\n"
                else:
                    if ctx.INTEGER_TOKEN():
                        self.python_code += self.get_indent() + f"{variable_name} = int({variable_value})\n"
                    else:
                        self.python_code += self.get_indent() + f"{variable_name} = {variable_value}\n"
            else:
                self.python_code += self.get_indent() + f"{variable_name} = None\n"

    # Exit a parse tree produced by java_babilon_parser#variableDefinition.
    def exitVariableDefinition(self, ctx: java_babilon_parser.VariableDefinitionContext):
        pass

    # Enter a parse tree produced by java_babilon_parser#methodCalling.
    def enterMethodCalling(self, ctx: java_babilon_parser.MethodCallingContext):
        if self.ifMainFunc:
            parent_class_ctx = ctx
            parent_class_body_ctx = ctx
            while parent_class_ctx and not isinstance(parent_class_ctx, java_babilon_parser.ClassDeclarationContext):
                parent_class_ctx = parent_class_ctx.parentCtx
            while parent_class_body_ctx and not isinstance(parent_class_body_ctx, java_babilon_parser.ClassBodyContext):
                parent_class_body_ctx = parent_class_body_ctx.parentCtx

            if parent_class_ctx and ctx.IDENTIFIER():
                method_name = ctx.IDENTIFIER(0).getText()
                method_static = self.is_static_method(parent_class_body_ctx, method_name)
                if method_static:
                    className = parent_class_ctx.IDENTIFIER()[0].getText()
                    self.mainFunc += self.get_indent_main() + f"{className}." + method_name + "("
                else:
                    instance_name = ctx.IDENTIFIER(0).getText()
                    method_name = ctx.IDENTIFIER(1).getText()
                    self.mainFunc += self.get_indent_main() + f"{instance_name}." + method_name + "("
        else:
            parent_method_ctx = ctx
            while parent_method_ctx and not isinstance(parent_method_ctx, java_babilon_parser.MethodDefinitionContext):
                parent_method_ctx = parent_method_ctx.parentCtx
            if parent_method_ctx and parent_method_ctx.STATIC():
                if parent_method_ctx.parentCtx.parentCtx.IDENTIFIER(0):
                    className = parent_method_ctx.parentCtx.parentCtx.IDENTIFIER(0).getText()
                    self.python_code += self.get_indent() + f"{className}." + ctx.IDENTIFIER(0).getText() + "("
            else:
                self.python_code += self.get_indent() + "self." + ctx.IDENTIFIER().getText() + "("

    # Exit a parse tree produced by java_babilon_parser#methodCalling.
    def exitMethodCalling(self, ctx: java_babilon_parser.MethodCallingContext):
        if self.ifMainFunc:
            self.mainFunc += ")\n"
        else:
            self.python_code += ")\n"

    def is_static_method(self, class_ctx, method_name):
        for method in class_ctx.methodDefinition():
            if method.IDENTIFIER().getText() == method_name and method.STATIC():
                return True
        return False

    def is_private_method(self, class_ctx, method_name):
        for method in class_ctx.methodDefinition():
            if method.IDENTIFIER().getText() == method_name and method.PRIVATE():
                return True
        return False


    # Enter a parse tree produced by java_babilon_parser#fieldAccessing.
    def enterFieldAccessing(self, ctx: java_babilon_parser.FieldAccessingContext):
        pass

    # Exit a parse tree produced by java_babilon_parser#fieldAccessing.
    def exitFieldAccessing(self, ctx: java_babilon_parser.FieldAccessingContext):
        pass

    # Enter a parse tree produced by java_babilon_parser#statements.
    def enterStatements(self, ctx: java_babilon_parser.StatementsContext):
        pass

    # Exit a parse tree produced by java_babilon_parser#statements.
    def exitStatements(self, ctx: java_babilon_parser.StatementsContext):
        pass

    # Enter a parse tree produced by java_babilon_parser#statement.
    def enterStatement(self, ctx: java_babilon_parser.StatementContext):
        pass

    # Exit a parse tree produced by java_babilon_parser#statement.
    def exitStatement(self, ctx: java_babilon_parser.StatementContext):
        pass

    # Enter a parse tree produced by java_babilon_parser#printStatement.
    def enterPrintStatement(self, ctx: java_babilon_parser.PrintStatementContext):
        if self.ifMainFunc:
            print_content = ""
            if ctx.expression():
                print_content = ctx.expression().getText()
            self.mainFunc += self.get_indent_main() + f"print({print_content})\n"
        else:
            print_content = ""
            if ctx.expression():
                print_content = ctx.expression().getText()
            self.python_code += self.get_indent() + f"print({print_content})\n"

    # Exit a parse tree produced by java_babilon_parser#printStatement.
    def exitPrintStatement(self, ctx: java_babilon_parser.PrintStatementContext):
        pass

    # Enter a parse tree produced by java_babilon_parser#doWhileStatement.
    def enterDoWhileStatement(self, ctx: java_babilon_parser.DoWhileStatementContext):
        if self.ifMainFunc:
            self.mainFunc += self.get_indent_main() + f"while True:\n"
            self.increase_indent_main()
        else:
            self.python_code += self.get_indent() + f"while True:\n"
            self.increase_indent()

    # Exit a parse tree produced by java_babilon_parser#doWhileStatement.
    def exitDoWhileStatement(self, ctx: java_babilon_parser.DoWhileStatementContext):
        if self.ifMainFunc:
            self.decrease_indent_main()
        else:
            self.decrease_indent()

    # Enter a parse tree produced by java_babilon_parser#continueStatement.
    def enterContinueStatement(self, ctx: java_babilon_parser.ContinueStatementContext):
        if self.ifMainFunc:
            self.mainFunc += self.get_indent_main() + f"continue\n"
        else:
            self.python_code += self.get_indent() + f"continue\n"

    # Exit a parse tree produced by java_babilon_parser#continueStatement.
    def exitContinueStatement(self, ctx: java_babilon_parser.ContinueStatementContext):
        pass

    # Enter a parse tree produced by java_babilon_parser#breakStatement.
    def enterBreakStatement(self, ctx: java_babilon_parser.BreakStatementContext):
        if self.ifMainFunc:
            self.mainFunc += self.get_indent_main() + f"break\n"
        else:
            self.python_code += self.get_indent() + f"break\n"

    # Exit a parse tree produced by java_babilon_parser#breakStatement.
    def exitBreakStatement(self, ctx: java_babilon_parser.BreakStatementContext):
        pass

    # Enter a parse tree produced by java_babilon_parser#returnStatement.
    def enterReturnStatement(self, ctx: java_babilon_parser.ReturnStatementContext):
        if self.ifMainFunc:
            value = ctx.expression().getText()
            self.mainFunc += self.get_indent_main() + f"return {value}\n"
        else:
            value = ctx.expression().getText()
            self.python_code += self.get_indent() + f"return {value}\n"

    # Exit a parse tree produced by java_babilon_parser#returnStatement.
    def exitReturnStatement(self, ctx: java_babilon_parser.ReturnStatementContext):
        pass

    # Enter a parse tree produced by java_babilon_parser#literal.
    def enterLiteral(self, ctx: java_babilon_parser.LiteralContext):
        pass

    # Exit a parse tree produced by java_babilon_parser#literal.
    def exitLiteral(self, ctx: java_babilon_parser.LiteralContext):
        pass

    # Enter a parse tree produced by java_babilon_parser#ifStatement.
    def enterIfStatement(self, ctx: java_babilon_parser.IfStatementContext):
        if self.ifMainFunc:
            self.mainFunc += self.get_indent_main() + "if "
            self.increase_indent_main()
        else:
            self.python_code += self.get_indent() + "if "
            self.increase_indent()

    def constructConditionText(self, logical_expression):
        if not logical_expression:
            return ""

        if isinstance(logical_expression, str):
            return logical_expression

        if len(logical_expression) > 3:
            raise ValueError("Logical expression should contain at most three elements.")

        left_expression, operator, right_expression = logical_expression

        condition_text = f"{left_expression} {operator} {right_expression}"

        return condition_text

    # Exit a parse tree produced by java_babilon_parser#ifStatement.
    def exitIfStatement(self, ctx: java_babilon_parser.IfStatementContext):
        if self.ifMainFunc:
            self.decrease_indent_main()
        else:
            self.decrease_indent()

    # Enter a parse tree produced by java_babilon_parser#elseStatement.
    def enterElseStatement(self, ctx: java_babilon_parser.ElseStatementContext):
        if self.ifMainFunc:
            self.decrease_indent_main()
            self.mainFunc += self.get_indent_main() + f"else:\n"
            self.increase_indent_main()
        else:
            self.decrease_indent()
            self.python_code += self.get_indent() + f"else:\n"
            self.increase_indent()

    # Exit a parse tree produced by java_babilon_parser#elseStatement.
    def exitElseStatement(self, ctx: java_babilon_parser.ElseStatementContext):
        pass

    # Enter a parse tree produced by java_babilon_parser#forLoopStatement.
    def enterForLoopStatement(self, ctx: java_babilon_parser.ForLoopStatementContext):
        if self.ifMainFunc:
            loop_variable_ctx = ctx.forLoopVariable(0)
            loop_variable = self.enterForLoopVariable(loop_variable_ctx)

            step_variable_ctx = ctx.forLoopVariable(1)
            step_variable = self.getStepValue(step_variable_ctx)

            logical_expression_ctx = ctx.oneLogicalExpression()
            loop_range = self.enterOneLogicalExpression(logical_expression_ctx)

            self.mainFunc += self.get_indent_main() + f"for {loop_variable[0]} in range({loop_variable[1]}, {loop_range[2]}, {step_variable}):\n"
            self.increase_indent_main()
        else:
            loop_variable_ctx = ctx.forLoopVariable(0)
            loop_variable = self.enterForLoopVariable(loop_variable_ctx)

            step_variable_ctx = ctx.forLoopVariable(1)
            step_variable = self.getStepValue(step_variable_ctx)

            logical_expression_ctx = ctx.oneLogicalExpression()
            loop_range = self.enterOneLogicalExpression(logical_expression_ctx)

            self.python_code += self.get_indent() + f"for {loop_variable[0]} in range({loop_variable[1]}, {loop_range[2]}, {step_variable}):\n"
            self.increase_indent()

    # Exit a parse tree produced by java_babilon_parser#forLoopStatement.
    def exitForLoopStatement(self, ctx: java_babilon_parser.ForLoopStatementContext):
        if self.ifMainFunc:
            self.decrease_indent_main()
        else:
            self.decrease_indent()

    # Enter a parse tree produced by java_babilon_parser#forLoopVariable.
    def enterForLoopVariable(self, ctx: java_babilon_parser.ForLoopVariableContext):
        if ctx.IDENTIFIER():
            if ctx.expression():
                initial_value = ctx.expression().getText()
                return (ctx.IDENTIFIER().getText(), initial_value)
        else:
            return (ctx.getChildren()[1].getText(), ctx.getChildren()[3].getText())

    # Exit a parse tree produced by java_babilon_parser#forLoopVariable.
    def exitForLoopVariable(self, ctx: java_babilon_parser.ForLoopVariableContext):
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

    # Enter a parse tree produced by java_babilon_parser#whileLoopStatement.
    def enterWhileLoopStatement(self, ctx: java_babilon_parser.WhileLoopStatementContext):
        if self.ifMainFunc:
            self.mainFunc += self.get_indent_main() + "while "
            self.increase_indent_main()
        else:
            self.python_code += self.get_indent() + "while "
            self.increase_indent()

    # Exit a parse tree produced by java_babilon_parser#whileLoopStatement.
    def exitWhileLoopStatement(self, ctx: java_babilon_parser.WhileLoopStatementContext):
        if self.ifMainFunc:
            self.decrease_indent_main()
        else:
            self.decrease_indent()

    # Enter a parse tree produced by java_babilon_parser#assignmentStatement.
    def enterAssignmentStatement(self, ctx: java_babilon_parser.AssignmentStatementContext):
        if self.ifMainFunc:
            if ctx.IDENTIFIER():
                variable_name = ctx.IDENTIFIER().getText()
                expression_ctx = ctx.expression().getText()
                if expression_ctx == "true":
                    self.mainFunc += self.get_indent_main() + f"{variable_name} = True\n"
                elif expression_ctx == "false":
                    self.mainFunc += self.get_indent_main() + f"{variable_name} = False\n"
                elif ".length" in expression_ctx or ".size()" in expression_ctx:
                    array_len = f"len({ctx.expression().additiveExpression().multiplicativeExpression(0).primaryExpression(0).fieldAccessing().IDENTIFIER(0).getText()})"
                    self.mainFunc += self.get_indent_main() + f"{variable_name} = {array_len}\n"
                else:
                    expression_ctx = ctx.expression().getText()
                    self.mainFunc += self.get_indent_main() + f"{variable_name} = {expression_ctx}\n"
            else:
                variable_name = ctx.arrayGet().getText()
                expression_ctx = ctx.expression().getText()
                self.mainFunc += self.get_indent_main() + f"{variable_name} = {expression_ctx}\n"
        else:
            if ctx.IDENTIFIER():
                variable_name = ctx.IDENTIFIER().getText()
                expression_ctx = ctx.expression().getText()
                if expression_ctx == "true":
                    self.python_code += self.get_indent() + f"{variable_name} = True\n"
                elif expression_ctx == "false":
                    self.python_code += self.get_indent() + f"{variable_name} = False\n"
                if ".length" in expression_ctx or ".size()" in expression_ctx:
                    array_len = f"len({ctx.expression().additiveExpression().multiplicativeExpression(0).primaryExpression(0).fieldAccessing().IDENTIFIER(0).getText()})"
                    self.python_code += self.get_indent() + f"{variable_name} = {array_len}\n"
                else:
                    expression_ctx = ctx.expression().getText()
                    self.python_code += self.get_indent() + f"{variable_name} = {expression_ctx}\n"
            else:
                variable_name = ctx.arrayGet().getText()
                expression_ctx = ctx.expression().getText()
                self.python_code += self.get_indent() + f"{variable_name} = {expression_ctx}\n"

    # Exit a parse tree produced by java_babilon_parser#assignmentStatement.
    def exitAssignmentStatement(self, ctx: java_babilon_parser.AssignmentStatementContext):
        pass

    # Enter a parse tree produced by java_babilon_parser#incrementStatement.
    def enterIncrementStatement(self, ctx: java_babilon_parser.IncrementStatementContext):
        if self.ifMainFunc:
            variable_name = ctx.IDENTIFIER().getText()
            self.mainFunc += self.get_indent_main() + f"{variable_name}+=1\n"
        else:
            variable_name = ctx.IDENTIFIER().getText()
            self.python_code += self.get_indent() + f"{variable_name}+=1\n"

    # Exit a parse tree produced by java_babilon_parser#incrementStatement.
    def exitIncrementStatement(self, ctx: java_babilon_parser.IncrementStatementContext):
        pass

    # Enter a parse tree produced by java_babilon_parser#decrementStatement.
    def enterDecrementStatement(self, ctx: java_babilon_parser.DecrementStatementContext):
        if self.ifMainFunc:
            variable_name = ctx.IDENTIFIER().getText()
            self.mainFunc += self.get_indent_main() + f"{variable_name}-=1\n"
        else:
            variable_name = ctx.IDENTIFIER().getText()
            self.python_code += self.get_indent() + f"{variable_name}-=1\n"

    # Exit a parse tree produced by java_babilon_parser#decrementStatement.
    def exitDecrementStatement(self, ctx: java_babilon_parser.DecrementStatementContext):
        pass

    # Enter a parse tree produced by java_babilon_parser#expression.
    def enterExpression(self, ctx: java_babilon_parser.ExpressionContext):
        pass

    # Exit a parse tree produced by java_babilon_parser#expression.
    def exitExpression(self, ctx: java_babilon_parser.ExpressionContext):
        pass

    # Enter a parse tree produced by java_babilon_parser#additiveExpression.
    def enterAdditiveExpression(self, ctx: java_babilon_parser.AdditiveExpressionContext):
        pass

    # Exit a parse tree produced by java_babilon_parser#additiveExpression.
    def exitAdditiveExpression(self, ctx: java_babilon_parser.AdditiveExpressionContext):
        pass

    # Enter a parse tree produced by java_babilon_parser#multiplicativeExpression.
    def enterMultiplicativeExpression(self, ctx: java_babilon_parser.MultiplicativeExpressionContext):
        pass

    # Exit a parse tree produced by java_babilon_parser#multiplicativeExpression.
    def exitMultiplicativeExpression(self, ctx: java_babilon_parser.MultiplicativeExpressionContext):
        pass

    # Enter a parse tree produced by java_babilon_parser#primaryExpression.
    def enterPrimaryExpression(self, ctx: java_babilon_parser.PrimaryExpressionContext):
        pass

    # Exit a parse tree produced by java_babilon_parser#primaryExpression.
    def exitPrimaryExpression(self, ctx: java_babilon_parser.PrimaryExpressionContext):
        pass

    # Enter a parse tree produced by java_babilon_parser#logicalExpression.
    def enterLogicalExpression(self, ctx: java_babilon_parser.LogicalExpressionContext):
        logical1_ctx = ctx.oneLogicalExpression(0).getText()
        logical2_ctx = None
        if ctx.oneLogicalExpression(1):
            logical2_ctx = ctx.oneLogicalExpression(1).getText()

        if "true" in logical1_ctx:
            var_name = ctx.oneLogicalExpression(0).expression(0).additiveExpression().multiplicativeExpression(0).primaryExpression(0).IDENTIFIER().getText()
            logical1_ctx = var_name + " == True"
        if "false" in logical1_ctx:
            var_name = ctx.oneLogicalExpression(0).expression(0).additiveExpression().multiplicativeExpression(0).primaryExpression(0).IDENTIFIER().getText()
            logical1_ctx = var_name + " == False"

        if ctx.OR():
            operator = "or"
        else:
            operator = "and"
        if logical2_ctx is None:
            logical = f"{logical1_ctx}:\n"
        else:
            logical = f"{logical1_ctx} {operator} {logical2_ctx}:\n"

        if self.ifMainFunc:
            self.mainFunc += logical
        else:
            self.python_code += logical

    # Exit a parse tree produced by java_babilon_parser#logicalExpression.
    def exitLogicalExpression(self, ctx: java_babilon_parser.LogicalExpressionContext):
        pass

    # Enter a parse tree produced by java_babilon_parser#oneLogicalExpression.
    def enterOneLogicalExpression(self, ctx: java_babilon_parser.OneLogicalExpressionContext):
        # Pobierz lewe i prawe wyrażenie z kontekstu
        left_expression = ctx.expression(0).getText()
        right_expression = None
        if ctx.expression(1):
            right_expression = ctx.expression(1).getText()

        # Pobierz operator logiczny z kontekstu
        operator = ctx.getChild(1).getText()

        # Skonstruuj wyrażenie logiczne
        logical_expression = (left_expression, operator, right_expression)
        return logical_expression

    # Exit a parse tree produced by java_babilon_parser#oneLogicalExpression.
    def exitOneLogicalExpression(self, ctx: java_babilon_parser.OneLogicalExpressionContext):
        pass

    # Enter a parse tree produced by java_babilon_parser#arrayDefinition.
    def enterArrayDefinition(self, ctx: java_babilon_parser.ArrayDefinitionContext):
        if self.ifMainFunc:
            variable_name = ctx.IDENTIFIER().getText()
            size = ctx.expression().getText()

            if size:
                self.mainFunc += self.get_indent_main() + f"{variable_name} = [0] * {size}\n"
            else:
                self.mainFunc += self.get_indent_main() + f"{variable_name} = []\n"
        else:
            variable_name = ctx.IDENTIFIER().getText()
            size = ctx.expression().getText()

            if size:
                self.python_code += self.get_indent() + f"{variable_name} = [0] * {size}\n"
            else:
                self.python_code += self.get_indent() + f"{variable_name} = []\n"

    # Exit a parse tree produced by java_babilon_parser#arrayDefinition.
    def exitArrayDefinition(self, ctx: java_babilon_parser.ArrayDefinitionContext):
        pass

    # Enter a parse tree produced by java_babilon_parser#listDefinition.
    def enterListDefinition(self, ctx: java_babilon_parser.ListDefinitionContext):
        if self.ifMainFunc:
            variable_name = ctx.IDENTIFIER().getText()
            self.mainFunc += self.get_indent_main() + f"{variable_name} = []\n"
        else:
            variable_name = ctx.IDENTIFIER().getText()
            self.python_code += self.get_indent() + f"{variable_name} = []\n"

    # Exit a parse tree produced by java_babilon_parser#listDefinition.
    def exitListDefinition(self, ctx: java_babilon_parser.ListDefinitionContext):
        pass

    # Enter a parse tree produced by java_babilon_parser#listAddDefinition.
    def enterListAddDefinition(self, ctx: java_babilon_parser.ListAddDefinitionContext):
        if self.ifMainFunc:
            variable_name = ctx.IDENTIFIER().getText()
            value = ctx.expression().getText()
            self.mainFunc += self.get_indent_main() + f"{variable_name}.append({value})\n"
        else:
            variable_name = ctx.IDENTIFIER().getText()
            value = ctx.expression().getText()
            self.python_code += self.get_indent() + f"{variable_name}.append({value})\n"

    # Exit a parse tree produced by java_babilon_parser#listAddDefinition.
    def exitListAddDefinition(self, ctx: java_babilon_parser.ListAddDefinitionContext):
        pass

    # Enter a parse tree produced by java_babilon_parser#objectCreating.
    def enterObjectCreating(self, ctx: java_babilon_parser.ObjectCreatingContext):
        if self.ifMainFunc:
            variable_name = ctx.IDENTIFIER(1).getText()
            class_name = ctx.IDENTIFIER(0).getText()
            parameters = ctx.parameters().getText()
            self.mainFunc += self.get_indent_main() + f"{variable_name} = {class_name}({parameters})\n"
        else:
            variable_name = ctx.IDENTIFIER(1).getText()
            class_name = ctx.IDENTIFIER(0).getText()
            parameters = ctx.parameters().getText()
            self.python_code += self.get_indent() + f"{variable_name} = {class_name}({parameters})\n"

    # Exit a parse tree produced by java_babilon_parser#objectCreating.
    def exitObjectCreating(self, ctx: java_babilon_parser.ObjectCreatingContext):
        pass

    # Enter a parse tree produced by java_babilon_parser#arrayGet.
    def enterArrayGet(self, ctx: java_babilon_parser.ArrayGetContext):
        pass

    # Exit a parse tree produced by java_babilon_parser#arrayGet.
    def exitArrayGet(self, ctx: java_babilon_parser.ArrayGetContext):
        pass

# todo DO ZROBIENIA
#     w metodzie main usunac self z wywolywania metod