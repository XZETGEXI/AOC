import os
from pprint import pprint
from collections import defaultdict
import time

w, h = os.get_terminal_size()

def read():
    with open("input.txt") as f:
        data = f.read().strip()
        data = data.split(",")
        data = [int(i) for i in data]
    return data

def logger(verbose = True):
    def log(*arg):
        if verbose:
            print("-"*w, *arg)
    return log

class Opcode:
    
    def __init__(self, _init):
        self.index = _init
        self.skip = 0
        self.steps = 0
        self.save_number = 0
        self.output = []
        self.save = {}
        _data = read()
        self.data = _data
        self.len = len(_data)
        if _data:
            log("Data loaded")
            _d = defaultdict(int)
            for n, i in enumerate(_data):
                _d[n] = i
            self.dict = _d
            log("OPcode initiated")
        else:
            log("Data problem")
    
    def save_state(self):
        """ saves dict state for debugging purposes """
        self.save_number += 1
        self.save[self.save_number] = self.dict
    
    def set_input(self, _input):
        """
        Part I: code 1, air conditioner
        Part II: code 5, thermal radiator
        """
        self.input = _input
    
    def get_mode(self, _inst):
        """
        Outputs modes in a list
        Outputting as a dict might be better
        Also, reading instruction as a string might fasten it
        """
        if _inst == 99:
            return -1
        else:
            _mode = []
            assert _inst % 100 in {1,2,3,4,5,6,7,8}
            _mode.append(_inst % 100)
            assert _inst % 1000 // 100 in {0,1}
            _mode.append(_inst % 1000 // 100)
            assert _inst % 10000 // 1000 in {0,1}
            _mode.append(_inst % 10000 // 1000)
            assert _inst % 100000 // 10000 in {0,1}
            _mode.append(_inst % 100000 // 10000)
            return _mode
    
    def get_var(self, _mode, _params, _index):
        """
        Get variables and outputs as list for future computation
        Variables take parameter mode into account
        """
        if _mode in {1,2,7,8}:
            _first = self.dict[_index + 1] * _params[0] + self.dict[self.dict[_index + 1]] * (1 - _params[0])
            _second = self.dict[_index + 2] * _params[1] + self.dict[self.dict[_index + 2]] * (1 - _params[1])
            _third = self.dict[_index + 3]
            return [_first, _second, _third]
        elif _mode in {3,4}:
            _first = self.dict[_index + 1]
            return [_first]
        elif _mode in {5,6}:
            _first = self.dict[_index + 1] * _params[0] + self.dict[self.dict[_index + 1]] * (1 - _params[0])
            _second = self.dict[_index + 2] * _params[1] + self.dict[self.dict[_index + 2]] * (1 - _params[1])
            return [_first, _second]
    
    def do_step(self, _mode, _params, _var):
        """
        Do the needful calculations
        """
        if _mode == 1:
            self.dict[_var[2]] = _var[0] + _var[1]
        elif _mode == 2:
            self.dict[_var[2]] = _var[0] * _var[1]
        elif _mode == 3:
            self.dict[_var[0]] = self.input
        elif _mode == 4:
            _output = self.dict[_var[0]] * (1 - _params[0]) + _var[0] * _params[0]
            return _output
        elif _mode == 5:
            _cond = _var[0]
            if _cond:
                _new_index = _var[1]
                self.index = _new_index - 3
        elif _mode == 6:
            _cond = _var[0]
            if not _cond:
                _new_index = _var[1]
                self.index = _new_index - 3
        elif _mode == 7:
            _first_val = _var[0]
            _second_val = _var[1]
            if _first_val < _second_val:
                self.dict[_var[2]] = 1
            else:
                self.dict[_var[2]] = 0
        elif _mode == 8:
            _first_val = _var[0]
            _second_val = _var[1]
            if _first_val == _second_val:
                self.dict[_var[2]] = 1
            else:
                self.dict[_var[2]] = 0
            
    def launch(self):
        """
        Runs the opcode
        Only stops at -99
        """
        _inst = self.dict[self.index]
        try:
            _mode, *_params = self.get_mode(_inst)
        except TypeError:
            log("Mode 99 -> Halted")
            return -1
        _var = self.get_var(_mode, _params, self.index)
        self.skip = len(_var) + 1
        log("Mode is", _mode)
        log("With parameters", _params)
        log("And variables", _var)
        _output = self.do_step(_mode, _params, _var)
        if _output:
            self.output.append(_output)
            log("Output is", self.output)
        self.index += self.skip
        self.save_state()
        log("Moving...", self.index)
        self.launch()
    
def main(part = 1):
    opcode = Opcode(0)
    if part == 1:
        opcode.set_input(1)
    elif part == 2:
        opcode.set_input(5)
    opcode.launch()
    return opcode.output

if __name__ == "__main__":
    log = logger(verbose = False)
    start = time.time()
    print("Silver", main(1))
    print("Gold", main(2))
    end = time.time()
    print("Done in", (end - start) * 1000, "ms")