# this file was generated automagically by pyLR1
# do not edit, if you want to modify the parser, adapt the grammar file

import mmap

import AST

class GotToken(Exception):
    pass

class Position(object):
    def __init__(self, file, line0, col0, line1, col1):
        self.file  = file
        self.line0 = line0
        self.col0  = col0
        self.line1 = line1
        self.col1  = col1

    def Add(self, oth):
        return Position(self.file, self.line0, self.col0, oth.line1, oth.col1)

    def __str__(self):
        return "Line %d:%d - %d:%d" % (self.line0, self.col0, self.line1, self.col1)


class Lexer(object):
    def __init__(self, codefile):
        code = file(codefile, 'r')
        self.buffer = mmap.mmap(code.fileno(), 0, access=mmap.ACCESS_READ)
        self.size = self.buffer.size()
        code.close()
        self.root = 0
        self.last_token_end = 0
        self.position = 0
        self.current_token = None
        self.start = 33
        self.table = ((0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2),
(2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 11, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2),
(2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2),
(2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 27, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2),
(25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 20),
(2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 14, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2),
(9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 2, 2, 2, 2, 2, 2, 2, 2, 2, 15, 2),
(1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2),
(2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 13, 2, 2),
(9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 2, 2, 2, 2, 2, 2, 2, 2, 2, 15, 2),
(2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 26, 26, 2, 26),
(2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 16, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2),
(2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 34, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2),
(2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 13, 2, 2),
(2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 29, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2),
(2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2),
(2, 32, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2),
(2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2),
(2, 2, 24, 24, 24, 24, 24, 24, 2, 2, 24, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2),
(2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2),
(2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2),
(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2),
(2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2),
(2, 2, 2, 2, 2, 2, 2, 2, 2, 18, 2, 2, 18, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2),
(2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2),
(25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 20),
(2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 26, 26, 2, 26),
(2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2),
(2, 2, 2, 2, 2, 2, 2, 5, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2),
(2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2),
(2, 2, 2, 2, 2, 7, 31, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2),
(2, 2, 2, 2, 2, 2, 2, 28, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2),
(2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2),
(6, 6, 2, 12, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 2, 2, 4, 17, 19, 22, 23, 30, 2, 8, 2, 10),
(21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2),
)
        self.actions = (
            self.action0, 
            self.action1, 
            self.action2, 
            self.action3, 
            self.action4, 
            self.action5, 
            self.action6, 
            self.action7, 
            self.action8, 
            self.action9, 
            self.action10, 
            self.action11, 
            self.action12, 
            self.action13, 
            self.action14, 
            self.action15, 
            self.action16, 
            self.action17, 
            self.action18, 
            self.action19, 
            self.action20, 
            self.action21, 
            self.action22, 
            self.action23, 
            self.action24, 
            self.action25, 
            self.action26, 
            self.action27, 
            self.action28, 
            self.action29, 
            self.action30, 
            self.action31, 
            self.action32, 
            self.action33, 
            self.action34, 
        )
        self.mapping = (16,16,16,16,16,16,16,16,16,24,26,23,23,23,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,24,16,16,16,16,21,16,16,18,20,16,16,19,16,22,16,3,2,2,2,2,2,2,2,2,2,25,17,16,16,16,16,16,4,4,4,4,4,4,8,8,8,8,8,8,8,8,8,8,8,9,8,8,8,8,8,8,8,8,16,16,16,16,15,16,6,4,5,7,10,4,8,8,8,8,8,8,8,14,0,8,8,12,13,1,8,8,8,11,8,8,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,)
        self.line    = 1
        self.linestart = 0

    def lex(self):
        self.current_token = (10, self.size)
        self.state = self.start
        table = self.table
        actions = self.actions
        buffer = self.buffer
        mapping = self.mapping
        try:
            while self.position != self.size:
                if buffer[self.position] == '\n': self.linestart = self.position - 1
                self.state = table[self.state][mapping[ord(buffer[self.position])]]
                self.position += 1
                actions[self.state]()
            raise GotToken()
        except GotToken:
           name, pos = self.current_token
           self.line += self.buffer[self.last_token_end:pos].count('\n'); position = Position('', self.line, self.root-self.linestart, self.line, pos - self.linestart)
           text = self.buffer[self.root:pos]
           self.root = pos
           self.last_token_end = pos
           self.position = self.root
           return (name, text, position)

    def action0(self):
        self.current_token = (3, self.position)

    def action1(self):
        pass

    def action2(self):
        if self.current_token:
            raise GotToken()
        else:
            raise Exception()

    def action3(self):
        pass

    def action4(self):
        pass

    def action5(self):
        pass

    def action6(self):
        self.current_token = (1, self.position)

    def action7(self):
        pass

    def action8(self):
        self.root = self.position; self.state = self.start

    def action9(self):
        self.current_token = (1, self.position)

    def action10(self):
        self.current_token = (0, self.position)

    def action11(self):
        pass

    def action12(self):
        pass

    def action13(self):
        self.root = self.position; self.state = self.start

    def action14(self):
        pass

    def action15(self):
        self.current_token = (2, self.position)

    def action16(self):
        pass

    def action17(self):
        self.current_token = (8, self.position)

    def action18(self):
        pass

    def action19(self):
        self.current_token = (7, self.position)

    def action20(self):
        self.current_token = (0, self.position)

    def action21(self):
        self.current_token = (3, self.position)

    def action22(self):
        self.current_token = (9, self.position)

    def action23(self):
        pass

    def action24(self):
        self.current_token = (4, self.position)

    def action25(self):
        pass

    def action26(self):
        self.current_token = (0, self.position)

    def action27(self):
        self.current_token = (6, self.position)

    def action28(self):
        pass

    def action29(self):
        pass

    def action30(self):
        pass

    def action31(self):
        pass

    def action32(self):
        self.current_token = (5, self.position)

    def action33(self):
        pass

    def action34(self):
        pass

