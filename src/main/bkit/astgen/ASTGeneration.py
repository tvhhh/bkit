from BKITVisitor import BKITVisitor
from BKITParser import BKITParser
from AST import *
from functools import reduce

class ASTGeneration(BKITVisitor):

    # Visit a parse tree produced by BKITParser#program.
    def visitProgram(self,ctx:BKITParser.ProgramContext):
        varDecls = reduce(lambda acc, ele: acc + ele.accept(self), ctx.varStmt() or [], [])
        funcDecls = reduce(lambda acc, ele: acc + [ele.accept(self)], ctx.func() or [], [])
        return Program(varDecls + funcDecls)

    # Visit a parse tree produced by BKITParser#func.
    def visitFunc(self, ctx:BKITParser.FuncContext):
        return FuncDecl(
            name=ctx.funcDecl().accept(self), 
            param=ctx.param().accept(self) if ctx.param() else [], 
            body=ctx.funcBody().accept(self)
        )


    # Visit a parse tree produced by BKITParser#funcDecl.
    def visitFuncDecl(self, ctx:BKITParser.FuncDeclContext):
        return Id(ctx.ID().getText())


    # Visit a parse tree produced by BKITParser#param.
    def visitParam(self, ctx:BKITParser.ParamContext):
        return ctx.paramDecls().accept(self)


    # Visit a parse tree produced by BKITParser#funcBody.
    def visitFuncBody(self, ctx:BKITParser.FuncBodyContext):
        return ctx.stmtlist().accept(self)


    # Visit a parse tree produced by BKITParser#paramDecls.
    def visitParamDecls(self, ctx:BKITParser.ParamDeclsContext):
        return list(map(lambda ele: ele.accept(self), ctx.paramDecl()))


    # Visit a parse tree produced by BKITParser#paramDecl.
    def visitParamDecl(self, ctx:BKITParser.ParamDeclContext):
        return VarDecl(
            variable=Id(ctx.ID().getText()), 
            varDimen=list(map(lambda ele: int(ele.getText()), ctx.INT() or [])), 
            varInit=None
        )


    # Visit a parse tree produced by BKITParser#varStmt.
    def visitVarStmt(self, ctx:BKITParser.VarStmtContext):
        return ctx.varDecls().accept(self)


    # Visit a parse tree produced by BKITParser#varDecls.
    def visitVarDecls(self, ctx:BKITParser.VarDeclsContext):
        return list(map(lambda ele: ele.accept(self), ctx.varDecl()))


    # Visit a parse tree produced by BKITParser#varDecl.
    def visitVarDecl(self, ctx:BKITParser.VarDeclContext):
        return VarDecl(
            variable=Id(ctx.ID().getText()), 
            varDimen=list(map(lambda ele: int(ele.getText(), 0), ctx.INT() or [])), 
            varInit=ctx.literal().accept(self) if ctx.literal() else None
        )


    # Visit a parse tree produced by BKITParser#arr.
    def visitArr(self, ctx:BKITParser.ArrContext):
        return ArrayLiteral(list(map(lambda ele: ele.accept(self), ctx.literal())))


    # Visit a parse tree produced by BKITParser#literal.
    def visitLiteral(self, ctx:BKITParser.LiteralContext):
        if ctx.INT():
            return IntLiteral(int(ctx.INT().getText(), 0))
        elif ctx.FLOAT():
            return FloatLiteral(float(ctx.FLOAT().getText()))
        elif ctx.BOOLEAN():
            return BooleanLiteral(ctx.BOOLEAN().getText() == 'True')
        elif ctx.STRING():
            return StringLiteral(ctx.STRING().getText())
        else:
            return ctx.arr().accept(self)


    # Visit a parse tree produced by BKITParser#stmtlist.
    def visitStmtlist(self, ctx:BKITParser.StmtlistContext):
        return (
            reduce(lambda acc, ele: acc + ele.accept(self), ctx.varStmt() or [], []),
            list(map(lambda ele: ele.accept(self), ctx.stmt() or []))
        )


    # Visit a parse tree produced by BKITParser#stmt.
    def visitStmt(self, ctx:BKITParser.StmtContext):
        return (
            ctx.assignStmt() or
            ctx.ifStmt() or
            ctx.forStmt() or
            ctx.whileStmt() or
            ctx.doWhileStmt() or
            ctx.breakStmt() or
            ctx.continueStmt() or
            ctx.callStmt() or
            ctx.returnStmt()
        ).accept(self)


    # Visit a parse tree produced by BKITParser#assignStmt.
    def visitAssignStmt(self, ctx:BKITParser.AssignStmtContext):
        return Assign(
            lhs=Id(ctx.ID().getText()) if ctx.ID() else 
                ArrayCell(
                    arr=ctx.expr7().accept(self),
                    idx=ctx.idxOperator().accept(self)
                ),
            rhs=ctx.expr().accept(self)
        )


    # Visit a parse tree produced by BKITParser#ifStmt.
    def visitIfStmt(self, ctx:BKITParser.IfStmtContext):
        ids = range(0, len(ctx.expr()))
        return If(
            ifthenStmt=list(map(lambda ele: (ctx.expr(ele).accept(self),) + ctx.stmtlist(ele).accept(self), ids)),
            elseStmt=([], []) if not ctx.ELSE() else ctx.stmtlist()[-1].accept(self)
        )


    # Visit a parse tree produced by BKITParser#forStmt.
    def visitForStmt(self, ctx:BKITParser.ForStmtContext):
        return For(
            idx1=Id(ctx.ID().getText()),
            expr1=ctx.expr(0).accept(self),
            expr2=ctx.expr(1).accept(self),
            expr3=ctx.expr(2).accept(self),
            loop=ctx.stmtlist().accept(self)
        )


    # Visit a parse tree produced by BKITParser#whileStmt.
    def visitWhileStmt(self, ctx:BKITParser.WhileStmtContext):
        return While(
            exp=ctx.expr().accept(self), 
            sl=ctx.stmtlist().accept(self)
        )


    # Visit a parse tree produced by BKITParser#doWhileStmt.
    def visitDoWhileStmt(self, ctx:BKITParser.DoWhileStmtContext):
        return Dowhile(
            sl=ctx.stmtlist().accept(self),
            exp=ctx.expr().accept(self)
        )


    # Visit a parse tree produced by BKITParser#breakStmt.
    def visitBreakStmt(self, ctx:BKITParser.BreakStmtContext):
        return Break()


    # Visit a parse tree produced by BKITParser#continueStmt.
    def visitContinueStmt(self, ctx:BKITParser.ContinueStmtContext):
        return Continue()


    # Visit a parse tree produced by BKITParser#callStmt.
    def visitCallStmt(self, ctx:BKITParser.CallStmtContext):
        return CallStmt(
            method=Id(ctx.ID().getText()), 
            param=list(map(lambda ele: ele.accept(self), ctx.expr() or []))
        )


    # Visit a parse tree produced by BKITParser#returnStmt.
    def visitReturnStmt(self, ctx:BKITParser.ReturnStmtContext):
        return Return(ctx.expr().accept(self) if ctx.expr() else None)


    # Visit a parse tree produced by BKITParser#expr.
    def visitExpr(self, ctx:BKITParser.ExprContext):
        return StringLiteral(ctx.STRING().getText()) if ctx.STRING() else (ctx.expr0() or ctx.arr()).accept(self)
    

    # Visit a parse tree produced by BKITParser#expr0.
    def visitExpr0(self, ctx:BKITParser.Expr0Context):
        return ctx.expr1(0).accept(self) if ctx.getChildCount() == 1 else \
            BinaryOp(
                op=ctx.RELATIONAL().getText(),
                left=ctx.expr1(0).accept(self),
                right=ctx.expr1(1).accept(self)
            )


    # Visit a parse tree produced by BKITParser#expr1.
    def visitExpr1(self, ctx:BKITParser.Expr1Context):
        return ctx.expr2().accept(self) if ctx.getChildCount() == 1 else \
            BinaryOp(
                op=ctx.LOGICAL().getText(),
                left=ctx.expr1().accept(self),
                right=ctx.expr2().accept(self)
            )


    # Visit a parse tree produced by BKITParser#expr2.
    def visitExpr2(self, ctx:BKITParser.Expr2Context):
        return ctx.expr3().accept(self) if ctx.getChildCount() == 1 else \
            BinaryOp(
                op=(ctx.ADD() or ctx.MINUS()).getText(),
                left=ctx.expr2().accept(self),
                right=ctx.expr3().accept(self)
            )


    # Visit a parse tree produced by BKITParser#expr3.
    def visitExpr3(self, ctx:BKITParser.Expr3Context):
        return ctx.expr4().accept(self) if ctx.getChildCount() == 1 else \
            BinaryOp(
                op=ctx.MUL().getText(),
                left=ctx.expr3().accept(self),
                right=ctx.expr4().accept(self)
            )


    # Visit a parse tree produced by BKITParser#expr4.
    def visitExpr4(self, ctx:BKITParser.Expr4Context):
        return ctx.expr5().accept(self) if ctx.getChildCount() == 1 else \
            UnaryOp(
                op=ctx.NOT().getText(),
                body=ctx.expr4().accept(self)
            )


    # Visit a parse tree produced by BKITParser#expr5.
    def visitExpr5(self, ctx:BKITParser.Expr5Context):
        return ctx.expr6().accept(self) if ctx.getChildCount() == 1 else \
            UnaryOp(
                op=ctx.MINUS().getText(),
                body=ctx.expr5().accept(self)
            )


    # Visit a parse tree produced by BKITParser#expr6.
    def visitExpr6(self, ctx:BKITParser.Expr6Context):
        return ctx.expr7().accept(self) if ctx.getChildCount() == 1 else \
            ArrayCell(
                arr=ctx.expr7().accept(self),
                idx=ctx.idxOperator().accept(self)
            )


    # Visit a parse tree produced by BKITParser#expr7.
    def visitExpr7(self, ctx:BKITParser.Expr7Context):
        if ctx.getChildCount() == 3:
            return ctx.expr0().accept(self)
        elif ctx.ID():
            return Id(ctx.ID().getText())
        elif ctx.INT():
            return IntLiteral(int(ctx.INT().getText(), 0))
        elif ctx.FLOAT():
            return FloatLiteral(float(ctx.FLOAT().getText()))
        elif ctx.BOOLEAN():
            return BooleanLiteral(ctx.BOOLEAN().getText() == 'True')
        else:
            return ctx.callExpr().accept(self)
    

    # Visit a parse tree produced by BKITParser#idxOperator.
    def visitIdxOperator(self, ctx:BKITParser.IdxOperatorContext):
        return list(map(lambda ele: ele.accept(self), ctx.expr0()))


    # Visit a parse tree produced by BKITParser#callExpr.
    def visitCallExpr(self, ctx:BKITParser.CallExprContext):
        return CallExpr(
            method=Id(ctx.ID().getText()), 
            param=list(map(lambda ele: ele.accept(self), ctx.expr() or []))
        )
