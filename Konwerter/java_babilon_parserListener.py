# Generated from java_babilon_parser.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .java_babilon_parser import java_babilon_parser
else:
    from java_babilon_parser import java_babilon_parser


# This class defines a complete listener for a parse tree produced by java_babilon_parser.
class java_babilon_parserListener(ParseTreeListener):

    def __init__(self):
        self.python_code = ""

    # Enter a parse tree produced by java_babilon_parser#program.
    def enterProgram(self, ctx:java_babilon_parser.ProgramContext):
        pass

    # Exit a parse tree produced by java_babilon_parser#program.
    def exitProgram(self, ctx:java_babilon_parser.ProgramContext):
        pass


    # Enter a parse tree produced by java_babilon_parser#classDeclaration.
    def enterClassDeclaration(self, ctx:java_babilon_parser.ClassDeclarationContext):
        self.python_code += "\nclass " + ctx.IDENTIFIER()[0].getText() + ":\n\t"


    # Exit a parse tree produced by java_babilon_parser#classDeclaration.
    def exitClassDeclaration(self, ctx:java_babilon_parser.ClassDeclarationContext):
        pass


    # Enter a parse tree produced by java_babilon_parser#classBody.
    def enterClassBody(self, ctx:java_babilon_parser.ClassBodyContext):
        pass

    # Exit a parse tree produced by java_babilon_parser#classBody.
    def exitClassBody(self, ctx:java_babilon_parser.ClassBodyContext):
        pass


    # Enter a parse tree produced by java_babilon_parser#importStatement.
    def enterImportStatement(self, ctx:java_babilon_parser.ImportStatementContext):
        if ctx.ARRAY_LIST():
            self.python_code += "import numpy as np\n"
        else:
            self.python_code += "import " + ctx.IDENTIFIER()[0].getText() + "\n"

    # Exit a parse tree produced by java_babilon_parser#importStatement.
    def exitImportStatement(self, ctx:java_babilon_parser.ImportStatementContext):
        pass


    # Enter a parse tree produced by java_babilon_parser#mainMethod.
    def enterMainMethod(self, ctx:java_babilon_parser.MainMethodContext):
        self.python_code += "def main():\n\t"
        pass

    # Exit a parse tree produced by java_babilon_parser#mainMethod.
    def exitMainMethod(self, ctx:java_babilon_parser.MainMethodContext):
        pass


    # Enter a parse tree produced by java_babilon_parser#methodDefinition.
    def enterMethodDefinition(self, ctx:java_babilon_parser.MethodDefinitionContext):
        pass

    # Exit a parse tree produced by java_babilon_parser#methodDefinition.
    def exitMethodDefinition(self, ctx:java_babilon_parser.MethodDefinitionContext):
        pass


    # Enter a parse tree produced by java_babilon_parser#parameters.
    def enterParameters(self, ctx:java_babilon_parser.ParametersContext):
        pass

    # Exit a parse tree produced by java_babilon_parser#parameters.
    def exitParameters(self, ctx:java_babilon_parser.ParametersContext):
        pass


    # Enter a parse tree produced by java_babilon_parser#parametersDefinition.
    def enterParametersDefinition(self, ctx:java_babilon_parser.ParametersDefinitionContext):
        pass

    # Exit a parse tree produced by java_babilon_parser#parametersDefinition.
    def exitParametersDefinition(self, ctx:java_babilon_parser.ParametersDefinitionContext):
        pass


    # Enter a parse tree produced by java_babilon_parser#oneParameterDefinition.
    def enterOneParameterDefinition(self, ctx:java_babilon_parser.OneParameterDefinitionContext):
        pass

    # Exit a parse tree produced by java_babilon_parser#oneParameterDefinition.
    def exitOneParameterDefinition(self, ctx:java_babilon_parser.OneParameterDefinitionContext):
        pass


    # Enter a parse tree produced by java_babilon_parser#fieldDefinition.
    def enterFieldDefinition(self, ctx:java_babilon_parser.FieldDefinitionContext):
        pass

    # Exit a parse tree produced by java_babilon_parser#fieldDefinition.
    def exitFieldDefinition(self, ctx:java_babilon_parser.FieldDefinitionContext):
        pass


    # Enter a parse tree produced by java_babilon_parser#variableDefinition.
    def enterVariableDefinition(self, ctx:java_babilon_parser.VariableDefinitionContext):
        pass

    # Exit a parse tree produced by java_babilon_parser#variableDefinition.
    def exitVariableDefinition(self, ctx:java_babilon_parser.VariableDefinitionContext):
        pass


    # Enter a parse tree produced by java_babilon_parser#methodCalling.
    def enterMethodCalling(self, ctx:java_babilon_parser.MethodCallingContext):
        pass

    # Exit a parse tree produced by java_babilon_parser#methodCalling.
    def exitMethodCalling(self, ctx:java_babilon_parser.MethodCallingContext):
        pass


    # Enter a parse tree produced by java_babilon_parser#fieldAccessing.
    def enterFieldAccessing(self, ctx:java_babilon_parser.FieldAccessingContext):
        pass

    # Exit a parse tree produced by java_babilon_parser#fieldAccessing.
    def exitFieldAccessing(self, ctx:java_babilon_parser.FieldAccessingContext):
        pass


    # Enter a parse tree produced by java_babilon_parser#statements.
    def enterStatements(self, ctx:java_babilon_parser.StatementsContext):
        pass

    # Exit a parse tree produced by java_babilon_parser#statements.
    def exitStatements(self, ctx:java_babilon_parser.StatementsContext):
        pass


    # Enter a parse tree produced by java_babilon_parser#statement.
    def enterStatement(self, ctx:java_babilon_parser.StatementContext):
        pass

    # Exit a parse tree produced by java_babilon_parser#statement.
    def exitStatement(self, ctx:java_babilon_parser.StatementContext):
        pass


    # Enter a parse tree produced by java_babilon_parser#printStatement.
    def enterPrintStatement(self, ctx:java_babilon_parser.PrintStatementContext):
        pass

    # Exit a parse tree produced by java_babilon_parser#printStatement.
    def exitPrintStatement(self, ctx:java_babilon_parser.PrintStatementContext):
        pass


    # Enter a parse tree produced by java_babilon_parser#doWhileStatement.
    def enterDoWhileStatement(self, ctx:java_babilon_parser.DoWhileStatementContext):
        pass

    # Exit a parse tree produced by java_babilon_parser#doWhileStatement.
    def exitDoWhileStatement(self, ctx:java_babilon_parser.DoWhileStatementContext):
        pass


    # Enter a parse tree produced by java_babilon_parser#continueStatement.
    def enterContinueStatement(self, ctx:java_babilon_parser.ContinueStatementContext):
        pass

    # Exit a parse tree produced by java_babilon_parser#continueStatement.
    def exitContinueStatement(self, ctx:java_babilon_parser.ContinueStatementContext):
        pass


    # Enter a parse tree produced by java_babilon_parser#breakStatement.
    def enterBreakStatement(self, ctx:java_babilon_parser.BreakStatementContext):
        pass

    # Exit a parse tree produced by java_babilon_parser#breakStatement.
    def exitBreakStatement(self, ctx:java_babilon_parser.BreakStatementContext):
        pass


    # Enter a parse tree produced by java_babilon_parser#returnStatement.
    def enterReturnStatement(self, ctx:java_babilon_parser.ReturnStatementContext):
        pass

    # Exit a parse tree produced by java_babilon_parser#returnStatement.
    def exitReturnStatement(self, ctx:java_babilon_parser.ReturnStatementContext):
        pass


    # Enter a parse tree produced by java_babilon_parser#literal.
    def enterLiteral(self, ctx:java_babilon_parser.LiteralContext):
        pass

    # Exit a parse tree produced by java_babilon_parser#literal.
    def exitLiteral(self, ctx:java_babilon_parser.LiteralContext):
        pass


    # Enter a parse tree produced by java_babilon_parser#ifStatement.
    def enterIfStatement(self, ctx:java_babilon_parser.IfStatementContext):
        pass

    # Exit a parse tree produced by java_babilon_parser#ifStatement.
    def exitIfStatement(self, ctx:java_babilon_parser.IfStatementContext):
        pass


    # Enter a parse tree produced by java_babilon_parser#forLoopStatement.
    def enterForLoopStatement(self, ctx:java_babilon_parser.ForLoopStatementContext):
        pass

    # Exit a parse tree produced by java_babilon_parser#forLoopStatement.
    def exitForLoopStatement(self, ctx:java_babilon_parser.ForLoopStatementContext):
        pass


    # Enter a parse tree produced by java_babilon_parser#forLoopVariable.
    def enterForLoopVariable(self, ctx:java_babilon_parser.ForLoopVariableContext):
        pass

    # Exit a parse tree produced by java_babilon_parser#forLoopVariable.
    def exitForLoopVariable(self, ctx:java_babilon_parser.ForLoopVariableContext):
        pass


    # Enter a parse tree produced by java_babilon_parser#whileLoopStatement.
    def enterWhileLoopStatement(self, ctx:java_babilon_parser.WhileLoopStatementContext):
        pass

    # Exit a parse tree produced by java_babilon_parser#whileLoopStatement.
    def exitWhileLoopStatement(self, ctx:java_babilon_parser.WhileLoopStatementContext):
        pass


    # Enter a parse tree produced by java_babilon_parser#assignmentStatement.
    def enterAssignmentStatement(self, ctx:java_babilon_parser.AssignmentStatementContext):
        pass

    # Exit a parse tree produced by java_babilon_parser#assignmentStatement.
    def exitAssignmentStatement(self, ctx:java_babilon_parser.AssignmentStatementContext):
        pass


    # Enter a parse tree produced by java_babilon_parser#incrementStatement.
    def enterIncrementStatement(self, ctx:java_babilon_parser.IncrementStatementContext):
        pass

    # Exit a parse tree produced by java_babilon_parser#incrementStatement.
    def exitIncrementStatement(self, ctx:java_babilon_parser.IncrementStatementContext):
        pass


    # Enter a parse tree produced by java_babilon_parser#decrementStatement.
    def enterDecrementStatement(self, ctx:java_babilon_parser.DecrementStatementContext):
        pass

    # Exit a parse tree produced by java_babilon_parser#decrementStatement.
    def exitDecrementStatement(self, ctx:java_babilon_parser.DecrementStatementContext):
        pass


    # Enter a parse tree produced by java_babilon_parser#expression.
    def enterExpression(self, ctx:java_babilon_parser.ExpressionContext):
        pass

    # Exit a parse tree produced by java_babilon_parser#expression.
    def exitExpression(self, ctx:java_babilon_parser.ExpressionContext):
        pass


    # Enter a parse tree produced by java_babilon_parser#additiveExpression.
    def enterAdditiveExpression(self, ctx:java_babilon_parser.AdditiveExpressionContext):
        pass

    # Exit a parse tree produced by java_babilon_parser#additiveExpression.
    def exitAdditiveExpression(self, ctx:java_babilon_parser.AdditiveExpressionContext):
        pass


    # Enter a parse tree produced by java_babilon_parser#multiplicativeExpression.
    def enterMultiplicativeExpression(self, ctx:java_babilon_parser.MultiplicativeExpressionContext):
        pass

    # Exit a parse tree produced by java_babilon_parser#multiplicativeExpression.
    def exitMultiplicativeExpression(self, ctx:java_babilon_parser.MultiplicativeExpressionContext):
        pass


    # Enter a parse tree produced by java_babilon_parser#primaryExpression.
    def enterPrimaryExpression(self, ctx:java_babilon_parser.PrimaryExpressionContext):
        pass

    # Exit a parse tree produced by java_babilon_parser#primaryExpression.
    def exitPrimaryExpression(self, ctx:java_babilon_parser.PrimaryExpressionContext):
        pass


    # Enter a parse tree produced by java_babilon_parser#logicalExpression.
    def enterLogicalExpression(self, ctx:java_babilon_parser.LogicalExpressionContext):
        pass

    # Exit a parse tree produced by java_babilon_parser#logicalExpression.
    def exitLogicalExpression(self, ctx:java_babilon_parser.LogicalExpressionContext):
        pass


    # Enter a parse tree produced by java_babilon_parser#oneLogicalExpression.
    def enterOneLogicalExpression(self, ctx:java_babilon_parser.OneLogicalExpressionContext):
        pass

    # Exit a parse tree produced by java_babilon_parser#oneLogicalExpression.
    def exitOneLogicalExpression(self, ctx:java_babilon_parser.OneLogicalExpressionContext):
        pass


    # Enter a parse tree produced by java_babilon_parser#arrayDefinition.
    def enterArrayDefinition(self, ctx:java_babilon_parser.ArrayDefinitionContext):
        pass

    # Exit a parse tree produced by java_babilon_parser#arrayDefinition.
    def exitArrayDefinition(self, ctx:java_babilon_parser.ArrayDefinitionContext):
        pass


    # Enter a parse tree produced by java_babilon_parser#listDefinition.
    def enterListDefinition(self, ctx:java_babilon_parser.ListDefinitionContext):
        pass

    # Exit a parse tree produced by java_babilon_parser#listDefinition.
    def exitListDefinition(self, ctx:java_babilon_parser.ListDefinitionContext):
        pass


    # Enter a parse tree produced by java_babilon_parser#listAddDefinition.
    def enterListAddDefinition(self, ctx:java_babilon_parser.ListAddDefinitionContext):
        pass

    # Exit a parse tree produced by java_babilon_parser#listAddDefinition.
    def exitListAddDefinition(self, ctx:java_babilon_parser.ListAddDefinitionContext):
        pass


    # Enter a parse tree produced by java_babilon_parser#objectCreating.
    def enterObjectCreating(self, ctx:java_babilon_parser.ObjectCreatingContext):
        pass

    # Exit a parse tree produced by java_babilon_parser#objectCreating.
    def exitObjectCreating(self, ctx:java_babilon_parser.ObjectCreatingContext):
        pass


