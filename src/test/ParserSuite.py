import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):

    def test_program_0(self):
        input = """Var: x;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,200))
    
    def test_program_1(self):
        input = """Var: x, y, z;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,201))
    
    def test_program_2(self):
        input = """Var: x, y = 1, z;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,202))
    
    def test_program_3(self):
        input = """Var: x[3] = {1, 2, 3};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,203))
    
    def test_program_4(self):
        input = """Var: x[2][3] = {{1,2,3},{4,5,6}};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,204))
    
    def test_program_5(self):
        input = """Var: x, y = 0, z[2] = {1, 2}, a[2][3] = {{1,2,3},{4,5,6}};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,205))
    
    def test_program_6(self):
        input = """Var: ;"""
        expect = "Error on line 1 col 5: ;"
        self.assertTrue(TestParser.checkParser(input,expect,206))
    
    def test_program_7(self):
        input = """Var: x,;"""
        expect = "Error on line 1 col 7: ;"
        self.assertTrue(TestParser.checkParser(input,expect,207))

    def test_program_8(self):
        input = """Var: x[];"""
        expect = "Error on line 1 col 7: ]"
        self.assertTrue(TestParser.checkParser(input,expect,208))

    def test_program_9(self):
        input = """
            Function: abc
                Body:
                EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,209))

    def test_program_10(self):
        input = """
            Function: main
                Parameter: n
                Body:
                    print(n);
                EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,210))

    def test_program_11(self):
        input = """Function: main Parameter: n"""
        expect = "Error on line 1 col 27: <EOF>"
        self.assertTrue(TestParser.checkParser(input,expect,211))

    def test_program_12(self):
        input = """Function: Body: EndBody."""
        expect = "Error on line 1 col 10: Body"
        self.assertTrue(TestParser.checkParser(input,expect,212))

    def test_program_13(self):
        input = """Function: main Body: print("Hello World");"""
        expect = "Error on line 1 col 42: <EOF>"
        self.assertTrue(TestParser.checkParser(input,expect,213))

    def test_program_14(self):
        input = """
            Function: main
                Parameter: a, b,
                Body:
                    print(a, b);
                EndBody.
        """
        expect = "Error on line 4 col 16: Body"
        self.assertTrue(TestParser.checkParser(input,expect,214))

    def test_program_15(self):
        input = """
            Function: main
                Parameter: a, b
                Body:
                    print(a, b);
                    Var: x;
                EndBody.
        """
        expect = "Error on line 6 col 20: Var"
        self.assertTrue(TestParser.checkParser(input,expect,215))

    def test_program_16(self):
        input = """
            Var: x;
            Function: main
                Body:
                    print(x);
                EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,216))

    def test_program_17(self):
        input = """
            Function: main
                Body:
                    print(x);
                EndBody.
            Var: x;
        """
        expect = "Error on line 6 col 12: Var"
        self.assertTrue(TestParser.checkParser(input,expect,217))

    def test_program_18(self):
        input = """
            Function: main
                Body:
                    Var: x;
                    x = 1 + 2;
                EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,218))

    def test_program_19(self):
        input = """
            Function: main
                Body:
                    Var: x, y, z;
                    x = y * z;
                EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,219))

    def test_program_20(self):
        input = """
            Function: main
                Body:
                    Var: x, y, z;
                    x = (x+y)*(x+z)\\(y+z);
                EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,220))

    def test_program_21(self):
        input = """
            Function: main
                Body:
                    Var: x, a, b, c;
                    x = (a > b) && (b < c);
                EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,221))

    def test_program_22(self):
        input = """
            Function: main
                Body:
                    Var: x, a, b, c;
                    x = a > b && b < c;
                EndBody.
        """
        expect = "Error on line 5 col 35: <"
        self.assertTrue(TestParser.checkParser(input,expect,222))

    def test_program_23(self):
        input = """
            Function: main
                Body:
                    Var: x, y, z;
                    x = (x + y) * (y +. z) % x;
                EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,223))

    def test_program_24(self):
        input = """
            Function: main
                Body:
                    Var: x, y, z;
                    x = !x + !!y + !!!z;
                EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,224))

    def test_program_25(self):
        input = """
            Function: main
                Body:
                    Var: x;
                    x = x[0] + x[1] + x[2];
                EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,225))

    def test_program_26(self):
        input = """
            Function: main
                Body:
                    Var: x, y, z;
                    x = x[(y+z)*y*z] * (x[y] + x[x[z]]);
                EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,226))

    def test_program_27(self):
        input = """
            Function: main
                Body:
                    Var: x, y, z;
                    x = x[x[y]+foo(z)*(y-z\\x)];
                EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,227))

    def test_program_28(self):
        input = """
            Function: main
                Body:
                    Var: x, y, z;
                    x = (x+y)[y+z*(z-y)];
                EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,228))

    def test_program_29(self):
        input = """
            Function: main
                Body:
                    Var: x, y, z;
                    x = x + x[y] + x[z[y]];
                EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,229))

    def test_program_30(self):
        input = """
            Function: main
                Body:
                    Var: x, y, z;
                    x = x[x[y][z]][x[y][z]];
                EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,230))

    def test_program_31(self):
        input = """
            Function: main
                Body:
                    Var: x, y, z;
                    x = -x[y[z]];
                EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,231))

    def test_program_32(self):
        input = """
            Function: main
                Body:
                    Var: x;
                    x = True && False;
                EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,232))

    def test_program_33(self):
        input = """
            Function: main
                Body:
                    Var: x, y, z;
                    x = foo(x) + y[z];
                EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,233))

    def test_program_34(self):
        input = """
            Function: main
                Body:
                    Var: x, y;
                    x = y[1] + y[0xABC] + y[0o123] + y[1+0xABC*0o123];
                EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,234))

    def test_program_35(self):
        input = """
            Function: main
                Body:
                    Var: x, y, z;
                    x = y[z][z+1][z+2][z+3][z+4][z+5][fact(z)];
                EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,235))

    def test_program_36(self):
        input = """
            Function: main
                Body:
                    Var: a, b;
                    a = int_of_string(read());
                    b = float_of_int(a) +. 2.0;
                EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,236))

    def test_program_37(self):
        input = """
            Function: main
                Body:
                    Var: x;
                    x = foo(foo(foo(foo(foo(x))))) + func();
                EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,237))

    def test_program_38(self):
        input = """
            Function: main
                Body:
                    Var: x, y, z;
                    x = foo(x, y+z, y[z][x], foo(x));
                EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,238))

    def test_program_39(self):
        input = """
            Function: main
                Body:
                    Var: x, y;
                    x = y[foo(y[foo(y[foo(y[foo(y[foo(y)])])])])];
                EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,239))

    def test_program_40(self):
        input = """
            Function: main
                Body:
                    Var: x, y, z;
                    x = (y + z)foo;
                EndBody.
        """
        expect = "Error on line 5 col 31: foo"
        self.assertTrue(TestParser.checkParser(input,expect,240))

    def test_program_41(self):
        input = """
            Function: main
                Body:
                    Var: x, y;
                    x[y] = y[x];
                EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,241))

    def test_program_42(self):
        input = """
            Function: main
                Body:
                    Var: x = 1 +. ;
                EndBody.
        """
        expect = "Error on line 4 col 31: +."
        self.assertTrue(TestParser.checkParser(input,expect,242))

    def test_program_43(self):
        input = """
            Function: main
                Body:
                    Var: x;
                    x = !-.foo(a[b + c]);
                EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,243))

    def test_program_44(self):
        input = """
            Function: main
                Body:
                    Var: x;
                    x = -.!foo(a[b + c]);
                EndBody.
        """
        expect = "Error on line 5 col 26: !"
        self.assertTrue(TestParser.checkParser(input,expect,244))

    def test_program_45(self):
        input = """
            Function: main
                Body:
                    Var: x;
                    x = !!!--.--.--.foo(x);
                EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,245))

    def test_program_46(self):
        input = """
            Function: main
                Body:
                    Var: x;
                    x = --.-.-!!foo(x);
                EndBody.
        """
        expect = "Error on line 5 col 30: !"
        self.assertTrue(TestParser.checkParser(input,expect,246))

    def test_program_47(self):
        input = """
            Function: main
                Body:
                    Var: x, y;
                    x = -y[!y[-.y[!y[x]]]][!-.-x][---y[!x]];
                EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,247))

    def test_program_48(self):
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,248))

    def test_program_49(self):
        input = """
            Function: main
                Body:
                    Var: x;
                    x = x && x < x + x * !-x[foo(x)];
                EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,249))

    def test_program_50(self):
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,250))
    
    def test_program_51(self):
        input = """
            Function: main
                Parameter: x
                Body: 
                    If x == 0 Then 
                        x = 1; 
                    EndIf.
                EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,251))
    
    def test_program_52(self):
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,252))
    
    def test_program_53(self):
        input = """
            Function: main
                Parameter: x
                Body:
                    If x == 0 Then
                        x = 1;
                EndBody.
        """
        expect = "Error on line 7 col 16: EndBody"
        self.assertTrue(TestParser.checkParser(input,expect,253))
    
    def test_program_54(self):
        input = """
            Function: main
                Body:
                    For (i = 0, i < 10, 2) Do
                        print(i);
                    EndFor.
                EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,254))
    
    def test_program_55(self):
        input = """
            Function: main
                Body:
                    For (,,) Do
                        print("Hello");
                    EndFor.
                EndBody.
        """
        expect = "Error on line 4 col 25: ,"
        self.assertTrue(TestParser.checkParser(input,expect,255))
    
    def test_program_56(self):
        input = """
            Function: main
                Body:
                    For (i = 0, i < 10, 1) Do
                        print(i);
                    EndFor
                EndBody.
        """
        expect = "Error on line 7 col 16: EndBody"
        self.assertTrue(TestParser.checkParser(input,expect,256))
    
    def test_program_57(self):
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,257))

    def test_program_58(self):
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,258))

    def test_program_59(self):
        input = """
            Function: main
                Parameter: n
                Body:
                    If n > 0 Then
                        For (i = n, i > 0, -1) Do
                            print(i);
                        EndIf.
                    EndFor.
                EndBody.
        """
        expect = "Error on line 8 col 24: EndIf"
        self.assertTrue(TestParser.checkParser(input,expect,259))

    def test_program_60(self):
        input = """
            Function: main
                Parameter: n
                Body:
                    While n > 0 Do
                        n = n - 1;
                    EndWhile.
                EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,260))

    def test_program_61(self):
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,261))

    def test_program_62(self):
        input = """
            Function: main
                Parameter: n
                Body:
                    While n > 0
                        n = n - 1;
                    EndWhile.
                EndBody.
        """
        expect = "Error on line 5 col 20: While"
        self.assertTrue(TestParser.checkParser(input,expect,262))

    def test_program_63(self):
        input = """
            Function: main
                Parameter: n
                Body:
                    While n > 0 Do
                    EndWhile.
                EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,263))

    def test_program_64(self):
        input = """
            Function: main
                Parameter: n
                Body:
                    Do
                        n = n - 1;
                    While n > 0 EndDo.
                EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,264))

    def test_program_65(self):
        input = """
            Function: main
                Parameter: n
                Body:
                    Do
                        n = n - 1;
                    While n > 0 Do
                        n = n - 1;
                    EndWhile.
                EndBody.
        """
        expect = "Error on line 10 col 16: EndBody"
        self.assertTrue(TestParser.checkParser(input,expect,265))

    def test_program_66(self):
        input = """
            Function: main
                Parameter: n
                Body:
                    While n > 0 Do
                        n = n - 1;
                    EndDo.
                EndBody.
        """
        expect = "Error on line 7 col 20: EndDo"
        self.assertTrue(TestParser.checkParser(input,expect,266))

    def test_program_67(self):
        input = """
            Function: main
                Parameter: n
                Body:
                    Do
                        n = n - 1;
                    EndDo.
                EndBody.
        """
        expect = "Error on line 7 col 20: EndDo"
        self.assertTrue(TestParser.checkParser(input,expect,267))

    def test_program_68(self):
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,268))

    def test_program_69(self):
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,269))

    def test_program_70(self):
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,270))

    def test_program_71(self):
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,271))

    def test_program_72(self):
        input = """
            Function: main
                Parameter: n
                Body:
                    For (i = 0, i < 10, 1) Do
                        If i == 5 Then
                            Continue Break;
                        EndIf.
                    EndFor.
                EndBody.
        """
        expect = "Error on line 7 col 37: Break"
        self.assertTrue(TestParser.checkParser(input,expect,272))

    def test_program_73(self):
        input = """
            Function: main
                Parameter: n
                Body:
                    Return n;
                EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,273))

    def test_program_74(self):
        input = """
            Function: main
                Parameter: n
                Body:
                    Return;
                EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,274))

    def test_program_75(self):
        input = """Function: main"""
        expect = "Error on line 1 col 14: <EOF>"
        self.assertTrue(TestParser.checkParser(input,expect,275))

    def test_program_76(self):
        input = """
            Function: mainParameter: n
                Body:
                EndBody.
        """
        expect = "Error on line 2 col 35: :"
        self.assertTrue(TestParser.checkParser(input,expect,276))

    def test_program_77(self):
        input = """
            Function: mainBody:
                EndBody.
        """
        expect = "Error on line 2 col 30: :"
        self.assertTrue(TestParser.checkParser(input,expect,277))

    def test_program_78(self):
        input = """Var: x = -1;"""
        expect = "Error on line 1 col 9: -"
        self.assertTrue(TestParser.checkParser(input,expect,278))

    def test_program_79(self):
        input = """
            Var: x, y = 0;
            Var: z = 1;
            Function: main
                Body:
                EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,279))

    def test_program_80(self):
        input = """
            Var: x = 0;
            Function: foo
                Body:
                EndBody.
            Function: main
                Body:
                EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,280))

    def test_program_81(self):
        input = """
            Var: x = 0;
            x = x + 1;
        """
        expect = "Error on line 3 col 12: x"
        self.assertTrue(TestParser.checkParser(input,expect,281))

    def test_program_82(self):
        input = """Var: s = "Function: main Body: EndBody.";"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,282))

    def test_program_83(self):
        input = """
            Var: x, y;
            Function: foo
                Body:
                EndBody.
            Var: z;
        """
        expect = "Error on line 6 col 12: Var"
        self.assertTrue(TestParser.checkParser(input,expect,283))

    def test_program_84(self):
        input = """"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,284))

    def test_program_85(self):
        input = """
            Function: main
                Body:
                    Var: x;
                    x = foo
                        (x);
                EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,285))

    def test_program_86(self):
        input = """
            Function: main
                Body:
                    Var: x;
                    foo(2 + x, 4. \\. y);
                    goo();
                EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,286))

    def test_program_87(self):
        input = """
            Function: main
                Body:
                    Var: x;
                    foo(x)
                EndBody.
        """
        expect = "Error on line 6 col 16: EndBody"
        self.assertTrue(TestParser.checkParser(input,expect,287))

    def test_program_88(self):
        input = """
            Function: main
                Body:
                    Function: foo
                        Body:
                        EndBody.
                EndBody.
        """
        expect = "Error on line 4 col 20: Function"
        self.assertTrue(TestParser.checkParser(input,expect,288))

    def test_program_89(self):
        input = """
            Function: main
                Body
                    Var: x;
                    Function: foo
                        Body:
                        EndBody.
                EndBody.
        """
        expect = "Error on line 4 col 20: Var"
        self.assertTrue(TestParser.checkParser(input,expect,289))

    def test_program_90(self):
        input = """
            Function: main
                Parameter:
                Body:
                EndBody.
        """
        expect = "Error on line 4 col 16: Body"
        self.assertTrue(TestParser.checkParser(input,expect,290))

    def test_program_91(self):
        input = """
            Function: main
                Body:
                    Parameter: n
                EndBody.
        """
        expect = "Error on line 4 col 20: Parameter"
        self.assertTrue(TestParser.checkParser(input,expect,291))

    def test_program_92(self):
        input = """
            Function: main
                Body:
                EndBody.
                Parameter: n
        """
        expect = "Error on line 5 col 16: Parameter"
        self.assertTrue(TestParser.checkParser(input,expect,292))

    def test_program_93(self):
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,293))

    def test_program_94(self):
        input = """Var: x = **Comment first** "String after";"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,294))

    def test_program_95(self):
        input = """********Var: x = 0;********"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,295))

    def test_program_96(self):
        input = """
            ** Outside the function **
            Function: main
                Body:
                    ** Inside the function **
                    Var: x;
                    x = 1 + 2 * 3 ** 4 ** \\ 5;
                EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,296))

    def test_program_97(self):
        input = """
            Function: main
                Body:
                    Return **a comment**;
                EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,297))

    def test_program_98(self):
        input = """
            Function: main
                Parameter: a, b, c
                Body:
                    foo(**first comment****second comment**a, b, c);
                EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,298))

    def test_program_99(self):
        input = """
        **
            Function: main
                Body:
                    print("Hello World");
                EndBody.
        **
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,299))
