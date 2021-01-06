import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):

    def test_lower_id(self):
        self.assertTrue(TestLexer.checkLexeme("abc", "abc,<EOF>", 100))
    
    def test_lower_upper_id(self):
        self.assertTrue(TestLexer.checkLexeme("abABab", "abABab,<EOF>", 101))
    
    def test_lower_number_id(self):
        self.assertTrue(TestLexer.checkLexeme("ab1234", "ab1234,<EOF>", 102))
    
    def test_lower_underscore_id(self):
        self.assertTrue(TestLexer.checkLexeme("ab__", "ab__,<EOF>", 103))
    
    def test_upper_id(self):
        self.assertTrue(TestLexer.checkLexeme("ABC", "Error Token A", 104))
    
    def test_multi_id(self):
        self.assertTrue(TestLexer.checkLexeme("abcDE ab_123", "abcDE,ab_123,<EOF>", 105))
    
    def test_invalid_id(self):
        self.assertTrue(TestLexer.checkLexeme("abc?def", "abc,Error Token ?", 106))
    
    def test_comment(self):
        self.assertTrue(TestLexer.checkLexeme("** This is a comment. **", "<EOF>", 107))
    
    def test_comment_with_star(self):
        self.assertTrue(TestLexer.checkLexeme("** There is a * inside this comment. **", "<EOF>", 108))
    
    def test_multiline_comment(self):
        self.assertTrue(TestLexer.checkLexeme("** This is a\n * multi-line\n * comment.\n **", "<EOF>", 109))
    
    def test_unterminated_comment(self):
        self.assertTrue(TestLexer.checkLexeme("** This comment is unterminated.", "Unterminated Comment", 110))
    
    def test_unterminated_multiline_comment(self):
        self.assertTrue(TestLexer.checkLexeme("** This multi-line comment\\n * is unterminated.", "Unterminated Comment", 111))
    
    def test_multiple_comment(self):
        self.assertTrue(TestLexer.checkLexeme("** This is the first comment. ** ** This is the second comment. **", "<EOF>", 112))
    
    def test_comment_and_unterminated_comment(self):
        self.assertTrue(TestLexer.checkLexeme("** This is a comment. ** ** This is an unterminated comment.", "Unterminated Comment", 113))
    
    def test_keyword(self):
        self.assertTrue(TestLexer.checkLexeme("Var: x, y, z", "Var,:,x,,,y,,,z,<EOF>", 114))
    
    def test_multiple_keyword(self):
        self.assertTrue(TestLexer.checkLexeme("Function: abc\n\tBody:\n\t\tdef\n\tEndBody.", "Function,:,abc,Body,:,def,EndBody,.,<EOF>", 115))
    
    def test_wrong_keyword(self):
        self.assertTrue(TestLexer.checkLexeme("Bodiyy", "Error Token B", 116))
    
    def test_separator(self):
        self.assertTrue(TestLexer.checkLexeme("a,b,c", "a,,,b,,,c,<EOF>", 117))
    
    def test_parentheses(self):
        self.assertTrue(TestLexer.checkLexeme("(abcdef)", "(,abcdef,),<EOF>", 118))
    
    def test_brackets(self):
        self.assertTrue(TestLexer.checkLexeme("{123} [456]", "{,123,},[,456,],<EOF>", 119))
    
    def test_multiple_separators(self):
        self.assertTrue(TestLexer.checkLexeme("1,2:3;4", "1,,,2,:,3,;,4,<EOF>", 120))

    def test_nested_separators(self):
        self.assertTrue(TestLexer.checkLexeme("{[(abcdef)]}", "{,[,(,abcdef,),],},<EOF>", 121))
    
    def test_decimal_integer(self):
        self.assertTrue(TestLexer.checkLexeme("12345", "12345,<EOF>", 122))
    
    def test_decimal_integer_begin_zero(self):
        self.assertTrue(TestLexer.checkLexeme("010101", "0,10101,<EOF>", 123))
    
    def test_hexa_integer(self):
        self.assertTrue(TestLexer.checkLexeme("0x123AB 0X45CDE", "0x123AB,0X45CDE,<EOF>", 124))
    
    def test_hexa_integer_begin_zero(self):
        self.assertTrue(TestLexer.checkLexeme("0x00ABC", "0,x00ABC,<EOF>", 125))
    
    def test_hexa_integer_prefix(self):
        self.assertTrue(TestLexer.checkLexeme("00xABC", "0,0xABC,<EOF>", 126))
    
    def test_hexa_integer_invalid_char(self):
        self.assertTrue(TestLexer.checkLexeme("0xABCDEFG", "0xABCDEF,Error Token G", 127))
    
    def test_octa_integer(self):
        self.assertTrue(TestLexer.checkLexeme("0o12367 0O10007", "0o12367,0O10007,<EOF>", 128))
    
    def test_octa_integer_begin_zero(self):
        self.assertTrue(TestLexer.checkLexeme("0o01234567", "0,o01234567,<EOF>", 129))
    
    def test_octa_integer_prefix(self):
        self.assertTrue(TestLexer.checkLexeme("00o1234567", "0,0o1234567,<EOF>", 130))
    
    def test_octa_integer_invalid_char(self):
        self.assertTrue(TestLexer.checkLexeme("0o123456789", "0o1234567,89,<EOF>", 131))
    
    def test_invalid_integer(self):
        self.assertTrue(TestLexer.checkLexeme("0A12345", "0,Error Token A", 132))
    
    def test_hexa_octa_integer(self):
        self.assertTrue(TestLexer.checkLexeme("0xABCo123", "0xABC,o123,<EOF>", 133))
    
    def test_merged_multiple_base_integer(self):
        self.assertTrue(TestLexer.checkLexeme("12340xabc0o123", "12340,xabc0o123,<EOF>", 134))
    
    def test_float_with_fraction(self):
        self.assertTrue(TestLexer.checkLexeme("1.01 10.", "1.01,10.,<EOF>", 135))
    
    def test_float_with_exp(self):
        self.assertTrue(TestLexer.checkLexeme("123e+10 45e-10", "123e+10,45e-10,<EOF>", 136))
    
    def test_float_with_both(self):
        self.assertTrue(TestLexer.checkLexeme("12.3e4 1.e-5", "12.3e4,1.e-5,<EOF>", 137))
    
    def test_float_without_int(self):
        self.assertTrue(TestLexer.checkLexeme(".12345e10", ".,12345e10,<EOF>", 138))
    
    def test_invalid_fraction_float(self):
        self.assertTrue(TestLexer.checkLexeme("1.2.3", "1.2,.,3,<EOF>", 139))
    
    def test_invalid_exp_float(self):
        self.assertTrue(TestLexer.checkLexeme("1.2e3e4e5", "1.2e3,e4e5,<EOF>", 140))
    
    def test_multiple_dot_float(self):
        self.assertTrue(TestLexer.checkLexeme("1.234.5", "1.234,.,5,<EOF>", 141))
    
    def test_true_boolean(self):
        self.assertTrue(TestLexer.checkLexeme("True", "True,<EOF>", 142))
    
    def test_false_boolean(self):
        self.assertTrue(TestLexer.checkLexeme("False", "False,<EOF>", 143))
    
    def test_boolean(self):
        self.assertTrue(TestLexer.checkLexeme("TrueFalseTrueFalse", "True,False,True,False,<EOF>", 144))

    def test_integer_op(self):
        self.assertTrue(TestLexer.checkLexeme("123 + 456 1 == 0 20 % 5", "123,+,456,1,==,0,20,%,5,<EOF>", 145))
    
    def test_float_op(self):
        self.assertTrue(TestLexer.checkLexeme("1.0 +. 0.1 1.2 =/= 1.2 5.5 \\. 1.1", "1.0,+.,0.1,1.2,=/=,1.2,5.5,\\.,1.1,<EOF>", 146))
    
    def test_boolean_op(self):
        self.assertTrue(TestLexer.checkLexeme("True && True False || False", "True,&&,True,False,||,False,<EOF>", 147))
    
    def test_arith_op(self):
        self.assertTrue(TestLexer.checkLexeme("1 + 2 - 3 * 4 \\ 5", "1,+,2,-,3,*,4,\\,5,<EOF>", 148))
    
    def test_rela_op(self):
        self.assertTrue(TestLexer.checkLexeme("a < b b == c c >= a", "a,<,b,b,==,c,c,>=,a,<EOF>", 149))
    
    def test_unary_op(self):
        self.assertTrue(TestLexer.checkLexeme("!a", "!,a,<EOF>", 150))
    
    def test_multiple_unary_op(self):
        self.assertTrue(TestLexer.checkLexeme("!!!!a", "!,!,!,!,a,<EOF>", 151))
    
    def test_ops(self):
        self.assertTrue(TestLexer.checkLexeme("++.--.* *.\\\\.<<.>>.<=<=.>=>=.===/=", "+,+.,-,-.,*,*.,\\,\\.,<,<.,>,>.,<=,<=.,>=,>=.,==,=/=,<EOF>", 152))
    
    def test_string(self):
        self.assertTrue(TestLexer.checkLexeme(""" "abcdef" """, """abcdef,<EOF>""", 153))
    
    def test_legal_escape(self):
        self.assertTrue(TestLexer.checkLexeme(""" "abc\\n def" """, """abc\\n def,<EOF>""", 154))
    
    def test_multiple_escape(self):
        self.assertTrue(TestLexer.checkLexeme(""" "ab\\tcd e\\nf" """, """ab\\tcd e\\nf,<EOF>""", 155))
    
    def test_quote_in_string(self):
        self.assertTrue(TestLexer.checkLexeme(""" "abc'"def gh" """, """abc'"def gh,<EOF>""", 156))
    
    def test_legal_escape_and_quote_string(self):
        self.assertTrue(TestLexer.checkLexeme(""" "abc'"def gh\\n" """, """abc'"def gh\\n,<EOF>""", 157))

    def test_illegal_escape_quote_in_string(self):
        self.assertTrue(TestLexer.checkLexeme(""" "abc'def gh" """, """Illegal Escape In String: abc'd""", 158))

    def test_illegal_escape_quote_begin_string(self):
        self.assertTrue(TestLexer.checkLexeme(""" "'abcdef" """, """Illegal Escape In String: 'a""", 159))
    
    def test_tab_in_string(self):
        self.assertTrue(TestLexer.checkLexeme(""" "This is a string containing tab \t" """, """This is a string containing tab \t,<EOF>""", 160))
    
    def test_line_break_string(self):
        self.assertTrue(TestLexer.checkLexeme(""" "abc'"def\nThis is a new line" """, """Unclosed String: abc'\"def""", 161))
    
    def test_illegal_escape_backslash(self):
        self.assertTrue(TestLexer.checkLexeme(""" "abc\\h def" """, """Illegal Escape In String: abc\\h""", 162))
    
    def test_illegal_escape_multiple_backslash(self):
        self.assertTrue(TestLexer.checkLexeme(""" "abc\\\\\\ def" """, """Illegal Escape In String: abc\\\\\\ """, 163))
    
    def test_unclose_string(self):
        self.assertTrue(TestLexer.checkLexeme(""" "abc def """, """Unclosed String: abc def """, 164))
    
    def test_multiple_quotes_string(self):
        self.assertTrue(TestLexer.checkLexeme(""" "abc" def"ab """, """abc,def,Unclosed String: ab """, 165))
    
    def test_multiple_string(self):
        self.assertTrue(TestLexer.checkLexeme(""" "abc""def" """, """abc,def,<EOF>""", 166))
    
    def test_illegal_escape_and_unclose_string(self):
        self.assertTrue(TestLexer.checkLexeme(""" "ab\\hc def """, """Illegal Escape In String: ab\\h""", 167))
    
    def test_single_quote_end_string(self):
        self.assertTrue(TestLexer.checkLexeme(""" "abcdef'" """, """Unclosed String: abcdef'\" """, 168))
    
    def test_illegal_backslash_end_string(self):
        self.assertTrue(TestLexer.checkLexeme(""" "abcdef\\" """, """Illegal Escape In String: abcdef\\\"""", 169))
    
    def test_single_double_quote_string(self):
        self.assertTrue(TestLexer.checkLexeme(""" "\\'" """, """\\',<EOF>""", 170))
    
    def test_multiple_legal_quote_string(self):
        self.assertTrue(TestLexer.checkLexeme(""" "\\''"'"\\'" """, """\\''"'"\\',<EOF>""", 171))
    
    def test_illegal_backslash_and_quote(self):
        self.assertTrue(TestLexer.checkLexeme(""" "\\abc'def" """, """Illegal Escape In String: \\a""", 172))
    
    def test_illegal_quote_and_backslash(self):
        self.assertTrue(TestLexer.checkLexeme(""" "'abc\\def" """, """Illegal Escape In String: 'a""", 173))
    
    def test_illegal_escape_outside_string(self):
        self.assertTrue(TestLexer.checkLexeme(""" "abcdef"\\ """, """abcdef,\\,<EOF>""", 174))
    
    def test_legal_escape_outside_string(self):
        self.assertTrue(TestLexer.checkLexeme(""" "abcdef"'" """, """abcdef,Error Token '""", 175))

    def test_string_inside_string(self):
        self.assertTrue(TestLexer.checkLexeme(""" "He asked me: '"Where is John?'"" """, """He asked me: '"Where is John?'",<EOF>""", 176))
    
    def test_string_of_comment(self):
        self.assertTrue(TestLexer.checkLexeme(""" " **This string contains a comment.** " """, """ **This string contains a comment.** ,<EOF>""", 177))
    
    def test_comment_of_string(self):
        self.assertTrue(TestLexer.checkLexeme(""" ** "This comment contains a string." ** """, """<EOF>""", 178))
    
    def test_complex_string(self):
        self.assertTrue(TestLexer.checkLexeme(""" \"\"\"We use \\' for single-quote and '" for double-quote\"\"\" """, """,We use \\' for single-quote and '" for double-quote,,<EOF>""", 179))
    
    def test_windows_path_string(self):
        self.assertTrue(TestLexer.checkLexeme(""" "C:\\\\Users\\\\Admin\\\\Windows\\\\" """, """C:\\\\Users\\\\Admin\\\\Windows\\\\,<EOF>""", 180))
    
    def test_array(self):
        self.assertTrue(TestLexer.checkLexeme("{1,2,3,4,5}", "{,1,,,2,,,3,,,4,,,5,},<EOF>", 181))
    
    def test_multiple_type_array(self):
        self.assertTrue(TestLexer.checkLexeme("{1,2.3,3e4,0x45,\"6789\"}", "{,1,,,2.3,,,3e4,,,0x45,,,6789,},<EOF>", 182))
    
    def test_nested_array(self):
        self.assertTrue(TestLexer.checkLexeme("{{1,2,3},{4,5,6}}", "{,{,1,,,2,,,3,},,,{,4,,,5,,,6,},},<EOF>", 183))
    
    def test_array_of_string(self):
        self.assertTrue(TestLexer.checkLexeme("{\"abc\",\"def\",\"xyz\"}", "{,abc,,,def,,,xyz,},<EOF>", 184))
    
    def test_string_of_array_without_escape(self):
        self.assertTrue(TestLexer.checkLexeme(""" "{"abc","def","xyz"}" """, """{,abc,,,def,,,xyz,},<EOF>""", 185))
    
    def test_string_of_array_with_escape(self):
        self.assertTrue(TestLexer.checkLexeme(""" "{'"abc'",'"def'",'"xyz'"}" """, """{'"abc'",'"def'",'"xyz'"},<EOF>""", 186))
    
    def test_comment_in_array(self):
        self.assertTrue(TestLexer.checkLexeme("{**Comment here**,1,2,3,4,5}", """{,,,1,,,2,,,3,,,4,,,5,},<EOF>""", 187))
    
    def test_multiline_array(self):
        self.assertTrue(TestLexer.checkLexeme("{\n**Comment here**,\n1,\n\"234\",\n34.e5}", """{,,,1,,,234,,,34.e5,},<EOF>""", 188))
    
    def test_2_3_star_comment(self):
        self.assertTrue(TestLexer.checkLexeme("** ***", """*,<EOF>""", 189))
    
    def test_3_2_star_comment(self):
        self.assertTrue(TestLexer.checkLexeme("*** **", """<EOF>""", 190))
    
    def test_5_star_comment(self):
        self.assertTrue(TestLexer.checkLexeme("*****", """*,<EOF>""", 191))
    
    def test_6_star_comment(self):
        self.assertTrue(TestLexer.checkLexeme("******", """Unterminated Comment""", 192))
    
    def test_token_mix_1(self):
        self.assertTrue(TestLexer.checkLexeme("*a*", """*,a,*,<EOF>""", 193))
    
    def test_token_mix_2(self):
        self.assertTrue(TestLexer.checkLexeme("12a9*\\\"str\"", """12,a9,*,\\,str,<EOF>""", 194))
    
    def test_token_mix_3(self):
        self.assertTrue(TestLexer.checkLexeme("*(**abcd*)***", """*,(,*,<EOF>""", 195))
    
    def test_string_multiple_double_quotes(self):
        self.assertTrue(TestLexer.checkLexeme("\"\"\"\"\"abcd__\"\"\"", """,,abcd__,,<EOF>""", 196))
    
    def test_comment_with_3_star_block(self):
        self.assertTrue(TestLexer.checkLexeme("***\\\\\\***", """*,<EOF>""", 197))
    
    def test_comment_with_4_star_block(self):
        self.assertTrue(TestLexer.checkLexeme("****\\\\\\****", """\\,\\,\\,<EOF>""", 198))
    
    def test_comment_in_expression(self):
        self.assertTrue(TestLexer.checkLexeme("1 + 2 * 3 ** 4 ** * 5", """1,+,2,*,3,*,5,<EOF>""", 199))
