from pynq import Overlay

class AluOverlay(Overlay):
    def __init__(self, bitfile_name):
        super().__init__(bitfile_name)
        
        self.registers = self.alu_0.register_map
    
    
    def _operate(self, a, b):
        self.registers.operand_1 = a
        self.registers.operand_2 = b
        return int(self.registers.result)
    
    def add(self, a, b):
        self.registers.opcode = 0
        return self._operate(a,b)
        
    def sub(self, a, b):
        self.registers.opcode = 1
        return self._operate(a,b)
    
    def mul(self, a, b):
        self.registers.opcode = 2
        return self._operate(a,b)
    def div(self, a, b):
        self.registers.opcode = 3
        return self._operate(a,b)
