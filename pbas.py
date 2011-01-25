#!/usr/bin/python

# Assembler for the PicoBlaze soft core architecture

import sys
import optparse
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
        raise NotImplementedError()

    def Finish(self):
        pass

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

                

class VHDLEmittor(BitEmittor):
    def __init__(self, f):
        self.f = f

        self.bits  = []
        self.bitsp = []

        self.nybbles  = ""
        self.nybblesp = ""

        self.text  = []
        self.textp = []

    def Finish(self):

        self.f.write("""--
-- Definition of a single port ROM for KCPSM3 program
--
-- Generated by kcpasm
--

library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.STD_LOGIC_ARITH.ALL;
use IEEE.STD_LOGIC_UNSIGNED.ALL;

library unisim;
use unisim.vcomponents.all;

entity code is
    Port( address : in std_logic_vector(9 downto 0);
          instruction : out std_logic_vector(17 downto 0);
          clk : in std_logic);
end code;

architecture low_level_definition of code is
""")

        for i in xrange(0x40):
            self.f.write("attribute INIT_%02x : string;\n" % i)

        for i in xrange(0x8):
            self.f.write("attribute INITP_%02x : string;\n" % i)

        for i in xrange(0x40):
            self.f.write("attribute INIT_%02x of ram_1024_x_18 : label is \"%s\";\n" % (i, self.text[i]))

        for i in xrange(0x8):
            self.f.write("attribute INITP_%02x of ram_1024_x_18 : label is \"%s\";\n" % (i, self.textp[i]))
        
        self.f.write("""
begin

ram_1024_x_18: RAMB16_S18
port map(    DI => "0000000000000000",
            DIP => "00",
             EN => '1',
             WE => '0',
            SSR => '0',
            CLK => clk,
           ADDR => address,
             DO => instruction(15 downto 0),
            DOP => instruction(17 downto 16));

end low_level_definition; 
""")

    def EmitBit(self, bit):
        self.bits.append(bit)

        def nybble(bits):
            nybble = 0
            pow2 = 1

            for bit in bits:
                if bit:
                    nybble += pow2
                pow2 *= 2

            if nybble < 10:
                return str(nybble)
            else:
                return chr(nybble-10 + ord('A'))

        # join bits to hex-nybbles
        if len(self.bits) == 18:
            self.bits.reverse()
            for i in xrange(4):
                self.nybbles = nybble(self.bits[4*i:4*i+4]) + self.nybbles
            self.bitsp   += self.bits[16:18]
            self.bits = []

        if len(self.bitsp) == 4:
            self.nybblesp = nybble(self.bitsp) + self.nybblesp
            self.bitsp = []

        # join hexnybbles to blocks
        if len(self.nybbles) == 64:
            self.text.append(self.nybbles)
            self.nybbles = ""

        if len(self.nybblesp) == 64:
            self.textp.append(self.nybblesp)
            self.nybblesp = ""


class Assembler(object):

    def __init__(self):
        self.res = None;

    def Parse(self, infile):
        
        p = Syntax.Parser(Syntax.Lexer(infile))
        p.doc = AST.Doc()
        p.Parse()
        p.doc.CheckForUndefinedLabels()
        self.res = p.doc.instructions

    def Emit(self, emittor):
        for instr in self.res:
            instr.Emit(emittor)

        emittor.Finish()


EMITTORS = {
    'vhdl' : VHDLEmittor,
    'debug': DebugEmittor,
}

if __name__ == '__main__':

    opt_parser = optparse.OptionParser(usage="usage: %prog [options] INFILE", version="%prog 0.1")
    opt_parser.add_option("-o", "--output-file", dest="ofile", help="set the output file to OFILE")
    opt_parser.add_option("-v", "--vhdl-output", dest="emittor", action="store_const", const="vhdl", help="emit VHDL code [default]", default='vhdl')
    opt_parser.add_option("-d", "--debug-output", dest="emittor", action="store_const", const="debug", help="emit debug output format")
    opt_parser.add_option("-m", "--output-mode", dest="emittor", action="store", help="emit in the format EMITTOR (currently one of 'debug' or 'vhdl')")

    options, args = opt_parser.parse_args()

    if len(args) != 1:
        opt_parser.error("you need to specify an input file")

    if options.emittor.lower() not in EMITTORS:
        opt_parser.error("invalid emission mode")

    emittor = EMITTORS[options.emittor.lower()]

    infile, = args

    of = sys.stdout

    if options.ofile != None:
        of = file(options.ofile, "w")

    asm = Assembler()
    asm.Parse(infile)
    asm.Emit(emittor(of))

    if options.ofile != None:
        of.close()
