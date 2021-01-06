'''
 *   @author Nguyen Hua Phung
 *   @version 1.0
 *   23/10/2015
 *   This file provides a simple version of code generator
 *
'''
from Visitor import *
from Emitter import Emitter
from Frame import Frame
from AST import *
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List, Tuple
from functools import *

class MethodEnv:
    def __init__(self,frame,sym,staticFields=[]):
        self.frame = frame
        self.sym = sym
        self.staticFields = staticFields
class SubBody(MethodEnv):
    def __init__(self,frame,sym,isGlobal=False):
        self.frame = frame
        self.sym = sym
        self.isGlobal = isGlobal
class Access:
    def __init__(self,frame,sym,isLeft=False):
        self.frame = frame
        self.sym = sym
        self.isLeft = isLeft
class Symbol:
    def __init__(self,name,mtype,value = None):
        self.name = name
        self.mtype = mtype
        self.value = value
    def __str__(self):
        return f"{self.name} {self.mtype} {self.value}"
class CName:
    def __init__(self,n):
        self.value = n
class Index:
    def __init__(self,n):
        self.value = n
class Type(ABC): 
    def __eq__(self,o):
        return type(self) is type(o)
class IntType(Type): pass
class FloatType(Type): pass
class VoidType(Type): pass
class ClassType(Type):
    def __init__(self,n):
        self.cname = n
class StringType(Type): pass
class BoolType(Type): pass
class Unknown(Type): pass
class MType(Type):
    def __init__(self,i,o):
        self.partype = i #List[Type]
        self.rettype = o #Type
    def __eq__(self,o):
        return type(self) is type(o) and self.partype == o.partype and self.rettype == o.rettype
class ArrayType(Type):
    def __init__(self,et,s=None):
        self.eleType = et #Type
        self.dimen = s   #List[int]
    def __eq__(self,o):
        return type(self) is type(o) and self.dimen == o.dimen and self.eleType == o.eleType

class Kind(ABC):
    pass
class Function(Kind):
    def __str__(self):
        return "Function"
class Parameter(Kind):
    def __str__(self):
        return "Parameter"
class Variable(Kind):
    def __str__(self):
        return "Variable"
class Identifier(Kind):
    def __str__(self):
        return "Identifier"
class StaticError(Exception):
    pass
@dataclass
class Undeclared(StaticError):
    k: Kind
    n: str  # name of identifier
    def __str__(self):
        return  "Undeclared "+ str(self.k) + ": " + self.n
@dataclass
class Redeclared(StaticError):
    k: Kind
    n: str # name of identifier 
    def __str__(self):
        return  "Redeclared "+ str(self.k) + ": " + self.n
@dataclass
class TypeMismatchInExpression(StaticError):
    exp: Expr
    def __str__(self):
        return  "Type Mismatch In Expression: "+ str(self.exp)
@dataclass
class TypeMismatchInStatement(StaticError):
    stmt: Stmt
    def __str__(self):
        return "Type Mismatch In Statement: "+ str(self.stmt)
@dataclass
class TypeCannotBeInferred(StaticError):
    stmt: Stmt
    def __str__(self):
        return "Type Cannot Be Inferred: "+ str(self.stmt)
class NoEntryPoint(StaticError):
    def __str__(self):
        return "No Entry Point"
@dataclass
class NotInLoop(StaticError):
    stmt: Stmt
    def __str__(self):
        return "Statement Not In Loop: " + str(self.stmt)
@dataclass
class InvalidArrayLiteral(StaticError):
    arr: ArrayLiteral
    def __str__(self):
        return "Invalid Array Literal: " + str(self.arr)
@dataclass
class FunctionNotReturn(StaticError):
    name: str
    def __str__(self):
        return "Function Not Return: " + self.name
@dataclass
class UnreachableFunction(StaticError):
    name: str
    def __str__(self):
        return "Unreachable Function: " + self.name
@dataclass
class UnreachableStatement(StaticError):
    stmt: Stmt
    def __str__(self):
        return "Unreachable Statement: " + str(self.stmt)
@dataclass
class IndexOutOfRange(StaticError):
    cell: ArrayCell
    def __str__(self):
        return "Index Out Of Range: " + str(self.cell)

