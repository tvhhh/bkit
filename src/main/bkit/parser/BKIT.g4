// Student ID: 1852435

grammar BKIT;

@lexer::header {
from lexererr import *
}

@lexer::members {
def emit(self):
    tk = self.type
    result = super().emit()
    if tk == self.UNCLOSE_STRING:       
        raise UncloseString(result.text[1:])
    elif tk == self.ILLEGAL_ESCAPE:
        raise IllegalEscape(result.text[1:])
    elif tk == self.ERROR_CHAR:
        raise ErrorToken(result.text)
    elif tk == self.UNTERMINATED_COMMENT:
        raise UnterminatedComment()
    else:
        if tk == self.STRING:
            result.text = result.text[1:-1]
        return result
}

options{
	language=Python3;
}

// Program structure

program: varStmt* func* EOF;

func: funcDecl param? funcBody;
funcDecl: FUNC COLON ID;
param: PARAM COLON paramDecls;
funcBody: BODY COLON stmtlist ENDBODY DOT;
paramDecls: paramDecl (COMMA paramDecl)*;
paramDecl: ID (LSB INT RSB)*;

varStmt: VAR COLON varDecls SEMI;
varDecls: varDecl (COMMA varDecl)*;
varDecl: ID (LSB INT RSB)* (ASSIGN literal)?;
arr: LCB (literal (COMMA literal)*)? RCB;
literal: INT | FLOAT | BOOLEAN | STRING | arr;

stmtlist: varStmt* stmt*;
stmt: assignStmt 
    | ifStmt 
    | forStmt 
    | whileStmt 
    | doWhileStmt 
    | breakStmt 
    | continueStmt 
    | callStmt 
    | returnStmt;
assignStmt: (ID | (expr7 idxOperator)) ASSIGN expr SEMI;
ifStmt: IF expr THEN stmtlist (ELSEIF expr THEN stmtlist)* (ELSE stmtlist)? ENDIF DOT;
forStmt: FOR LB ID ASSIGN expr COMMA expr COMMA expr RB DO stmtlist ENDFOR DOT;
whileStmt: WHILE expr DO stmtlist ENDWHILE DOT;
doWhileStmt: DO stmtlist WHILE expr ENDDO DOT;
breakStmt: BREAK SEMI;
continueStmt: CONTINUE SEMI;
callStmt: ID LB (expr (COMMA expr)*)? RB SEMI;
returnStmt: RET expr? SEMI;

expr : expr0 | STRING | arr;
expr0: expr1 | expr1 RELATIONAL expr1;
expr1: expr2 | expr1 LOGICAL expr2;
expr2: expr3 | expr2 (ADD | MINUS) expr3;
expr3: expr4 | expr3 MUL expr4;
expr4: expr5 | NOT expr4;
expr5: expr6 | MINUS expr5;
expr6: expr7 | expr7 idxOperator;
expr7: LB expr0 RB | callExpr | ID | INT | FLOAT | BOOLEAN;
idxOperator: (LSB expr0 RSB)+;
callExpr: ID LB (expr (COMMA expr)*)? RB;


// Lexical structure

fragment LEGAL_CHAR_CMT: ~'*' | '*'(~'*')+;
COMMENT: '**' LEGAL_CHAR_CMT* '**' -> skip;
UNTERMINATED_COMMENT: '**' LEGAL_CHAR_CMT*;

BODY: 'Body';
BREAK: 'Break';
CONTINUE: 'Continue';
DO: 'Do';
ELSE: 'Else';
ELSEIF: 'ElseIf';
ENDBODY: 'EndBody';
ENDDO: 'EndDo';
ENDFOR: 'EndFor';
ENDIF: 'EndIf';
ENDWHILE: 'EndWhile';
FOR: 'For';
FUNC: 'Function';
IF: 'If';
PARAM: 'Parameter';
RET: 'Return';
THEN: 'Then';
VAR: 'Var';
WHILE: 'While';

ASSIGN: '=';
RELATIONAL: '==' | '!=' | '<' | '>' | '<=' | '>=' | '=/=' | '<.' | '>.' | '<=.' | '>=.';
LOGICAL: '&&' | '||';
ADD: '+' | '+.';
MINUS: '-' | '-.';
MUL: '*' | '\\' | '%' | '*.' | '\\.';
NOT: '!';

ID: [a-z][0-9a-zA-Z_]*;
SEMI: ';';
COLON: ':';
COMMA: ',';
DOT: '.';
LB: '('; // brackets
RB: ')';
LSB: '['; // square brackets
RSB: ']';
LCB: '{'; // curly brackets
RCB: '}';
WS : [ \t\r\n]+ -> skip;

fragment INT_DEC: '0' | [1-9][0-9]*;
fragment INT_HEX: '0'[xX][1-9A-F][0-9A-F]*;
fragment INT_OCT: '0'[oO][1-7][0-7]*;
INT: INT_DEC | INT_HEX | INT_OCT;

fragment DIGIT: [0-9];
fragment FLOAT_DEC_PART: '.' DIGIT*;
fragment FLOAT_EXP_PART: [eE][+-]? DIGIT+;
FLOAT: INT_DEC (FLOAT_DEC_PART | FLOAT_EXP_PART | FLOAT_DEC_PART FLOAT_EXP_PART);

BOOLEAN: 'True' | 'False';

fragment ESC_SEQ: '\\'[bfrnt'\\];
fragment QUOTE_IN_STR: '\'"';
fragment LEGAL_CHAR_STR: ~[\n\r\\"'] | ESC_SEQ | QUOTE_IN_STR;
STRING: '"' LEGAL_CHAR_STR* '"';
ILLEGAL_ESCAPE: '"' (~'"')*?('\\'~[bfrnt'\\] | '\''~'"');
UNCLOSE_STRING: '"' LEGAL_CHAR_STR*;

ERROR_CHAR: .;