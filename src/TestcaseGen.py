import sys, os

TARGET = '../target/main/bkit/parser'
sys.path.append(TARGET)
locpath = ['./main/bkit/parser/','./main/bkit/astgen/','./main/bkit/utils/','./main/bkit/checker','./test/']
for p in locpath:
    if not p in sys.path:
        sys.path.append(p)

from TestUtils import *

f = open("./test/CheckSuite.py", "w")
content = "import unittest\nfrom TestUtils import TestChecker\nfrom StaticError import *\nfrom AST import *\n\nclass CheckSuite(unittest.TestCase):\n\n"
with open("test.txt", "r") as tc:
    line = ""
    while True:
        try:
            counter = int(tc.readline())
        except:
            break
        print(counter)
        inp = ""
        expect = ""
        while True:
            line = tc.readline().strip('\n')
            if line == ".":
                break
            inp = inp + '\n\t\t' + line
        inp = inp[1:]
        testcase = "\tdef test_checker_{}(self):\n\t\tinput = \"\"\"\n{}\n\t\t\"\"\"".format(counter, inp)
        TestChecker.checkStatic(inp, expect, 400 + counter)
        dest = open("./test/solutions/" + str(400 + counter) + ".txt","r")
        expect = dest.read()
        testcase = testcase + "\n\t\texpect = str(" + expect + ")\n\t\tself.assertTrue(TestChecker.test(input,expect,{}))\n\n".format(400 + counter)
        content = content + testcase

f.write(content)
f.close()
