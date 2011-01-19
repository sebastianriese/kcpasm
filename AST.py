
INSTR_LIMIT = 1024

class Argument(object):
    def IsName(self):
        return False

    def IsReg(self):
        return False

    def IsLit(self):
        return False

    def IsRegRef(self):
        return False

class Reg(Argument):
    def __init__(self, string):
        self.reg = int(string[2:3], base=16)

    def IsReg(self):
        return True

class Lit(Argument):
    def __init__(self, num):
        self.num = num

    def IsLit(self):
        return True 

class Name(Argument):
    def __init__(self, name):
        self.name = name

    def IsName(self):
        return True

class RegRef(Argument):
    def __init__(self, num):
        self.reg = int(num[2:3], base=16)

    def IsRegRef(self):
        return False


class Instruction(object):

    def __init__(self, doc, leader, params):
        self.doc = doc
        self.leader = leader
        self.ParseParams(doc, params)

    def ParseParams(self, doc, params):
        # check for empty parameter list
        if params:
            raise NotImplementedError()
        
    def Patch(self, value):
        raise NotImplementedError()

    def Emit(self, emittor):
        emittor.EmitBitStr(self.leader)
        self.ChildEmit(emittor)

    def ChildEmit(self, emittor):
        pass
    
class Null(Instruction):

    def __init__(self):
        pass
    
    def Emit(self, emittor):
        emittor.EmitBitStr('0' * 18)

class JumpLike(Instruction):
    
    def __init__(self, doc, leader, params):
        self.address = None
        super(JumpLike, self).__init__(doc, leader, params)

    def ParseParams(self, doc, params):
        if len(params) != 1:
            raise Exception()

        param = params[0]

        if param.IsName():
            doc.UseLabel(param.name, self)

        elif param.IsLit():
            self.address = param.num

        else:
            raise Exception()

    def Patch(self, value):
        self.address = value

    def ChildEmit(self, emittor):
        emittor.EmitNumber(self.address, 10)

class LoadLike(Instruction):
    
    def __init__(self, doc, leader, params):
        self.reg = None
        self.arg = None
        self.const = False

        super(LoadLike, self).__init__(doc, leader, params)
    
    def ChildEmit(self, emittor):
        if self.const:
            emittor.EmitBitStr("0")
            emittor.EmitNumber(self.reg, 4)
            emittor.EmitNumber(self.arg, 8)
        else:
            emittor.EmitBitStr("1")
            emittor.EmitNumber(self.reg, 4)
            emittor.EmitNumber(self.arg, 4)
            emittor.EmitBitStr("0000")

    def ParseParams(self, doc, params):
        if len(params) != 2:
            raise Exception()


        if not params[0].IsReg():
            raise Exception()

        self.reg = params[0].reg

        param = params[1]
        if param.IsName():
            self.arg = doc.GetConst(param.name)
            self.const = True

        elif param.IsLit():
            self.arg = param.num
            self.const = True

        elif param.IsReg():
            self.arg = param.reg
            self.const = False

        else:
            raise Exception()

class InOut(LoadLike):
    def __init__(self, doc, leader, params):
        super(InOut, self).__init__(doc, leader, params)

    def ParseParams(self, doc, params):
        if len(params) != 2:
            raise Exception()


        if not params[0].IsReg():
            raise Exception()

        self.reg = params[0].reg

        param = params[1]
        if param.IsName():
            self.arg = doc.GetConst(param.name)
            self.const = True

        elif param.IsLit():
            self.arg = param.num
            self.const = True

        elif param.IsRegRef():
            self.arg = param.reg
            self.const = False

        else:
            raise Exception()

class StoreFetch(LoadLike):
    def __init__(self, doc, leader, params):
        super(InOut, self).__init__(doc, leader, params)

    def ParseParams(self, doc, params):
        if len(params) != 2:
            raise Exception()


        if not params[0].IsReg():
            raise Exception()

        self.reg = params[0].reg

        param = params[1]
        if param.IsName():
            self.arg = doc.GetConst(param.name)
            self.const = True

        elif param.IsLit():
            if param.num >= 0x40:
                print "Scratchpad address literal too large!\n"
                exit(1)

            self.arg = param.num
            self.const = True

        elif param.IsRegRef():
            self.arg = param.reg
            self.const = False

        else:
            raise Exception()

