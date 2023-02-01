from collections import deque

class DPDA:

    def __init__(self, states, input_symbols , stack_symbols, initial_stack_symbol, transitions, initial_state, final_states):
        self.states = states
        self.input_symbols = input_symbols
        self.stack_symbols = stack_symbols
        self.initial_stack_symbol = initial_stack_symbol
        self.transitions = transitions
        self.initial_state = initial_state
        self.final_states = final_states

        # dpda = DPDA(
        #     states={'q0', 'q1', 'q2','q3'},
        #     input_symbols={'a', 'b'},
        #     stack_symbols = {'a','b','Z0'},
        #     initial_stack_symbol = 'Z0',
        #     transitions={
        #         'q0': {['a','Z0']: ['q1',['a','Z0']]},
        #         'q1': {['a','a']: ['q1',['a','a']], ['b','a']: ['q2',[]]}, # [] or ['']
        #         'q2': {['b','a']: ['q2',[]], ['','Z0']: ['q3',['Z0']]}
        #     },
        #     initial_state='q0',
        #     final_states={'q3'}
        # )

    def accept_string(self, string):

        current_state = self.initial_state
        stack = deque()
        stack.append(self.initial_stack_symbol)
        index = 0
        while index < len(string):
            top_of_stack = stack.pop()
            symbol = string[index]
            if current_state in self.transitions.keys() and symbol in self.transitions[current_state].keys() and top_of_stack in self.transitions[current_state][symbol].keys():
                move = self.transitions[current_state][symbol][top_of_stack]
                current_state = move[0]
                to_push = move[1]
                if len(to_push) != 0:
                    for i in range(1,len(to_push)+1):
                        sym = to_push[-i]
                        stack.append(sym)
                index = index + 1
            elif current_state in self.transitions.keys() and '' in self.transitions[current_state].keys() and top_of_stack in self.transitions[current_state][''].keys():
                move = self.transitions[current_state][''][top_of_stack]
                current_state = move[0]
                to_push = move[1]
                if len(to_push) != 0:
                    for i in range(1,len(to_push)+1):
                        sym = to_push[-i]
                        stack.append(sym)
            else:
                return False
        
        is_finished = False
        while(not is_finished):
            top_of_stack = stack.pop()
            if current_state in self.transitions.keys() and '' in self.transitions[current_state].keys() and top_of_stack in self.transitions[current_state][''].keys():
                move = self.transitions[current_state][''][top_of_stack]
                current_state = move[0]
                to_push = move[1]
                if len(to_push) != 0:
                    for i in range(1,len(to_push)+1):
                        sym = to_push[-i]
                        stack.append(sym)
            else:
                is_finished = True

        if current_state in self.final_states:
            return True
        else:
            return False