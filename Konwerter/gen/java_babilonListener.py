# Generated from java_babilon.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .java_babilonParser import java_babilonParser
else:
    from java_babilonParser import java_babilonParser

# This class defines a complete listener for a parse tree produced by java_babilonParser.
class java_babilonListener(ParseTreeListener):

    # Enter a parse tree produced by java_babilonParser#program.
    def enterProgram(self, ctx:java_babilonParser.ProgramContext):
        pass

    # Exit a parse tree produced by java_babilonParser#program.
    def exitProgram(self, ctx:java_babilonParser.ProgramContext):
        pass


    # Enter a parse tree produced by java_babilonParser#classDeclaration.
    def enterClassDeclaration(self, ctx:java_babilonParser.ClassDeclarationContext):
        pass

    # Exit a parse tree produced by java_babilonParser#classDeclaration.
    def exitClassDeclaration(self, ctx:java_babilonParser.ClassDeclarationContext):
        pass


    # Enter a parse tree produced by java_babilonParser#classBody.
    def enterClassBody(self, ctx:java_babilonParser.ClassBodyContext):
        pass

    # Exit a parse tree produced by java_babilonParser#classBody.
    def exitClassBody(self, ctx:java_babilonParser.ClassBodyContext):
        pass


    # Enter a parse tree produced by java_babilonParser#methodDefinition.
    def enterMethodDefinition(self, ctx:java_babilonParser.MethodDefinitionContext):
        pass

    # Exit a parse tree produced by java_babilonParser#methodDefinition.
    def exitMethodDefinition(self, ctx:java_babilonParser.MethodDefinitionContext):
        pass


    # Enter a parse tree produced by java_babilonParser#parameters.
    def enterParameters(self, ctx:java_babilonParser.ParametersContext):
        pass

    # Exit a parse tree produced by java_babilonParser#parameters.
    def exitParameters(self, ctx:java_babilonParser.ParametersContext):
        pass


    # Enter a parse tree produced by java_babilonParser#parametersDefinition.
    def enterParametersDefinition(self, ctx:java_babilonParser.ParametersDefinitionContext):
        pass

    # Exit a parse tree produced by java_babilonParser#parametersDefinition.
    def exitParametersDefinition(self, ctx:java_babilonParser.ParametersDefinitionContext):
        pass


    # Enter a parse tree produced by java_babilonParser#oneParameterDefinition.
    def enterOneParameterDefinition(self, ctx:java_babilonParser.OneParameterDefinitionContext):
        pass

    # Exit a parse tree produced by java_babilonParser#oneParameterDefinition.
    def exitOneParameterDefinition(self, ctx:java_babilonParser.OneParameterDefinitionContext):
        pass


    # Enter a parse tree produced by java_babilonParser#fieldDefinition.
    def enterFieldDefinition(self, ctx:java_babilonParser.FieldDefinitionContext):
        pass

    # Exit a parse tree produced by java_babilonParser#fieldDefinition.
    def exitFieldDefinition(self, ctx:java_babilonParser.FieldDefinitionContext):
        pass


    # Enter a parse tree produced by java_babilonParser#variableDefinition.
    def enterVariableDefinition(self, ctx:java_babilonParser.VariableDefinitionContext):
        pass

    # Exit a parse tree produced by java_babilonParser#variableDefinition.
    def exitVariableDefinition(self, ctx:java_babilonParser.VariableDefinitionContext):
        pass


    # Enter a parse tree produced by java_babilonParser#methodCalling.
    def enterMethodCalling(self, ctx:java_babilonParser.MethodCallingContext):
        pass

    # Exit a parse tree produced by java_babilonParser#methodCalling.
    def exitMethodCalling(self, ctx:java_babilonParser.MethodCallingContext):
        pass


    # Enter a parse tree produced by java_babilonParser#fieldAccesing.
    def enterFieldAccesing(self, ctx:java_babilonParser.FieldAccesingContext):
        pass

    # Exit a parse tree produced by java_babilonParser#fieldAccesing.
    def exitFieldAccesing(self, ctx:java_babilonParser.FieldAccesingContext):
        pass


    # Enter a parse tree produced by java_babilonParser#statements.
    def enterStatements(self, ctx:java_babilonParser.StatementsContext):
        pass

    # Exit a parse tree produced by java_babilonParser#statements.
    def exitStatements(self, ctx:java_babilonParser.StatementsContext):
        pass


    # Enter a parse tree produced by java_babilonParser#statement.
    def enterStatement(self, ctx:java_babilonParser.StatementContext):
        pass

    # Exit a parse tree produced by java_babilonParser#statement.
    def exitStatement(self, ctx:java_babilonParser.StatementContext):
        pass


    # Enter a parse tree produced by java_babilonParser#printStatement.
    def enterPrintStatement(self, ctx:java_babilonParser.PrintStatementContext):
        pass

    # Exit a parse tree produced by java_babilonParser#printStatement.
    def exitPrintStatement(self, ctx:java_babilonParser.PrintStatementContext):
        pass


    # Enter a parse tree produced by java_babilonParser#doWhileStatement.
    def enterDoWhileStatement(self, ctx:java_babilonParser.DoWhileStatementContext):
        pass

    # Exit a parse tree produced by java_babilonParser#doWhileStatement.
    def exitDoWhileStatement(self, ctx:java_babilonParser.DoWhileStatementContext):
        pass


    # Enter a parse tree produced by java_babilonParser#continueStatement.
    def enterContinueStatement(self, ctx:java_babilonParser.ContinueStatementContext):
        pass

    # Exit a parse tree produced by java_babilonParser#continueStatement.
    def exitContinueStatement(self, ctx:java_babilonParser.ContinueStatementContext):
        pass


    # Enter a parse tree produced by java_babilonParser#breakStatement.
    def enterBreakStatement(self, ctx:java_babilonParser.BreakStatementContext):
        pass

    # Exit a parse tree produced by java_babilonParser#breakStatement.
    def exitBreakStatement(self, ctx:java_babilonParser.BreakStatementContext):
        pass


    # Enter a parse tree produced by java_babilonParser#returnStatement.
    def enterReturnStatement(self, ctx:java_babilonParser.ReturnStatementContext):
        pass

    # Exit a parse tree produced by java_babilonParser#returnStatement.
    def exitReturnStatement(self, ctx:java_babilonParser.ReturnStatementContext):
        pass


    # Enter a parse tree produced by java_babilonParser#literal.
    def enterLiteral(self, ctx:java_babilonParser.LiteralContext):
        pass

    # Exit a parse tree produced by java_babilonParser#literal.
    def exitLiteral(self, ctx:java_babilonParser.LiteralContext):
        pass


    # Enter a parse tree produced by java_babilonParser#ifStatement.
    def enterIfStatement(self, ctx:java_babilonParser.IfStatementContext):
        pass

    # Exit a parse tree produced by java_babilonParser#ifStatement.
    def exitIfStatement(self, ctx:java_babilonParser.IfStatementContext):
        pass


    # Enter a parse tree produced by java_babilonParser#forLoopStatement.
    def enterForLoopStatement(self, ctx:java_babilonParser.ForLoopStatementContext):
        pass

    # Exit a parse tree produced by java_babilonParser#forLoopStatement.
    def exitForLoopStatement(self, ctx:java_babilonParser.ForLoopStatementContext):
        pass


    # Enter a parse tree produced by java_babilonParser#forLoopVariable.
    def enterForLoopVariable(self, ctx:java_babilonParser.ForLoopVariableContext):
        pass

    # Exit a parse tree produced by java_babilonParser#forLoopVariable.
    def exitForLoopVariable(self, ctx:java_babilonParser.ForLoopVariableContext):
        pass


    # Enter a parse tree produced by java_babilonParser#whileLoopStatement.
    def enterWhileLoopStatement(self, ctx:java_babilonParser.WhileLoopStatementContext):
        pass

    # Exit a parse tree produced by java_babilonParser#whileLoopStatement.
    def exitWhileLoopStatement(self, ctx:java_babilonParser.WhileLoopStatementContext):
        pass


    # Enter a parse tree produced by java_babilonParser#assignmentStatement.
    def enterAssignmentStatement(self, ctx:java_babilonParser.AssignmentStatementContext):
        pass

    # Exit a parse tree produced by java_babilonParser#assignmentStatement.
    def exitAssignmentStatement(self, ctx:java_babilonParser.AssignmentStatementContext):
        pass


    # Enter a parse tree produced by java_babilonParser#incrementStatement.
    def enterIncrementStatement(self, ctx:java_babilonParser.IncrementStatementContext):
        pass

    # Exit a parse tree produced by java_babilonParser#incrementStatement.
    def exitIncrementStatement(self, ctx:java_babilonParser.IncrementStatementContext):
        pass


    # Enter a parse tree produced by java_babilonParser#decrementStatement.
    def enterDecrementStatement(self, ctx:java_babilonParser.DecrementStatementContext):
        pass

    # Exit a parse tree produced by java_babilonParser#decrementStatement.
    def exitDecrementStatement(self, ctx:java_babilonParser.DecrementStatementContext):
        pass


    # Enter a parse tree produced by java_babilonParser#expression.
    def enterExpression(self, ctx:java_babilonParser.ExpressionContext):
        pass

    # Exit a parse tree produced by java_babilonParser#expression.
    def exitExpression(self, ctx:java_babilonParser.ExpressionContext):
        pass


    # Enter a parse tree produced by java_babilonParser#additiveExpression.
    def enterAdditiveExpression(self, ctx:java_babilonParser.AdditiveExpressionContext):
        pass

    # Exit a parse tree produced by java_babilonParser#additiveExpression.
    def exitAdditiveExpression(self, ctx:java_babilonParser.AdditiveExpressionContext):
        pass


    # Enter a parse tree produced by java_babilonParser#multiplicativeExpression.
    def enterMultiplicativeExpression(self, ctx:java_babilonParser.MultiplicativeExpressionContext):
        pass

    # Exit a parse tree produced by java_babilonParser#multiplicativeExpression.
    def exitMultiplicativeExpression(self, ctx:java_babilonParser.MultiplicativeExpressionContext):
        pass


    # Enter a parse tree produced by java_babilonParser#primaryExpression.
    def enterPrimaryExpression(self, ctx:java_babilonParser.PrimaryExpressionContext):
        pass

    # Exit a parse tree produced by java_babilonParser#primaryExpression.
    def exitPrimaryExpression(self, ctx:java_babilonParser.PrimaryExpressionContext):
        pass


    # Enter a parse tree produced by java_babilonParser#logicalExpression.
    def enterLogicalExpression(self, ctx:java_babilonParser.LogicalExpressionContext):
        pass

    # Exit a parse tree produced by java_babilonParser#logicalExpression.
    def exitLogicalExpression(self, ctx:java_babilonParser.LogicalExpressionContext):
        pass


    # Enter a parse tree produced by java_babilonParser#oneLogicalExpression.
    def enterOneLogicalExpression(self, ctx:java_babilonParser.OneLogicalExpressionContext):
        pass

    # Exit a parse tree produced by java_babilonParser#oneLogicalExpression.
    def exitOneLogicalExpression(self, ctx:java_babilonParser.OneLogicalExpressionContext):
        pass


    # Enter a parse tree produced by java_babilonParser#arrayDefinition.
    def enterArrayDefinition(self, ctx:java_babilonParser.ArrayDefinitionContext):
        pass

    # Exit a parse tree produced by java_babilonParser#arrayDefinition.
    def exitArrayDefinition(self, ctx:java_babilonParser.ArrayDefinitionContext):
        pass


    # Enter a parse tree produced by java_babilonParser#listDefinition.
    def enterListDefinition(self, ctx:java_babilonParser.ListDefinitionContext):
        pass

    # Exit a parse tree produced by java_babilonParser#listDefinition.
    def exitListDefinition(self, ctx:java_babilonParser.ListDefinitionContext):
        pass


    # Enter a parse tree produced by java_babilonParser#listAddDefinition.
    def enterListAddDefinition(self, ctx:java_babilonParser.ListAddDefinitionContext):
        pass

    # Exit a parse tree produced by java_babilonParser#listAddDefinition.
    def exitListAddDefinition(self, ctx:java_babilonParser.ListAddDefinitionContext):
        pass


    # Enter a parse tree produced by java_babilonParser#objectCreating.
    def enterObjectCreating(self, ctx:java_babilonParser.ObjectCreatingContext):
        pass

    # Exit a parse tree produced by java_babilonParser#objectCreating.
    def exitObjectCreating(self, ctx:java_babilonParser.ObjectCreatingContext):
        pass