class ShiftRot(Instruction):
    def __init__(self, doc, leader, params):
        self.reg = None

        super(ShiftRot, self).__init__(doc, leader, params)
        self.leader, self.tail = self.leader.split("xxxx")

    def ParseParams(self, doc, params):
        if len(params) != 1:
            raise Exception()

        if not params[0].IsReg():
            raise Exception()

        self.reg = params[0].reg


    # we have to overwrite emit, because we do not fit into the 
    # usual leader -- custom scheme
    def Emit(self, emittor):
        emittor.EmitBitStr(self.leader)
        emittor.EmitNumber(self.reg, 4)
        emittor.EmitBitStr(self.tail)


# compare documentation
# leading strings plus packing class

INSTR_DATA = {
    "jmp"   : ("11010000", JumpLike),
    "jmpc"  : ("11010110", JumpLike),
    "jmpnc" : ("11010111", JumpLike),
    "jmpz"  : ("11010100", JumpLike),
    "jmpnz" : ("11010101", JumpLike),
    
    "call"  : ("11000000", JumpLike),
    "callc" : ("11000110", JumpLike),
    "callnc": ("11000111", JumpLike),
    "callz" : ("11000100", JumpLike),
    "callnz": ("11000101", JumpLike),

    "ret"   : ("101010000000000000", Instruction),
    "retc"  : ("101011100000000000", Instruction),
    "retnc" : ("101011110000000000", Instruction),
    "retz"  : ("101011000000000000", Instruction),
    "retnz" : ("101011010000000000", Instruction),

    "retie" : ("111000000000000001", Instruction),
    "retid" : ("111000000000000000", Instruction),

    "sti"   : ("111100000000000001", Instruction),
    "cli"   : ("111100000000000000", Instruction),

    "ld"    : ("00000", LoadLike),
    "and"   : ("00101", LoadLike),
    "or"    : ("00110", LoadLike),
    "xor"   : ("00111", LoadLike),
    "test"  : ("01001", LoadLike),
    "add"   : ("01100", LoadLike),
    "addc"  : ("01101", LoadLike),
    "sub"   : ("01110", LoadLike),
    "subc"  : ("01111", LoadLike),
    "cmp"   : ("01010", LoadLike),
    
    "in"    : ("00010", InOut),
    "out"   : ("10110", InOut),

    "store" : ("10111", StoreFetch),
    "fetch" : ("00011", StoreFetch),

    "sr0"   : ("100000xxxx00001110", ShiftRot),
    "sr1"   : ("100000xxxx00001111", ShiftRot),
    "srx"   : ("100000xxxx00001010", ShiftRot),
    "sra"   : ("100000xxxx00001000", ShiftRot),
    "rr"    : ("100000xxxx00001100", ShiftRot),

    "sl0"   : ("100000xxxx00000110", ShiftRot),
    "sl1"   : ("100000xxxx00000111", ShiftRot),
    "slx"   : ("100000xxxx00000010", ShiftRot),
    "sla"   : ("100000xxxx00000000", ShiftRot),
    "rl"    : ("100000xxxx00000100", ShiftRot),
}

class Label(object):
    def __init__(self, name):
        self.name = name
        self.topatch = []
        self.address = None

    def Address(self):
        return self.address

    def ToPatch(self, instr):
        self.topatch.append(instr)
        
    def Define(self, address):
        for instr in self.topatch:
            instr.Patch(address)

        self.topatch = []
        self.address = address

class Doc(object):
    def __init__(self):
        self.ip = 0
        self.instructions = [Null() for i in xrange(1024)]

        self.labels = {}
        self.consts = {}

    def BuildInstr(self, name, params):
        leader, instrtype = INSTR_DATA[name]

        return instrtype(self, leader, params)


    def AddInstr(self, instr):
        if self.ip == INSTR_LIMIT:
            print "Instruction Limit exceeded!"
            exit(1)

        self.instructions[self.ip] = instr
        self.ip += 1

    def DefineLabel(self, name):
        if name not in self.labels:
            self.labels[name] = Label(name)

        self.labels[name].Define(self.ip)

    def UseLabel(self, name, instr):
        if name not in self.labels:
            self.labels[name] = Label(name)

        address = self.labels[name].Address()
        if address:
            instr.Patch(address)
        else:
            self.labels[name].ToPatch(instr)

    def DefineConst(self, name, value):
        self.consts[name] = value

    def GetConst(self, name):
        return self.consts[name]

    def SetIP(self, newip):
        if newip < self.ip or newip > INSTR_LIMIT:
            print "Error in address directive: invalid address!"
            exit(1)
                
        self.ip = newip
