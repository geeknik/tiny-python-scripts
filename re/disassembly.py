
import capstone

def disassemble(binary_code, arch, mode):
    md = capstone.Cs(arch, mode)
    for i in md.disasm(binary_code, 0x1000):
        print("0x%x:\t%s\t%s" %(i.address, i.mnemonic, i.op_str))

if __name__ == "__main__":
    binary_code = b"\x55\x48\x8b\x05\xb8\x13\x00\x00"
    arch = capstone.CS_ARCH_X86
    mode = capstone.CS_MODE_64
    disassemble(binary_code, arch, mode)
