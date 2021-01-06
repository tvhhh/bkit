
"""
 * @author nhphung
"""
from abc import ABC, abstractmethod, ABCMeta
from dataclasses import dataclass
from typing import List, Tuple
from AST import * 
from Visitor import *
from StaticError import *
from functools import *

class Type(ABC):
    __metaclass__ = ABCMeta
    def __eq__(self, o):
        return type(self) is type(o)
class Prim(Type):
    __metaclass__ = ABCMeta
    pass
class IntType(Prim):
    pass
class FloatType(Prim):
    pass
class StringType(Prim):
    pass
class BoolType(Prim):
    pass
class VoidType(Type):
    pass
class Unknown(Type):
    pass

@dataclass
class ArrayType(Type):
    dimen:List[int]
    eletype: Type
    def __eq__(self, o):
        return type(self) is type(o) and self.dimen == o.dimen and self.eletype == o.eletype

@dataclass
class MType:
    intype:List[Type]
    restype:Type

@dataclass
class Symbol:
    name: str
    mtype:Type

class Utils:
    @staticmethod
    def flatten(lst):
        return [x for sub in lst for x in sub]
    
    @staticmethod
    def lookup(lst, item):
        return None if len(lst) == 0 else lst[0] if lst[0].name == item else Utils.lookup(lst[1:], item)
    
    @staticmethod
    def lookupToGet(lst, item, kind=Identifier()):
        res = Utils.lookup(lst, item)
        if res == None or (type(kind) is Function and type(res.mtype) is not MType) or (type(kind) is Identifier and type(res.mtype) is MType):
            raise Undeclared(kind, item)
        return res
    
    @staticmethod
    def lookupToInsert(lst, item, kind=Identifier()):
        res = Utils.lookup(lst, item)
        if res != None:
            raise Redeclared(kind, item)
        return res
    
    @staticmethod
    def infer(pattern, param, stmt=None):
        if type(pattern) is not ArrayType and type(param) is not ArrayType:
            return Utils.inferScalarType(pattern, param, stmt)
        elif type(pattern) is ArrayType and type(param) is ArrayType:
            return Utils.inferArrayType(pattern, param, stmt)
        return None
    
    @staticmethod
    def inferScalarType(pattern, param, stmt=None):
        if pattern == Unknown() and param == Unknown():
            raise TypeCannotBeInferred(stmt)
        if pattern != param and pattern != Unknown() and param != Unknown():
            return None
        return pattern if param == Unknown() else param
    
    @staticmethod
    def inferArrayType(pattern, param, stmt=None):
        if pattern.dimen == param.dimen:
            eletype = Utils.inferScalarType(pattern.eletype, param.eletype, stmt)
            return ArrayType(pattern.dimen, eletype) if eletype else None
        return None

@dataclass
class Scope:
    func: Symbol
    params: List[Symbol]

