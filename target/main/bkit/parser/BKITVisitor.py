# Generated from main/bkit/parser/BKIT.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .BKITParser import BKITParser
else:
    from BKITParser import BKITParser

# This class defines a complete generic visitor for a parse tree produced by BKITParser.

class BKITVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by BKITParser#program.
    def visitProgram(self, ctx:BKITParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#func.
    def visitFunc(self, ctx:BKITParser.FuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#funcDecl.
    def visitFuncDecl(self, ctx:BKITParser.FuncDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#param.
    def visitParam(self, ctx:BKITParser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#funcBody.
    def visitFuncBody(self, ctx:BKITParser.FuncBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#paramDecls.
    def visitParamDecls(self, ctx:BKITParser.ParamDeclsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#paramDecl.
    def visitParamDecl(self, ctx:BKITParser.ParamDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#varStmt.
    def visitVarStmt(self, ctx:BKITParser.VarStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#varDecls.
    def visitVarDecls(self, ctx:BKITParser.VarDeclsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#varDecl.
    def visitVarDecl(self, ctx:BKITParser.VarDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#arr.
    def visitArr(self, ctx:BKITParser.ArrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#literal.
    def visitLiteral(self, ctx:BKITParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#stmtlist.
    def visitStmtlist(self, ctx:BKITParser.StmtlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#stmt.
    def visitStmt(self, ctx:BKITParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#assignStmt.
    def visitAssignStmt(self, ctx:BKITParser.AssignStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#ifStmt.
    def visitIfStmt(self, ctx:BKITParser.IfStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#forStmt.
    def visitForStmt(self, ctx:BKITParser.ForStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#whileStmt.
    def visitWhileStmt(self, ctx:BKITParser.WhileStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#doWhileStmt.
    def visitDoWhileStmt(self, ctx:BKITParser.DoWhileStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#breakStmt.
    def visitBreakStmt(self, ctx:BKITParser.BreakStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#continueStmt.
    def visitContinueStmt(self, ctx:BKITParser.ContinueStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#callStmt.
    def visitCallStmt(self, ctx:BKITParser.CallStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#returnStmt.
    def visitReturnStmt(self, ctx:BKITParser.ReturnStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#expr.
    def visitExpr(self, ctx:BKITParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#expr0.
    def visitExpr0(self, ctx:BKITParser.Expr0Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#expr1.
    def visitExpr1(self, ctx:BKITParser.Expr1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#expr2.
    def visitExpr2(self, ctx:BKITParser.Expr2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#expr3.
    def visitExpr3(self, ctx:BKITParser.Expr3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#expr4.
    def visitExpr4(self, ctx:BKITParser.Expr4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#expr5.
    def visitExpr5(self, ctx:BKITParser.Expr5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#expr6.
    def visitExpr6(self, ctx:BKITParser.Expr6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#expr7.
    def visitExpr7(self, ctx:BKITParser.Expr7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#idxOperator.
    def visitIdxOperator(self, ctx:BKITParser.IdxOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#callExpr.
    def visitCallExpr(self, ctx:BKITParser.CallExprContext):
        return self.visitChildren(ctx)



del BKITParser