
import dis

def bytecode_analysis(file_path):
    with open(file_path, 'r') as file:
        code = compile(file.read(), file_path, 'exec')
        dis.dis(code)

if __name__ == "__main__":
    import sys
    bytecode_analysis(sys.argv[1])