class Accept(Exception):
    pass

class StackObject(object):
    def __init__(self, state):
        self.state = state
        self.pos = None
        self.sem = None

class Parser(object):
    # actions from the grammar

    # auto generated methods
    def __init__(self, lexer):
        self.lexer = lexer
        self.stack = []
        self.start = 0
        self.atable = (((0, 1),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),),
((1, 1),(1, 1),(1, 1),(2,0),(2,0),(1, 1),(1, 1),(2,0),(2,0),(2,0),(2,0),),
((0, 15),(0, 3),(0, 16),(2,0),(2,0),(0, 17),(0, 22),(2,0),(2,0),(2,0),(2,0),),
((1, 7),(0, 13),(2,0),(2,0),(0, 4),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),),
((1, 2),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(0, 5),(2,0),(2,0),(2,0),),
((2,0),(0, 10),(2,0),(0, 6),(0, 11),(2,0),(2,0),(2,0),(0, 7),(2,0),(2,0),),
((1, 3),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),),
((2,0),(2,0),(2,0),(2,0),(0, 8),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),),
((2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(0, 9),(2,0),),
((1, 5),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),),
((1, 6),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),),
((1, 4),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),),
((1, 24),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),),
((1, 23),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),),
((1, 8),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),),
((1, 0),(1, 0),(1, 0),(2,0),(2,0),(1, 0),(1, 0),(2,0),(2,0),(2,0),(2,0),),
((1, 17),(0, 3),(2,0),(2,0),(2,0),(0, 17),(0, 22),(2,0),(2,0),(2,0),(2,0),),
((2,0),(0, 18),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),),
((2,0),(2,0),(2,0),(0, 19),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),),
((1, 9),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),),
((1, 14),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),),
((1, 21),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),),
((2,0),(2,0),(2,0),(0, 23),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),),
((1, 10),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),),
((0, 32),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),),
((0, 31),(0, 3),(0, 28),(2,0),(2,0),(0, 17),(0, 22),(2,0),(2,0),(2,0),(1, 11),),
((1, 20),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),),
((1, 16),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),),
((1, 18),(0, 3),(2,0),(2,0),(2,0),(0, 17),(0, 22),(2,0),(2,0),(2,0),(2,0),),
((1, 22),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),),
((1, 15),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),),
((1, 0),(1, 0),(1, 0),(2,0),(2,0),(1, 0),(1, 0),(2,0),(2,0),(2,0),(1, 0),),
((1, 1),(1, 1),(1, 1),(2,0),(2,0),(1, 1),(1, 1),(2,0),(2,0),(2,0),(1, 1),),
((1, 19),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),),
((1, 13),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),),
((2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(1, 12),),
)
        self.gtable = ((35,2,0,0,0,0,0,0,),
(0,0,0,0,0,0,0,0,),
(0,0,24,34,33,0,0,0,),
(0,0,0,0,0,14,0,0,),
(0,0,0,0,0,0,12,0,),
(0,0,0,0,0,0,0,0,),
(0,0,0,0,0,0,0,0,),
(0,0,0,0,0,0,0,0,),
(0,0,0,0,0,0,0,0,),
(0,0,0,0,0,0,0,0,),
(0,0,0,0,0,0,0,0,),
(0,0,0,0,0,0,0,0,),
(0,0,0,0,0,0,0,0,),
(0,0,0,0,0,0,0,0,),
(0,0,0,0,0,0,0,0,),
(0,0,0,0,0,0,0,0,),
(0,0,0,20,21,0,0,0,),
(0,0,0,0,0,0,0,0,),
(0,0,0,0,0,0,0,0,),
(0,0,0,0,0,0,0,0,),
(0,0,0,0,0,0,0,0,),
(0,0,0,0,0,0,0,0,),
(0,0,0,0,0,0,0,0,),
(0,0,0,0,0,0,0,0,),
(0,25,0,0,0,0,0,0,),
(0,0,0,27,26,0,0,0,),
(0,0,0,0,0,0,0,0,),
(0,0,0,0,0,0,0,0,),
(0,0,0,30,29,0,0,0,),
(0,0,0,0,0,0,0,0,),
(0,0,0,0,0,0,0,0,),
(0,0,0,0,0,0,0,0,),
(0,0,0,0,0,0,0,0,),
(0,0,0,0,0,0,0,0,),
(0,0,0,0,0,0,0,0,),
(0,0,0,0,0,0,0,0,),
)
        self.reductions = ((2,1,self.action0),
(1,1,self.action1),
(0,6,self.action2),
(2,6,self.action3),
(2,6,self.action4),
(4,6,self.action5),
(2,6,self.action6),
(1,3,self.action7),
(2,3,self.action8),
(3,4,self.action9),
(2,4,self.action10),
(3,0,self.action11),
(1,7,self.action12),
(1,2,self.action13),
(2,2,self.action14),
(4,2,self.action15),
(3,2,self.action16),
(1,2,self.action17),
(3,2,self.action18),
(1,2,self.action19),
(3,2,self.action20),
(2,2,self.action21),
(4,2,self.action22),
(1,5,self.action23),
(2,5,self.action24),
)
 
    def Parse(self):
        lexer = self.lexer
        atable = self.atable
        gtable = self.gtable
        stack = self.stack
        reductions = self.reductions
        stack.append(StackObject(self.start))
        stack[-1].pos = Position('', 0,0,0,0)

        try:
            while True:
                token, lexeme, pos = lexer.lex()
                t, d = atable[stack[-1].state][token]

                while t == 1:
                    size, sym, action = reductions[d]
                    state = gtable[stack[-size-1].state][sym]
                    new = StackObject(state)
                    new.pos = stack[-size].pos.Add(stack[-1].pos)
                    action(new)

                    for j in xrange(size):
                        stack.pop()

                    stack.append(new)
                    t, d = atable[stack[-1].state][token]

                if t == 0:
                    new = StackObject(d)
                    new.sem = lexeme
                    new.pos = pos
                    stack.append(new)
                    # action, e.g. a lexcal tie-in

                else:
                    raise Exception("Syntax Error: " + str(stack[-1].pos))
        except Accept:
            return stack[-1].sem

    def action0(self, result):pass
    def action1(self, result):pass
    def action2(self, result):result.sem = []
    def action3(self, result):result.sem = [AST.Lit(int(self.stack[-1].sem, base=16))]
    def action4(self, result):result.sem = [AST.Reg(self.stack[-1].sem)]
    def action5(self, result):result.sem = [AST.RegRef(self.stack[-2].sem)]
    def action6(self, result):result.sem = [AST.Name(self.stack[-1].sem)]
    def action7(self, result):result.sem = self.doc.BuildInstr(self.stack[-1].sem.lower(), [])
    def action8(self, result):result.sem = self.doc.BuildInstr(self.stack[-2].sem.lower(), self.stack[-1].sem)
    def action9(self, result):self.doc.DefineConst(self.stack[-2].sem, int(self.stack[-1].sem, base=16))
    def action10(self, result):self.doc.SetIP(int(self.stack[-1].sem, base=16))
    def action11(self, result):pass
    def action12(self, result):raise Accept()
    def action13(self, result):
        self.doc.AddInstr(self.stack[-1].sem)
    def action14(self, result):
        self.doc.DefineLabel(self.stack[-2].sem[:-1])
        self.doc.AddInstr(self.stack[-1].sem)
    def action15(self, result):
        self.doc.DefineLabel(self.stack[-2].sem[:-1])
        self.doc.AddInstr(self.stack[-1].sem)
    def action16(self, result):
        self.doc.AddInstr(self.stack[-1].sem)
    def action17(self, result):
        self.doc.DefineLabel(self.stack[-1].sem[:-1])
    def action18(self, result):
        self.doc.DefineLabel(self.stack[-1].sem[:-1])
    def action19(self, result):
        pass
    def action20(self, result):
        pass
    def action21(self, result):
        self.doc.DefineLabel(self.stack[-2].sem[:-1])
    def action22(self, result):
        self.doc.DefineLabel(self.stack[-2].sem[:-1])
    def action23(self, result):result.sem = [AST.Name(self.stack[-1].sem)]
    def action24(self, result):result.sem = [AST.Reg(self.stack[-2].sem)] + self.stack[-1].sem