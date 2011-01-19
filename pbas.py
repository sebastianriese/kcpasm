#!/usr/bin/python

# Assembler for the PicoBlaze soft core architecture

import sys
import re

import Syntax
import AST

class BitEmittor(object):
    def EmitBitStr(self, bits):

        for bit in bits:
            self.EmitBit(bit == '1')
    
    def EmitNumber(self, number, bitcnt):
        # XXX use sliding bit mask
        bits = []
        for i in xrange(bitcnt):
            bits.append(number & 1)
            number >>= 1

        bits.reverse()
        for bit in bits:
            self.EmitBit(bit)

        if number != 0:
            print "Number too wide!"
            exit(1)

    def EmitBit(self, bit):
        raise NotImplemented()

class DebugEmittor(BitEmittor):
    def __init__(self, f):
        self.bits = 0
        self.f = f

    def EmitBit(self, bit):
        
        if self.bits % 18 == 0:
            if self.bits != 0:
                self.f.write("\n")

            self.f.write("%-3x " % (self.bits / 18))

        if bit:
            self.f.write("1")
        else:
            self.f.write("0")
        
        self.bits += 1

class Assembler(object):

    def __init__(self):
        self.res = None;

    def Parse(self, infile):
        
        p = Syntax.Parser(Syntax.Lexer(infile))
        p.doc = AST.Doc()
        p.Parse()
        self.res = p.doc.instructions

    def Emit(self, emittor):
        for instr in self.res:
            instr.Emit(emittor)


if __name__ == '__main__':
    infile = None
    outfile = None

    args = sys.argv[1:]
    while args:
        arg = args.pop(0)
        
        if arg[0] == '-':
            for opt in arg[1:]:
                if opt == 'o':
                    outfile = args.pop(0)
                else:
                    print "Invalid option!"
                    exit(1)
                        

        else:
            if infile:
                print "You can only specify one input file"
                exit(1)
            infile = arg


    of = sys.stdout

    if outfile != None:
        of = file(outfile, "w")

    asm = Assembler()
    asm.Parse(infile)
    asm.Emit(DebugEmittor(of))

    if of != sys.stdout:
        of.close()
