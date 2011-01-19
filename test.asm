        ;; Test file
        .const abc 0x45         ; a constant
        
        ld %r0, abc
abcd:   add %r0, 0x1            ; a label
        ld %r1, 0x33
        rr %r1
        jmp abcd

int:    retie
        
        .address 0x3ff
        jmp int

        