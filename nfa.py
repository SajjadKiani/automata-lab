from dfa import DFA
class NFA:

    def __init__(self, states, input_symbols, transitions, initial_state, final_states):
        self.states = states
        self.input_symbols = input_symbols
        self.transitions = transitions
        self.initial_state = initial_state
        self.final_states = final_states

        # nfa = NFA(
        #     states={'q0', 'q1', 'q2'},
        #     input_symbols={'0', '1'},
        #     transitions={
        #         'q0': {'0': [q0], '': [q1]},
        #         'q1': {'': [q0,q2], '1': [q2]},
        #         'q2': {'0': [q2], '1': [q1]}
        #     },
        #     initial_state='q0',
        #     final_states={'q1'}
        # )
    
    def eliminate_nondeterminism(self):
        
        for key in self.transitions.keys():
            for symbol in [''] + self.input_symbols:
                if symbol not in self.transitions[key].keys():
                    self.transitions[key][symbol] = []

        for state in self.transitions.keys():
            for symbol in self.input_symbols:
                states_set = set()
                for s in NFA.lambda_closure(set([state]),self.transitions):
                    states_set = states_set.union(set(self.transitions[s][symbol]))
                states_set = NFA.lambda_closure(states_set,self.transitions)
                self.transitions[state][symbol] = list(states_set)

        for state in self.transitions.keys():
            self.transitions[state].pop('')
        
        is_finished = False
        while(not is_finished):
            is_finished = True
            to_be_added = {}
            for key in self.transitions.keys():
                for symbol in self.input_symbols:
                    if ''.join(self.transitions[key][symbol]) not in self.states:
                        is_finished = False
                        if ''.join(str(self.transitions[key][symbol])) == '':
                            new_state = ''
                            self.states.append(new_state)
                            to_be_added[new_state] = {}
                            for sym in self.input_symbols:
                                to_be_added[new_state][sym] = ''
                        else:
                            new_state = ''.join(self.transitions[key][symbol])
                            self.states.append(new_state)
                            to_be_added[new_state] = {}
                            for sym in self.input_symbols:
                                destinations = []
                                for start in self.transitions[key][symbol]:
                                    destinations = destinations + list(self.transitions[start][sym])
                                to_be_added[new_state][sym] = list(set(destinations))
                            
                    
            self.transitions = {**self.transitions, **to_be_added}
                        
        for key in self.transitions.keys():
            for symbol in self.input_symbols:
                if len(self.transitions[key][symbol]) == 0:
                    self.transitions[key][symbol] = 'phi'
                else:
                    self.transitions[key][symbol] = ''.join(self.transitions[key][symbol])
        self.transitions['phi'] = self.transitions.pop('')
        self.states.remove('')
        self.states.append('phi')

        for final_state in self.final_states:
            for state in self.states:
                if final_state in state and state not in self.final_states:
                    self.final_states.append(state)

        return DFA(
            self.states,
            self.input_symbols,
            self.transitions,
            self.initial_state,
            self.final_states
        ).minimize()


        
    def lambda_closure(states_set,transitions):
        visited = set()
        while(len(states_set) > 0):
            state = states_set.pop()
            visited.add(state)
            for s in transitions[state]['']:
                if s not in visited:
                    states_set.add(s)
        return visited
    
    def __str__(self):
        print('nfa: ')
        for i in self.transitions:
            print('\t' + i + ': ', self.transitions[i])
        print('initial states:', self.initial_state)
        print('final states', self.final_states)
        return ''