import gdb

class BreakpointHandler(gdb.Breakpoint):
    def stop(self):
        print("Breakpoint hit at: ", self.location)
        return True

class DebuggingAutomation:
    def __init__(self, binary_path):
        self.binary_path = binary_path
        self.breakpoints = []

    def add_breakpoint(self, location):
        breakpoint = BreakpointHandler(location)
        self.breakpoints.append(breakpoint)

    def start_debugging(self):
        gdb.execute("file " + self.binary_path)
        gdb.execute("run")

if __name__ == "__main__":
    debugger = DebuggingAutomation("/path/to/binary")
    debugger.add_breakpoint("*0x400000")
    debugger.start_debugging()
