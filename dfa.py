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
        for i in string:
            current_state = self.transitions[current_state][i]

        if current_state in self.final_states:
            return True
        else:
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

    def intersection(self, dfa):
        new_initial_states = (self.initial_state, dfa.initial_state)
        new_final_states = []

        for i in self.states :
            for j in dfa.states :
                if i in self.final_states and j in dfa.final_states:
                    new_final_states.append(i+j)

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

    def difference(self, dfa):
        new_initial_states = (self.initial_state, dfa.initial_state)
        new_final_states = []

        for i in self.states :
            for j in dfa.states :
                if i in self.final_states and  j not in dfa.final_states:
                    new_final_states.append(i+j)


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
        answer = []
        self.all_language_accept(0 , len(self.states) - 1, answer)
        return len(answer) == 0

    def all_language_accept(self,min_lenght, max_lenght, answer, string=''):
        if self.accept_language(string):
            answer.append(string)

        if max_lenght == min_lenght:
            return

        for i in self.input_symbols:
            self.all_language_accept(min_lenght, max_lenght - 1,answer, string + i)

    def is_finite(self):
        answer = []
        self.all_language_accept (len(self.states) , 2 * len(self.states) - 1, answer)
        return not len(answer) == 0

    def shortest_language(self):
        answer = []
        self.all_language_accept(0 , len(self.states) - 1, answer)
        return min(answer,key=len )

    def longest_language(self):
        answer = []
        self.all_language_accept(0 , len(self.states) - 1, answer)
        return max(answer,key=len )

    def __str__(self):
        print('dfa: ')
        for i in self.transitions:
            print('\t' + i + ': ', self.transitions[i])
        print('initial states:', self.initial_state)
        print('final states', self.final_states)
        return ''

    def minimize(self): #TODO: delete states that are not reachable from initial state.
        # Applying the minimization algorithm (in example 2.41)
        states_not_equal = []
        is_finished = False
        while(not is_finished): # Run until there is no change in states_not_equal
            visited=[]
            is_finished = True
            for state1 in self.states[:-1]:
                for state2 in self.states[1:]:
                    if set((state1,state2)) in visited + states_not_equal or state1 == state2:
                        continue
                    else:
                        visited.append(set((state1,state2)))
                    # If one of two states is a final state and the other isn't, they are not equal.
                    if (state1 in self.final_states and state2 not in self.final_states) or (state1 not in self.final_states and state2 in self.final_states):
                        states_not_equal.append(set((state1,state2)))
                        is_finished = False
                    # If we transition from two states with a symbol, and the two destinations are not equal, then the two states are not equal.
                    elif set((self.transitions[state1][str(self.input_symbols[0])],self.transitions[state2][str(self.input_symbols[0])])) in states_not_equal or set((self.transitions[state1][str(self.input_symbols[1])],self.transitions[state2][str(self.input_symbols[1])])) in states_not_equal:
                        states_not_equal.append(set((state1,state2)))
                        is_finished = False
        
        # Creating a dictionary with states as keys and for each key, the assigned value is a list of states, 
        # that are equal to that key according to the states_not_equal.
        minimized_states = {}
        for state in self.states:
            minimized_states[state] = [state]
        for states_set in visited:
            if states_set not in states_not_equal:
                minimized_states[tuple(states_set)[0]].append(tuple(states_set)[1])
        # adding states that are equal to a state in values of a key, to the values of that key. (if state1~state2 & state2~state3 => state1~state3)
        for key,value in minimized_states.items():
            for item in value:
                if key not in minimized_states[item]:
                    minimized_states[str(item)].append(key)
        # Finding duplicates and removing them.
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

        # Finding transitions & initial state & final states of the minimized DFA:
        minimized_transitions = {}
        minimized_final_states = []
        for state in minimized_states.keys():
            # Finding transitions for each new state:
            transitions_from_key = self.transitions[state]
            for symbol,destination in transitions_from_key.items():
                for possible_destination in minimized_states.keys():
                    if destination in minimized_states[possible_destination]:
                        transitions_from_key[symbol] = possible_destination
            minimized_transitions[state] = transitions_from_key
            # Finding initial state of the minimized DFA:
            if self.initial_state in minimized_states[state]:
                minimized_initial_state = state
            # Finding final states of the minimized DFA:
            if state in self.final_states:
                minimized_final_states.append(state)

        # Find states that are not reachable from initial state.
        visited = []
        fringe = [minimized_initial_state]
        while fringe:
            popped_state = fringe.pop()
            visited.append(popped_state)
            for sym in self.input_symbols:
                if minimized_transitions[popped_state][sym] not in fringe+visited:
                    fringe.append(minimized_transitions[popped_state][sym])
        # Delete states that are not reachable from initial state.
        to_be_deleted = []
        for state in minimized_states.keys():
            if state not in visited:
                to_be_deleted.append(state)
        for state in to_be_deleted:
            minimized_states.pop(state)
            minimized_transitions.pop(state)
            if state in minimized_final_states:
                minimized_final_states.pop(state)


        # Create minimized DFA and return it.
        return DFA(
            states = list(minimized_states.keys()),
            input_symbols = self.input_symbols,
            transitions= minimized_transitions,
            initial_state=minimized_initial_state,
            final_states=minimized_final_states
        )
        