class StaticChecker(BaseVisitor):
    def __init__(self,ast):
        self.ast = ast
        self.global_envi = [
            Symbol("int_of_float",MType([FloatType()],IntType())),
            Symbol("float_to_int",MType([IntType()],FloatType())),
            Symbol("int_of_string",MType([StringType()],IntType())),
            Symbol("string_of_int",MType([IntType()],StringType())),
            Symbol("float_of_string",MType([StringType()],FloatType())),
            Symbol("string_of_float",MType([FloatType()],StringType())),
            Symbol("bool_of_string",MType([StringType()],BoolType())),
            Symbol("string_of_bool",MType([BoolType()],StringType())),
            Symbol("read",MType([],StringType())),
            Symbol("printLn",MType([],VoidType())),
            Symbol("print",MType([StringType()],VoidType())),
            Symbol("printStrLn",MType([StringType()],VoidType()))
        ]
    
    def check(self):
        return self.visit(self.ast,self.global_envi)
    
    def visitProgram(self,ast, c):
        c = reduce(lambda acc, ele: self.visitName(ele, acc, Variable() if type(ele) is VarDecl else Function()), ast.decl, c)
        try:
            Utils.lookupToGet(c, "main", Function())
        except Undeclared:
            raise NoEntryPoint()
        # print(print('\n'.join('{}: {}'.format(*k) for k in enumerate(c))))
        c = reduce(lambda acc, ele: ele.accept(self, acc), ast.decl, [c])
    
    def visitName(self, ast, c, kind=Variable()):
        if type(kind) is Variable or type(kind) is Parameter:
            Utils.lookupToInsert(c, ast.variable.name, kind)
            c += [Symbol(ast.variable.name, ArrayType(ast.varDimen, Unknown()) if ast.varDimen else Unknown())]
        else:
            Utils.lookupToInsert(c, ast.name.name, Function())
            params = reduce(lambda acc, ele: self.visitName(ele, acc, Parameter()), ast.param, [])
            c += [Symbol(ast.name.name, MType(list(map(lambda ele: ele.mtype, params)), Unknown()))]
        return c
    
    def visitVarDecl(self, ast, c):
        res = Utils.lookupToGet(Utils.flatten(c), ast.variable.name, Identifier())
        res.mtype = ast.varInit.accept(self, None) if ast.varInit else ArrayType(ast.varDimen, Unknown()) if ast.varDimen else Unknown()
        return c
    
    def visitFuncDecl(self, ast, c):
        res = Utils.lookupToGet(Utils.flatten(c), ast.name.name, Function())
        params = reduce(lambda acc, ele: self.visitName(ele, acc, Parameter()), ast.param, [])
        params = [Symbol(sym.name, res.mtype.intype[i]) for i, sym in enumerate(params)]
        self.scope = Scope(res, params)
        c = self.visitScope(ast.body, c, params)
        return c
    
    def visitScope(self, ast, c, params=[]):
        c = [[x for x in params]] + c
        c[0] = reduce(lambda acc, ele: self.visitName(ele, acc, Variable()), ast[0], c[0])
        c = reduce(lambda acc, ele: ele.accept(self, acc), ast[0] + ast[1], c)
        return c[1:]
    
    def visitBinaryOp(self, ast, c):
        int_int = ['+', '-', '*', '\\', '%']
        float_float = ['+.', '-.', '*.', '\\.']
        bool_bool = ['&&', '||']
        int_bool = ['==', '!=', '<', '>', '<=', '>=']
        float_bool = ['=/=', '<.', '>.', '<=.', '>=.']
        if ast.op in int_int:
            left = ast.left.accept(self, [c[0], IntType(), c[2]])
            right = ast.right.accept(self, [c[0], IntType(), c[2]])
            if [left, right] != [IntType(), IntType()]:
                raise TypeMismatchInExpression(ast)
            return IntType()
        elif ast.op in float_float:
            left = ast.left.accept(self, [c[0], FloatType(), c[2]])
            right = ast.right.accept(self, [c[0], FloatType(), c[2]])
            if [left, right] != [FloatType(), FloatType()]:
                raise TypeMismatchInExpression(ast)
            return FloatType()
        elif ast.op in bool_bool:
            left = ast.left.accept(self, [c[0], BoolType(), c[2]])
            right = ast.right.accept(self, [c[0], BoolType(), c[2]])
            if [left, right] != [BoolType(), BoolType()]:
                raise TypeMismatchInExpression(ast)
            return BoolType()
        elif ast.op in int_bool:
            left = ast.left.accept(self, [c[0], IntType(), c[2]])
            right = ast.right.accept(self, [c[0], IntType(), c[2]])
            if [left, right] != [IntType(), IntType()]:
                raise TypeMismatchInExpression(ast)
            return BoolType()
        elif ast.op in float_bool:
            left = ast.left.accept(self, [c[0], FloatType(), c[2]])
            right = ast.right.accept(self, [c[0], FloatType(), c[2]])
            if [left, right] != [FloatType(), FloatType()]:
                raise TypeMismatchInExpression(ast)
            return BoolType()
    
    def visitUnaryOp(self, ast, c):
        if ast.op == '-':
            body = ast.body.accept(self, [c[0], IntType(), c[2]])
            if body != IntType():
                raise TypeMismatchInExpression(ast)
            return IntType()
        elif ast.op == '-.':
            body = ast.body.accept(self, [c[0], FloatType(), c[2]])
            if body != FloatType():
                raise TypeMismatchInExpression(ast)
            return FloatType()
        elif ast.op == '!':
            body = ast.body.accept(self, [c[0], BoolType(), c[2]])
            if body != BoolType():
                raise TypeMismatchInExpression(ast)
            return BoolType()
    
    def visitCall(self, ast, c):
        res = Utils.lookupToGet(Utils.flatten(c[0]), ast.method.name, Function())
        infertype = Utils.infer(res.mtype.restype, c[1], c[2]) if c[1] else res.mtype.restype
        if infertype == None and isinstance(ast, Stmt):
            raise TypeMismatchInStatement(ast)
        res.mtype.restype = infertype or res.mtype.restype
        if len(ast.param) != len(res.mtype.intype):
            raise TypeMismatchInStatement(ast) if isinstance(ast, Stmt) else TypeMismatchInExpression(ast)
        for idx, ele in enumerate(ast.param):
            expr = ele.accept(self, [c[0], res.mtype.intype[idx], c[2]])
            infertype = Utils.infer(expr, res.mtype.intype[idx], c[2])
            if infertype == None or infertype == VoidType():
                raise TypeMismatchInStatement(ast) if isinstance(ast, Stmt) else TypeMismatchInExpression(ast)
            res.mtype.intype[idx] = infertype
            if res == self.scope.func:
                self.scope.params[idx].mtype = infertype
        return res.mtype.restype
    
    def visitCallExpr(self, ast, c):
        return self.visitCall(ast, c)
    
    def visitId(self, ast, c):
        res = Utils.lookupToGet(Utils.flatten(c[0]), ast.name)
        res.mtype = (Utils.infer(res.mtype, c[1], c[2]) or res.mtype) if c[1] else res.mtype
        if res in self.scope.params:
            func = self.scope.func
            paramidx = self.scope.params.index(res)
            func.mtype.intype[paramidx] = res.mtype
        return res.mtype
    
    def visitArrayCell(self, ast, c):
        idxs = reduce(lambda acc, ele: acc + [ele.accept(self, [c[0], IntType(), c[2]]) == IntType()], ast.idx, [])
        arr = ast.arr.accept(self, [c[0], None, c[2]])
        if type(ast.arr) is CallExpr and arr == Unknown():
            raise TypeCannotBeInferred(c[2])
        if not all(idxs) or type(arr) is not ArrayType or len(arr.dimen) < len(idxs):
            raise TypeMismatchInExpression(ast)
        eletype = c[1].eletype if type(c[1]) is ArrayType else c[1]
        arr = ast.arr.accept(self, [c[0], ArrayType(arr.dimen, eletype), c[2]]) if eletype else arr
        retdim = arr.dimen[len(idxs):]
        return ArrayType(retdim, arr.eletype) if retdim else arr.eletype
    
    def visitAssign(self, ast, c):
        left = ast.lhs.accept(self, [c, None, ast])
        right = ast.rhs.accept(self, [c, left, ast])
        if left == Unknown() or type(left) is ArrayType and left.eletype == Unknown():
            left = ast.lhs.accept(self, [c, right, ast])
        infertype = Utils.infer(left, right, ast)
        if infertype == None or left == VoidType():
            raise TypeMismatchInStatement(ast)
        return c
    
    def visitIf(self, ast, c):
        def visitIfThenScope(acc, ele):
            cond = ele[0].accept(self, [c, BoolType(), ast])
            if cond != BoolType():
                raise TypeMismatchInStatement(ast)
            return self.visitScope(ele[1:], acc)
        c = reduce(visitIfThenScope, ast.ifthenStmt, c)
        c = self.visitScope(ast.elseStmt, c)
        return c
    
    def visitFor(self, ast, c):
        id = ast.idx1.accept(self, [c, IntType(), ast])
        e1 = ast.expr1.accept(self, [c, IntType(), ast])
        e2 = ast.expr2.accept(self, [c, BoolType(), ast])
        e3 = ast.expr3.accept(self, [c, IntType(), ast])
        if [id,e1,e2,e3] != [IntType(),IntType(),BoolType(),IntType()]:
            raise TypeMismatchInStatement(ast)
        c = self.visitScope(ast.loop, c)
        return c
    
    def visitContinue(self, ast, c):
        return c
    
    def visitBreak(self, ast, c):
        return c
    
    def visitReturn(self, ast, c):
        functype = self.scope.func.mtype
        etype = ast.expr.accept(self, [c, None if functype.restype == Unknown() else functype.restype, ast]) if ast.expr else VoidType()
        functype.restype = etype if functype.restype == Unknown() else functype.restype
        functype.restype = Utils.infer(functype.restype, etype, ast)
        if functype.restype == None or functype.restype == VoidType() and ast.expr:
            raise TypeMismatchInStatement(ast)
        return c
    
    def visitDowhile(self, ast, c):
        c = self.visitScope(ast.sl, c)
        exp = ast.exp.accept(self, [c, BoolType(), ast])
        if exp != BoolType():
            raise TypeMismatchInStatement(ast)
        return c

    def visitWhile(self, ast, c):
        exp = ast.exp.accept(self, [c, BoolType(), ast])
        if exp != BoolType():
            raise TypeMismatchInStatement(ast)
        c = self.visitScope(ast.sl, c)
        return c

    def visitCallStmt(self, ast, c):
        self.visitCall(ast, [c, VoidType(), ast])
        return c
    
    def visitIntLiteral(self, ast, c):
        return IntType()
    
    def visitFloatLiteral(self, ast, c):
        return FloatType()
    
    def visitBooleanLiteral(self, ast, c):
        return BoolType()
    
    def visitStringLiteral(self, ast, c):
        return StringType()

    def visitArrayLiteral(self, ast, c):
        dim, ele = self.visitArray(ast, None)
        return ArrayType(dim, ele)
    
    def visitArray(self, ast, c):
        ele = self.visitArray(ast.value[0], None) if type(ast) is ArrayLiteral else [[], ast.accept(self, None)]
        return [[len(ast.value)]+ele[0] if type(ast) is ArrayLiteral else ele[0], ele[1]]
