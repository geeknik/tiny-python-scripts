
import dis

def opcode_analysis(function):
    bytecode = dis.Bytecode(function)
    for instruction in bytecode:
        print(instruction.opname)

if __name__ == "__main__":
    # Test function
    def test_func():
        x = 10
        y = 20
        z = x + y
        return z

    opcode_analysis(test_func)
