import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    def test_codegen_0(self):
        input = """
        Function: main
        Body: 
            print(string_of_int(120));
        EndBody.
        """
        expect = "120"
        self.assertTrue(TestCodeGen.test(input,expect,500))
    
    def test_codegen_1(self):
        input = """
        Function: foo
        Body:
            Var: x = 1;
            Return x;
        EndBody.
        Function: main
        Body:
            Var: x = 0;
            x = foo();
            print(string_of_int(x));
        EndBody.
        """
        expect = "1"
        self.assertTrue(TestCodeGen.test(input,expect,501))
    
    def test_codegen_2(self):
        input = """
        Function: foo
        Parameter: n
        Body:
            If True Then
                Var: x = 0;
                Return x;
            Else
                Var: x = 1;
                Return x;
            EndIf.
        EndBody.
        Function: main
        Body:
            Var: x = 0;
            x = foo(1); 
            print(string_of_int(x));
        EndBody.
        """
        expect = "0"
        self.assertTrue(TestCodeGen.test(input,expect,502))
    
    def test_codegen_3(self):
        input = """
        Function: foo
        Body:
            Var: x = 0, i = 1;
            For (i = 1, i < 10, 1) Do
                x = x + i;
            EndFor.
            For (i = 1, i < 10, 1) Do
                x = x * i;
            EndFor.
            Return x;
        EndBody.
        Function: main
        Body:
            Var: x = 0;
            x = foo(); 
            print(string_of_int(x));
        EndBody.
        """
        expect = "16329600"
        self.assertTrue(TestCodeGen.test(input,expect,503))

    def test_codegen_4(self):
        input = """
        Function: main
        Body:
            Var: x = 0;
            x = x + 1; 
            print(string_of_int(x));
        EndBody.
        """
        expect = "1"
        self.assertTrue(TestCodeGen.test(input,expect,504))
    
    def test_codegen_5(self):
        input = """
        Function: foo
        Parameter: n
        Body:
            If n >. 2.0 Then
                Return 2.0;
            Else
                Return n;
            EndIf.
        EndBody.
        Function: main
        Body:
            Var: x = 0.0;
            x = foo(5.0); 
            print(string_of_float(x));
        EndBody.
        """
        expect = "2.0"
        self.assertTrue(TestCodeGen.test(input,expect,505))

    def test_codegen_6(self):
        input = """
        Function: main
        Body:
            Var: x[5] = {1, 2, 3, 4, 5}, y = 0;
            y = x[1];
            print(string_of_int(y));
        EndBody.
        """
        expect = "2"
        self.assertTrue(TestCodeGen.test(input,expect,506))
    
    def test_codegen_7(self):
        input = """
        Function: main
        Body:
            Var: x[2][2] = {{1,2},{3,4}}, y = 0;
            y = x[1][1];
            print(string_of_int(y));
        EndBody.
        """
        expect = "4"
        self.assertTrue(TestCodeGen.test(input,expect,507))

    def test_codegen_8(self):
        input = """
        Function: main
        Body:
            Var: x[2][2][2] = {{{1,2},{3,4}},{{5,6},{7,8}}}, y = 0;
            y = x[1][1][1];
            print(string_of_int(y));
        EndBody.
        """
        expect = "8"
        self.assertTrue(TestCodeGen.test(input,expect,508))
    
    def test_codegen_9(self):
        input = """
        Function: main
        Body:
            Var: x[5] = {1, 2, 3, 4, 5}, y = 0;
            x[1] = x[1] + 1;
            y = x[1];
            print(string_of_int(y));
        EndBody.
        """
        expect = "3"
        self.assertTrue(TestCodeGen.test(input,expect,509))
    
    def test_codegen_10(self):
        input = """
        Function: main
        Body:
            print("120");
        EndBody.
        """
        expect = "120"
        self.assertTrue(TestCodeGen.test(input,expect,510))
    
    def test_codegen_11(self):
        input = """
        Function: foo
        Parameter: n
        Body:
            While n > 0 Do
                n = n - 1;
            EndWhile.
            Return n;
        EndBody.
        Function: main
        Body:
            print(string_of_int(foo(-1)));
        EndBody.
        """
        expect = "-1"
        self.assertTrue(TestCodeGen.test(input,expect,511))

    def test_codegen_12(self):
        input = """
        Function: foo
        Parameter: n
        Body:
            Do
                n = n - 1;
            While n > 0 EndDo.
            Return n;
        EndBody.
        Function: main
        Body:
            print(string_of_int(foo(-1)));
        EndBody.
        """
        expect = "-2"
        self.assertTrue(TestCodeGen.test(input,expect,512))

    def test_codegen_13(self):
        input = """
        Function: foo
        Parameter: n
        Body:
            Var: i = 0, j = 0;
            For (i = 0, i < n, 1) Do
                If i == 4 Then
                    Continue;
                EndIf.
                If i % 2 == 0 Then
                    j = j + 1;
                EndIf.
            EndFor.
            Return j;
        EndBody.
        Function: main
        Body:
            Var: x = 0;
            x = foo(10);
            print(string_of_int(x));
        EndBody.
        """
        expect = "4"
        self.assertTrue(TestCodeGen.test(input,expect,513))
    
    def test_codegen_14(self):
        input = """
        Function: foo
        Parameter: n, a[5]
        Body:
            Var: i = 0;
            For (i = 0, i < 5, 1) Do
                If a[i] == n Then
                    Return True;
                EndIf.
            EndFor.
            Return False;
        EndBody.
        Function: main
        Body:
            Var: x = False, a[5] = {1,2,3,4,5};
            x = foo(4, a);
            print(string_of_bool(x));
        EndBody.
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,514))
    
    def test_codegen_15(self):
        input = """
        Var: x = 10;
        Function: main
        Body:
            print(string_of_int(x));
        EndBody.
        """
        expect = "10"
        self.assertTrue(TestCodeGen.test(input,expect,515))
    
    def test_codegen_16(self):
        input = """
        Var: x = 3, a[5] = {1,2,3,4,5};
        Function: main
        Body:
            Var: i = 0;
            For (i = 0, i < 5, 1) Do
                If a[i] == x Then
                    print("1");
                Else
                    print("0");
                EndIf.
            EndFor.
        EndBody.
        """
        expect = "00100"
        self.assertTrue(TestCodeGen.test(input,expect,516))
    
    def test_codegen_17(self):
        input = """
        Function: main
        Body:
            Var: x = 0, y = 0, z = 0;
            If x == 0 Then
                If y == 0 Then
                    If z == 0 Then
                        print("Hello World");
                    EndIf.
                EndIf.
            EndIf.
        EndBody.
        """
        expect = "Hello World"
        self.assertTrue(TestCodeGen.test(input,expect,517))
    
    def test_codegen_18(self):
        input = """
        Function: foo
        Parameter: n
        Body:
            If n == 0 Then
                Return 1;
            Else
                Return n * foo(n-1);
            EndIf.
        EndBody.
        Function: main
        Body:
            Var: x = 0;
            x = foo(10);
            print(string_of_int(x));
        EndBody.
        """
        expect = "3628800"
        self.assertTrue(TestCodeGen.test(input,expect,518))
    
    def test_codegen_19(self):
        input = """
        Function: foo
        Parameter: n
        Body:
            If n <= 0 Then
                Return n;
            Else
                Return foo(n-1);
            EndIf.
        EndBody.
        Function: main
        Body:
            Var: x = 0;
            x = foo(-10);
            print(string_of_int(x));
        EndBody.
        """
        expect = "-10"
        self.assertTrue(TestCodeGen.test(input,expect,519))
    
    def test_codegen_20(self):
        input = """
        Function: a
        Parameter: n
        Body:
            If n < 0 Then
                Return 0;
            EndIf.
            Return n;
        EndBody.
        Function: b
        Parameter: n
        Body:
            If n > 0 Then
                Return 0;
            EndIf.
            Return n;
        EndBody.
        Function: main
        Body:
            Var: x = 10, y = True;
            If y Then
                print(string_of_int(a(x)));
            Else
                print(string_of_int(b(x)));
            EndIf.
        EndBody.
        """
        expect = "10"
        self.assertTrue(TestCodeGen.test(input,expect,520))
    
    def test_codegen_21(self):
        input = """
        Function: fibonacci
        Parameter: n
        Body:
            If n < 2 Then
                Return 1;
            Else
                Return fibonacci(n-2) + fibonacci(n-1);
            EndIf.
        EndBody.
        Function: main
        Body:
            Var: x = 6;
            x = fibonacci(x);
            print(string_of_int(x));
        EndBody.
        """
        expect = "13"
        self.assertTrue(TestCodeGen.test(input,expect,521))
    
    def test_codegen_22(self):
        input = """
        Function: inc
        Parameter: n
        Body:
            Return n + 1;
        EndBody.
        Function: dub
        Parameter: n
        Body:
            Return 2 * n;
        EndBody.
        Function: main
        Body:
            Var: x = 3, a = 0, b = 0;
            a = inc(dub(x));
            b = dub(inc(x));
            print(string_of_int(a));
            print(string_of_int(b));
        EndBody.
        """
        expect = "78"
        self.assertTrue(TestCodeGen.test(input,expect,522))
    
    def test_codegen_23(self):
        input = """
        Function: f
        Parameter: n
        Body:
            Return n * n;
        EndBody.
        Function: g
        Parameter: n
        Body:
            Return n + n;
        EndBody.
        Function: compose
        Parameter: n
        Body:
            Return f(g(n));
        EndBody.
        Function: main
        Body:
            Var: x = 3;
            x = compose(x);
            print(string_of_int(x));
        EndBody.
        """
        expect = "36"
        self.assertTrue(TestCodeGen.test(input,expect,523))
    
    def test_codegen_24(self):
        input = """
        Function: foo
        Parameter: a[2][3], i
        Body:
            a[0][0] = 1;
            Return a[i];
        EndBody.
        Function: main
        Body:
            Var: i = 0, a[2][3] = {{1,2,3},{4,5,6}}, x[3] = {0,0,0};
            x = foo(a, i);
            print(string_of_int(x[2]));
        EndBody.
        """
        expect = "3"
        self.assertTrue(TestCodeGen.test(input,expect,524))
    
    def test_codegen_25(self):
        input = """
        Function: findMax
        Parameter: a[10], i
        Body:
            Var: x = 0;
            x = a[i];
            If i == 9 Then
                Return x;
            Else
                Var: y = 0;
                y = findMax(a, i + 1);
                If x > y Then
                    Return x;
                Else
                    Return y;
                EndIf.
            EndIf.
        EndBody.
        Function: main
        Body:
            Var: i = 0, a[10] = {2,4,6,8,1,3,5,7,9,0}, x = 0;
            x = findMax(a, i);
            print(string_of_int(x));
        EndBody.
        """
        expect = "9"
        self.assertTrue(TestCodeGen.test(input,expect,525))
    
    def test_codegen_26(self):
        input = """
        Function: findMin
        Parameter: a[10], i
        Body:
            Var: x = 0;
            x = a[i];
            If i == 9 Then
                Return x;
            Else
                Var: y = 0;
                y = findMin(a, i + 1);
                If x < y Then
                    Return x;
                Else
                    Return y;
                EndIf.
            EndIf.
        EndBody.
        Function: main
        Body:
            Var: i = 0, a[10] = {2,4,6,8,1,3,5,7,9,0}, x = 0;
            x = findMin(a, i);
            print(string_of_int(x));
        EndBody.
        """
        expect = "0"
        self.assertTrue(TestCodeGen.test(input,expect,526))
    
    def test_codegen_27(self):
        input = """
        Function: main
        Body:
            Var: a[10] = {0,1,2,3,4,5,6,7,8,9}, i = 0;
            For (i = 0, i < 10, 1) Do
                print(string_of_int(a[i]));
            EndFor.
        EndBody.
        """
        expect = "0123456789"
        self.assertTrue(TestCodeGen.test(input,expect,527))
    
    def test_codegen_28(self):
        input = """
        Function: main
        Body:
            Var: a[10] = {0,1,2,3,4,5,6,7,8,9}, i = 0;
            While i < 10 Do
                print(string_of_int(a[i]));
                i = i + 1;
            EndWhile.
        EndBody.
        """
        expect = "0123456789"
        self.assertTrue(TestCodeGen.test(input,expect,528))
    
    def test_codegen_29(self):
        input = """
        Function: main
        Body:
            Var: x = 0, y = 5;
            While True Do
                x = x + 1;
                print(string_of_int(x));
                If x > y Then
                    Break;
                EndIf.
            EndWhile.
        EndBody.
        """
        expect = "123456"
        self.assertTrue(TestCodeGen.test(input,expect,529))
    
    def test_codegen_30(self):
        input = """
        Function: main
        Body:
            Var: x = "1.0", y = 1.5, z = 4.5;
            While y =/= z Do
                y = y +. float_of_string(x);
            EndWhile.
            x = "Hello";
            print(string_of_float(y));
            print(x);
        EndBody.
        """
        expect = "4.5Hello"
        self.assertTrue(TestCodeGen.test(input,expect,530))
    
    def test_codegen_31(self):
        input = """
        Function: foo
        Parameter: a[2][3], i
        Body:
            a[0][0] = 1;
            Return a[i];
        EndBody.
        Function: main
        Body:
            Var: a[2][3] = {{1,2,3},{4,5,6}};
            print(string_of_int(foo(a,0)[1]));
        EndBody.
        """
        expect = "2"
        self.assertTrue(TestCodeGen.test(input,expect,531))
    
    def test_codegen_32(self):
        input = """
        Function: main
        Body:
            Var: a[3][3] = {{1,2,3},{4,5,6},{7,8,9}}, i = 0, j = 0;
            For (i = 0, i < 3, 1) Do
                For (j = 0, j < i, 1) Do
                    Var: tmp = 0;
                    tmp = a[i][j];
                    a[i][j] = a[j][i];
                    a[j][i] = tmp;
                EndFor.
            EndFor.
            For (i = 0, i < 3, 1) Do
                For (j = 0, j < 3, 1) Do
                    print(string_of_int(a[i][j]));
                EndFor.
            EndFor.
        EndBody.
        """
        expect = "147258369"
        self.assertTrue(TestCodeGen.test(input,expect,532))
    
    def test_codegen_33(self):
        input = """
        Function: transpose
        Parameter: a[2][3]
        Body:
            Var: b[3][2] = {{0,0},{0,0},{0,0}}, i = 0, j = 0;
            For (i = 0, i < 2, 1) Do
                For (j = 0, j < 3, 1) Do
                    b[j][i] = a[i][j];
                EndFor.
            EndFor.
            Return b;
        EndBody.
        Function: main
        Body:
            Var: a[2][3] = {{1,2,3},{4,5,6}}, b[3][2] = {{0,0},{0,0},{0,0}}, i = 0, j = 0;
            b = transpose(a);
            For (i = 0, i < 3, 1) Do
                For (j = 0, j < 2, 1) Do
                    print(string_of_int(b[i][j]));
                EndFor.
            EndFor.
        EndBody.
        """
        expect = "142536"
        self.assertTrue(TestCodeGen.test(input,expect,533))
    
    def test_codegen_34(self):
        input = """
        Function: mul
        Parameter: a[2][3], b[3][2]
        Body:
            Var: c[2][2] = {{0,0},{0,0}}, i = 0, j = 0, k = 0;
            For (i = 0, i < 2, 1) Do
                For (j = 0, j < 2, 1) Do
                    For (k = 0, k < 3, 1) Do
                        c[i][j] = c[i][j] + a[i][k] * b[k][j];
                    EndFor.
                EndFor.
            EndFor.
            Return c;
        EndBody.
        Function: main
        Body:
            Var: a[2][3] = {{1,1,1},{1,1,1}}, b[3][2] = {{1,1},{1,1},{1,1}}, c[2][2] = {{0,0},{0,0}};
            Var: i = 0, j = 0;
            c = mul(a, b);
            For (i = 0, i < 2, 1) Do
                For (j = 0, j < 2, 1) Do
                    print(string_of_int(c[i][j]));
                EndFor.
            EndFor.
        EndBody.
        """
        expect = "3333"
        self.assertTrue(TestCodeGen.test(input,expect,534))
    
    def test_codegen_35(self):
        input = """
        Function: main
        Body:
            print("Hello World");
        EndBody.
        """
        expect = "Hello World"
        self.assertTrue(TestCodeGen.test(input,expect,535))
    
    def test_codegen_36(self):
        input = """
        Function: main
        Body:
            Var: a[5] = {0,1,2,3,4}, x = 0;
            x = a[foo(a[foo(a[foo(a[foo(a[0])])])])];
            print(string_of_int(x));
        EndBody.
        Function: foo
        Parameter: x
        Body:
            Return x + 1;
        EndBody.
        """
        expect = "4"
        self.assertTrue(TestCodeGen.test(input,expect,536))
    
    def test_codegen_37(self):
        input = """
        Function: main
        Body:
            Var: a[5] = {1,2,3,4,5}, x = 0;
            x = a[a[a[a[a[0]]]]];
            print(string_of_int(x));
        EndBody.
        """
        expect = "5"
        self.assertTrue(TestCodeGen.test(input,expect,537))
    
    def test_codegen_38(self):
        input = """
        Function: foo
        Parameter: n
        Body:
            print(n);
        EndBody.
        Function: main
        Body:
            foo("Hello World");
        EndBody.
        """
        expect = "Hello World"
        self.assertTrue(TestCodeGen.test(input,expect,538))
    
    def test_codegen_39(self):
        input = """
        Function: printInt
        Parameter: n
        Body:
            print(string_of_int(n));
        EndBody.
        Function: main
        Body:
            printInt(120);
        EndBody.
        """
        expect = "120"
        self.assertTrue(TestCodeGen.test(input,expect,539))
    
    def test_codegen_40(self):
        input = """
        Function: main
        Body:
            print("\\n");
        EndBody.
        """
        expect = "\n"
        self.assertTrue(TestCodeGen.test(input,expect,540))
    
    def test_codegen_41(self):
        input = """
        Function: main
        Body:
            Var: i = 0;
            For (i = 1, i < 5, 1) Do
                Var: j = 0;
                For (j = 0, j < i, 1) Do
                    print("*");
                EndFor.
                print("\\n");
            EndFor.
        EndBody.
        """
        expect = "*\n**\n***\n****\n"
        self.assertTrue(TestCodeGen.test(input,expect,541))
    
    def test_codegen_42(self):
        input = """
        Function: main
        Body:
            Var: i = 1;
            i = i + i * i \\ i;
            print(string_of_int(i));
        EndBody.
        """
        expect = "2"
        self.assertTrue(TestCodeGen.test(input,expect,542))
    
    def test_codegen_43(self):
        input = """
        Function: main
        Body:
        EndBody.
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input,expect,543))
    
    def test_codegen_44(self):
        input = """
        Var: x = 0, y = 0, z = 0;
        Function: getX
        Body:
            Return x;
        EndBody.
        Function: getY
        Body:
            Return y;
        EndBody.
        Function: getZ
        Body:
            Return z;
        EndBody.
        Function: main
        Body:
            print(string_of_int(getX()+getY()+getZ()));
        EndBody.
        """
        expect = "0"
        self.assertTrue(TestCodeGen.test(input,expect,544))
    
    def test_codegen_45(self):
        input = """
        Function: foo
        Parameter: n
        Body:
            print(string_of_int(n));
            If n > 0 Then
                print(foo(n-1));
            EndIf.
            Return string_of_int(n);
        EndBody.
        Function: main
        Body:
            Var: x = "";
            x = foo(5);
        EndBody.
        """
        expect = "54321001234"
        self.assertTrue(TestCodeGen.test(input,expect,545))
    
    def test_codegen_46(self):
        input = """
        Var: a[5] = {1,2,3,4,5};
        Function: main
        Body:
            Var: i = 0;
            For (i = 0, i < 4, 1) Do
                a[i] = a[a[i]];
            EndFor.
            For (i = 0, i < 5, 1) Do
                print(string_of_int(a[i]));
            EndFor.
        EndBody.
        """
        expect = "23455"
        self.assertTrue(TestCodeGen.test(input,expect,546))
    
    def test_codegen_47(self):
        input = """
        Function: swap
        Parameter: a[2]
        Body:
            Var: tmp = 0;
            tmp = a[0];
            a[0] = a[1];
            a[1] = tmp;
        EndBody.
        Function: main
        Body:
            Var: a[2] = {1,2};
            swap(a);
            print(string_of_int(a[0]));
            print(string_of_int(a[1]));
        EndBody.
        """
        expect = "21"
        self.assertTrue(TestCodeGen.test(input,expect,547))
    
    def test_codegen_48(self):
        input = """
        Function: getSec
        Parameter: d, h, m
        Body:
            Return 60*(m+60*(h+24*d));
        EndBody.
        Function: main
        Body:
            Var: x = 0;
            x = getSec(1,1,1);
            print(string_of_int(x));
        EndBody.
        """
        expect = "90060"
        self.assertTrue(TestCodeGen.test(input,expect,548))
    
    def test_codegen_49(self):
        input = """
        Function: isLeapYear
        Parameter: y
        Body:
            Return y % 4 == 0;
        EndBody.
        Function: main
        Body:
            print(string_of_bool(isLeapYear(2021)));
        EndBody.
        """
        expect = "false"
        self.assertTrue(TestCodeGen.test(input,expect,549))
    
    def test_codegen_50(self):
        input = """
        Var: a[10] = {2,1,2,3,4,4,3,4,3,3}, x = 3;
        Function: count
        Parameter: a[10], x
        Body:
            Var: c = 0, i = 0;
            For (i = 0, i < 10, 1) Do
                If a[i] == x Then
                    c = c + 1;
                EndIf.
            EndFor.
            Return c;
        EndBody.
        Function: main
        Body:
            Var: c = 4;
            c = count(a, c);
            print(string_of_int(c));
        EndBody.
        """
        expect = "3"
        self.assertTrue(TestCodeGen.test(input,expect,550))
    
    def test_codegen_51(self):
        input = """
        Function: main
        Body:
            Var: x = 3, y = 4;
            If x < y Then
                print(string_of_int(x));
                print(string_of_int(y));
            Else
                print(string_of_int(y));
                print(string_of_int(x));
            EndIf.
        EndBody.
        """
        expect = "34"
        self.assertTrue(TestCodeGen.test(input,expect,551))
    
    def test_codegen_52(self):
        input = """
        Function: factorial
        Parameter: n
        Body:
            Var: x = 1, i = 1;
            For (i = 1, i <= n, 1) Do
                x = x * i;
            EndFor.
            Return x;
        EndBody.
        Function: main
        Body:
            Var: x = 10;
            x = factorial(x);
            print(string_of_int(x));
        EndBody.
        """
        expect = "3628800"
        self.assertTrue(TestCodeGen.test(input,expect,552))
    
    def test_codegen_53(self):
        input = """
        Function: factorial
        Parameter: n
        Body:
            Var: x = 1, i = 1;
            While True Do
                i = i + 1;
                x = x * i;
                If i == n Then
                    Return x;
                EndIf.
            EndWhile.
            Return x;
        EndBody.
        Function: main
        Body:
            Var: x = 10;
            x = factorial(x);
            print(string_of_int(x));
        EndBody.
        """
        expect = "3628800"
        self.assertTrue(TestCodeGen.test(input,expect,553))
    
    def test_codegen_54(self):
        input = """
        Function: fibonacci
        Parameter: n
        Body:
            Var: i = 0, x = 0, y = 0;
            For (i = 0, i < n, 1) Do
                If (i == 0) || (i == 1) Then
                    x = 1;
                    y = 1;
                Else
                    Var: z = 0;
                    z = x;
                    x = x + y;
                    y = z;
                EndIf.
            EndFor.
            Return x;
        EndBody.
        Function: main
        Body:
            Var: x = 6;
            x = fibonacci(x);
            print(string_of_int(x));
        EndBody.
        """
        expect = "8"
        self.assertTrue(TestCodeGen.test(input,expect,554))
    
    def test_codegen_55(self):
        input = """
        Function: foo
        Body:
            Var: i = 0;
            For (i = 0, i < 10, 1) Do
                If i == 5 Then
                    Return i;
                EndIf.
            EndFor.
            Return i;
        EndBody.
        Function: main
        Body:
            Var: x = 0;
            x = foo();
            print(string_of_int(x));
        EndBody.
        """
        expect = "5"
        self.assertTrue(TestCodeGen.test(input,expect,555))
    
    def test_codegen_56(self):
        input = """
        Function: main
        Body:
            Var: a[3] = {"Hello", "World", "Again"};
            print(a[0]);
        EndBody.
        """
        expect = "Hello"
        self.assertTrue(TestCodeGen.test(input,expect,556))
    
    def test_codegen_57(self):
        input = """
        Function: foo
        Body:
            Return {"Hello", "World", "Again"};
        EndBody.
        Function: main
        Body:
            print(foo()[0]);
        EndBody.
        """
        expect = "Hello"
        self.assertTrue(TestCodeGen.test(input,expect,557))
    
    def test_codegen_58(self):
        input = """
        Function: main
        Body:
            print(string_of_bool(True && False));
        EndBody.
        """
        expect = "false"
        self.assertTrue(TestCodeGen.test(input,expect,558))
    
    def test_codegen_59(self):
        input = """
        Function: main
        Body:
            print(string_of_bool(True || False));
        EndBody.
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,559))
    
    def test_codegen_60(self):
        input = """
        Function: main
        Body:
            print(string_of_bool(!True));
        EndBody.
        """
        expect = "false"
        self.assertTrue(TestCodeGen.test(input,expect,560))
    
    def test_codegen_61(self):
        input = """
        Function: gcd
        Parameter: x, y
        Body:
            Var: z = 0;
            If x > y Then
                z = x \\ 2;
            Else
                z = y \\ 2;
            EndIf.
            While z > 0 Do
                If (x % z == 0) && (y % z == 0) Then
                    Return z;
                EndIf.
                z = z - 1;
            EndWhile.
            Return 1;
        EndBody.
        Function: main
        Body:
            print(string_of_int(gcd(20,24)));
        EndBody.
        """
        expect = "4"
        self.assertTrue(TestCodeGen.test(input,expect,561))
    
    def test_codegen_62(self):
        input = """
        Function: gcd
        Parameter: x, y
        Body:
            Var: z = 0;
            If x > y Then
                z = x \\ 2;
            Else
                z = y \\ 2;
            EndIf.
            While z > 0 Do
                If (x % z == 0) && (y % z == 0) Then
                    Return z;
                EndIf.
                z = z - 1;
            EndWhile.
            Return 1;
        EndBody.
        Function: main
        Body:
            print(string_of_int(gcd(10,20)));
        EndBody.
        """
        expect = "10"
        self.assertTrue(TestCodeGen.test(input,expect,562))
    
    def test_codegen_63(self):
        input = """
        Function: lcm
        Parameter: x, y
        Body:
            Var: z = 0;
            If x > y Then
                z = y * 2;
            Else
                z = x * 2;
            EndIf.
            While z < x * y Do
                If (z % x == 0) && (z % y == 0) Then
                    Return z;
                EndIf.
                z = z + 1;
            EndWhile.
            Return x * y;
        EndBody.
        Function: main
        Body:
            print(string_of_int(lcm(4,6)));
        EndBody.
        """
        expect = "12"
        self.assertTrue(TestCodeGen.test(input,expect,563))
    
    def test_codegen_64(self):
        input = """
        Function: lcm
        Parameter: x, y
        Body:
            Var: z = 0;
            If x > y Then
                z = y * 2;
            Else
                z = x * 2;
            EndIf.
            While z < x * y Do
                If (z % x == 0) && (z % y == 0) Then
                    Return z;
                EndIf.
                z = z + 1;
            EndWhile.
            Return x * y;
        EndBody.
        Function: main
        Body:
            print(string_of_int(lcm(10,20)));
        EndBody.
        """
        expect = "20"
        self.assertTrue(TestCodeGen.test(input,expect,564))
    
    def test_codegen_65(self):
        input = """
        Function: isPrime
        Parameter: n
        Body:
            Var: x = 0;
            x = n \\ 2;
            While x > 0 Do
                If n % x == 0 Then
                    Break;
                EndIf.
                x = x - 1;
            EndWhile.
            Return x == 1;
        EndBody.
        Function: main
        Body:
            print(string_of_bool(isPrime(11)));
        EndBody.
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,565))
    
    def test_codegen_66(self):
        input = """
        Function: isPrime
        Parameter: n
        Body:
            Var: x = 0;
            x = n \\ 2;
            While x > 0 Do
                If n % x == 0 Then
                    Break;
                EndIf.
                x = x - 1;
            EndWhile.
            Return x == 1;
        EndBody.
        Function: main
        Body:
            print(string_of_bool(isPrime(10)));
        EndBody.
        """
        expect = "false"
        self.assertTrue(TestCodeGen.test(input,expect,566))
    
    def test_codegen_67(self):
        input = """
        Function: exp
        Parameter: a, n
        Body:
            Var: x = 1, i = 0;
            For (i = 0, i < n, 1) Do
                x = x * a;
            EndFor.
            Return x;
        EndBody.
        Function: main
        Body:
            print(string_of_int(exp(5,3)));
        EndBody.
        """
        expect = "125"
        self.assertTrue(TestCodeGen.test(input,expect,567))
    
    def test_codegen_68(self):
        input = """
        Function: exp
        Parameter: a, n
        Body:
            Var: x = 1;
            While n > 0 Do
                x = x * a;
                n = n - 1;
            EndWhile.
            Return x;
        EndBody.
        Function: main
        Body:
            print(string_of_int(exp(5,3)));
        EndBody.
        """
        expect = "125"
        self.assertTrue(TestCodeGen.test(input,expect,568))
    
    def test_codegen_69(self):
        input = """
        Function: isSquare
        Parameter: n
        Body:
            Var: i = 1;
            If n == 1 Then
                Return True;
            EndIf.
            For (i = 1, i <= n \\ 2, 1) Do
                If i * i == n Then
                    Return True;
                EndIf.
            EndFor.
            Return False;
        EndBody.
        Function: main
        Body:
            print(string_of_bool(isSquare(25)));
        EndBody.
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,569))
    
    def test_codegen_70(self):
        input = """
        Function: isSquare
        Parameter: n
        Body:
            Var: i = 1;
            If n == 1 Then
                Return True;
            EndIf.
            For (i = 1, i <= n \\ 2, 1) Do
                If i * i == n Then
                    Return True;
                EndIf.
            EndFor.
            Return False;
        EndBody.
        Function: main
        Body:
            print(string_of_bool(isSquare(24)));
        EndBody.
        """
        expect = "false"
        self.assertTrue(TestCodeGen.test(input,expect,570))
    
    def test_codegen_71(self):
        input = """
        Function: main
        Body:
            Var: x = 3, y = 3.2;
            print(string_of_bool(x == int_of_float(y)));
        EndBody.
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,571))
    
    def test_codegen_72(self):
        input = """
        Function: main
        Body:
            Var: x = 3, y = 3.2;
            print(string_of_bool(y <=. float_to_int(x)));
        EndBody.
        """
        expect = "false"
        self.assertTrue(TestCodeGen.test(input,expect,572))
    
    def test_codegen_73(self):
        input = """
        Function: isTrue
        Parameter: x
        Body:
            If x Then
                Return True;
            Else
                Return False;
            EndIf.
        EndBody.
        Function: main
        Body:
            print(string_of_bool(!!isTrue(True)));
        EndBody.
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,573))
    
    def test_codegen_74(self):
        input = """
        Function: foo
        Body:
            Return {True, False, True};
        EndBody.
        Function: main
        Body:
            Var: x = False, i = 1;
            x = !bool_of_string("True") || foo()[i];
            print(string_of_bool(x));
        EndBody.
        """
        expect = "false"
        self.assertTrue(TestCodeGen.test(input,expect,574))
    
    def test_codegen_75(self):
        input = """
        Function: canIPassThisCourse
        Body:
            Return True;
        EndBody.
        Function: main
        Body:
            printStrLn("Can I pass this course?");
            If canIPassThisCourse() Then
                print("Yes");
            Else
                print("Also yes");
            EndIf.
        EndBody.
        """
        expect = "Can I pass this course?\nYes"
        self.assertTrue(TestCodeGen.test(input,expect,575))
    
    def test_codegen_76(self):
        input = """
        Function: getIntMyself
        Parameter: n
        Body:
            Return n + 0;
        EndBody.
        Function: main
        Body:
            print(string_of_int(getIntMyself(5)));
        EndBody.
        """
        expect = "5"
        self.assertTrue(TestCodeGen.test(input,expect,576))
    
    def test_codegen_77(self):
        input = """
        Function: getFloatMyself
        Parameter: n
        Body:
            Return n +. 0.0;
        EndBody.
        Function: main
        Body:
            print(string_of_float(getFloatMyself(5.0)));
        EndBody.
        """
        expect = "5.0"
        self.assertTrue(TestCodeGen.test(input,expect,577))
    
    def test_codegen_78(self):
        input = """
        Function: getBooleanMyself
        Parameter: n
        Body:
            Return n && True;
        EndBody.
        Function: main
        Body:
            print(string_of_bool(getBooleanMyself(False)));
        EndBody.
        """
        expect = "false"
        self.assertTrue(TestCodeGen.test(input,expect,578))
    
    def test_codegen_79(self):
        input = """
        Function: getStringMyself
        Parameter: n
        Body:
            print("Getting ");
            print(n);
            print("\\n");
            printStrLn("Successful");
            Return n;
        EndBody.
        Function: main
        Body:
            print(getStringMyself("Hello World"));
        EndBody.
        """
        expect = "Getting Hello World\nSuccessful\nHello World"
        self.assertTrue(TestCodeGen.test(input,expect,579))
    
    def test_codegen_80(self):
        input = """
        Function: compareFloat
        Parameter: a, b
        Body:
            Return !(a =/= b);
        EndBody.
        Function: main
        Body:
            Var: x = 1.5, y = 1.5;
            print(string_of_bool(compareFloat(x, y)));
        EndBody.
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,580))
    
    def test_codegen_81(self):
        input = """
        Function: factorial
        Parameter: n
        Body:
            If n == 0 Then
                Return 1;
            Else
                Return n * factorial(n-1);
            EndIf.
        EndBody.
        Function: combination
        Parameter: n, r
        Body:
            Return factorial(n) \\ (factorial(r) * factorial(n-r));
        EndBody.
        Function: main
        Body:
            Var: x = 10, y = 5;
            print(string_of_int(combination(x, y)));
        EndBody.
        """
        expect = "252"
        self.assertTrue(TestCodeGen.test(input,expect,581))
    
    def test_codegen_82(self):
        input = """
        Function: factorial
        Parameter: n
        Body:
            If n == 0 Then
                Return 1;
            Else
                Return n * factorial(n-1);
            EndIf.
        EndBody.
        Function: arrangement
        Parameter: n, r
        Body:
            Return factorial(n) \\ factorial(n-r);
        EndBody.
        Function: main
        Body:
            Var: x = 10, y = 5;
            print(string_of_int(arrangement(x, y)));
        EndBody.
        """
        expect = "30240"
        self.assertTrue(TestCodeGen.test(input,expect,582))
    
    def test_codegen_83(self):
        input = """
        Function: foo
        Parameter: a[5]
        Body:
            a[0] = a[0] + 0;
            Return a;
        EndBody.
        Function: main
        Body:
            Var: a[5] = {1,2,3,4,5}, i = 0;
            a[0] = 6;
            foo(a)[1] = 7;
            For (i = 0, i < 5, 1) Do
                print(string_of_int(a[i]));
            EndFor.
        EndBody.
        """
        expect = "67345"
        self.assertTrue(TestCodeGen.test(input,expect,583))
    
    def test_codegen_84(self):
        input = """
        Function: getDistance
        Parameter: v, t
        Body:
            Return v *. t;
        EndBody.
        Function: main
        Body:
            Var: v = 30.0, t = 60.0, s = 0.0;
            s = getDistance(v, t);
            print(string_of_float(s));
        EndBody.
        """
        expect = "1800.0"
        self.assertTrue(TestCodeGen.test(input,expect,584))
    
    def test_codegen_85(self):
        input = """
        Function: getVelocity
        Parameter: s, t
        Body:
            Return s \\. t;
        EndBody.
        Function: main
        Body:
            Var: v = 0.0, t = 60.0, s = 1800.0;
            v = getVelocity(s, t);
            print(string_of_float(v));
        EndBody.
        """
        expect = "30.0"
        self.assertTrue(TestCodeGen.test(input,expect,585))
    
    def test_codegen_86(self):
        input = """
        Function: getTime
        Parameter: s, v
        Body:
            Return s \\. v;
        EndBody.
        Function: main
        Body:
            Var: v = 30.0, t = 0.0, s = 1800.0;
            t = getTime(s, v);
            print(string_of_float(t));
        EndBody.
        """
        expect = "60.0"
        self.assertTrue(TestCodeGen.test(input,expect,586))
    
    def test_codegen_87(self):
        input = """
        Function: getEnergy
        Parameter: m, f
        Body:
            Var: c = 3, res[2] = {0, 0};
            res[0] = m * c * c;
            res[1] = f + 8 + 8;
            Return res;
        EndBody.
        Function: main
        Body:
            Var: e[2] = {0, 0};
            e = getEnergy(1, -10);
            print(string_of_int(e[0]));
            print("e");
            print(string_of_int(e[1]));
        EndBody.
        """
        expect = "9e6"
        self.assertTrue(TestCodeGen.test(input,expect,587))
    
    def test_codegen_88(self):
        input = """
        Function: getResistance
        Parameter: u, i
        Body:
            Return u \\. i;
        EndBody.
        Function: main
        Body:
            Var: u = 10.0, i = 0.2, r = 0.0;
            r = getResistance(u, i);
            print(string_of_float(r));
        EndBody.
        """
        expect = "50.0"
        self.assertTrue(TestCodeGen.test(input,expect,588))
    
    def test_codegen_89(self):
        input = """
        Function: getAmperage
        Parameter: u, r
        Body:
            Return u \\. r;
        EndBody.
        Function: main
        Body:
            Var: u = 10.0, i = 0.0, r = 50.0;
            i = getAmperage(u, r);
            print(string_of_float(i));
        EndBody.
        """
        expect = "0.2"
        self.assertTrue(TestCodeGen.test(input,expect,589))
    
    def test_codegen_90(self):
        input = """
        Function: getVoltage
        Parameter: i, r
        Body:
            Return i *. r;
        EndBody.
        Function: main
        Body:
            Var: u = 0.0, i = 0.2, r = 50.0;
            u = getVoltage(i, r);
            print(string_of_float(u));
        EndBody.
        """
        expect = "10.0"
        self.assertTrue(TestCodeGen.test(input,expect,590))
    
    def test_codegen_91(self):
        input = """
        Function: getCubeVolume
        Parameter: s
        Body:
            Return s *. s *. s;
        EndBody.
        Function: main
        Body:
            Var: s = 5.0, v = 0.0;
            v = getCubeVolume(s);
            print(string_of_float(v));
        EndBody.
        """
        expect = "125.0"
        self.assertTrue(TestCodeGen.test(input,expect,591))
    
    def test_codegen_92(self):
        input = """
        Function: getSphereVolume
        Parameter: r
        Body:
            Var: pi = 3.14;
            Return 4.0 \\. 3.0 *. pi *. r *. r *. r;
        EndBody.
        Function: main
        Body:
            Var: r = 3.0, v = 0.0;
            v = getSphereVolume(r);
            print(string_of_float(v));
        EndBody.
        """
        expect = "113.04001"
        self.assertTrue(TestCodeGen.test(input,expect,592))
    
    def test_codegen_93(self):
        input = """
        Function: getRectangularPrismVolume
        Parameter: w, h, l
        Body:
            Return w *. h *. l;
        EndBody.
        Function: main
        Body:
            Var: w = 3.0, h = 4.0, l = 5.0, v = 0.0;
            v = getRectangularPrismVolume(w,h,l);
            print(string_of_float(v));
        EndBody.
        """
        expect = "60.0"
        self.assertTrue(TestCodeGen.test(input,expect,593))
    
    def test_codegen_94(self):
        input = """
        Function: getCylinderVolume
        Parameter: r, h
        Body:
            Var: pi = 3.14;
            Return pi *. r *. r *. h;
        EndBody.
        Function: main
        Body:
            Var: r = 3.0, h = 4.0, v = 0.0;
            v = getCylinderVolume(r,h);
            print(string_of_float(v));
        EndBody.
        """
        expect = "113.04001"
        self.assertTrue(TestCodeGen.test(input,expect,594))
    
    def test_codegen_94(self):
        input = """
        Function: getCylinderVolume
        Parameter: r, h
        Body:
            Var: pi = 3.14;
            Return pi *. r *. r *. h;
        EndBody.
        Function: main
        Body:
            Var: r = 3.0, h = 4.0, v = 0.0;
            v = getCylinderVolume(r,h);
            print(string_of_float(v));
        EndBody.
        """
        expect = "113.04"
        self.assertTrue(TestCodeGen.test(input,expect,594))
    
    def test_codegen_95(self):
        input = """
        Function: isTriangle
        Parameter: a, b, c
        Body:
            Return (a + b > c) && (a + c > b) && (b + c > a);
        EndBody.
        Function: main
        Body:
            Var: a = 3, b = 4, c = 5;
            print(string_of_bool(isTriangle(a, b, c)));
        EndBody.
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,595))
    
    def test_codegen_96(self):
        input = """
        Function: isTriangle
        Parameter: a, b, c
        Body:
            Return (a + b > c) && (a + c > b) && (b + c > a);
        EndBody.
        Function: isEquilateralTriangle
        Parameter: a, b, c
        Body:
            Return isTriangle(a, b, c) && (a == b) && (b == c);
        EndBody.
        Function: main
        Body:
            Var: a = 4, b = 4, c = 5;
            print(string_of_bool(isEquilateralTriangle(a, b, c)));
        EndBody.
        """
        expect = "false"
        self.assertTrue(TestCodeGen.test(input,expect,596))
    
    def test_codegen_97(self):
        input = """
        Function: isTriangle
        Parameter: a, b, c
        Body:
            Return (a + b > c) && (a + c > b) && (b + c > a);
        EndBody.
        Function: isIsoscelesTriangle
        Parameter: a, b, c
        Body:
            Return isTriangle(a, b, c) && ((a == b) || (b == c) || (a == c));
        EndBody.
        Function: main
        Body:
            Var: a = 4, b = 4, c = 5;
            print(string_of_bool(isIsoscelesTriangle(a, b, c)));
        EndBody.
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,597))
    
    def test_codegen_98(self):
        input = """
        Function: isTriangle
        Parameter: a, b, c
        Body:
            Return (a + b > c) && (a + c > b) && (b + c > a);
        EndBody.
        Function: isRightAngledTriangle
        Parameter: a, b, c
        Body:
            Var: x = False;
            x = x || (a * a + b * b == c * c);
            x = x || (a * a + c * c == b * b);
            x = x || (b * b + c * c == a * a);
            Return x;
        EndBody.
        Function: main
        Body:
            Var: a = 3, b = 4, c = 5;
            print(string_of_bool(isRightAngledTriangle(a, b, c)));
        EndBody.
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,598))
    
    def test_codegen_99(self):
        input = """
        Function: main
        Body:
            print("Goodbye");
        EndBody.
        """
        expect = "Goodbye"
        self.assertTrue(TestCodeGen.test(input,expect,599))