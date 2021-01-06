import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):

	def test_program_0(self):
		input = """
			Var: x;
		"""
		expect = Program([VarDecl(Id("x"),[],None)])
		self.assertTrue(TestAST.checkASTGen(input,expect,300))

	def test_program_1(self):
		input = """
			Var: x = 0;
		"""
		expect = Program([VarDecl(Id("x"),[],IntLiteral(0))])
		self.assertTrue(TestAST.checkASTGen(input,expect,301))

	def test_program_2(self):
		input = """
			Var: x, y = 1, z;
		"""
		expect = Program([VarDecl(Id("x"),[],None),VarDecl(Id("y"),[],IntLiteral(1)),VarDecl(Id("z"),[],None)])
		self.assertTrue(TestAST.checkASTGen(input,expect,302))

	def test_program_3(self):
		input = """
			Var: x[3] = {1, 2, 3};
		"""
		expect = Program([VarDecl(Id("x"),[3],ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3)]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,303))

	def test_program_4(self):
		input = """
			Var: x[2][3] = {{1,2,3},{4,5,6}};
		"""
		expect = Program([VarDecl(Id("x"),[2,3],ArrayLiteral([ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3)]),ArrayLiteral([IntLiteral(4),IntLiteral(5),IntLiteral(6)])]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,304))

	def test_program_5(self):
		input = """
			Var: x, y = 0, z[2] = {1,2}, a[2][3] = {{1,2,3},{4,5,6}};
		"""
		expect = Program([VarDecl(Id("x"),[],None),VarDecl(Id("y"),[],IntLiteral(0)),VarDecl(Id("z"),[2],ArrayLiteral([IntLiteral(1),IntLiteral(2)])),VarDecl(Id("a"),[2,3],ArrayLiteral([ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3)]),ArrayLiteral([IntLiteral(4),IntLiteral(5),IntLiteral(6)])]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,305))

	def test_program_6(self):
		input = """
			Function: abc
			    Body:
			    EndBody.
		"""
		expect = Program([FuncDecl(Id("abc"),[],([],[]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,306))

	def test_program_7(self):
		input = """
			Function: main
			    Parameter: n
			    Body:
			    EndBody.
		"""
		expect = Program([FuncDecl(Id("main"),[VarDecl(Id("n"),[],None)],([],[]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,307))

	def test_program_8(self):
		input = """
			Function: main
			    Parameter: n
			    Body:
			        Var: x;
			        print(x);
			    EndBody.
		"""
		expect = Program([FuncDecl(Id("main"),[VarDecl(Id("n"),[],None)],([VarDecl(Id("x"),[],None)],[CallStmt(Id("print"),[Id("x")])]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,308))

	def test_program_9(self):
		input = """
			Function: main
			    Parameter: n
			    Body:
			        Var: x, y = 0;
			        print(x + y);
			    EndBody.
		"""
		expect = Program([FuncDecl(Id("main"),[VarDecl(Id("n"),[],None)],([VarDecl(Id("x"),[],None),VarDecl(Id("y"),[],IntLiteral(0))],[CallStmt(Id("print"),[BinaryOp("+",Id("x"),Id("y"))])]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,309))

	def test_program_10(self):
		input = """
			Function: main
			    Parameter: n
			    Body:
			        Var: x, y = 0;
			        print(x + y + n);
			    EndBody.
		"""
		expect = Program([FuncDecl(Id("main"),[VarDecl(Id("n"),[],None)],([VarDecl(Id("x"),[],None),VarDecl(Id("y"),[],IntLiteral(0))],[CallStmt(Id("print"),[BinaryOp("+",BinaryOp("+",Id("x"),Id("y")),Id("n"))])]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,310))

	def test_program_11(self):
		input = """
			Var: x;
			Function: main
			    Body:
			        print(x);
			    EndBody.
		"""
		expect = Program([VarDecl(Id("x"),[],None),FuncDecl(Id("main"),[],([],[CallStmt(Id("print"),[Id("x")])]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,311))

	def test_program_12(self):
		input = """
			Function: main
			    Body:
			        Var: x;
			        x = 1 + 2;
			    EndBody.
		"""
		expect = Program([FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],None)],[Assign(Id("x"),BinaryOp("+",IntLiteral(1),IntLiteral(2)))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,312))

	def test_program_13(self):
		input = """
			Function: main
			    Body:
			        Var: x, y, z;
			        x = y * z;
			    EndBody.
		"""
		expect = Program([FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],None),VarDecl(Id("y"),[],None),VarDecl(Id("z"),[],None)],[Assign(Id("x"),BinaryOp("*",Id("y"),Id("z")))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,313))

	def test_program_14(self):
		input = """
			Function: main
			    Body:
			        Var: x, y, z;
			        x = (x+y)*(x+z)\\(y+z);
			    EndBody.
		"""
		expect = Program([FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],None),VarDecl(Id("y"),[],None),VarDecl(Id("z"),[],None)],[Assign(Id("x"),BinaryOp("\\",BinaryOp("*",BinaryOp("+",Id("x"),Id("y")),BinaryOp("+",Id("x"),Id("z"))),BinaryOp("+",Id("y"),Id("z"))))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,314))

	def test_program_15(self):
		input = """
			Function: main
			    Body:
			        Var: x, a, b, c;
			        x = (a > b) && (b < c);
			    EndBody.
		"""
		expect = Program([FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],None),VarDecl(Id("a"),[],None),VarDecl(Id("b"),[],None),VarDecl(Id("c"),[],None)],[Assign(Id("x"),BinaryOp("&&",BinaryOp(">",Id("a"),Id("b")),BinaryOp("<",Id("b"),Id("c"))))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,315))

	def test_program_16(self):
		input = """
			Function: main
			    Body:
			        Var: x, y, z;
			        x = (x + y) * (y +. z) % x;
			    EndBody.
		"""
		expect = Program([FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],None),VarDecl(Id("y"),[],None),VarDecl(Id("z"),[],None)],[Assign(Id("x"),BinaryOp("%",BinaryOp("*",BinaryOp("+",Id("x"),Id("y")),BinaryOp("+.",Id("y"),Id("z"))),Id("x")))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,316))

	def test_program_17(self):
		input = """
			Function: main
			    Body:
			        Var: x, y, z;
			        x = !x + !!y + !!!z;
			    EndBody.
		"""
		expect = Program([FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],None),VarDecl(Id("y"),[],None),VarDecl(Id("z"),[],None)],[Assign(Id("x"),BinaryOp("+",BinaryOp("+",UnaryOp("!",Id("x")),UnaryOp("!",UnaryOp("!",Id("y")))),UnaryOp("!",UnaryOp("!",UnaryOp("!",Id("z"))))))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,317))

	def test_program_18(self):
		input = """
			Function: main
			    Body:
			        Var: x;
			        x = x[0] + x[1] + x[2];
			    EndBody.
		"""
		expect = Program([FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],None)],[Assign(Id("x"),BinaryOp("+",BinaryOp("+",ArrayCell(Id("x"),[IntLiteral(0)]),ArrayCell(Id("x"),[IntLiteral(1)])),ArrayCell(Id("x"),[IntLiteral(2)])))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,318))

	def test_program_19(self):
		input = """
			Function: main
			    Body:
			        Var: x, y, z;
			        x = x[(y+z)*y*z] * (x[y] + x[x[z]]);
			    EndBody.
		"""
		expect = Program([FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],None),VarDecl(Id("y"),[],None),VarDecl(Id("z"),[],None)],[Assign(Id("x"),BinaryOp("*",ArrayCell(Id("x"),[BinaryOp("*",BinaryOp("*",BinaryOp("+",Id("y"),Id("z")),Id("y")),Id("z"))]),BinaryOp("+",ArrayCell(Id("x"),[Id("y")]),ArrayCell(Id("x"),[ArrayCell(Id("x"),[Id("z")])]))))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,319))

	def test_program_20(self):
		input = """
			Function: main
			    Body:
			        Var: x, y, z;
			        x = x[x[y]+foo(z)*(y-z\\x)];
			    EndBody.
		"""
		expect = Program([FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],None),VarDecl(Id("y"),[],None),VarDecl(Id("z"),[],None)],[Assign(Id("x"),ArrayCell(Id("x"),[BinaryOp("+",ArrayCell(Id("x"),[Id("y")]),BinaryOp("*",CallExpr(Id("foo"),[Id("z")]),BinaryOp("-",Id("y"),BinaryOp("\\",Id("z"),Id("x")))))]))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,320))

	def test_program_21(self):
		input = """
			Function: main
			    Body:
			        Var: x, y, z;
			        x = (x+y)[y+z*(z-y)];
			    EndBody.
		"""
		expect = Program([FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],None),VarDecl(Id("y"),[],None),VarDecl(Id("z"),[],None)],[Assign(Id("x"),ArrayCell(BinaryOp("+",Id("x"),Id("y")),[BinaryOp("+",Id("y"),BinaryOp("*",Id("z"),BinaryOp("-",Id("z"),Id("y"))))]))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,321))

	def test_program_22(self):
		input = """
			Function: main
			    Body:
			        Var: x, y, z;
			        x = x + x[y] + x[z[y]];
			    EndBody.
		"""
		expect = Program([FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],None),VarDecl(Id("y"),[],None),VarDecl(Id("z"),[],None)],[Assign(Id("x"),BinaryOp("+",BinaryOp("+",Id("x"),ArrayCell(Id("x"),[Id("y")])),ArrayCell(Id("x"),[ArrayCell(Id("z"),[Id("y")])])))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,322))

	def test_program_23(self):
		input = """
			Function: main
			    Body:
			        Var: x, y, z;
			        x = x[x[y][z]][x[y][z]];
			    EndBody.
		"""
		expect = Program([FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],None),VarDecl(Id("y"),[],None),VarDecl(Id("z"),[],None)],[Assign(Id("x"),ArrayCell(Id("x"),[ArrayCell(Id("x"),[Id("y"),Id("z")]),ArrayCell(Id("x"),[Id("y"),Id("z")])]))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,323))

	def test_program_24(self):
		input = """
			Function: main
			    Body:
			        Var: x, y, z;
			        x = -x[y[z]];
			    EndBody.
		"""
		expect = Program([FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],None),VarDecl(Id("y"),[],None),VarDecl(Id("z"),[],None)],[Assign(Id("x"),UnaryOp("-",ArrayCell(Id("x"),[ArrayCell(Id("y"),[Id("z")])])))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,324))

	def test_program_25(self):
		input = """
			Function: main
			    Body:
			        Var: x;
			        x = True && False;
			    EndBody.
		"""
		expect = Program([FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],None)],[Assign(Id("x"),BinaryOp("&&",BooleanLiteral(True),BooleanLiteral(False)))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,325))

	def test_program_26(self):
		input = """
			Function: main
			    Body:
			        Var: x, y, z;
			        x = foo(x) + y[z];
			    EndBody.
		"""
		expect = Program([FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],None),VarDecl(Id("y"),[],None),VarDecl(Id("z"),[],None)],[Assign(Id("x"),BinaryOp("+",CallExpr(Id("foo"),[Id("x")]),ArrayCell(Id("y"),[Id("z")])))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,326))

	def test_program_27(self):
		input = """
			Function: main
			    Body:
			        Var: x, y;
			        x = y[1] + y[0xABC] + y[0o123] + y[1+0xABC*0o123];
			    EndBody.
		"""
		expect = Program([FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],None),VarDecl(Id("y"),[],None)],[Assign(Id("x"),BinaryOp("+",BinaryOp("+",BinaryOp("+",ArrayCell(Id("y"),[IntLiteral(1)]),ArrayCell(Id("y"),[IntLiteral(2748)])),ArrayCell(Id("y"),[IntLiteral(83)])),ArrayCell(Id("y"),[BinaryOp("+",IntLiteral(1),BinaryOp("*",IntLiteral(2748),IntLiteral(83)))])))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,327))

	def test_program_28(self):
		input = """
			Function: main
			    Body:
			        Var: x, y, z;
			        x = y[z][z+1][z+2][z+3][z+4][z+5][fact(z)];
			    EndBody.
		"""
		expect = Program([FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],None),VarDecl(Id("y"),[],None),VarDecl(Id("z"),[],None)],[Assign(Id("x"),ArrayCell(Id("y"),[Id("z"),BinaryOp("+",Id("z"),IntLiteral(1)),BinaryOp("+",Id("z"),IntLiteral(2)),BinaryOp("+",Id("z"),IntLiteral(3)),BinaryOp("+",Id("z"),IntLiteral(4)),BinaryOp("+",Id("z"),IntLiteral(5)),CallExpr(Id("fact"),[Id("z")])]))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,328))

	def test_program_29(self):
		input = """
			Function: main
			    Body:
			        Var: a, b;
			        a = int_of_string(read());
			        b = float_of_int(a) +. 2.0;
			    EndBody.
		"""
		expect = Program([FuncDecl(Id("main"),[],([VarDecl(Id("a"),[],None),VarDecl(Id("b"),[],None)],[Assign(Id("a"),CallExpr(Id("int_of_string"),[CallExpr(Id("read"),[])])),Assign(Id("b"),BinaryOp("+.",CallExpr(Id("float_of_int"),[Id("a")]),FloatLiteral(2.0)))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,329))

	def test_program_30(self):
		input = """
			Function: main
			    Body:
			        Var: x;
			        x = foo(foo(foo(foo(foo(x))))) + func();
			    EndBody.
		"""
		expect = Program([FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],None)],[Assign(Id("x"),BinaryOp("+",CallExpr(Id("foo"),[CallExpr(Id("foo"),[CallExpr(Id("foo"),[CallExpr(Id("foo"),[CallExpr(Id("foo"),[Id("x")])])])])]),CallExpr(Id("func"),[])))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,330))

	def test_program_31(self):
		input = """
			Function: main
			    Body:
			        Var: x, y, z;
			        x = foo(x, y+z, y[z][x], foo(x));
			    EndBody.
		"""
		expect = Program([FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],None),VarDecl(Id("y"),[],None),VarDecl(Id("z"),[],None)],[Assign(Id("x"),CallExpr(Id("foo"),[Id("x"),BinaryOp("+",Id("y"),Id("z")),ArrayCell(Id("y"),[Id("z"),Id("x")]),CallExpr(Id("foo"),[Id("x")])]))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,331))

	def test_program_32(self):
		input = """
			Function: main
			    Body:
			        Var: x, y;
			        x = y[foo(y[foo(y[foo(y[foo(y[foo(y)])])])])];
			    EndBody.
		"""
		expect = Program([FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],None),VarDecl(Id("y"),[],None)],[Assign(Id("x"),ArrayCell(Id("y"),[CallExpr(Id("foo"),[ArrayCell(Id("y"),[CallExpr(Id("foo"),[ArrayCell(Id("y"),[CallExpr(Id("foo"),[ArrayCell(Id("y"),[CallExpr(Id("foo"),[ArrayCell(Id("y"),[CallExpr(Id("foo"),[Id("y")])])])])])])])])])]))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,332))

	def test_program_33(self):
		input = """
			Function: main
			    Body:
			        Var: x, y;
			        x[y] = y[x];
			    EndBody.
		"""
		expect = Program([FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],None),VarDecl(Id("y"),[],None)],[Assign(ArrayCell(Id("x"),[Id("y")]),ArrayCell(Id("y"),[Id("x")]))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,333))

	def test_program_34(self):
		input = """
			Function: main
			    Body:
			        Var: x;
			        x = !-.foo(a[b + c]);
			    EndBody.
		"""
		expect = Program([FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],None)],[Assign(Id("x"),UnaryOp("!",UnaryOp("-.",CallExpr(Id("foo"),[ArrayCell(Id("a"),[BinaryOp("+",Id("b"),Id("c"))])]))))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,334))

	def test_program_35(self):
		input = """
			Function: main
			    Body:
			        Var: x;
			        x = !!!--.--.--.foo(x);
			    EndBody.
		"""
		expect = Program([FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],None)],[Assign(Id("x"),UnaryOp("!",UnaryOp("!",UnaryOp("!",UnaryOp("-",UnaryOp("-.",UnaryOp("-",UnaryOp("-.",UnaryOp("-",UnaryOp("-.",CallExpr(Id("foo"),[Id("x")])))))))))))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,335))

	def test_program_36(self):
		input = """
			Function: main
			    Body:
			        Var: x, y;
			        x = -y[!y[-.y[!y[x]]]][!-.-x][---y[!x]];
			    EndBody.
		"""
		expect = Program([FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],None),VarDecl(Id("y"),[],None)],[Assign(Id("x"),UnaryOp("-",ArrayCell(Id("y"),[UnaryOp("!",ArrayCell(Id("y"),[UnaryOp("-.",ArrayCell(Id("y"),[UnaryOp("!",ArrayCell(Id("y"),[Id("x")]))]))])),UnaryOp("!",UnaryOp("-.",UnaryOp("-",Id("x")))),UnaryOp("-",UnaryOp("-",UnaryOp("-",ArrayCell(Id("y"),[UnaryOp("!",Id("x"))]))))])))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,336))

	def test_program_37(self):
		input = """
			Function: main
			    Body:
			        Var: x, y, z;
			        x = func1(x)
			            + y[z]
			            + func2(y)
			            + !!x
			            + y % z
			            + y < z;
			    EndBody.
		"""
		expect = Program([FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],None),VarDecl(Id("y"),[],None),VarDecl(Id("z"),[],None)],[Assign(Id("x"),BinaryOp("<",BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",CallExpr(Id("func1"),[Id("x")]),ArrayCell(Id("y"),[Id("z")])),CallExpr(Id("func2"),[Id("y")])),UnaryOp("!",UnaryOp("!",Id("x")))),BinaryOp("%",Id("y"),Id("z"))),Id("y")),Id("z")))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,337))

	def test_program_38(self):
		input = """
			Function: main
			    Body:
			        Var: x;
			        x = x && x < x + x * !-x[foo(x)];
			    EndBody.
		"""
		expect = Program([FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],None)],[Assign(Id("x"),BinaryOp("<",BinaryOp("&&",Id("x"),Id("x")),BinaryOp("+",Id("x"),BinaryOp("*",Id("x"),UnaryOp("!",UnaryOp("-",ArrayCell(Id("x"),[CallExpr(Id("foo"),[Id("x")])])))))))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,338))

	def test_program_39(self):
		input = """
			Function: main
			    Parameter: n
			    Body:
			        If n == 0 Then
			            Return 1;
			        Else
			            Return n * fact (n - 1);
			        EndIf.
			    EndBody.
		"""
		expect = Program([FuncDecl(Id("main"),[VarDecl(Id("n"),[],None)],([],[If([(BinaryOp("==",Id("n"),IntLiteral(0)),[],[Return(IntLiteral(1))])],([],[Return(BinaryOp("*",Id("n"),CallExpr(Id("fact"),[BinaryOp("-",Id("n"),IntLiteral(1))])))]))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,339))

	def test_program_40(self):
		input = """
			Function: main
			    Parameter: x
			    Body: 
			        If x == 0 Then 
			            x = 1; 
			        EndIf.
			    EndBody.
		"""
		expect = Program([FuncDecl(Id("main"),[VarDecl(Id("x"),[],None)],([],[If([(BinaryOp("==",Id("x"),IntLiteral(0)),[],[Assign(Id("x"),IntLiteral(1))])],([],[]))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,340))

	def test_program_41(self):
		input = """
			Function: main
			    Parameter: x
			    Body:
			        If x == 0 Then
			            x = 1;
			        ElseIf x == 1 Then
			            x = 0;
			        EndIf.
			    EndBody.
		"""
		expect = Program([FuncDecl(Id("main"),[VarDecl(Id("x"),[],None)],([],[If([(BinaryOp("==",Id("x"),IntLiteral(0)),[],[Assign(Id("x"),IntLiteral(1))]),(BinaryOp("==",Id("x"),IntLiteral(1)),[],[Assign(Id("x"),IntLiteral(0))])],([],[]))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,341))

	def test_program_42(self):
		input = """
			Function: main
			    Body:
			        For (i = 0, i < 10, 2) Do
			            print(i);
			        EndFor.
			    EndBody.
		"""
		expect = Program([FuncDecl(Id("main"),[],([],[For(Id("i"),IntLiteral(0),BinaryOp("<",Id("i"),IntLiteral(10)),IntLiteral(2),([],[CallStmt(Id("print"),[Id("i")])]))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,342))

	def test_program_43(self):
		input = """
			Function: main
			    Body:
			        For (i = 0, i < 10, 1) Do
			            If i % 2 == 0 Then
			                print(i);
			            EndIf.
			        EndFor.
			    EndBody.
		"""
		expect = Program([FuncDecl(Id("main"),[],([],[For(Id("i"),IntLiteral(0),BinaryOp("<",Id("i"),IntLiteral(10)),IntLiteral(1),([],[If([(BinaryOp("==",BinaryOp("%",Id("i"),IntLiteral(2)),IntLiteral(0)),[],[CallStmt(Id("print"),[Id("i")])])],([],[]))]))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,343))

	def test_program_44(self):
		input = """
			Function: main
			    Parameter: n
			    Body:
			        If n > 0 Then
			            For (i = n, i > 0, -1) Do
			                print(i);
			            EndFor.
			        EndIf.
			    EndBody.
		"""
		expect = Program([FuncDecl(Id("main"),[VarDecl(Id("n"),[],None)],([],[If([(BinaryOp(">",Id("n"),IntLiteral(0)),[],[For(Id("i"),Id("n"),BinaryOp(">",Id("i"),IntLiteral(0)),UnaryOp("-",IntLiteral(1)),([],[CallStmt(Id("print"),[Id("i")])]))])],([],[]))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,344))

	def test_program_45(self):
		input = """
			Function: main
			    Parameter: n
			    Body:
			        While n > 0 Do
			            n = n - 1;
			        EndWhile.
			    EndBody.
		"""
		expect = Program([FuncDecl(Id("main"),[VarDecl(Id("n"),[],None)],([],[While(BinaryOp(">",Id("n"),IntLiteral(0)),([],[Assign(Id("n"),BinaryOp("-",Id("n"),IntLiteral(1)))]))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,345))

	def test_program_46(self):
		input = """
			Function: main
			    Parameter: n
			    Body:
			        While n > 0 Do
			            For (i = 0, i < 10, 1) Do
			                If i > 5 Then
			                    print(i);
			                EndIf.
			            EndFor.
			        EndWhile.
			    EndBody.
		"""
		expect = Program([FuncDecl(Id("main"),[VarDecl(Id("n"),[],None)],([],[While(BinaryOp(">",Id("n"),IntLiteral(0)),([],[For(Id("i"),IntLiteral(0),BinaryOp("<",Id("i"),IntLiteral(10)),IntLiteral(1),([],[If([(BinaryOp(">",Id("i"),IntLiteral(5)),[],[CallStmt(Id("print"),[Id("i")])])],([],[]))]))]))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,346))

	def test_program_47(self):
		input = """
			Function: main
			    Parameter: n
			    Body:
			        While n > 0 Do
			        EndWhile.
			    EndBody.
		"""
		expect = Program([FuncDecl(Id("main"),[VarDecl(Id("n"),[],None)],([],[While(BinaryOp(">",Id("n"),IntLiteral(0)),([],[]))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,347))

	def test_program_48(self):
		input = """
			Function: main
			    Parameter: n
			    Body:
			        Do
			            n = n - 1;
			        While n > 0 EndDo.
			    EndBody.
		"""
		expect = Program([FuncDecl(Id("main"),[VarDecl(Id("n"),[],None)],([],[Dowhile(([],[Assign(Id("n"),BinaryOp("-",Id("n"),IntLiteral(1)))]),BinaryOp(">",Id("n"),IntLiteral(0)))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,348))

	def test_program_49(self):
		input = """
			Function: main
			    Parameter: x, y
			    Body:
			        Do
			            x = x - 1;
			            While y > x Do
			                y = y - 1;
			            EndWhile.
			        While x > 0 EndDo.
			    EndBody.
		"""
		expect = Program([FuncDecl(Id("main"),[VarDecl(Id("x"),[],None),VarDecl(Id("y"),[],None)],([],[Dowhile(([],[Assign(Id("x"),BinaryOp("-",Id("x"),IntLiteral(1))),While(BinaryOp(">",Id("y"),Id("x")),([],[Assign(Id("y"),BinaryOp("-",Id("y"),IntLiteral(1)))]))]),BinaryOp(">",Id("x"),IntLiteral(0)))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,349))

	def test_program_50(self):
		input = """
			Function: main
			    Parameter: n
			    Body:
			        Do
			            For (i = 0, i < 10, 1) Do
			                Do
			                    If i % 2 == 0 Then
			                    EndIf.
			                    i = i - 1;
			                While i > 0 EndDo.
			            EndFor.
			        While x > 0 EndDo.
			    EndBody.
		"""
		expect = Program([FuncDecl(Id("main"),[VarDecl(Id("n"),[],None)],([],[Dowhile(([],[For(Id("i"),IntLiteral(0),BinaryOp("<",Id("i"),IntLiteral(10)),IntLiteral(1),([],[Dowhile(([],[If([(BinaryOp("==",BinaryOp("%",Id("i"),IntLiteral(2)),IntLiteral(0)),[],[])],([],[])),Assign(Id("i"),BinaryOp("-",Id("i"),IntLiteral(1)))]),BinaryOp(">",Id("i"),IntLiteral(0)))]))]),BinaryOp(">",Id("x"),IntLiteral(0)))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,350))

	def test_program_51(self):
		input = """
			Function: main
			    Parameter: n
			    Body:
			        For (i = 0, i < 10, 1) Do
			            If i == 5 Then
			                Break;
			            EndIf.
			        EndFor.
			    EndBody.
		"""
		expect = Program([FuncDecl(Id("main"),[VarDecl(Id("n"),[],None)],([],[For(Id("i"),IntLiteral(0),BinaryOp("<",Id("i"),IntLiteral(10)),IntLiteral(1),([],[If([(BinaryOp("==",Id("i"),IntLiteral(5)),[],[Break()])],([],[]))]))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,351))

	def test_program_52(self):
		input = """
			Function: main
			    Parameter: n
			    Body:
			        For (i = 0, i < 10, 1) Do
			            If i == 5 Then
			                Continue;
			            EndIf.
			        EndFor.
			    EndBody.
		"""
		expect = Program([FuncDecl(Id("main"),[VarDecl(Id("n"),[],None)],([],[For(Id("i"),IntLiteral(0),BinaryOp("<",Id("i"),IntLiteral(10)),IntLiteral(1),([],[If([(BinaryOp("==",Id("i"),IntLiteral(5)),[],[Continue()])],([],[]))]))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,352))

	def test_program_53(self):
		input = """
			Function: main
			    Parameter: n
			    Body:
			        Return n;
			    EndBody.
		"""
		expect = Program([FuncDecl(Id("main"),[VarDecl(Id("n"),[],None)],([],[Return(Id("n"))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,353))

	def test_program_54(self):
		input = """
			Function: main
			    Parameter: n
			    Body:
			        Return;
			    EndBody.
		"""
		expect = Program([FuncDecl(Id("main"),[VarDecl(Id("n"),[],None)],([],[Return(None)]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,354))

	def test_program_55(self):
		input = """
			Var: x, y = 0;
			Var: z = 1;
			Function: main
			    Body:
			    EndBody.
		"""
		expect = Program([VarDecl(Id("x"),[],None),VarDecl(Id("y"),[],IntLiteral(0)),VarDecl(Id("z"),[],IntLiteral(1)),FuncDecl(Id("main"),[],([],[]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,355))

	def test_program_56(self):
		input = """
			Var: x = 0;
			Function: foo
			    Body:
			    EndBody.
			Function: main
			    Body:
			    EndBody.
		"""
		expect = Program([VarDecl(Id("x"),[],IntLiteral(0)),FuncDecl(Id("foo"),[],([],[])),FuncDecl(Id("main"),[],([],[]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,356))

	def test_program_57(self):
		input = """
			Var: s = "Function: main Body: EndBody.";
		"""
		expect = Program([VarDecl(Id("s"),[],StringLiteral("Function: main Body: EndBody."))])
		self.assertTrue(TestAST.checkASTGen(input,expect,357))

	def test_program_58(self):
		input = """
			
		"""
		expect = Program([])
		self.assertTrue(TestAST.checkASTGen(input,expect,358))

	def test_program_59(self):
		input = """
			Function: main
			    Body:
			        Var: x;
			        x = foo
			            (x);
			    EndBody.
		"""
		expect = Program([FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],None)],[Assign(Id("x"),CallExpr(Id("foo"),[Id("x")]))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,359))

	def test_program_60(self):
		input = """
			Function: main
			    Body:
			        Var: x;
			        foo(2 + x, 4. \\. y);
			        goo();
			    EndBody.
		"""
		expect = Program([FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],None)],[CallStmt(Id("foo"),[BinaryOp("+",IntLiteral(2),Id("x")),BinaryOp("\\.",FloatLiteral(4.0),Id("y"))]),CallStmt(Id("goo"),[])]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,360))

	def test_program_61(self):
		input = """
			** This is a
			 * multi-line
			 * comment.
			 **
			Var: x = "Hello World";
			** This is a comment. **
			Function: main
			    Body:
			        print(x);
			    EndBody.
			** Hello World **
		"""
		expect = Program([VarDecl(Id("x"),[],StringLiteral("Hello World")),FuncDecl(Id("main"),[],([],[CallStmt(Id("print"),[Id("x")])]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,361))

	def test_program_62(self):
		input = """
			Var: x = **Comment first** "String after";
		"""
		expect = Program([VarDecl(Id("x"),[],StringLiteral("String after"))])
		self.assertTrue(TestAST.checkASTGen(input,expect,362))

	def test_program_63(self):
		input = """
			********Var: x = 0;********
		"""
		expect = Program([VarDecl(Id("x"),[],IntLiteral(0))])
		self.assertTrue(TestAST.checkASTGen(input,expect,363))

	def test_program_64(self):
		input = """
			** Outside the function **
			Function: main
			    Body:
			        ** Inside the function **
			        Var: x;
			        x = 1 + 2 * 3 ** 4 ** \\ 5;
			    EndBody.
		"""
		expect = Program([FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],None)],[Assign(Id("x"),BinaryOp("+",IntLiteral(1),BinaryOp("\\",BinaryOp("*",IntLiteral(2),IntLiteral(3)),IntLiteral(5))))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,364))

	def test_program_65(self):
		input = """
			Function: main
			    Body:
			        Return **a comment**;
			    EndBody.
		"""
		expect = Program([FuncDecl(Id("main"),[],([],[Return(None)]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,365))

	def test_program_66(self):
		input = """
			Function: main
			    Parameter: a, b, c
			    Body:
			        foo(**first comment****second comment**a, b, c);
			    EndBody.
		"""
		expect = Program([FuncDecl(Id("main"),[VarDecl(Id("a"),[],None),VarDecl(Id("b"),[],None),VarDecl(Id("c"),[],None)],([],[CallStmt(Id("foo"),[Id("a"),Id("b"),Id("c")])]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,366))

	def test_program_67(self):
		input = """
			**
			Function: main
			    Body:
			        print("Hello World");
			    EndBody.
			**
		"""
		expect = Program([])
		self.assertTrue(TestAST.checkASTGen(input,expect,367))

	def test_program_68(self):
		input = """
			****
			Function: main
			    Body:
			        print("Hello World");
			    EndBody.
			****
		"""
		expect = Program([FuncDecl(Id("main"),[],([],[CallStmt(Id("print"),[StringLiteral("Hello World")])]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,368))

	def test_program_69(self):
		input = """
			***
			****
			Var: x = 0;
			******
		"""
		expect = Program([])
		self.assertTrue(TestAST.checkASTGen(input,expect,369))

	def test_program_70(self):
		input = """
			Function: main
			    Parameter: n
			    Body:
			        Do
			            While n > 0 Do
			                For (i = 0, i < n, 1) Do
			                    If n % i == 0 Then
			                    ElseIf n % i == 1 Then
			                    Else
			                    EndIf.
			                EndFor.
			            EndWhile.
			        While n > 0 EndDo.
			    EndBody.
		"""
		expect = Program([FuncDecl(Id("main"),[VarDecl(Id("n"),[],None)],([],[Dowhile(([],[While(BinaryOp(">",Id("n"),IntLiteral(0)),([],[For(Id("i"),IntLiteral(0),BinaryOp("<",Id("i"),Id("n")),IntLiteral(1),([],[If([(BinaryOp("==",BinaryOp("%",Id("n"),Id("i")),IntLiteral(0)),[],[]),(BinaryOp("==",BinaryOp("%",Id("n"),Id("i")),IntLiteral(1)),[],[])],([],[]))]))]))]),BinaryOp(">",Id("n"),IntLiteral(0)))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,370))

	def test_program_71(self):
		input = """
			Function: main
			    Parameter: n
			    Body:
			        If n > 0 Then
			            If n > 1 Then
			                If n > 2 Then
			                EndIf.
			            ElseIf n > 0.5 Then
			                If n > 0.75 Then
			                Else
			                EndIf.
			            Else
			                If n > 0.25 Then
			                EndIf.
			            EndIf.
			        ElseIf n > -1 Then
			            If n > -0.5 Then
			            EndIf.
			            If n > -0.25 Then
			            Else
			            EndIf.
			        Else
			        EndIf.
			    EndBody.
		"""
		expect = Program([FuncDecl(Id("main"),[VarDecl(Id("n"),[],None)],([],[If([(BinaryOp(">",Id("n"),IntLiteral(0)),[],[If([(BinaryOp(">",Id("n"),IntLiteral(1)),[],[If([(BinaryOp(">",Id("n"),IntLiteral(2)),[],[])],([],[]))]),(BinaryOp(">",Id("n"),FloatLiteral(0.5)),[],[If([(BinaryOp(">",Id("n"),FloatLiteral(0.75)),[],[])],([],[]))])],([],[If([(BinaryOp(">",Id("n"),FloatLiteral(0.25)),[],[])],([],[]))]))]),(BinaryOp(">",Id("n"),UnaryOp("-",IntLiteral(1))),[],[If([(BinaryOp(">",Id("n"),UnaryOp("-",FloatLiteral(0.5))),[],[])],([],[])),If([(BinaryOp(">",Id("n"),UnaryOp("-",FloatLiteral(0.25))),[],[])],([],[]))])],([],[]))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,371))

	def test_program_72(self):
		input = """
			Function: main
			    Parameter: n
			    Body:
			        If n > 0 Then
			            If n > 1 Then
			                If n > 2 Then
			                    If n > 3 Then
			                        If n > 4 Then
			                            If n > 5 Then
			                            EndIf.
			                        EndIf.
			                    EndIf.
			                EndIf.
			            EndIf.
			        EndIf.
			    EndBody.
		"""
		expect = Program([FuncDecl(Id("main"),[VarDecl(Id("n"),[],None)],([],[If([(BinaryOp(">",Id("n"),IntLiteral(0)),[],[If([(BinaryOp(">",Id("n"),IntLiteral(1)),[],[If([(BinaryOp(">",Id("n"),IntLiteral(2)),[],[If([(BinaryOp(">",Id("n"),IntLiteral(3)),[],[If([(BinaryOp(">",Id("n"),IntLiteral(4)),[],[If([(BinaryOp(">",Id("n"),IntLiteral(5)),[],[])],([],[]))])],([],[]))])],([],[]))])],([],[]))])],([],[]))])],([],[]))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,372))

	def test_program_73(self):
		input = """
			Function: main
			    Parameter: n
			    Body:
			        For (i = 0, i < n, 1) Do
			            For (i = 0, i < n, 1) Do
			                For (i = 0, i < n, 1) Do
			                    For (i = 0, i < n, 1) Do
			                        For (i = 0, i < n, 1) Do
			                        EndFor.
			                    EndFor.
			                EndFor.
			            EndFor.
			        EndFor.
			    EndBody.
		"""
		expect = Program([FuncDecl(Id("main"),[VarDecl(Id("n"),[],None)],([],[For(Id("i"),IntLiteral(0),BinaryOp("<",Id("i"),Id("n")),IntLiteral(1),([],[For(Id("i"),IntLiteral(0),BinaryOp("<",Id("i"),Id("n")),IntLiteral(1),([],[For(Id("i"),IntLiteral(0),BinaryOp("<",Id("i"),Id("n")),IntLiteral(1),([],[For(Id("i"),IntLiteral(0),BinaryOp("<",Id("i"),Id("n")),IntLiteral(1),([],[For(Id("i"),IntLiteral(0),BinaryOp("<",Id("i"),Id("n")),IntLiteral(1),([],[]))]))]))]))]))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,373))

	def test_program_74(self):
		input = """
			Function: main
			    Parameter: n
			    Body:
			        While i < n Do
			            While i < n Do
			                While i < n Do
			                    While i < n Do
			                        While i < n Do
			                            i = i + 1;
			                        EndWhile.
			                    EndWhile.
			                EndWhile.
			            EndWhile.
			        EndWhile.
			    EndBody.
		"""
		expect = Program([FuncDecl(Id("main"),[VarDecl(Id("n"),[],None)],([],[While(BinaryOp("<",Id("i"),Id("n")),([],[While(BinaryOp("<",Id("i"),Id("n")),([],[While(BinaryOp("<",Id("i"),Id("n")),([],[While(BinaryOp("<",Id("i"),Id("n")),([],[While(BinaryOp("<",Id("i"),Id("n")),([],[Assign(Id("i"),BinaryOp("+",Id("i"),IntLiteral(1)))]))]))]))]))]))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,374))

	def test_program_75(self):
		input = """
			***********
			*    F    *
			*    u    *
			*    N    *
			*    C    *
			*    T    *
			*    I    *
			*    O    *
			*    N    *
			**********
		"""
		expect = Program([])
		self.assertTrue(TestAST.checkASTGen(input,expect,375))

	def test_program_76(self):
		input = """
			Var: x = "Var: y = '"Var: z = 0'"";
		"""
		expect = Program([VarDecl(Id("x"),[],StringLiteral("Var: y = '\"Var: z = 0'\""))])
		self.assertTrue(TestAST.checkASTGen(input,expect,376))

	def test_program_77(self):
		input = """
			Var: x = 
			    {
			        {
			            {
			                1, 2, 3, 4, 5
			            },
			            {
			                6, 7, 8, 9, 0
			            }
			        },
			        {
			            {
			                1, 2, 3, 4, 5
			            },
			            {
			                6, 7, 8, 9, 0
			            }
			        }
			    };
		"""
		expect = Program([VarDecl(Id("x"),[],ArrayLiteral([ArrayLiteral([ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3),IntLiteral(4),IntLiteral(5)]),ArrayLiteral([IntLiteral(6),IntLiteral(7),IntLiteral(8),IntLiteral(9),IntLiteral(0)])]),ArrayLiteral([ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3),IntLiteral(4),IntLiteral(5)]),ArrayLiteral([IntLiteral(6),IntLiteral(7),IntLiteral(8),IntLiteral(9),IntLiteral(0)])])]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,377))

	def test_program_78(self):
		input = """
			Function: a
			    Body:
			        Var: x;
			        Return b(x);
			    EndBody.
			Function: b
			    Body:
			        Var: x;
			        Return a(x);
			    EndBody.
			Function: main
			    Body:
			        Var: x;
			        x = a(x) + b(x);
			    EndBody.
		"""
		expect = Program([FuncDecl(Id("a"),[],([VarDecl(Id("x"),[],None)],[Return(CallExpr(Id("b"),[Id("x")]))])),FuncDecl(Id("b"),[],([VarDecl(Id("x"),[],None)],[Return(CallExpr(Id("a"),[Id("x")]))])),FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],None)],[Assign(Id("x"),BinaryOp("+",CallExpr(Id("a"),[Id("x")]),CallExpr(Id("b"),[Id("x")])))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,378))

	def test_program_79(self):
		input = """
			Function: main
			    Parameter: x, y, z
			    Body:
			        For (x = x, y, z) Do
			            If x > 0 Then
			                If y > 0 Then
			                    y = 0;
			                ElseIf z > 0 Then
			                    z = 0;
			                EndIf.
			            ElseIf y < z Then
			                x = x + y;
			            ElseIf x < z Then
			                x = x + z;
			            Else
			                Var: a, b, c;
			                a = x;
			                b = y;
			                c = z;
			            EndIf.
			        EndFor.
			    EndBody.
		"""
		expect = Program([FuncDecl(Id("main"),[VarDecl(Id("x"),[],None),VarDecl(Id("y"),[],None),VarDecl(Id("z"),[],None)],([],[For(Id("x"),Id("x"),Id("y"),Id("z"),([],[If([(BinaryOp(">",Id("x"),IntLiteral(0)),[],[If([(BinaryOp(">",Id("y"),IntLiteral(0)),[],[Assign(Id("y"),IntLiteral(0))]),(BinaryOp(">",Id("z"),IntLiteral(0)),[],[Assign(Id("z"),IntLiteral(0))])],([],[]))]),(BinaryOp("<",Id("y"),Id("z")),[],[Assign(Id("x"),BinaryOp("+",Id("x"),Id("y")))]),(BinaryOp("<",Id("x"),Id("z")),[],[Assign(Id("x"),BinaryOp("+",Id("x"),Id("z")))])],([VarDecl(Id("a"),[],None),VarDecl(Id("b"),[],None),VarDecl(Id("c"),[],None)],[Assign(Id("a"),Id("x")),Assign(Id("b"),Id("y")),Assign(Id("c"),Id("z"))]))]))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,379))

	def test_program_80(self):
		input = """
			Function: main
			    Parameter: a
			    Body:
			        Break;
			        Break;
			        Break;
			    EndBody.
		"""
		expect = Program([FuncDecl(Id("main"),[VarDecl(Id("a"),[],None)],([],[Break(),Break(),Break()]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,380))

	def test_program_81(self):
		input = """
			Function: main
			    Body:
			        Var: r = 10., v;
			        v = (4. \\. 3.) *. 3.14 *. r *. r *. r;
			    EndBody.
		"""
		expect = Program([FuncDecl(Id("main"),[],([VarDecl(Id("r"),[],FloatLiteral(10.0)),VarDecl(Id("v"),[],None)],[Assign(Id("v"),BinaryOp("*.",BinaryOp("*.",BinaryOp("*.",BinaryOp("*.",BinaryOp("\\.",FloatLiteral(4.0),FloatLiteral(3.0)),FloatLiteral(3.14)),Id("r")),Id("r")),Id("r")))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,381))

	def test_program_82(self):
		input = """
			Var: a, b, c;
			Var: x[1], y[2], z[3];
			Function: main
			    Body:
			        Var: x, y, z;
			        Var: a[1], b[2], c[3];
			        x = y + z;
			        a[0] = foo(b, c);
			    EndBody.
		"""
		expect = Program([VarDecl(Id("a"),[],None),VarDecl(Id("b"),[],None),VarDecl(Id("c"),[],None),VarDecl(Id("x"),[1],None),VarDecl(Id("y"),[2],None),VarDecl(Id("z"),[3],None),FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],None),VarDecl(Id("y"),[],None),VarDecl(Id("z"),[],None),VarDecl(Id("a"),[1],None),VarDecl(Id("b"),[2],None),VarDecl(Id("c"),[3],None)],[Assign(Id("x"),BinaryOp("+",Id("y"),Id("z"))),Assign(ArrayCell(Id("a"),[IntLiteral(0)]),CallExpr(Id("foo"),[Id("b"),Id("c")]))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,382))

	def test_program_83(self):
		input = """
			Function: compose
			    Parameter: f, g, x
			    Body:
			        Return f(g(x));
			    EndBody.
		"""
		expect = Program([FuncDecl(Id("compose"),[VarDecl(Id("f"),[],None),VarDecl(Id("g"),[],None),VarDecl(Id("x"),[],None)],([],[Return(CallExpr(Id("f"),[CallExpr(Id("g"),[Id("x")])]))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,383))

	def test_program_84(self):
		input = """
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
			Function: composefg
			    Parameter: x
			    Body:
			        Return f(g(x));
			    EndBody.
		"""
		expect = Program([FuncDecl(Id("f"),[VarDecl(Id("x"),[],None)],([],[Return(CallExpr(Id("f"),[Id("x")]))])),FuncDecl(Id("g"),[VarDecl(Id("x"),[],None)],([],[Return(CallExpr(Id("g"),[Id("x")]))])),FuncDecl(Id("composefg"),[VarDecl(Id("x"),[],None)],([],[Return(CallExpr(Id("f"),[CallExpr(Id("g"),[Id("x")])]))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,384))

	def test_program_85(self):
		input = """
			Function: main
			    Body:
			        Var: a[10][10];
			        For (i = 0, i < 10, 1) Do
			            For (j = 0, j < 10, 1) Do
			                If i == j Then
			                    Continue;
			                EndIf.
			                a[i][j] = i*10 + j;
			            EndFor.
			        EndFor.
			    EndBody.
		"""
		expect = Program([FuncDecl(Id("main"),[],([VarDecl(Id("a"),[10,10],None)],[For(Id("i"),IntLiteral(0),BinaryOp("<",Id("i"),IntLiteral(10)),IntLiteral(1),([],[For(Id("j"),IntLiteral(0),BinaryOp("<",Id("j"),IntLiteral(10)),IntLiteral(1),([],[If([(BinaryOp("==",Id("i"),Id("j")),[],[Continue()])],([],[])),Assign(ArrayCell(Id("a"),[Id("i"),Id("j")]),BinaryOp("+",BinaryOp("*",Id("i"),IntLiteral(10)),Id("j")))]))]))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,385))

	def test_program_86(self):
		input = """
			Function: main
			    Body:
			        Var: x = 0;
			        Var: y, z = 1;
			        Var: a[3] = {0, 1, 2};
			        a[z] = x;
			        a[x] = z;
			        Return a;
			    EndBody.
		"""
		expect = Program([FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],IntLiteral(0)),VarDecl(Id("y"),[],None),VarDecl(Id("z"),[],IntLiteral(1)),VarDecl(Id("a"),[3],ArrayLiteral([IntLiteral(0),IntLiteral(1),IntLiteral(2)]))],[Assign(ArrayCell(Id("a"),[Id("z")]),Id("x")),Assign(ArrayCell(Id("a"),[Id("x")]),Id("z")),Return(Id("a"))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,386))

	def test_program_87(self):
		input = """
			Function: main
			    Parameter: x, y
			    Body:
			        If x > y Then
			            While x > y Do
			                x = x - 1;
			                y = y + 1;
			            EndWhile.
			        EndIf.
			        Return x == y;
			    EndBody.
		"""
		expect = Program([FuncDecl(Id("main"),[VarDecl(Id("x"),[],None),VarDecl(Id("y"),[],None)],([],[If([(BinaryOp(">",Id("x"),Id("y")),[],[While(BinaryOp(">",Id("x"),Id("y")),([],[Assign(Id("x"),BinaryOp("-",Id("x"),IntLiteral(1))),Assign(Id("y"),BinaryOp("+",Id("y"),IntLiteral(1)))]))])],([],[])),Return(BinaryOp("==",Id("x"),Id("y")))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,387))

	def test_program_88(self):
		input = """
			Function: main
			    Body:
			        While True Do Do
			        While False EndDo. EndWhile.
			    EndBody.
		"""
		expect = Program([FuncDecl(Id("main"),[],([],[While(BooleanLiteral(True),([],[Dowhile(([],[]),BooleanLiteral(False))]))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,388))

	def test_program_89(self):
		input = """
			Var: x;
			Function: f
			    Parameter: x
			    Body:
			        For (x = x, x > 0, -1) Do
			        EndFor.
			    EndBody.
			Function: main
			    Body:
			        f(x);
			    EndBody.
		"""
		expect = Program([VarDecl(Id("x"),[],None),FuncDecl(Id("f"),[VarDecl(Id("x"),[],None)],([],[For(Id("x"),Id("x"),BinaryOp(">",Id("x"),IntLiteral(0)),UnaryOp("-",IntLiteral(1)),([],[]))])),FuncDecl(Id("main"),[],([],[CallStmt(Id("f"),[Id("x")])]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,389))

	def test_program_90(self):
		input = """
			Function: main
			    Parameter: t
			    Body:
			        Var: h, m, s;
			        h = t \\ 3600;
			        m = t % 3600 \\ 60;
			        s = t % 60;
			        print(h, m, s);
			    EndBody.
		"""
		expect = Program([FuncDecl(Id("main"),[VarDecl(Id("t"),[],None)],([VarDecl(Id("h"),[],None),VarDecl(Id("m"),[],None),VarDecl(Id("s"),[],None)],[Assign(Id("h"),BinaryOp("\\",Id("t"),IntLiteral(3600))),Assign(Id("m"),BinaryOp("\\",BinaryOp("%",Id("t"),IntLiteral(3600)),IntLiteral(60))),Assign(Id("s"),BinaryOp("%",Id("t"),IntLiteral(60))),CallStmt(Id("print"),[Id("h"),Id("m"),Id("s")])]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,390))

	def test_program_91(self):
		input = """
			Function: fibonacci
			    Parameter: n
			    Body:
			        Var: x = 1, y = 1, z = 0;
			        For (i = i, i < n, 1) Do
			            If i < 2 Then
			                Continue;
			            EndIf.
			            z = x + y;
			            x = y;
			            y = z;
			        EndFor.
			        Return z;
			    EndBody.
		"""
		expect = Program([FuncDecl(Id("fibonacci"),[VarDecl(Id("n"),[],None)],([VarDecl(Id("x"),[],IntLiteral(1)),VarDecl(Id("y"),[],IntLiteral(1)),VarDecl(Id("z"),[],IntLiteral(0))],[For(Id("i"),Id("i"),BinaryOp("<",Id("i"),Id("n")),IntLiteral(1),([],[If([(BinaryOp("<",Id("i"),IntLiteral(2)),[],[Continue()])],([],[])),Assign(Id("z"),BinaryOp("+",Id("x"),Id("y"))),Assign(Id("x"),Id("y")),Assign(Id("y"),Id("z"))])),Return(Id("z"))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,391))

	def test_program_92(self):
		input = """
			Function: main
			    Body:
			        Var: x, y, z;
			        x = y----------z;
			    EndBody.
		"""
		expect = Program([FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],None),VarDecl(Id("y"),[],None),VarDecl(Id("z"),[],None)],[Assign(Id("x"),BinaryOp("-",Id("y"),UnaryOp("-",UnaryOp("-",UnaryOp("-",UnaryOp("-",UnaryOp("-",UnaryOp("-",UnaryOp("-",UnaryOp("-",UnaryOp("-",Id("z"))))))))))))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,392))

	def test_program_93(self):
		input = """
			Function: main
			    Body:
			        Var: x, y, z;
			        x = y-!!!!!!!!!z;
			    EndBody.
		"""
		expect = Program([FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],None),VarDecl(Id("y"),[],None),VarDecl(Id("z"),[],None)],[Assign(Id("x"),BinaryOp("-",Id("y"),UnaryOp("!",UnaryOp("!",UnaryOp("!",UnaryOp("!",UnaryOp("!",UnaryOp("!",UnaryOp("!",UnaryOp("!",UnaryOp("!",Id("z"))))))))))))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,393))

	def test_program_94(self):
		input = """
			Function: main
			    Parameter: x
			    Body:
			        Return ---init__(---x);
			    EndBody.
		"""
		expect = Program([FuncDecl(Id("main"),[VarDecl(Id("x"),[],None)],([],[Return(UnaryOp("-",UnaryOp("-",UnaryOp("-",CallExpr(Id("init__"),[UnaryOp("-",UnaryOp("-",UnaryOp("-",Id("x"))))])))))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,394))

	def test_program_95(self):
		input = """
			Function: main
			    Parameter: x
			    Body:
			        If x == True Then
			            x = False;
			        Else
			            x = True;
			        EndIf.
			        x = !x;
			        Return x;
			    EndBody.
		"""
		expect = Program([FuncDecl(Id("main"),[VarDecl(Id("x"),[],None)],([],[If([(BinaryOp("==",Id("x"),BooleanLiteral(True)),[],[Assign(Id("x"),BooleanLiteral(False))])],([],[Assign(Id("x"),BooleanLiteral(True))])),Assign(Id("x"),UnaryOp("!",Id("x"))),Return(Id("x"))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,395))

	def test_program_96(self):
		input = """
			Function: increment
			    Parameter: x
			    Body:
			        x = x * 1 + 0 -- 1;
			    EndBody.
		"""
		expect = Program([FuncDecl(Id("increment"),[VarDecl(Id("x"),[],None)],([],[Assign(Id("x"),BinaryOp("-",BinaryOp("+",BinaryOp("*",Id("x"),IntLiteral(1)),IntLiteral(0)),UnaryOp("-",IntLiteral(1))))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,396))

	def test_program_97(self):
		input = """
			Function: main
			    Parameter: x
			    Body:
			        If x == 0 Then
			            x = x + 1;
			        Else If x == 1 Then
			            x = x + 2;
			        Else If x == 2 Then
			            x = x + 3;
			        Else
			            x = x + 4;
			        EndIf. EndIf. EndIf.
			    EndBody.
		"""
		expect = Program([FuncDecl(Id("main"),[VarDecl(Id("x"),[],None)],([],[If([(BinaryOp("==",Id("x"),IntLiteral(0)),[],[Assign(Id("x"),BinaryOp("+",Id("x"),IntLiteral(1)))])],([],[If([(BinaryOp("==",Id("x"),IntLiteral(1)),[],[Assign(Id("x"),BinaryOp("+",Id("x"),IntLiteral(2)))])],([],[If([(BinaryOp("==",Id("x"),IntLiteral(2)),[],[Assign(Id("x"),BinaryOp("+",Id("x"),IntLiteral(3)))])],([],[Assign(Id("x"),BinaryOp("+",Id("x"),IntLiteral(4)))]))]))]))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,397))

	def test_program_98(self):
		input = """
			Function: divide_conquer
			    Parameter: lst, begin, end
			    Body:
			        If begin == end Then
			            Return lst[begin];
			        Else
			            Return divide_conquer(lst, begin, end \\ 2) + divide_conquer(lst, end \\ 2 + 1, end);
			        EndIf.
			    EndBody.
		"""
		expect = Program([FuncDecl(Id("divide_conquer"),[VarDecl(Id("lst"),[],None),VarDecl(Id("begin"),[],None),VarDecl(Id("end"),[],None)],([],[If([(BinaryOp("==",Id("begin"),Id("end")),[],[Return(ArrayCell(Id("lst"),[Id("begin")]))])],([],[Return(BinaryOp("+",CallExpr(Id("divide_conquer"),[Id("lst"),Id("begin"),BinaryOp("\\",Id("end"),IntLiteral(2))]),CallExpr(Id("divide_conquer"),[Id("lst"),BinaryOp("+",BinaryOp("\\",Id("end"),IntLiteral(2)),IntLiteral(1)),Id("end")])))]))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,398))

	def test_program_99(self):
		input = """
			Function: recursion
			    Parameter: x
			    Body:
			        Return recursion(x);
			    EndBody.
		"""
		expect = Program([FuncDecl(Id("recursion"),[VarDecl(Id("x"),[],None)],([],[Return(CallExpr(Id("recursion"),[Id("x")]))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,399))

