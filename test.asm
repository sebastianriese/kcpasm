        .const abc 0x45
        
        ld %r0, abc
abcd:   add %r0, 0x1
        ld %r1, 0x33
        jmp abcd
        .address 0x100
        retie