import os
import time
import itertools as it
from pprint import pprint
from collections import defaultdict

w, h = os.get_terminal_size()

# UTILITIES

def read():
    with open("example.txt") as f:
        data = f.read().strip()
        data = data.split(",")
        data = [int(i) for i in data]
    return data

def logger(verbose = True):
    def log(*arg):
        if verbose:
            print("-"*w, *arg)
    return log

def tic(): return time.time()

def toc(start):
    end = time.time()
    msg = "TIME %.02f s" % (end - start)
    print(msg.center(w, "_"))
    return end

# CLASSES

class Opcode:
    
    def __init__(self, _init, _data = None):
        self.index = _init
        self.skip = 0
        self.steps = 0
        self.save_number = 0
        self.output = []
        self.save = {}
        
        if not _data:
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
            self.dict = _data
            log("Data from dict")
    
    def save_state(self):
        """ saves dict state for debugging purposes """
        self.save[self.index] = self.dict
    
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
            try:
                _next_input = self.input.pop(0)
                log("Input is", _next_input)
                self.dict[_var[0]] = _next_input
            except IndexError:
                
                return -1
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
        log("Mode is", _mode, "With parameters", _params, "And variables", _var)
        
        _output = self.do_step(_mode, _params, _var)
        if _output == -1:
            log("No more inputs")
            return -1
        if _output != None:
            self.output.append(_output)
            log("Output is", self.output, "output".rjust(w-20))
            self.save_state()
        self.index += self.skip
        log("Moving...", self.index, "down".rjust(w-20))
        self.launch()
    
    def output(self):
        return self.output



class Looper:
    
    def __init__(self, _nb_opcode, _phases):
        _d = {}
        assert len(_phases) == _nb_opcode
        self.nb_opcode = _nb_opcode
        
        for i in range(_nb_opcode):
            phase = _phases.pop(0)
            if i == 0:
                _d[i] = [Opcode(0), [0, phase]]
            else:
                _d[i] = [Opcode(0), [phase]]
        
        self.d = _d
    
    def loop(self):
        _selector = 0
        
        while len(self.d[0][1]) != 1:
            _temp_lst = []
            for i in self.d[_selector][1]:
                _temp_lst.append(i)
                
            self.d[_selector][0].set_input(_temp_lst)
            self.d[_selector][0].launch()
            
            _selector_next = (_selector + 1) % self.nb_opcode
            
            for i in self.d[_selector][0].output:
                self.d[_selector_next][1].append(i)
            
            self.d[_selector][1] = []
            
            _selector = _selector_next
            
            print(self.d)
        
# FONCTIONS

def main_silver():
    result = {}
    PHASES = it.permutations(range(5), 5)
    first_input_signal = 0
    
    for i in PHASES:
        log("Testing phases:", i)
        for n, j in enumerate(i):
            new_phase = j
            if n == 0:
                new_input = first_input_signal
            else:
                new_input = opcode.output[0]
            
            opcode = Opcode(0)
            opcode.set_input([new_phase, new_input])
            opcode.launch()
        
        result[opcode.output[0]] = i
    return result

def main_gold():
    result = {}
    PHASES = it.permutations(range(5, 10), 5)
    
    l = Looper(5, [9,7,8,5,6])
    log(l.d)
    l.loop()
    
    


def main_gold_butifuckedup():
    for i in PHASES:
        
        start_dict_lst = [None]*5
        start_index_lst = [0]*5
        
        log("Testing phases:", i)
        cycle = [*i]
        cycle.reverse()
        cycle.append(0)
        log(cycle)
        
        while True:
            # new input
            a = cycle.pop()
            # new phase
            b = cycle.pop()
            start_index = start_index_lst.pop(0)
            start_dict = start_dict_lst.pop(0)
            
            opcode = Opcode(start_index, start_dict)
            opcode.set_input([b, a])
            log(cycle, a, b, "init variables")
            
            opcode.launch()
            
            try:
                if len(cycle) == 0:
                    buff = []
                    buff.append(opcode.output[0])
                    start_index = [*opcode.save.keys()][0] + 2
                    start_dict = [*opcode.save.values()][0]
                    
                    opcode = Opcode(start_index, start_dict)
                    opcode.set_input([b, a])
                    opcode.launch()
                    if opcode.output != True:
                        log("t", opcode.output)
                        buff.append(opcode.output[0])
                    for j in buff:
                        cycle.append(j)
                    log("here")
                    start_index_lst.append([*opcode.save.keys()][0] + 2)
                    start_dict_lst.append([*opcode.save.values()][0])
                else:
                    output = opcode.output[0]
                    cycle.append(output)
                    start_index_lst.append([*opcode.save.keys()][0] + 2)
                    start_dict_lst.append([*opcode.save.values()][0])
            except IndexError:
                result[output] = i
                break
        return result
        
        break
        
        start_dict_lst = [None]*5
        start_index_lst = [0]*5
        memo_index = {}
        
        while start_index_lst:
            
            start_index = start_index_lst.pop(0)
            start_dict = start_dict_lst.pop(0)
            
            if new_input_lst:
                new_input = new_input_lst.pop(0)
            else:
                print("no more inputs")
            
            opcode = Opcode(start_index, start_dict)
            opcode.set_input([new_phase, new_input])
            print("opcode init", start_index, start_dict)
            print("opcode set", new_phase, new_input)
        
            opcode.launch()
        
            try:
                output = opcode.output[0]
                print("Output found:", output)
                new_input_lst.append(output)
                start_index_lst.append([*opcode.save.keys()][0] + 2)
                start_dict_lst.append([*opcode.save.values()][0])
            except IndexError:
                result[output] = i

    return result


if __name__ == "__main__":
    data = read()
    
    start = tic()
    toc(start)
    
    log = logger(False)
    result = main_silver()
    print("Silver: ", max(result))
    
    step = toc(start)
    
    log = logger(False)
    result = main_gold()
    print("Gold: ", result)
    
    end = toc(step)