class Utils:
    @staticmethod
    def flatten(lst):
        return [x for sub in lst for x in sub]  
    @staticmethod
    def lookup(lst, item):
        try:
            return next(filter(lambda ele: ele.name == item, lst))
        except:
            return None
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
            eletype = Utils.inferScalarType(pattern.eleType, param.eleType, stmt)
            return ArrayType(eletype, pattern.dimen) if eletype else None
        return None
    @staticmethod
    def convertArrayType(typ):
        return reduce(lambda acc, ele: ArrayType(acc, ele), typ.dimen, typ.eleType)


class StaticChecker(BaseVisitor):
    @dataclass
    class Scope:
        func: Symbol
        params: List[Symbol]

    def __init__(self,ast,lib):
        self.ast = ast
        self.lib = lib
        self.global_envi = [
            Symbol("int_of_float",MType([FloatType()],IntType()),CName(self.lib)),
            Symbol("float_to_int",MType([IntType()],FloatType()),CName(self.lib)),
            Symbol("int_of_string",MType([StringType()],IntType()),CName(self.lib)),
            Symbol("string_of_int",MType([IntType()],StringType()),CName(self.lib)),
            Symbol("float_of_string",MType([StringType()],FloatType()),CName(self.lib)),
            Symbol("string_of_float",MType([FloatType()],StringType()),CName(self.lib)),
            Symbol("bool_of_string",MType([StringType()],BoolType()),CName(self.lib)),
            Symbol("string_of_bool",MType([BoolType()],StringType()),CName(self.lib)),
            Symbol("read",MType([],StringType()),CName(self.lib)),
            Symbol("printLn",MType([],VoidType()),CName(self.lib)),
            Symbol("print",MType([StringType()],VoidType()),CName(self.lib)),
            Symbol("printStrLn",MType([StringType()],VoidType()),CName(self.lib))
        ]
    
    def check(self):
        c = self.visit(self.ast,self.global_envi)
        for sym in c:
            if type(sym.mtype) is MType:
                if sym.mtype.rettype == Unknown():
                    sym.mtype.rettype = VoidType()
                elif type(sym.mtype.rettype) is ArrayType:
                    sym.mtype.rettype = Utils.convertArrayType(sym.mtype.rettype)
                sym.mtype.partype = list(map(lambda ele: Utils.convertArrayType(ele) if type(ele) is ArrayType else ele, sym.mtype.partype))
            elif type(sym.mtype) is ArrayType:
                sym.mtype = Utils.convertArrayType(sym.mtype)
            if sym.name == "main":
                sym.mtype.partype = [ArrayType(StringType())]
        return c
    
    def visitProgram(self,ast, c):
        c = reduce(lambda acc, ele: self.visitName(ele, acc, Variable() if type(ele) is VarDecl else Function()), ast.decl, c)
        try:
            Utils.lookupToGet(c, "main", Function())
        except Undeclared:
            raise NoEntryPoint()
        c = reduce(lambda acc, ele: ele.accept(self, acc), ast.decl, [c])
        return c[0]
    
    def visitName(self, ast, c, kind=Variable()):
        if type(kind) is Variable or type(kind) is Parameter:
            Utils.lookupToInsert(c, ast.variable.name, kind)
            c += [Symbol(ast.variable.name, ArrayType(Unknown(), ast.varDimen) if ast.varDimen else Unknown())]
        else:
            Utils.lookupToInsert(c, ast.name.name, Function())
            params = reduce(lambda acc, ele: self.visitName(ele, acc, Parameter()), ast.param, [])
            c += [Symbol(ast.name.name, MType(list(map(lambda ele: ele.mtype, params)), Unknown()))]
        return c
    
    def visitVarDecl(self, ast, c):
        res = Utils.lookupToGet(Utils.flatten(c), ast.variable.name, Identifier())
        res.mtype = ast.varInit.accept(self, None) if ast.varInit else ArrayType(Unknown(), ast.varDimen) if ast.varDimen else Unknown()
        return c
    
    def visitFuncDecl(self, ast, c):
        res = Utils.lookupToGet(Utils.flatten(c), ast.name.name, Function())
        params = reduce(lambda acc, ele: self.visitName(ele, acc, Parameter()), ast.param, [])
        params = [Symbol(sym.name, res.mtype.partype[i]) for i, sym in enumerate(params)]
        self.scope = self.Scope(res, params)
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
        infertype = Utils.infer(res.mtype.rettype, c[1], c[2]) if c[1] else res.mtype.rettype
        if infertype == None and isinstance(ast, Stmt):
            raise TypeMismatchInStatement(ast)
        res.mtype.rettype = infertype or res.mtype.rettype
        if len(ast.param) != len(res.mtype.partype):
            raise TypeMismatchInStatement(ast) if isinstance(ast, Stmt) else TypeMismatchInExpression(ast)
        for idx, ele in enumerate(ast.param):
            expr = ele.accept(self, [c[0], res.mtype.partype[idx], c[2]])
            infertype = Utils.infer(expr, res.mtype.partype[idx], c[2])
            if infertype == None or infertype == VoidType():
                raise TypeMismatchInStatement(ast) if isinstance(ast, Stmt) else TypeMismatchInExpression(ast)
            res.mtype.partype[idx] = infertype
            if res == self.scope.func:
                self.scope.params[idx].mtype = infertype
        return res.mtype.rettype
    
    def visitCallExpr(self, ast, c):
        return self.visitCall(ast, c)
    
    def visitId(self, ast, c):
        res = Utils.lookupToGet(Utils.flatten(c[0]), ast.name)
        res.mtype = (Utils.infer(res.mtype, c[1], c[2]) or res.mtype) if c[1] else res.mtype
        if res in self.scope.params:
            func = self.scope.func
            paramidx = self.scope.params.index(res)
            func.mtype.partype[paramidx] = res.mtype
        return res.mtype
    
    def visitArrayCell(self, ast, c):
        idxs = reduce(lambda acc, ele: acc + [ele.accept(self, [c[0], IntType(), c[2]]) == IntType()], ast.idx, [])
        arr = ast.arr.accept(self, [c[0], None, c[2]])
        if type(ast.arr) is CallExpr and arr == Unknown():
            raise TypeCannotBeInferred(c[2])
        if not all(idxs) or type(arr) is not ArrayType or len(arr.dimen) < len(idxs):
            raise TypeMismatchInExpression(ast)
        eletype = c[1].eleType if type(c[1]) is ArrayType else c[1]
        arr = ast.arr.accept(self, [c[0], ArrayType(eletype, arr.dimen), c[2]]) if eletype else arr
        retdim = arr.dimen[len(idxs):]
        return ArrayType(arr.eleType, retdim) if retdim else arr.eleType
    
    def visitAssign(self, ast, c):
        left = ast.lhs.accept(self, [c, None, ast])
        right = ast.rhs.accept(self, [c, left, ast])
        if left == Unknown() or type(left) is ArrayType and left.eleType == Unknown():
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
        etype = ast.expr.accept(self, [c, None if functype.rettype == Unknown() else functype.rettype, ast]) if ast.expr else VoidType()
        functype.rettype = etype if functype.rettype == Unknown() else functype.rettype
        functype.rettype = Utils.infer(functype.rettype, etype, ast)
        if functype.rettype == None or functype.rettype == VoidType() and ast.expr:
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
        return ArrayType(ele, dim)
    
    def visitArray(self, ast, c):
        ele = self.visitArray(ast.value[0], None) if type(ast) is ArrayLiteral else [[], ast.accept(self, None)]
        return [[len(ast.value)]+ele[0] if type(ast) is ArrayLiteral else ele[0], ele[1]]


