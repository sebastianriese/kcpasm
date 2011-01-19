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
        self.start = 23
        self.table = ((0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3),
(3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 29, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3),
(3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3),
(3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3),
(26, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3),
(10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 19),
(3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3),
(3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3),
(11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 3, 3, 3, 3, 3, 3, 3, 3, 3, 7, 3),
(3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 9, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3),
(10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 19),
(11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 3, 3, 3, 3, 3, 3, 3, 3, 3, 7, 3),
(3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 25, 25, 3, 3, 3, 3, 3, 3, 3, 3, 25),
(3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3),
(30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3),
(3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3),
(31, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 31, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3),
(3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 21, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3),
(3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3),
(3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3),
(3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 22, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3),
(3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 20, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3),
(3, 3, 3, 3, 3, 3, 3, 3, 3, 28, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3),
(8, 24, 8, 8, 8, 8, 8, 8, 3, 8, 8, 8, 8, 8, 8, 3, 27, 3, 33, 2, 3, 5, 34, 15, 16, 3, 12),
(3, 3, 3, 3, 3, 3, 3, 14, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3),
(3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 25, 25, 3, 3, 3, 3, 3, 3, 3, 3, 25),
(3, 3, 1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3),
(3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 9, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3),
(3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3),
(3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 18, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3),
(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3),
(3, 13, 13, 3, 13, 13, 13, 3, 13, 3, 3, 3, 3, 13, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3),
(3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 6, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3),
(3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3),
(3, 3, 3, 3, 32, 17, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3),
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
        self.mapping = (20,20,20,20,20,20,20,20,20,16,26,17,17,17,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,16,20,20,20,20,24,20,20,19,23,20,20,18,20,22,20,1,8,8,8,8,8,8,8,8,8,25,21,20,20,20,20,20,6,6,6,6,6,6,3,3,3,3,3,3,3,3,3,3,3,12,3,3,3,3,3,3,3,3,20,20,20,20,15,20,4,6,5,13,2,6,3,3,3,3,3,3,3,10,11,3,3,0,14,9,3,3,3,7,3,3,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,)
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
        self.current_token = (8, self.position)

    def action3(self):
        if self.current_token:
            raise GotToken()
        else:
            raise Exception()

    def action4(self):
        pass

    def action5(self):
        pass

    def action6(self):
        pass

    def action7(self):
        self.current_token = (2, self.position)

    def action8(self):
        self.current_token = (1, self.position)

    def action9(self):
        self.root = self.position; self.state = self.start

    def action10(self):
        pass

    def action11(self):
        self.current_token = (1, self.position)

    def action12(self):
        self.current_token = (0, self.position)

    def action13(self):
        self.current_token = (4, self.position)

    def action14(self):
        pass

    def action15(self):
        self.current_token = (9, self.position)

    def action16(self):
        pass

    def action17(self):
        pass

    def action18(self):
        self.current_token = (6, self.position)

    def action19(self):
        self.current_token = (0, self.position)

    def action20(self):
        pass

    def action21(self):
        pass

    def action22(self):
        pass

    def action23(self):
        pass

    def action24(self):
        pass

    def action25(self):
        self.current_token = (0, self.position)

    def action26(self):
        pass

    def action27(self):
        self.root = self.position; self.state = self.start

    def action28(self):
        self.current_token = (5, self.position)

    def action29(self):
        pass

    def action30(self):
        self.current_token = (3, self.position)

    def action31(self):
        pass

    def action32(self):
        pass

    def action33(self):
        self.current_token = (7, self.position)

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
        self.atable = (((1, 15),(1, 15),(1, 15),(2,0),(2,0),(1, 15),(1, 15),(2,0),(2,0),(2,0),(2,0),),
((0, 4),(0, 8),(0, 29),(2,0),(2,0),(0, 20),(0, 2),(2,0),(2,0),(2,0),(2,0),),
((2,0),(2,0),(2,0),(0, 3),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),),
((1, 12),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),),
((1, 16),(1, 16),(1, 16),(2,0),(2,0),(1, 16),(1, 16),(2,0),(2,0),(2,0),(2,0),),
((0, 28),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),),
((0, 25),(0, 8),(0, 7),(2,0),(2,0),(0, 20),(0, 2),(2,0),(2,0),(2,0),(1, 13),),
((1, 22),(0, 8),(2,0),(2,0),(2,0),(0, 20),(0, 2),(2,0),(2,0),(2,0),(2,0),),
((1, 4),(0, 19),(2,0),(2,0),(0, 10),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),),
((1, 5),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),),
((1, 6),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(0, 11),(2,0),(2,0),(2,0),),
((2,0),(0, 12),(2,0),(0, 17),(0, 16),(2,0),(2,0),(2,0),(0, 13),(2,0),(2,0),),
((1, 10),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),),
((2,0),(2,0),(2,0),(2,0),(0, 14),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),),
((2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(0, 15),(2,0),),
((1, 9),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),),
((1, 8),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),),
((1, 7),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),),
((1, 3),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),),
((1, 2),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),),
((2,0),(0, 21),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),),
((2,0),(2,0),(2,0),(0, 22),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),),
((1, 11),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),),
((1, 19),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),),
((1, 26),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),),
((1, 0),(1, 0),(1, 0),(2,0),(2,0),(1, 0),(1, 0),(2,0),(2,0),(2,0),(1, 0),),
((1, 20),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),),
((1, 24),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),),
((1, 1),(1, 1),(1, 1),(2,0),(2,0),(1, 1),(1, 1),(2,0),(2,0),(2,0),(1, 1),),
((1, 21),(0, 8),(2,0),(2,0),(2,0),(0, 20),(0, 2),(2,0),(2,0),(2,0),(2,0),),
((1, 25),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),),
((1, 18),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),),
((1, 23),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),),
((1, 17),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),),
((2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(2,0),(1, 14),),
)
        self.gtable = ((34,1,0,0,0,0,0,0,0,),
(0,0,5,0,33,32,0,0,0,),
(0,0,0,0,0,0,0,0,0,),
(0,0,0,0,0,0,0,0,0,),
(0,0,0,0,0,0,0,0,0,),
(0,0,0,6,0,0,0,0,0,),
(0,0,0,0,26,27,0,0,0,),
(0,0,0,0,23,24,0,0,0,),
(0,0,0,0,0,0,9,0,0,),
(0,0,0,0,0,0,0,0,0,),
(0,0,0,0,0,0,0,18,0,),
(0,0,0,0,0,0,0,0,0,),
(0,0,0,0,0,0,0,0,0,),
(0,0,0,0,0,0,0,0,0,),
(0,0,0,0,0,0,0,0,0,),
(0,0,0,0,0,0,0,0,0,),
(0,0,0,0,0,0,0,0,0,),
(0,0,0,0,0,0,0,0,0,),
(0,0,0,0,0,0,0,0,0,),
(0,0,0,0,0,0,0,0,0,),
(0,0,0,0,0,0,0,0,0,),
(0,0,0,0,0,0,0,0,0,),
(0,0,0,0,0,0,0,0,0,),
(0,0,0,0,0,0,0,0,0,),
(0,0,0,0,0,0,0,0,0,),
(0,0,0,0,0,0,0,0,0,),
(0,0,0,0,0,0,0,0,0,),
(0,0,0,0,0,0,0,0,0,),
(0,0,0,0,0,0,0,0,0,),
(0,0,0,0,31,30,0,0,0,),
(0,0,0,0,0,0,0,0,0,),
(0,0,0,0,0,0,0,0,0,),
(0,0,0,0,0,0,0,0,0,),
(0,0,0,0,0,0,0,0,0,),
(0,0,0,0,0,0,0,0,0,),
)
        self.reductions = ((2,3,self.action0),
(1,3,self.action1),
(1,6,self.action2),
(2,6,self.action3),
(1,4,self.action4),
(2,4,self.action5),
(0,7,self.action6),
(2,7,self.action7),
(2,7,self.action8),
(4,7,self.action9),
(2,7,self.action10),
(3,5,self.action11),
(2,5,self.action12),
(3,0,self.action13),
(1,8,self.action14),
(0,1,self.action15),
(2,1,self.action16),
(1,2,self.action17),
(2,2,self.action18),
(4,2,self.action19),
(3,2,self.action20),
(1,2,self.action21),
(3,2,self.action22),
(1,2,self.action23),
(3,2,self.action24),
(2,2,self.action25),
(4,2,self.action26),
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
    def action2(self, result):result.sem = [AST.Name(self.stack[-1].sem)]
    def action3(self, result):result.sem = [AST.Reg(self.stack[-2].sem)] + self.stack[-1].sem
    def action4(self, result):result.sem = self.doc.BuildInstr(self.stack[-1].sem.lower(), [])
    def action5(self, result):result.sem = self.doc.BuildInstr(self.stack[-2].sem.lower(), self.stack[-1].sem)
    def action6(self, result):result.sem = []
    def action7(self, result):result.sem = [AST.Lit(int(self.stack[-1].sem, base=16))]
    def action8(self, result):result.sem = [AST.Reg(self.stack[-1].sem)]
    def action9(self, result):result.sem = [AST.RegRef(self.stack[-2].sem)]
    def action10(self, result):result.sem = [AST.Name(self.stack[-1].sem)]
    def action11(self, result):self.doc.DefineConst(self.stack[-2].sem, int(self.stack[-1].sem, base=16))
    def action12(self, result):self.doc.SetIP(int(self.stack[-1].sem, base=16))
    def action13(self, result):pass
    def action14(self, result):raise Accept()
    def action15(self, result):pass
    def action16(self, result):pass
    def action17(self, result):
        self.doc.AddInstr(self.stack[-1].sem)
    def action18(self, result):
        self.doc.DefineLabel(self.stack[-2].sem[:-1])
        self.doc.AddInstr(self.stack[-1].sem)
    def action19(self, result):
        self.doc.DefineLabel(self.stack[-2].sem[:-1])
        self.doc.AddInstr(self.stack[-1].sem)
    def action20(self, result):
        self.doc.AddInstr(self.stack[-1].sem)
    def action21(self, result):
        self.doc.DefineLabel(self.stack[-1].sem[:-1])
    def action22(self, result):
        self.doc.DefineLabel(self.stack[-1].sem[:-1])
    def action23(self, result):
        pass
    def action24(self, result):
        pass
    def action25(self, result):
        self.doc.DefineLabel(self.stack[-2].sem[:-1])
    def action26(self, result):
        self.doc.DefineLabel(self.stack[-2].sem[:-1])