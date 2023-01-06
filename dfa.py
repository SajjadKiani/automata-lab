class DFA:

    def __init__(self, states, input_symbols, transitions, initial_state, final_states):
        self.states = states
        self.input_symbols = input_symbols
        self.transitions = transitions
        self.initial_state = initial_state
        self.final_states = final_states

        # dfa = DFA(
        #     states={'q0', 'q1', 'q2'},
        #     input_symbols={'0', '1'},
        #     transitions={
        #         'q0': {'0': 'q0', '1': 'q1'},
        #         'q1': {'0': 'q0', '1': 'q2'},
        #         'q2': {'0': 'q2', '1': 'q1'}
        #     },
        #     initial_state='q0',
        #     final_states={'q1'}
        # )

    def accept_language(self, string):

        current_state = self.initial_state
        print('-> ' + current_state, end=' ')
        for i in string:
            current_state = self.transitions[current_state][i]
            print('-> ' + current_state, end=' ')

        if current_state in self.final_states:
            print()
            print('accepted by DFA!')
            return True
        else:
            print()
            print('not accepted by DFA!')
            return False

    def union(self, dfa):
        new_initial_states = (self.initial_state, dfa.initial_state)
        new_final_states = (self.final_states, dfa.final_states)

        new_transitions = {}

        for i in self.transitions:
            for value in self.transitions[i]:
                for j in dfa.transitions:
                    if i + j in new_transitions:
                        new_transitions[i + j].update(
                            {value: self.transitions[i][value] + dfa.transitions[j][value]})
                    else:
                        new_transitions[i + j] = {value: self.transitions[i][value] + dfa.transitions[j][value]}

        return DFA(self.states, self.input_symbols, new_transitions, new_initial_states, new_final_states)

    def is_empty(self):
        return len(self.final_states) == 0

    def minify(self):
        pass

    def __str__(self):
        print('dfa: ')
        for i in self.transitions:
            print('\t' + i + ': ', self.transitions[i])
        print('initial states:', self.initial_state)
        print('final states', self.final_states)
        return ''
