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

    def minimize(self):

        states_not_equal = []
        is_finished = False
        while(not is_finished):
            visited=[]
            is_finished = True
            for state1 in self.states[:-1]:
                for state2 in self.states[1:]:
                    if set((state1,state2)) in visited or state1 == state2:
                        continue
                    else:
                        visited.append(set((state1,state2)))
                    if set((state1,state2)) not in states_not_equal:
                        if (state1 in self.final_states and state2 not in self.final_states) or (state1 not in self.final_states and state2 in self.final_states):
                            states_not_equal.append(set((state1,state2)))
                            is_finished = False
                        elif set((self.transitions[state1][str(self.input_symbols[0])],self.transitions[state2][str(self.input_symbols[0])])) in states_not_equal or set((self.transitions[state1][str(self.input_symbols[1])],self.transitions[state2][str(self.input_symbols[1])])) in states_not_equal:
                            states_not_equal.append(set((state1,state2)))
                            is_finished = False
        

        minimized_states = {}
        for state in self.states:
            minimized_states[state] = [state]
        for states_set in visited:
            if states_set not in states_not_equal:
                minimized_states[tuple(states_set)[0]].append(tuple(states_set)[1])
        for key,value in minimized_states.items():
            for item in value:
                if key not in minimized_states[item]:
                    minimized_states[str(item)].append(key)

        to_be_deleted = []
        visited = []
        for key,value in minimized_states.items():
            for item in value:
                if not item == key and item not in to_be_deleted and item not in visited:
                    to_be_deleted.append(item)
            visited.append(key)    
        for item in to_be_deleted:
            if item in minimized_states.keys():
                minimized_states.pop(item)


        minimized_transitions = {}
        for key in minimized_states.keys():
            transitions_from_key = self.transitions[key]
            for symbol,destination in transitions_from_key.items():
                for state in minimized_states.keys():
                    if destination in minimized_states[state]:
                        transitions_from_key[symbol] = state
            minimized_transitions[key] = transitions_from_key
        

        minimized_final_states = []
        for key in minimized_states.keys():
            if self.initial_state in minimized_states[key]:
                minimized_initial_state = key
            if key in self.final_states:
                minimized_final_states.append(key)
        

        return DFA(
            states = list(minimized_states.keys()),
            input_symbols = self.input_symbols,
            transitions= minimized_transitions,
            initial_state=minimized_initial_state,
            final_states=minimized_final_states
        )
        