class CodeGenerator():
    def __init__(self):
        self.libName = "io"

    def init(self):
        return []

    def gen(self, ast, dir_):
        #ast: AST
        #dir_: String
        gl = self.init() + StaticChecker(ast, self.libName).check()
        gc = CodeGenVisitor(ast, gl, dir_)
        gc.visit(ast, None)


class CodeGenVisitor(BaseVisitor):
    def __init__(self, astTree, env, dir_):
        #astTree: AST
        #env: List[Symbol]
        #dir_: File
        self.astTree = astTree
        self.className = "MCClass"
        self.env = [Symbol(sym.name, sym.mtype, CName(self.className)) if sym.value is None else sym for sym in env]
        self.path = dir_
        self.emit = Emitter(self.path + "/" + self.className + ".j")

    def visitProgram(self, ast: Program, c: any):
        #ast: Program
        #c: Any
        self.emit.printout(self.emit.emitPROLOG(self.className, "java.lang.Object"))
        c = MethodEnv(None, self.env, list(filter(lambda ele: type(ele) is VarDecl, ast.decl)))
        # self.genMain(c)
        # generate default constructor
        list(map(lambda ele: ele.accept(self, c), ast.decl))
        self.genInit()
        # generate class init if necessary
        self.emit.emitEPILOG()
        return c

    def genInit(self):
        methodname,methodtype = "<init>",MType([],VoidType())
        frame = Frame(methodname, methodtype.rettype)
        self.emit.printout(self.emit.emitMETHOD(methodname,methodtype,False,frame))
        frame.enterScope(True)
        varname,vartype,varindex = "this",ClassType(self.className),frame.getNewIndex()
        startLabel, endLabel = frame.getStartLabel(), frame.getEndLabel()
        self.emit.printout(self.emit.emitVAR(varindex, varname, vartype, startLabel, endLabel, frame))
        self.emit.printout(self.emit.emitLABEL(startLabel,frame))
        self.emit.printout(self.emit.emitREADVAR(varname, vartype, varindex, frame))
        self.emit.printout(self.emit.emitINVOKESPECIAL(frame))
        self.emit.printout(self.emit.emitLABEL(endLabel, frame))
        self.emit.printout(self.emit.emitRETURN(methodtype.rettype, frame))
        self.emit.printout(self.emit.emitENDMETHOD(frame))

    # # The following code is just for initial, students should remove it and write your visitor from here
    # def genMain(self,o):
    #     methodname,methodtype = "main",MType([ArrayType(StringType())],VoidType())
    #     frame = Frame(methodname, methodtype.rettype)
    #     self.emit.printout(self.emit.emitMETHOD(methodname,methodtype,True,frame))
    #     frame.enterScope(True)
    #     varname,vartype,varindex = "args",methodtype.partype[0],frame.getNewIndex()
    #     startLabel, endLabel = frame.getStartLabel(), frame.getEndLabel()
    #     self.emit.printout(self.emit.emitVAR(varindex, varname, vartype, startLabel, endLabel,frame ))
    #     self.emit.printout(self.emit.emitLABEL(startLabel,frame))
    #     self.emit.printout(self.emit.emitPUSHICONST(120, frame))
    #     sym = next(filter(lambda x: x.name == "string_of_int",o.sym))
    #     self.emit.printout(self.emit.emitINVOKESTATIC(sym.value.value+"/string_of_int",sym.mtype,frame))
    #     sym = next(filter(lambda x: x.name == "print",o.sym))
    #     self.emit.printout(self.emit.emitINVOKESTATIC(sym.value.value+"/print",sym.mtype,frame))
    #     self.emit.printout(self.emit.emitLABEL(endLabel, frame))
    #     self.emit.printout(self.emit.emitRETURN(methodtype.rettype, frame))
    #     self.emit.printout(self.emit.emitENDMETHOD(frame))
    
    def visitVarDecl(self, ast: VarDecl, c: MethodEnv):
        name = ast.variable.name
        if c.frame is None:
            _, typ = ast.varInit.accept(self, c)
            self.emit.printout(self.emit.emitATTRIBUTE(name, typ, False, None))
        else:
            initCode, typ = ast.varInit.accept(self, Access(c.frame, c.sym))
            if c.isGlobal:
                self.emit.printout(initCode)
                self.emit.printout(self.emit.emitPUTSTATIC(f"{self.className}.{name}", typ, c.frame))
            else:
                index = c.frame.getNewIndex()
                fromLabel,toLabel = c.frame.getStartLabel(),c.frame.getEndLabel()
                self.emit.printout(self.emit.emitVAR(index, name, typ, fromLabel, toLabel, c.frame))
                self.emit.printout(initCode)
                self.emit.printout(self.emit.emitWRITEVAR(name, typ, index, c.frame))
                c.sym = [Symbol(name, typ, Index(index))] + c.sym
    
    def visitFuncDecl(self, ast: FuncDecl, c: MethodEnv):
        sym = next(filter(lambda ele: ele.name == ast.name.name, c.sym))
        frame = Frame(sym.name, sym.mtype.rettype)
        self.emit.printout(self.emit.emitMETHOD(sym.name, sym.mtype, True, frame))
        frame.enterScope(True)
        startLabel,endLabel = frame.getStartLabel(),frame.getEndLabel()
        subBody = SubBody(frame, c.sym)
        if sym.name == "main":
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "args", sym.mtype.partype[0], startLabel, endLabel, frame))
            list(map(lambda ele: ele.accept(self, SubBody(frame, c.sym, True)), c.staticFields))
        else:
            for item in zip(ast.param, sym.mtype.partype):
                name, typ = item[0].variable.name, item[1]
                index = frame.getNewIndex()
                self.emit.printout(self.emit.emitVAR(index, name, typ, startLabel, endLabel, frame))
                subBody.sym = [Symbol(name, typ, Index(index))] + subBody.sym
        list(map(lambda ele: ele.accept(self, subBody), ast.body[0]))
        self.emit.printout(self.emit.emitLABEL(startLabel, frame))
        list(map(lambda ele: ele.accept(self, subBody), ast.body[1]))
        self.emit.printout(self.emit.emitLABEL(endLabel, frame))
        self.emit.printout(self.emit.emitRETURN(sym.mtype.rettype, frame))
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope()
    
    def visitBinaryOp(self, ast: BinaryOp, c: Access):
        op = ast.op
        leftCode, typ = ast.left.accept(self, Access(c.frame, c.sym))
        rightCode, _ = ast.right.accept(self, Access(c.frame, c.sym))
        code = leftCode + rightCode
        if op in ['+', '-', '+.', '-.']:
            return code + self.emit.emitADDOP(op[0], typ, c.frame), typ
        elif op in ['*', '\\', '*.', '\\.']:
            return code + self.emit.emitMULOP(op[0], typ, c.frame), typ
        elif op == '%':
            return code + self.emit.emitMOD(c.frame), IntType()
        elif op == '&&':
            return code + self.emit.emitANDOP(c.frame), BoolType()
        elif op == '||':
            return code + self.emit.emitOROP(c.frame), BoolType()
        elif op in ['==', '!=', '<', '>', '<=', '>=', '<.', '>.', '<=.', '>=.']:
            return code + self.emit.emitREOP(op[:-1] if op[-1] == '.' else op, typ, c.frame), BoolType()
        elif op == '=/=':
            return code + self.emit.emitREOP('!=', typ, c.frame), BoolType()
    
    def visitUnaryOp(self, ast: UnaryOp, c: Access):
        op = ast.op
        rightCode, typ = ast.body.accept(self, Access(c.frame, c.sym))
        if op in ['-', '-.']:
            return rightCode + self.emit.emitNEGOP(typ, c.frame), typ
        elif op == '!':
            return rightCode + self.emit.emitNOT(BoolType(), c.frame), BoolType()
    
    def visitCallExpr(self, ast: CallExpr, c: Access):
        sym = next(filter(lambda ele: ele.name == ast.method.name, c.sym))
        expCode = list(map(lambda ele: ele.accept(self, Access(c.frame, c.sym))[0], ast.param))
        invokeCode = self.emit.emitINVOKESTATIC(f"{sym.value.value}/{sym.name}", sym.mtype, c.frame)
        return ''.join(expCode) + invokeCode, sym.mtype.rettype
    
    def visitId(self, ast: Id, c: Access):
        sym = next(filter(lambda ele: ele.name == ast.name, c.sym))
        if type(sym.value) is Index:
            return self.emit.emitWRITEVAR(sym.name, sym.mtype, sym.value.value, c.frame) if c.isLeft \
                else self.emit.emitREADVAR(sym.name, sym.mtype, sym.value.value, c.frame), sym.mtype
        else:
            return self.emit.emitPUTSTATIC(f"{sym.value.value}.{sym.name}", sym.mtype, c.frame) if c.isLeft \
                else self.emit.emitGETSTATIC(f"{sym.value.value}.{sym.name}", sym.mtype, c.frame), sym.mtype
    
    def visitArrayCell(self, ast: ArrayCell, c: Access):
        arrCode, typ = ast.arr.accept(self, Access(c.frame, c.sym))
        typ = typ.eleType
        idxCode, rettyp = reduce(lambda acc, ele: 
            (acc[0] + self.emit.emitALOAD(acc[1], c.frame) + ele.accept(self, Access(c.frame, c.sym))[0], acc[1].eleType), 
            ast.idx[1:], 
            (ast.idx[0].accept(self, Access(c.frame, c.sym))[0], typ))
        rCode = self.emit.emitALOAD(rettyp, c.frame) if not c.isLeft else ""
        return arrCode + idxCode + rCode, rettyp
    
    def visitAssign(self, ast: Assign, c: SubBody):
        if type(ast.lhs) is ArrayCell:
            leftCode, typ = ast.lhs.accept(self, Access(c.frame, c.sym, True))
            rightCode, _ = ast.rhs.accept(self, Access(c.frame, c.sym))
            self.emit.printout(leftCode)
            self.emit.printout(rightCode)
            self.emit.printout(self.emit.emitASTORE(typ, c.frame))
        else:
            rightCode, _ = ast.rhs.accept(self, Access(c.frame, c.sym))
            leftCode, _ = ast.lhs.accept(self, Access(c.frame, c.sym, True))
            self.emit.printout(rightCode)
            self.emit.printout(leftCode)
    
    def visitIf(self, ast: If, c: SubBody):
        endLabel = c.frame.getNewLabel()
        def visitIfThenScope(scope):
            subBody = SubBody(c.frame, c.sym)
            newLabel = c.frame.getNewLabel()
            expCode, _ = scope[0].accept(self, Access(c.frame, c.sym))
            self.emit.printout(expCode)
            self.emit.printout(self.emit.emitIFFALSE(newLabel, c.frame))
            list(map(lambda ele: ele.accept(self, subBody), scope[1] + scope[2]))
            self.emit.printout(self.emit.emitGOTO(endLabel, c.frame))
            self.emit.printout(self.emit.emitLABEL(newLabel, c.frame))
        subBody = SubBody(c.frame, c.sym)
        list(map(visitIfThenScope, ast.ifthenStmt))
        list(map(lambda ele: ele.accept(self, subBody), ast.elseStmt[0] + ast.elseStmt[1]))
        self.emit.printout(self.emit.emitLABEL(endLabel, c.frame))
    
    def visitFor(self, ast: For, c: SubBody):
        c.frame.enterLoop()
        exp1Code, _ = ast.expr1.accept(self, Access(c.frame, c.sym))
        exp2Code, _ = ast.expr2.accept(self, Access(c.frame, c.sym))
        exp3Code, _ = ast.expr3.accept(self, Access(c.frame, c.sym))
        idRCode, _ = ast.idx1.accept(self, Access(c.frame, c.sym))
        idWCode, _ = ast.idx1.accept(self, Access(c.frame, c.sym, True))
        subBody = SubBody(c.frame, c.sym)
        enterLabel = c.frame.getNewLabel()
        self.emit.printout(exp1Code)
        self.emit.printout(idWCode)
        self.emit.printout(self.emit.emitGOTO(enterLabel, c.frame))
        self.emit.printout(self.emit.emitLABEL(c.frame.getContinueLabel(), c.frame))
        self.emit.printout(exp3Code)
        self.emit.printout(idRCode)
        self.emit.printout(self.emit.emitADDOP('+', IntType(), c.frame))
        self.emit.printout(idWCode)
        self.emit.printout(self.emit.emitLABEL(enterLabel, c.frame))
        self.emit.printout(exp2Code)
        self.emit.printout(self.emit.emitIFFALSE(c.frame.getBreakLabel(), c.frame))
        list(map(lambda ele: ele.accept(self, subBody), ast.loop[0] + ast.loop[1]))
        self.emit.printout(self.emit.emitGOTO(c.frame.getContinueLabel(), c.frame))
        self.emit.printout(self.emit.emitLABEL(c.frame.getBreakLabel(), c.frame))
        c.frame.exitLoop()
    
    def visitContinue(self, ast: Continue, c: SubBody):
        self.emit.printout(self.emit.emitGOTO(c.frame.getContinueLabel(), c.frame))
    
    def visitBreak(self, ast: Break, c: SubBody):
        self.emit.printout(self.emit.emitGOTO(c.frame.getBreakLabel(), c.frame))
    
    def visitReturn(self, ast: Return, c: SubBody):
        # typ = VoidType()
        if ast.expr:
            expCode, typ = ast.expr.accept(self, Access(c.frame, c.sym))
            self.emit.printout(expCode)
        # self.emit.printout(self.emit.emitRETURN(typ, c.frame))
        self.emit.printout(self.emit.emitGOTO(c.frame.getEndLabel(), c.frame))
    
    def visitDowhile(self, ast: Dowhile, c: SubBody):
        c.frame.enterLoop()
        subBody = SubBody(c.frame, c.sym)
        self.emit.printout(self.emit.emitLABEL(c.frame.getContinueLabel(), c.frame))
        expCode, _ = ast.exp.accept(self, Access(c.frame, c.sym))
        list(map(lambda ele: ele.accept(self, subBody), ast.sl[0] + ast.sl[1]))
        self.emit.printout(expCode)
        self.emit.printout(self.emit.emitIFTRUE(c.frame.getContinueLabel(), c.frame))
        self.emit.printout(self.emit.emitLABEL(c.frame.getBreakLabel(), c.frame))
        c.frame.exitLoop()

    def visitWhile(self, ast: While, c: SubBody):
        c.frame.enterLoop()
        subBody = SubBody(c.frame, c.sym)
        self.emit.printout(self.emit.emitLABEL(c.frame.getContinueLabel(), c.frame))
        expCode, _ = ast.exp.accept(self, Access(c.frame, c.sym))
        self.emit.printout(expCode)
        self.emit.printout(self.emit.emitIFFALSE(c.frame.getBreakLabel(), c.frame))
        list(map(lambda ele: ele.accept(self, subBody), ast.sl[0] + ast.sl[1]))
        self.emit.printout(self.emit.emitGOTO(c.frame.getContinueLabel(), c.frame))
        self.emit.printout(self.emit.emitLABEL(c.frame.getBreakLabel(), c.frame))
        c.frame.exitLoop()

    def visitCallStmt(self, ast: CallStmt, c: SubBody):
        sym = next(filter(lambda ele: ele.name == ast.method.name, c.sym))
        list(map(lambda ele: self.emit.printout(ele.accept(self, Access(c.frame, c.sym))[0]), ast.param))
        self.emit.printout(self.emit.emitINVOKESTATIC(f"{sym.value.value}/{sym.name}", sym.mtype, c.frame))
    
    def visitIntLiteral(self, ast: IntLiteral, c: Access):
        return self.emit.emitPUSHICONST(ast.value, c.frame) if c.frame else None, IntType()
    
    def visitFloatLiteral(self, ast: FloatLiteral, c: Access):
        return self.emit.emitPUSHFCONST(str(ast.value), c.frame) if c.frame else None, FloatType()
    
    def visitBooleanLiteral(self, ast: BooleanLiteral, c: Access):
        return self.emit.emitPUSHICONST(str(ast.value).lower(), c.frame) if c.frame else None, BoolType()
    
    def visitStringLiteral(self, ast: StringLiteral, c: Access):
        return self.emit.emitPUSHCONST(ast.value, StringType(), c.frame) if c.frame else None, StringType()

    def visitArrayLiteral(self, ast: ArrayLiteral, c: Access):
        def visitArray(arr):
            if type(arr) is IntLiteral:
                return IntType()
            elif type(arr) is FloatLiteral:
                return FloatType()
            elif type(arr) is BooleanLiteral:
                return BoolType()
            elif type(arr) is StringLiteral:
                return StringType()
            else:
                return ArrayType(visitArray(arr.value[0]), len(arr.value))
        typ = visitArray(ast)
        return self.emit.emitPUSHACONST(ast, typ, c.frame) if c.frame else None, typ

    
