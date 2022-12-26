class DFA:

    def __init__(self, states: list, input_symbols: list, transitions: list, initial_state: str, final_states: list):
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
        new_initial_state = (self.initial_state, dfa.initial_state)

        new_transition = {}

        for i in self.transitions:
            for j in dfa.transitions:
                new_transition,

        return DFA()

    def is_empty(self):
        return len(self.final_states) == 0

    def minify(self):
        pass
