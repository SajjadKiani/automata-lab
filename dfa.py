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

    # accepts a string and returns True if the string is accepted by the DFA
    def accept_string(self, string):

        current_state = self.initial_state
        for i in string:
            current_state = self.transitions[current_state][i]

        if current_state in self.final_states:
            return True
        else:
            return False

    # returns union of two DFAs
    def union(self, dfa):
        # concatanation of initial states
        new_initial_states = []
        for i in self.initial_state:
            for j in dfa.initial_state:
                new_initial_states.append(i + j)

        new_final_states = []

        # union of final states
        for i in self.states:
            for j in dfa.states:
                if i in self.final_states or j in dfa.final_states:
                    new_final_states.append(i + j)

        new_transitions = {}

        # create new transitions
        for i in self.transitions:
            for value in self.transitions[i]:
                for j in dfa.transitions:
                    if i + j in new_transitions:
                        new_transitions[i + j].update(
                            {value: self.transitions[i][value] + dfa.transitions[j][value]})
                    else:
                        new_transitions[i + j] = {value: self.transitions[i][value] + dfa.transitions[j][value]}

        return DFA(self.states, self.input_symbols, new_transitions, new_initial_states, new_final_states)

    # returns intersection of two DFAs
    def intersection(self, dfa):
        new_initial_states = []
        for i in self.initial_state:
            for j in dfa.initial_state:
                new_initial_states.append(i + j)

        new_final_states = []

        # intersection of final states
        for i in self.states:
            for j in dfa.states:
                if i in self.final_states and j in dfa.final_states:
                    new_final_states.append(i + j)

        new_transitions = {}

        # create new transitions
        for i in self.transitions:
            for value in self.transitions[i]:
                for j in dfa.transitions:
                    if i + j in new_transitions:
                        new_transitions[i + j].update(
                            {value: self.transitions[i][value] + dfa.transitions[j][value]})
                    else:
                        new_transitions[i + j] = {value: self.transitions[i][value] + dfa.transitions[j][value]}

        return DFA(self.states, self.input_symbols, new_transitions, new_initial_states, new_final_states)

    # returns difference of two DFAs
    def difference(self, dfa):
        # concatanation of initial states
        new_initial_states = []
        for i in self.initial_state:
            for j in dfa.initial_state:
                new_initial_states.append(i + j)

        new_final_states = []

        for i in self.states:
            for j in dfa.states:
                if i in self.final_states and j not in dfa.final_states:
                    new_final_states.append(i + j)

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

    # returns True if two FDAs are separated
    def separate(self, dfa):
        diff1 = self.difference(dfa)
        diff2 = dfa.difference(self)
        if diff1.is_empty() or diff2.is_empty():
            return True
        else:
            return False

    # returns complement of DFA
    def complement(self):
        new_final_states = []
        for i in self.states:
            if i not in self.final_states:
                new_final_states.append(i)

        return DFA(self.states, self.input_symbols, self.transitions, self.initial_state, new_final_states)

    # returns True if DFA is empty
    def is_empty(self):
        answer = []
        self.all_string_accept(0, len(self.states) - 1, answer)
        return len(answer) == 0

    # returns all strings accepted by DFA
    def all_string_accept(self, min_lenght, max_lenght, answer, string=''):
        if self.accept_string(string):
            answer.append(string)

        if max_lenght == min_lenght:
            return

        for i in self.input_symbols:
            self.all_string_accept(min_lenght, max_lenght - 1, answer, string + i)

    # returns True if DFA is finite
    def is_finite(self):
        answer = []
        self.all_string_accept(len(self.states), 2 * len(self.states) - 1, answer)
        return not len(answer) == 0

    # returns shortest string accepted by DFA
    def shortest_string(self):
        answer = []
        self.all_string_accept(0, len(self.states) - 1, answer)
        return min(answer, key=len)

    # returns longest string accepted by DFA
    def longest_string(self):
        answer = []
        self.all_string_accept(0, len(self.states) - 1, answer)
        return max(answer, key=len)

    # prints DFA
    def __str__(self):
        print('dfa: ')
        for i in self.transitions:
            print('\t' + i + ': ', self.transitions[i])
        print('initial states:', self.initial_state)
        print('final states', self.final_states)
        return ''

    def minimize(self):
        # Applying the minimization algorithm (in example 2.41)
        states_not_equal = []
        is_finished = False
        while (not is_finished):  # Run until there is no change in states_not_equal
            visited = []
            is_finished = True
            for state1 in self.states[:-1]:
                for state2 in self.states[1:]:
                    if set((state1, state2)) in visited + states_not_equal or state1 == state2:
                        continue
                    else:
                        visited.append(set((state1, state2)))
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
        for key, value in minimized_states.items():
            for item in value:
                if key not in minimized_states[item]:
                    minimized_states[str(item)].append(key)
        # Finding duplicates and removing them.
        to_be_deleted = []
        visited = []
        for key, value in minimized_states.items():
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
            for symbol, destination in transitions_from_key.items():
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
                if minimized_transitions[popped_state][sym] not in fringe + visited:
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
            states=list(minimized_states.keys()),
            input_symbols=self.input_symbols,
            transitions=minimized_transitions,
            initial_state=minimized_initial_state,
            final_states=minimized_final_states
        )

    # regex to dfa
    def regex_to_dfa(regex: str):

        states = []
        initial_state = ''
        final_state = []
        transitions = {}
        input_symbols = []

        ops = []

        # define variable for regex without parentheses
        new_regex = ''

        # create new state
        def new_state():
            state = 'q' + str(len(states))
            states.append(state)
            return state

        # iteration over regex
        i = 0
        while i < len(regex):
            if regex[i] == '(':
                ops.append(regex[i])

            # if plus, and if the last operator is a parentheses, then add it to the new regex else add it to the operators stack
            elif regex[i] == '+':
                if ops and ops[-1] == '(':
                    new_regex += regex[i]
                else:
                    ops.append(regex[i])

            elif i+1 < len(regex) and regex[i+1] == '*' and regex[i] != ')':
                regex = regex[:i] + '(' + regex[i] + ')' + regex[i+1:]
                # go to the previous character in list range(len(regex))
                continue


            elif regex[i] == ')': # end of parentheses
                if ops and ops[-1] == '(':
                    ops.pop()
                    # convert new regex to dfa
                    new_nfa = DFA.regex_to_dfa(new_regex)

                    # if star, add new state and connect it to the initial state of the new dfa
                    # if regex[i+1] not out of range
                    if i+1 < len(regex) and regex[i+1] == '*':
                        # new state for new_nfa
                        state = 'q' + str(len(new_nfa['states']))
                        new_nfa['states'].append(state)
                        
                        new_nfa['transitions'][state] = {'lambda': new_nfa['initial_state']}
                        new_nfa['transitions'][new_nfa['final_state'][0]] = {'lambda': state}
                        
                        new_nfa['initial_state'] = state
                        new_nfa['final_state'] = [state]

                        i += 1
                    # if plus before parantes , add new state and connect it with lambda to the initial state of two dfas
                    if ops and ops[-1] == '+':
                        states.extend(new_nfa['states'])
                        state = new_state()
                        transitions[state] = {'lambda': [initial_state, new_nfa['initial_state']]}
                        transitions.update(new_nfa['transitions'])
                        initial_state = state
                        final_state.extend(new_nfa['final_states'])

                        ops.pop()

                    # if no plus before parantes, connect the final state of the dfa to initial state on new dfa with lambda
                    else: 
                        states.extend(new_nfa['states'])
                        if len(transitions) != 0:
                            transitions[final_state[0]] = {'lambda': new_nfa['initial_state']}
                            transitions.update(new_nfa['transitions'])
                            final_state = new_nfa['final_state']
                        else:
                            transitions.update(new_nfa['transitions'])
                            initial_state = new_nfa['initial_state']
                            final_state = new_nfa['final_state']
                        
                else:
                    print('Invalid regex')
                    return

            # if regex[i] is a symbol 
            else:
                if regex[i] not in input_symbols: # add to symbols
                    input_symbols.append(regex[i])
                if ops and ops[-1] == '(':  # if last operator is a parentheses, add it to the new regex
                    new_regex += regex[i]
                else: # if not, create new state and add it to the transitions
                    state1 = new_state()
                    state2 = new_state()
                    new_transition = {}
                    new_transition[state1] = {regex[i]: state2}
                    if ops and ops[-1] == '+': # if plus before state, add new state and connect it with lambda to the initial state of two dfas
                        concat_state = new_state()
                        transitions[concat_state] = {'lambda': [state1, initial_state]}
                        transitions.update(new_transition)
                        initial_state = concat_state
                        final_state.append(state2)

                        ops.pop()
                    else: # if not, connect the final state of the dfa to initial state on new dfa with lambda
                        if len(transitions) != 0:
                            transitions[final_state[0]] = {'lambda': state1}
                            transitions.update(new_transition)
                            final_state.clear()
                            final_state.append(state2)
                        else:
                            transitions.update(new_transition)
                            initial_state = state1
                            final_state.append(state2)
            
            # go to the next character in list range(len(regex))
            i += 1

        if '(' in ops:
            return 'Invalid regex'
        else:
            return {
                'states': states,
                'input_symbols': input_symbols,
                'transitions': transitions,
                'initial_state': initial_state,
                'final_state': final_state
            }
        
    # dfa to regex
    def dfa_to_regex(dfa):
        # create table r(p,q,0)
        transition_matrix = {}
        for origin_state in dfa.states:
            transition_matrix[origin_state] = {}
            
            for dest_state in dfa.states:
                transition = list (filter(lambda t: dfa.transitions[origin_state][t] == dest_state,  dfa.transitions[origin_state]) )
                transition = transition[0] if len(transition) != 0 else ''

                if origin_state == dest_state:
                    transition = transition + ' + \u039B' if len(transition) != 0 else '\u039B'

                transition_matrix[origin_state].update({dest_state: transition})

        
        # calculate L(p,q,k+1)
        def formula(p,q,x):
            k = int(x)-1

            if k <= 0:
                return transition_matrix[str(p)][str(q)]

            # L(p,q,k+1) = L(p,q,k) U L(p,k+1,k)L(k+1,k+1,k)*L(k+1,q,k)
            tokens = [(p,q,k), (p,k+1,k), (k+1,k+1,k), (k+1,q,k)]

            answer = []
            for token in tokens:
                answer.append (formula(token[0], token[1], token[2]))

            return '({}) U ({}) ({})* ({})'.format(answer[0], answer[1], answer[2], answer[3])

        p = dfa.initial_state
        final_states = dfa.final_states
        x = len(dfa.states)

        answer = []
        for q in final_states:
            answer.append(formula(p,q,x))

        return answer


