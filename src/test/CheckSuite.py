import unittest
from TestUtils import TestChecker
from StaticError import *
from AST import *

class CheckSuite(unittest.TestCase):

	def test_checker_0(self):
		input = """
		Function: main
		Body:
		    foo();
		EndBody.
		"""
		expect = str(Undeclared(Function(),"foo"))
		self.assertTrue(TestChecker.test(input,expect,400))

	def test_checker_1(self):
		input = """
		Function: main  
		Body:
		    printStrLn();
		EndBody.
		"""
		expect = str(TypeMismatchInStatement(CallStmt(Id("printStrLn"),[])))
		self.assertTrue(TestChecker.test(input,expect,401))

	def test_checker_2(self):
		input = """
		Function: main 
		Body:
		    printStrLn(read(4));
		EndBody.
		"""
		expect = str(TypeMismatchInExpression(CallExpr(Id("read"),[IntLiteral(4)])))
		self.assertTrue(TestChecker.test(input,expect,402))

	def test_checker_3(self):
		input = """
		Function: main
		Body:
		    Var: x, x;
		EndBody.
		"""
		expect = str(Redeclared(Variable(),"x"))
		self.assertTrue(TestChecker.test(input,expect,403))

	def test_checker_4(self):
		input = """
		Function: main
		Parameter: x, x
		Body:
		EndBody.
		"""
		expect = str(Redeclared(Parameter(),"x"))
		self.assertTrue(TestChecker.test(input,expect,404))

	def test_checker_5(self):
		input = """
		Var: x;
		Function: x
		Body:
		EndBody.
		Function: main
		Body:
		EndBody.
		"""
		expect = str(Redeclared(Function(),"x"))
		self.assertTrue(TestChecker.test(input,expect,405))

	def test_checker_6(self):
		input = """
		Var: x;
		Function: main
		Body:
		    x();
		EndBody.
		"""
		expect = str(Undeclared(Function(),"x"))
		self.assertTrue(TestChecker.test(input,expect,406))

	def test_checker_7(self):
		input = """
		Function: main
		Body:
		    x = 1;
		EndBody.
		"""
		expect = str(Undeclared(Identifier(),"x"))
		self.assertTrue(TestChecker.test(input,expect,407))

	def test_checker_8(self):
		input = """
		Function: main
		Parameter: x
		Body:
		    Var: x;
		EndBody.
		"""
		expect = str(Redeclared(Variable(),"x"))
		self.assertTrue(TestChecker.test(input,expect,408))

	def test_checker_9(self):
		input = """
		Function: main
		Parameter: x
		Body:
		    x();
		EndBody.
		"""
		expect = str(Undeclared(Function(),"x"))
		self.assertTrue(TestChecker.test(input,expect,409))

	def test_checker_10(self):
		input = """
		Function: main
		Parameter: x
		Body:
		    x = x();
		EndBody.
		"""
		expect = str(Undeclared(Function(),"x"))
		self.assertTrue(TestChecker.test(input,expect,410))

	def test_checker_11(self):
		input = """
		Function: x
		Body:
		EndBody.
		Function: main
		Parameter: x
		Body:
		    x();
		EndBody.
		"""
		expect = str(Undeclared(Function(),"x"))
		self.assertTrue(TestChecker.test(input,expect,411))

	def test_checker_12(self):
		input = """
		Function: x
		Body:
		EndBody.
		Function: main
		Body:
		    x = 1;
		EndBody.
		"""
		expect = str(Undeclared(Identifier(),"x"))
		self.assertTrue(TestChecker.test(input,expect,412))

	def test_checker_13(self):
		input = """
		Function: x
		Parameter: x
		Body:
		    x = 1;
		    main(x);
		EndBody.
		Function: main
		Body:
		EndBody.
		"""
		expect = str(TypeMismatchInStatement(CallStmt(Id("main"),[Id("x")])))
		self.assertTrue(TestChecker.test(input,expect,413))

	def test_checker_14(self):
		input = """
		Var: x, y, z;
		Function: main
		Parameter: x, y
		Body:
		    x(y, z);
		EndBody.
		"""
		expect = str(Undeclared(Function(),"x"))
		self.assertTrue(TestChecker.test(input,expect,414))

	def test_checker_15(self):
		input = """
		Function: main
		Body:
		    Var: a, b[5];
		    a = b;
		EndBody.
		"""
		expect = str(TypeMismatchInStatement(Assign(Id("a"),Id("b"))))
		self.assertTrue(TestChecker.test(input,expect,415))

	def test_checker_16(self):
		input = """
		Function: foo
		Body:
		    Var: a;
		EndBody.
		Function: main
		Body:
		    a = 1;
		EndBody.
		"""
		expect = str(Undeclared(Identifier(),"a"))
		self.assertTrue(TestChecker.test(input,expect,416))

	def test_checker_17(self):
		input = """
		Function: main
		Body:
		EndBody.
		Function: main
		Body:
		EndBody.
		"""
		expect = str(Redeclared(Function(),"main"))
		self.assertTrue(TestChecker.test(input,expect,417))

	def test_checker_18(self):
		input = """
		Var: main;
		Function: main
		Body:
		EndBody.
		"""
		expect = str(Redeclared(Function(),"main"))
		self.assertTrue(TestChecker.test(input,expect,418))

	def test_checker_19(self):
		input = """
		Var: x;
		Function: x
		Body:
		EndBody.
		Function: main
		Body:
		EndBody.
		"""
		expect = str(Redeclared(Function(),"x"))
		self.assertTrue(TestChecker.test(input,expect,419))

	def test_checker_20(self):
		input = """
		Function: foo
		Body:
		    Var: x, y;
		    x = y;
		EndBody.
		Function: main
		Body:
		EndBody.
		"""
		expect = str(TypeCannotBeInferred(Assign(Id("x"),Id("y"))))
		self.assertTrue(TestChecker.test(input,expect,420))

	def test_checker_21(self):
		input = """
		Function: foo
		Body:
		    Var: x, y = 1, z;
		    x = y;
		    y = z;
		EndBody.
		Function: main
		Body:
		EndBody.
		"""
		expect = str()
		self.assertTrue(TestChecker.test(input,expect,421))

	def test_checker_22(self):
		input = """
		Function: foo
		Body:
		    Var: x[5], y[5];
		    x = y;
		EndBody.
		Function: main
		Body:
		EndBody.
		"""
		expect = str(TypeCannotBeInferred(Assign(Id("x"),Id("y"))))
		self.assertTrue(TestChecker.test(input,expect,422))

	def test_checker_23(self):
		input = """
		Function: foo
		Body:
		    Var: x, y[5];
		    x = y;
		EndBody.
		Function: main
		Body:
		EndBody.
		"""
		expect = str(TypeMismatchInStatement(Assign(Id("x"),Id("y"))))
		self.assertTrue(TestChecker.test(input,expect,423))

	def test_checker_24(self):
		input = """
		Function: foo
		Body:
		    Var: x;
		    Return x;
		EndBody.
		Function: main
		Body:
		EndBody.
		"""
		expect = str(TypeCannotBeInferred(Return(Id("x"))))
		self.assertTrue(TestChecker.test(input,expect,424))

	def test_checker_25(self):
		input = """
		Function: main
		Body:
		    foo();
		EndBody.
		Function: foo
		Body:
		    Var: x = 1;
		    Return x;
		EndBody.
		"""
		expect = str(TypeMismatchInStatement(Return(Id("x"))))
		self.assertTrue(TestChecker.test(input,expect,425))

	def test_checker_26(self):
		input = """
		Function: main
		Body:
		    Var: x;
		    x = foo();
		EndBody.
		Function: foo
		Body:
		EndBody.
		"""
		expect = str(TypeCannotBeInferred(Assign(Id("x"),CallExpr(Id("foo"),[]))))
		self.assertTrue(TestChecker.test(input,expect,426))

	def test_checker_27(self):
		input = """
		Function: main
		Body:
		    Var: x = 1;
		    x = foo();
		EndBody.
		Function: foo
		Body:
		    Return;
		EndBody.
		"""
		expect = str(TypeMismatchInStatement(Return(None)))
		self.assertTrue(TestChecker.test(input,expect,427))

	def test_checker_28(self):
		input = """
		Function: main
		Body:
		    foo();
		EndBody.
		Function: foo
		Body:
		    main();
		EndBody.
		"""
		expect = str()
		self.assertTrue(TestChecker.test(input,expect,428))

	def test_checker_29(self):
		input = """
		Function: main
		Body:
		    Var: x = 0;
		    foo(x);
		EndBody.
		Function: foo
		Parameter: a, b
		Body:
		    Return;
		EndBody.
		"""
		expect = str(TypeMismatchInStatement(CallStmt(Id("foo"),[Id("x")])))
		self.assertTrue(TestChecker.test(input,expect,429))

	def test_checker_30(self):
		input = """
		Function: main
		Body:
		    Var: x, y = 1;
		    x = foo(y) + 1;
		    Return x;
		EndBody.
		Function: foo
		Parameter: a
		Body:
		    a = 1.5;
		EndBody.
		"""
		expect = str(TypeMismatchInStatement(Assign(Id("a"),FloatLiteral(1.5))))
		self.assertTrue(TestChecker.test(input,expect,430))

	def test_checker_31(self):
		input = """
		Function: main
		Body:
		    Var: x, y = 1;
		    x = foo(y) + 1;
		    Return x;
		EndBody.
		Function: foo
		Parameter: a
		Body:
		    Return 0.5;
		EndBody.
		"""
		expect = str(TypeMismatchInStatement(Return(FloatLiteral(0.5))))
		self.assertTrue(TestChecker.test(input,expect,431))

	def test_checker_32(self):
		input = """
		Function: foo
		Parameter: x
		Body:
		    Var: a[1] = {0};
		    Return a;
		EndBody.
		Function: main
		Body:
		    foo(0)[0] = foo(0.0)[0];
		EndBody.
		"""
		expect = str(TypeMismatchInExpression(CallExpr(Id("foo"),[FloatLiteral(0.0)])))
		self.assertTrue(TestChecker.test(input,expect,432))

	def test_checker_33(self):
		input = """
		Var: x;
		Function: main
		Body:
		    x = 1 + 2.0;
		EndBody.
		"""
		expect = str(TypeMismatchInExpression(BinaryOp("+",IntLiteral(1),FloatLiteral(2.0))))
		self.assertTrue(TestChecker.test(input,expect,433))

	def test_checker_34(self):
		input = """
		Var: x;
		Function: main
		Body:
		    x = 1 && True;
		EndBody.
		"""
		expect = str(TypeMismatchInExpression(BinaryOp("&&",IntLiteral(1),BooleanLiteral(True))))
		self.assertTrue(TestChecker.test(input,expect,434))

	def test_checker_35(self):
		input = """
		Var: x;
		Function: main
		Body:
		    x = 1 + int_of_float(2.0);
		EndBody.
		"""
		expect = str()
		self.assertTrue(TestChecker.test(input,expect,435))

	def test_checker_36(self):
		input = """
		Var: x;
		Function: main
		Body:
		    x = float_to_int(1) +. 2.0;
		EndBody.
		"""
		expect = str()
		self.assertTrue(TestChecker.test(input,expect,436))

	def test_checker_37(self):
		input = """
		Var: x;
		Function: main
		Body:
		    printStrLn(read() + 1);
		EndBody.
		"""
		expect = str(TypeMismatchInExpression(BinaryOp("+",CallExpr(Id("read"),[]),IntLiteral(1))))
		self.assertTrue(TestChecker.test(input,expect,437))

	def test_checker_38(self):
		input = """
		Var: x;
		Function: main
		Body:
		    x = bool_of_string(read()) && bool_of_string(string_of_bool(True));
		EndBody.
		"""
		expect = str()
		self.assertTrue(TestChecker.test(input,expect,438))

	def test_checker_39(self):
		input = """
		Var: x;
		Function: main
		Body:
		    x = 1;
		    x = 2;
		    x = string_of_int(x);
		EndBody.
		"""
		expect = str(TypeMismatchInStatement(Assign(Id("x"),CallExpr(Id("string_of_int"),[Id("x")]))))
		self.assertTrue(TestChecker.test(input,expect,439))

	def test_checker_40(self):
		input = """
		Var: x;
		Function: main
		Body:
		    x = 1;
		    x = main();
		    main();
		EndBody.
		"""
		expect = str(TypeMismatchInStatement(CallStmt(Id("main"),[])))
		self.assertTrue(TestChecker.test(input,expect,440))

	def test_checker_41(self):
		input = """
		Function: main
		Body:
		    foo()[0] = 1;
		EndBody.
		Function: foo
		Body:
		    Return 0;
		EndBody.
		"""
		expect = str(TypeCannotBeInferred(Assign(ArrayCell(CallExpr(Id("foo"),[]),[IntLiteral(0)]),IntLiteral(1))))
		self.assertTrue(TestChecker.test(input,expect,441))

	def test_checker_42(self):
		input = """
		Var: x;
		Function: main
		Body:
		    x = x;
		EndBody.
		"""
		expect = str(TypeCannotBeInferred(Assign(Id("x"),Id("x"))))
		self.assertTrue(TestChecker.test(input,expect,442))

	def test_checker_43(self):
		input = """
		Var: x;
		Function: main
		Body:
		    x = -x;
		EndBody.
		"""
		expect = str()
		self.assertTrue(TestChecker.test(input,expect,443))

	def test_checker_44(self):
		input = """
		Var: x;
		Function: main
		Body:
		    x = -.-x;
		EndBody.
		"""
		expect = str(TypeMismatchInExpression(UnaryOp("-.",UnaryOp("-",Id("x")))))
		self.assertTrue(TestChecker.test(input,expect,444))

	def test_checker_45(self):
		input = """
		Var: x = 0;
		Function: foo
		Parameter: x
		Body:
		    x = 0.5;
		EndBody.
		Function: main
		Body:
		    x = 1.5;
		EndBody.
		"""
		expect = str(TypeMismatchInStatement(Assign(Id("x"),FloatLiteral(1.5))))
		self.assertTrue(TestChecker.test(input,expect,445))

	def test_checker_46(self):
		input = """
		Var: x = 0;
		Function: foo
		Parameter: a
		Body:
		    x = main(x) + a;
		EndBody.
		Function: main
		Parameter: a
		Body:
		    x = foo(a);
		    a = a +. 1.0;
		EndBody.
		"""
		expect = str(TypeMismatchInExpression(BinaryOp("+.",Id("a"),FloatLiteral(1.0))))
		self.assertTrue(TestChecker.test(input,expect,446))

	def test_checker_47(self):
		input = """
		Function: main
		Body:
		    Var: x[5];
		    Return x;
		EndBody.
		"""
		expect = str(TypeCannotBeInferred(Return(Id("x"))))
		self.assertTrue(TestChecker.test(input,expect,447))

	def test_checker_48(self):
		input = """
		Var: x, y, z;
		Function: a
		Parameter: x, y
		Body:
		    Return x + y + z;
		EndBody.
		Function: b
		Parameter: y, z
		Body:
		    Return x +. y +. z;
		EndBody.
		Function: c
		Parameter: x, z
		Body:
		    Return x && y && z;
		EndBody.
		Function: main
		Body:
		EndBody.
		"""
		expect = str()
		self.assertTrue(TestChecker.test(input,expect,448))

	def test_checker_49(self):
		input = """
		Var: x = 1, y = 1.0, z;
		Function: foo
		Body:
		    z = float_to_int(x + int_of_float(y +. float_to_int(x + int_of_float(y)))) >=. 2.0 *. (float_to_int(x) +. y);
		    Return z;
		EndBody.
		Function: main
		Body:
		    Var: a;
		    a = z;
		    Return a || foo();
		EndBody.
		"""
		expect = str()
		self.assertTrue(TestChecker.test(input,expect,449))

	def test_checker_50(self):
		input = """
		Function: main
		Body:
		    Var: a;
		    a = a =/= 1.0;
		EndBody.
		"""
		expect = str(TypeMismatchInStatement(Assign(Id("a"),BinaryOp("=/=",Id("a"),FloatLiteral(1.0)))))
		self.assertTrue(TestChecker.test(input,expect,450))

	def test_checker_51(self):
		input = """
		Function: main
		Parameter: a
		Body:
		    main(main(5));
		EndBody.
		"""
		expect = str(TypeMismatchInStatement(CallStmt(Id("main"),[CallExpr(Id("main"),[IntLiteral(5)])])))
		self.assertTrue(TestChecker.test(input,expect,451))

	def test_checker_52(self):
		input = """
		Var: x = 0, y[5], z[5][5], t[5][5][5];
		Function: main
		Body:
		    t[z[y[x]][x]][y[x]][x] = 0;
		EndBody.
		"""
		expect = str()
		self.assertTrue(TestChecker.test(input,expect,452))

	def test_checker_53(self):
		input = """
		Function: main
		Parameter: a
		Body:
		    If main(main(5)) Then
		    EndIf.
		EndBody.
		"""
		expect = str(TypeMismatchInExpression(CallExpr(Id("main"),[CallExpr(Id("main"),[IntLiteral(5)])])))
		self.assertTrue(TestChecker.test(input,expect,453))

	def test_checker_54(self):
		input = """
		Function: main
		Body:
		    Var: a[10], x;
		    a[x] = a[x] =/= 1.0;
		EndBody.
		"""
		expect = str(TypeMismatchInStatement(Assign(ArrayCell(Id("a"),[Id("x")]),BinaryOp("=/=",ArrayCell(Id("a"),[Id("x")]),FloatLiteral(1.0)))))
		self.assertTrue(TestChecker.test(input,expect,454))

	def test_checker_55(self):
		input = """
		Function: main
		Body:
		    Var: a[10], x;
		    a[x] = a[a[x]] + a[a[a[x]]];
		EndBody.
		"""
		expect = str()
		self.assertTrue(TestChecker.test(input,expect,455))

	def test_checker_56(self):
		input = """
		Function: main
		Body:
		    Var: a[10], x;
		    a[x] = a[a[x]] +. a[a[a[x]]];
		EndBody.
		"""
		expect = str(TypeMismatchInExpression(BinaryOp("+.",ArrayCell(Id("a"),[ArrayCell(Id("a"),[Id("x")])]),ArrayCell(Id("a"),[ArrayCell(Id("a"),[ArrayCell(Id("a"),[Id("x")])])]))))
		self.assertTrue(TestChecker.test(input,expect,456))

	def test_checker_57(self):
		input = """
		Function: main
		Body:
		    Var: main;
		    main();
		EndBody.
		"""
		expect = str(Undeclared(Function(),"main"))
		self.assertTrue(TestChecker.test(input,expect,457))

	def test_checker_58(self):
		input = """
		Function: foo
		Parameter: a
		Body:
		    a = 0;
		    a = main(a);
		    foo(main(a));
		EndBody.
		Function: main
		Parameter: a
		Body:
		    a = foo(a);
		EndBody.
		"""
		expect = str(TypeMismatchInStatement(Assign(Id("a"),CallExpr(Id("foo"),[Id("a")]))))
		self.assertTrue(TestChecker.test(input,expect,458))

	def test_checker_59(self):
		input = """
		Function: a
		Parameter: x
		Body:
		    x = 0;
		    b(x);
		EndBody.
		Function: b
		Parameter: x
		Body:
		    c(x);
		EndBody.
		Function: c
		Parameter: x
		Body:
		    a(x);
		EndBody.
		Function: main
		Body:
		    main(a(x));
		EndBody.
		"""
		expect = str(TypeMismatchInStatement(CallStmt(Id("main"),[CallExpr(Id("a"),[Id("x")])])))
		self.assertTrue(TestChecker.test(input,expect,459))

	def test_checker_60(self):
		input = """
		Function: main
		Body:
		    Var: a[2], b[2] = {1.2,2.2};
		    a[0] = b[a[0]];
		EndBody.
		"""
		expect = str(TypeMismatchInStatement(Assign(ArrayCell(Id("a"),[IntLiteral(0)]),ArrayCell(Id("b"),[ArrayCell(Id("a"),[IntLiteral(0)])]))))
		self.assertTrue(TestChecker.test(input,expect,460))

	def test_checker_61(self):
		input = """
		Function: foo
		Body:
		    foo();
		    Return foo();
		EndBody.
		Function: main
		Body:
		EndBody.
		"""
		expect = str(TypeMismatchInStatement(Return(CallExpr(Id("foo"),[]))))
		self.assertTrue(TestChecker.test(input,expect,461))

	def test_checker_62(self):
		input = """
		Function: main
		Parameter: x
		Body:
		    If main(main(x)) Then
		        x = False;
		        main(x);
		    EndIf.
		EndBody.
		"""
		expect = str(TypeCannotBeInferred(If([(CallExpr(Id("main"),[CallExpr(Id("main"),[Id("x")])]),[],[Assign(Id("x"),BooleanLiteral(False)),CallStmt(Id("main"),[Id("x")])])],([],[]))))
		self.assertTrue(TestChecker.test(input,expect,462))

	def test_checker_63(self):
		input = """
		Function: main
		Body:
		    If main() Then
		        Return 0;
		    Else
		        Return 0.5;
		    EndIf.
		EndBody.
		"""
		expect = str(TypeMismatchInStatement(Return(IntLiteral(0))))
		self.assertTrue(TestChecker.test(input,expect,463))

	def test_checker_64(self):
		input = """
		Function: main
		Parameter: a
		Body:
		    For (a = 0, a <. 10, 1) Do
		    EndFor.
		EndBody.
		"""
		expect = str(TypeMismatchInExpression(BinaryOp("<.",Id("a"),IntLiteral(10))))
		self.assertTrue(TestChecker.test(input,expect,464))

	def test_checker_65(self):
		input = """
		Function: main
		Parameter: a
		Body:
		    If a > 1 Then
		        If a >. 1.0 Then
		        EndIf.
		    EndIf.
		EndBody.
		"""
		expect = str(TypeMismatchInExpression(BinaryOp(">.",Id("a"),FloatLiteral(1.0))))
		self.assertTrue(TestChecker.test(input,expect,465))

	def test_checker_66(self):
		input = """
		Function: main
		Parameter: a[10], x
		Body:
		    If a[a[x]] Then
		    EndIf.
		EndBody.
		"""
		expect = str(TypeMismatchInStatement(If([(ArrayCell(Id("a"),[ArrayCell(Id("a"),[Id("x")])]),[],[])],([],[]))))
		self.assertTrue(TestChecker.test(input,expect,466))

	def test_checker_67(self):
		input = """
		Function: main
		Parameter: a[10], x
		Body:
		    If a[x] Then
		        a[x+1] = a[x] && a[x-1];
		        Return main(a, x+1);
		    EndIf.
		EndBody.
		"""
		expect = str(TypeCannotBeInferred(Return(CallExpr(Id("main"),[Id("a"),BinaryOp("+",Id("x"),IntLiteral(1))]))))
		self.assertTrue(TestChecker.test(input,expect,467))

	def test_checker_68(self):
		input = """
		Function: foo
		Parameter: x
		Body:
		    x = 1;
		    If main(x) Then
		        x = foo(x);
		    EndIf.
		EndBody.
		Function: main
		Parameter: x
		Body:
		    If foo(x) Then
		        Return True;
		    EndIf.
		EndBody.
		"""
		expect = str(TypeMismatchInStatement(If([(CallExpr(Id("foo"),[Id("x")]),[],[Return(BooleanLiteral(True))])],([],[]))))
		self.assertTrue(TestChecker.test(input,expect,468))

	def test_checker_69(self):
		input = """
		Function: main
		Parameter: a[10]
		Body:
		    If True Then
		        Return;
		    Else
		        Return a[1];
		    EndIf.
		EndBody.
		"""
		expect = str(TypeMismatchInStatement(Return(ArrayCell(Id("a"),[IntLiteral(1)]))))
		self.assertTrue(TestChecker.test(input,expect,469))

	def test_checker_70(self):
		input = """
		Function: main
		Parameter: x
		Body:
		    While x Do
		        x = 1;
		    EndWhile.
		EndBody.
		"""
		expect = str(TypeMismatchInStatement(Assign(Id("x"),IntLiteral(1))))
		self.assertTrue(TestChecker.test(input,expect,470))

	def test_checker_71(self):
		input = """
		Function: main
		Parameter: x
		Body:
		    Do
		        x = 1;
		    While x EndDo.
		EndBody.
		"""
		expect = str(TypeMismatchInStatement(Dowhile(([],[Assign(Id("x"),IntLiteral(1))]),Id("x"))))
		self.assertTrue(TestChecker.test(input,expect,471))

	def test_checker_72(self):
		input = """
		Function: foo
		Parameter: x[3]
		Body:
		    x[0] = x[1] + x[2];
		    Return x[0];
		EndBody.
		Function: main
		Parameter: x[5]
		Body:
		    x = {1, 2, 3, 4, 5};
		    Return x[foo(x[foo(x[foo(x)])])];
		EndBody.
		"""
		expect = str(TypeMismatchInExpression(CallExpr(Id("foo"),[Id("x")])))
		self.assertTrue(TestChecker.test(input,expect,472))

	def test_checker_73(self):
		input = """
		Function: main
		Body:
		    If True Then
		        Var: x = 0;
		    EndIf.
		    Return x;
		EndBody.
		"""
		expect = str(Undeclared(Identifier(),"x"))
		self.assertTrue(TestChecker.test(input,expect,473))

	def test_checker_74(self):
		input = """
		Function: main
		Body:
		    Var: x;
		    x = foo(5.0) + 1;
		EndBody.
		Function: foo
		Parameter: a
		Body:
		    Return a;
		EndBody.
		"""
		expect = str(TypeMismatchInStatement(Return(Id("a"))))
		self.assertTrue(TestChecker.test(input,expect,474))

	def test_checker_75(self):
		input = """
		Function: main
		Body:
		    Var: x = 0;
		    x = foo(x, {1, 2});
		EndBody.
		Function: foo
		Parameter: a, b[5]
		Body:
		    Return a + b[0];
		EndBody.
		"""
		expect = str(TypeMismatchInExpression(CallExpr(Id("foo"),[Id("x"),ArrayLiteral([IntLiteral(1),IntLiteral(2)])])))
		self.assertTrue(TestChecker.test(input,expect,475))

	def test_checker_76(self):
		input = """
		Function: main
		Parameter: x
		Body:
		    If x == 0 Then
		        Return x;    
		    Else
		        Var: x;
		        x = main(x);
		    EndIf.
		EndBody.
		"""
		expect = str()
		self.assertTrue(TestChecker.test(input,expect,476))

	def test_checker_77(self):
		input = """
		Function: main
		Parameter: x
		Body:
		    Var: i = 0, j;
		    If main(i) Then
		        If x == 0 Then
		            Return j;
		        Else
		            Return main(j);
		        EndIf.
		    EndIf.
		EndBody.
		"""
		expect = str(TypeMismatchInExpression(CallExpr(Id("main"),[Id("j")])))
		self.assertTrue(TestChecker.test(input,expect,477))

	def test_checker_78(self):
		input = """
		Function: foo
		Parameter: x
		Body:
		    Return -.main(foo(x));
		EndBody.
		Function: main
		Parameter: x
		Body:
		    Return -.x;
		EndBody.
		"""
		expect = str(TypeCannotBeInferred(Return(UnaryOp("-.",CallExpr(Id("main"),[CallExpr(Id("foo"),[Id("x")])])))))
		self.assertTrue(TestChecker.test(input,expect,478))

	def test_checker_79(self):
		input = """
		Function: main
		Body:
		    Return a(1.0) +. 1.0;
		EndBody.
		Function: a
		Parameter: x
		Body:
		    Return b(int_of_float(x));
		EndBody.
		Function: b
		Parameter: x
		Body:
		    Return c(string_of_int(x));
		EndBody.
		Function: c
		Parameter: x
		Body:
		    Return a(float_of_string(x));
		EndBody.
		"""
		expect = str()
		self.assertTrue(TestChecker.test(input,expect,479))

	def test_checker_80(self):
		input = """
		Function: a
		Parameter: x
		Body:
		    Return x + 1;
		EndBody.
		Function: b
		Parameter: x
		Body:
		    Return a(x);
		EndBody.
		Function: c
		Parameter: x
		Body:
		    Return b(x);
		EndBody.
		Function: main
		Parameter: x
		Body:
		    While a(b(x)) == b(c(x)) Do
		        Do
		            x = x + 1;
		        While c(b(x)) == b(a(x)) EndDo.
		    EndWhile.
		EndBody.
		"""
		expect = str()
		self.assertTrue(TestChecker.test(input,expect,480))

	def test_checker_81(self):
		input = """
		Function: a
		Parameter: x
		Body:
		    Return x + 1;
		EndBody.
		Function: b
		Parameter: x
		Body:
		    Return a(x) == b(x);
		EndBody.
		Function: main
		Body:
		EndBody.
		"""
		expect = str(TypeMismatchInStatement(Return(BinaryOp("==",CallExpr(Id("a"),[Id("x")]),CallExpr(Id("b"),[Id("x")])))))
		self.assertTrue(TestChecker.test(input,expect,481))

	def test_checker_82(self):
		input = """
		Function: main
		Parameter: x
		Body:
		    If main(x > 1) Then
		    EndIf.
		EndBody.
		"""
		expect = str(TypeMismatchInExpression(CallExpr(Id("main"),[BinaryOp(">",Id("x"),IntLiteral(1))])))
		self.assertTrue(TestChecker.test(input,expect,482))

	def test_checker_83(self):
		input = """
		Function: main
		Parameter: x
		Body:
		    If main(x && True) Then
		        Return x;
		    Else
		        Return a({1, 2});
		    EndIf.
		EndBody.
		Function: a
		Parameter: x[2]
		Body:
		    Return x[0];
		EndBody.
		"""
		expect = str(TypeMismatchInStatement(Return(ArrayCell(Id("x"),[IntLiteral(0)]))))
		self.assertTrue(TestChecker.test(input,expect,483))

	def test_checker_84(self):
		input = """
		Function: main
		Body:
		    Return int_of_float(a({1.0, 2.0}));
		EndBody.
		Function: a
		Parameter: x[2]
		Body:
		    Return x[0];
		EndBody.
		Function: b
		Parameter: x[2][2]
		Body:
		    Return a(x[0]);
		EndBody.
		Function: c
		Parameter: x[2][2][2]
		Body:
		    Return b(x[0]);
		EndBody.
		"""
		expect = str()
		self.assertTrue(TestChecker.test(input,expect,484))

	def test_checker_85(self):
		input = """
		Function: main
		Body:
		    Return int_of_float(a(1.0));
		EndBody.
		Function: a
		Parameter: x
		Body:
		    Return main();
		EndBody.
		"""
		expect = str(TypeMismatchInStatement(Return(CallExpr(Id("main"),[]))))
		self.assertTrue(TestChecker.test(input,expect,485))

	def test_checker_86(self):
		input = """
		Function: main
		Parameter: x
		Body:
		    x = 10;
		    x = foo(x);
		    Return float_to_int(x);
		EndBody.
		Function: foo
		Parameter: x
		Body:
		    Return foo(main(x));
		EndBody.
		"""
		expect = str(TypeMismatchInExpression(CallExpr(Id("foo"),[CallExpr(Id("main"),[Id("x")])])))
		self.assertTrue(TestChecker.test(input,expect,486))

	def test_checker_87(self):
		input = """
		Function: main
		Parameter: main
		Body:
		    If main Then
		        Var: main;
		        For (main = main, main == main, main) Do
		            Var: main;
		            While main =/= main Do
		                Var: main;
		                Do
		                    Return main;
		                While main && main EndDo.
		            EndWhile.
		        EndFor.
		    EndIf.
		EndBody.
		"""
		expect = str(TypeCannotBeInferred(Return(Id("main"))))
		self.assertTrue(TestChecker.test(input,expect,487))

	def test_checker_88(self):
		input = """
		Var: a, b;
		Function: a
		Body:
		    Return a() + b;
		EndBody.
		Function: b
		Body:
		    Return a + b();
		EndBody.
		Function: main
		Body:
		    Return a + b;
		EndBody.
		"""
		expect = str(Redeclared(Function(),"a"))
		self.assertTrue(TestChecker.test(input,expect,488))

	def test_checker_89(self):
		input = """
		Function: main
		Parameter: x, y
		Body:
		    Var: a;
		    x = 0;
		    a = 1;
		    main(x, a);
		    y = 1.0;
		EndBody.
		"""
		expect = str(TypeMismatchInStatement(Assign(Id("y"),FloatLiteral(1.0))))
		self.assertTrue(TestChecker.test(input,expect,489))

	def test_checker_90(self):
		input = """
		Function: foo
		Parameter: x
		Body:
		    If x > 0 Then
		        Var: a;
		        a = foo(x-1);
		    Else
		        Return 0;
		    EndIf.
		EndBody.
		Function: main
		Body:
		EndBody.
		"""
		expect = str(TypeCannotBeInferred(Assign(Id("a"),CallExpr(Id("foo"),[BinaryOp("-",Id("x"),IntLiteral(1))]))))
		self.assertTrue(TestChecker.test(input,expect,490))

	def test_checker_91(self):
		input = """
		Function: main
		Parameter: x
		Body:
		    Var: a, b, c;
		    a = int_of_string(x);
		    b = float_to_int(a);
		    Return main(b) + 1;
		EndBody.
		"""
		expect = str(TypeMismatchInExpression(CallExpr(Id("main"),[Id("b")])))
		self.assertTrue(TestChecker.test(input,expect,491))

	def test_checker_92(self):
		input = """
		Var: x;
		Function: foo
		Parameter: x
		Body:
		    Return foo(foo(x)) +. 1.0;
		EndBody.
		Function: main
		Parameter: a
		Body:
		    x = foo(a);
		EndBody.
		"""
		expect = str(TypeCannotBeInferred(Return(BinaryOp("+.",CallExpr(Id("foo"),[CallExpr(Id("foo"),[Id("x")])]),FloatLiteral(1.0)))))
		self.assertTrue(TestChecker.test(input,expect,492))

	def test_checker_93(self):
		input = """
		Function: foo
		Parameter: x
		Body:
		    Return foo(foo(x)+foo(x));
		EndBody.
		Function: main
		Body:
		EndBody.
		"""
		expect = str(TypeCannotBeInferred(Return(CallExpr(Id("foo"),[BinaryOp("+",CallExpr(Id("foo"),[Id("x")]),CallExpr(Id("foo"),[Id("x")]))]))))
		self.assertTrue(TestChecker.test(input,expect,493))

	def test_checker_94(self):
		input = """
		Function: main
		Body:
		    Var: x = 0;
		    If f(g(x)) == g(f(x)) Then
		        printStrLn("Hello World");
		    EndIf.
		EndBody.
		Function: f
		Parameter: x
		Body:
		    Return f(x);
		EndBody.
		Function: g
		Parameter: x
		Body:
		    Return g(x);
		EndBody.
		"""
		expect = str(TypeCannotBeInferred(If([(BinaryOp("==",CallExpr(Id("f"),[CallExpr(Id("g"),[Id("x")])]),CallExpr(Id("g"),[CallExpr(Id("f"),[Id("x")])])),[],[CallStmt(Id("printStrLn"),[StringLiteral("Hello World")])])],([],[]))))
		self.assertTrue(TestChecker.test(input,expect,494))

	def test_checker_95(self):
		input = """
		Var: a[10];
		Function: main
		Body:
		    Var: x;
		    x = a[x]; 
		EndBody.
		Function: foo
		Body:
		    a[0] = 0.5;
		EndBody.
		"""
		expect = str(TypeCannotBeInferred(Assign(Id("x"),ArrayCell(Id("a"),[Id("x")]))))
		self.assertTrue(TestChecker.test(input,expect,495))

	def test_checker_96(self):
		input = """
		Var: a = 0, b = 1, c = 2;
		Function: foo
		Parameter: x, y, z
		Body:
		    foo(a, b, c);
		EndBody.
		Function: main
		Parameter: x, y, z
		Body:
		    x = y +. z;
		    foo(x, y, z);
		EndBody.
		"""
		expect = str(TypeMismatchInStatement(CallStmt(Id("foo"),[Id("x"),Id("y"),Id("z")])))
		self.assertTrue(TestChecker.test(input,expect,496))

	def test_checker_97(self):
		input = """
		Function: main
		Body:
		    Var: x[10];
		    x[x[foo(x)]] = 1;
		EndBody.
		Function: foo
		Parameter: x[10]
		Body:
		    Return 0;
		EndBody.
		"""
		expect = str(TypeCannotBeInferred(Assign(ArrayCell(Id("x"),[ArrayCell(Id("x"),[CallExpr(Id("foo"),[Id("x")])])]),IntLiteral(1))))
		self.assertTrue(TestChecker.test(input,expect,497))

	def test_checker_98(self):
		input = """
		Function: main
		Parameter: x[5]
		Body:
		    If x[x[0]] > foo(x) Then
		        Var: a[5];
		        a[0] = a[foo(a)];
		    EndIf.
		EndBody.
		Function: foo
		Parameter: x[5]
		Body:
		EndBody.
		"""
		expect = str()
		self.assertTrue(TestChecker.test(input,expect,498))

	def test_checker_99(self):
		input = """
		Function: main
		Body:
		    printStrLn("Hello World!");
		EndBody.
		"""
		expect = str()
		self.assertTrue(TestChecker.test(input,expect,499))

