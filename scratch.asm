        .data
        .text
main:
        li $t0, 1
        j l1

order1_return:
        add $t0, $t0, 1
        j l1

order2_return:
        li $v0, 10
        syscall

l1:
        li $a0, 1
        jal print
        beq $t0,1,l3
        beq $t0,2,l5
l3:
        li $a0, 2
        jal print
        beq $t0,1,order1_return
l5:
        li $a0, 3
        jal print
        beq $t0,2,order2_return

print:
        li $v0, 1
        syscall
        jr $ra
